#!/usr/bin/env python3
"""Refresh the generated catalog in README.md from GitHub repository metadata."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
START = "<!-- CATALOG:START -->"
END = "<!-- CATALOG:END -->"


def load_catalog() -> dict[str, Any]:
    catalog = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))
    seen: dict[str, str] = {}
    for category in catalog["categories"]:
        for project in category["projects"]:
            key = project["repo"].casefold()
            if key in seen:
                raise ValueError(
                    f"duplicate repository {project['repo']} in "
                    f"{seen[key]!r} and {category['title']!r}"
                )
            seen[key] = category["title"]
    return catalog


def load_metadata_file(path: Path | None) -> dict[str, dict[str, Any]]:
    if path is None:
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {item["full_name"].casefold(): item for item in payload}


def fetch_repo(repo: str, token: str | None) -> dict[str, Any]:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-passport-catalog",
            "X-GitHub-Api-Version": "2022-11-28",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def markdown_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def render_repo(project: dict[str, str], metadata: dict[str, Any] | None) -> str:
    repo = project["repo"]
    summary = markdown_cell(project["summary"])
    if metadata is None:
        return f"| [{repo}](https://github.com/{repo}) | {summary} | — | — | ⚠️ 暂不可用 |"

    name = metadata.get("full_name", repo)
    url = metadata.get("html_url", f"https://github.com/{repo}")
    stars = metadata.get("stargazers_count", 0)
    license_data = metadata.get("license") or {}
    license_name = license_data.get("spdx_id") or "未声明"
    pushed_at = (metadata.get("pushed_at") or "未知")[:10]
    flags = []
    if metadata.get("archived"):
        flags.append("已归档")
    if metadata.get("disabled"):
        flags.append("已禁用")
    status = "、".join(flags) if flags else pushed_at
    return (
        f"| [{markdown_cell(name)}]({url}) | {summary} | {stars} | "
        f"{markdown_cell(license_name)} | {markdown_cell(status)} |"
    )


def render(
    catalog: dict[str, Any],
    supplied_metadata: dict[str, dict[str, Any]],
    token: str | None,
    offline: bool,
) -> str:
    lines: list[str] = []
    project_count = sum(len(category["projects"]) for category in catalog["categories"])
    lines.extend(
        [
            START,
            f"**收录 {project_count} 个仓库 · 元数据更新于 {date.today().isoformat()}**",
            "",
        ]
    )
    errors: list[str] = []
    for category in catalog["categories"]:
        lines.extend(
            [
                f"## {category['title']}",
                "",
                category["description"],
                "",
                "| 项目 | 简介 | Stars | 许可证 | 最近推送 / 状态 |",
                "| --- | --- | ---: | --- | --- |",
            ]
        )
        for project in category["projects"]:
            key = project["repo"].casefold()
            metadata = supplied_metadata.get(key)
            if metadata is None and not offline:
                try:
                    metadata = fetch_repo(project["repo"], token)
                except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
                    errors.append(f"{project['repo']}: {exc}")
            lines.append(render_repo(project, metadata))
        lines.append("")
    lines.extend([END, ""])
    if errors:
        print("Metadata unavailable for:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
    return "\n".join(lines)


def replace_generated(readme: str, generated: str) -> str:
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README must contain exactly one catalog marker pair")
    prefix, remainder = readme.split(START, 1)
    _, suffix = remainder.split(END, 1)
    return f"{prefix}{generated.rstrip()}{suffix}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata-json", type=Path)
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    catalog = load_catalog()
    supplied_metadata = load_metadata_file(args.metadata_json)
    generated = render(
        catalog,
        supplied_metadata,
        os.environ.get("GITHUB_TOKEN"),
        args.offline,
    )
    readme_path = ROOT / "README.md"
    current = readme_path.read_text(encoding="utf-8")
    updated = replace_generated(current, generated)

    if args.check:
        if current != updated:
            print("README.md catalog is out of date", file=sys.stderr)
            return 1
        return 0

    readme_path.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
