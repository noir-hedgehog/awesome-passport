# Awesome FoloToy AI Passport

一个持续维护的 FoloToy AI Passport 开源项目导航，收录官方仓库、社区固件、Agent/桌面集成、开发工具与相关生态资源。

[在线浏览](https://noir-hedgehog.github.io/awesome-passport/) · [FoloToy 官方组织](https://github.com/FoloToy) · [提交遗漏项目](https://github.com/noir-hedgehog/awesome-passport/issues/new?title=%E6%B7%BB%E5%8A%A0%E9%A1%B9%E7%9B%AE%EF%BC%9A)

> 收录表示项目与 FoloToy AI Passport 有明确关联，不代表经过安全、硬件或版权审核。刷写第三方固件前，请核对目标板型、Flash 分区、Recovery 保留方式和许可证；重要数据应先备份。

## 如何使用

- 想从官方基线开发：从“官方核心项目”开始。
- 想直接体验玩法：查看“效率、信息与学习”或“游戏、宠物与多媒体”。
- 想连接电脑或 Agent：查看“Agent、桌面与遥控集成”。
- 想找模拟器、刷机和分析工具：查看“开发工具与研究”。
- 带有“间接相关”标记的资源服务于更广泛的 FoloToy 生态，并非 AI Passport 专用。

<!-- CATALOG:START -->
**收录 86 个仓库 · 元数据更新于 2026-09-01**

## 官方核心项目

由 FoloToy 组织维护、直接面向 AI Passport 的基线、固件与 Agent 工具。

| 项目 | 简介 | Stars | 许可证 | 最近推送 / 状态 |
| --- | --- | ---: | --- | --- |
| [FoloToy/ai-passport](https://github.com/FoloToy/ai-passport) | AI Passport 官方硬件与 ESP-IDF 开发基线。 | 171 | MIT | 2026-08-31 |
| [FoloToy/folo-ai-passport-xiaozhi](https://github.com/FoloToy/folo-ai-passport-xiaozhi) | 适配 AI Passport 的小智语音助手固件。 | 3 | MIT | 2026-08-23 |
| [FoloToy/folo-ai-passport-skill](https://github.com/FoloToy/folo-ai-passport-skill) | 面向 AI 工具与 MCP 工作流的官方 Skill。 | 1 | 未声明 | 2026-08-12 |

## 开发工具与研究

模拟器、刷机工具、固件分析、开发 Agent 与硬件验证参考。

| 项目 | 简介 | Stars | 许可证 | 最近推送 / 状态 |
| --- | --- | ---: | --- | --- |
| [KoLoRang/ai-passport-simulator](https://github.com/KoLoRang/ai-passport-simulator) | 带 LCD、按键和音频设备模型的 QEMU PC 模拟器。 | 2 | MIT | 2026-08-28 |
| [ChenYiGeEr/ai-passport-simulator](https://github.com/ChenYiGeEr/ai-passport-simulator) | 面向 FoloToy/ai-passport 的桌面模拟器。 | 0 | Apache-2.0 | 2026-08-27 |
| [caogenfunan123/passport-flasher](https://github.com/caogenfunan123/passport-flasher) | 通过 Android USB OTG 刷写 AI Passport 的工具。 | 0 | 未声明 | 2026-08-26 |
| [ZGF0423/esp32-ai-passport-flasher](https://github.com/ZGF0423/esp32-ai-passport-flasher) | 使用 Python 自动化刷写 ESP32 AI Passport 固件。 | 0 | 未声明 | 2026-08-27 |
| [neverleftWTF/folotoy-ai-passport-re](https://github.com/neverleftWTF/folotoy-ai-passport-re) | AI Passport 逆向研究与分析工具集。 | 0 | MIT | 2026-08-23 |
| [zlhdxb/ai-pass-port](https://github.com/zlhdxb/ai-pass-port) | 固件提取、NVS 修改与开发工具集。 | 0 | 未声明 | 2026-08-23 |
| [iCurrer/ai-passport-agent](https://github.com/iCurrer/ai-passport-agent) | 引导式 AI Passport 固件开发 Agent 预设。 | 0 | MIT | 2026-08-26 |
| [timzenxia/ai-passport-skill](https://github.com/timzenxia/ai-passport-skill) | 面向 Claude Code 的 AI Passport 固件开发 Skill。 | 0 | MIT | 2026-08-22 |
| [mingdedi/passport-demo](https://github.com/mingdedi/passport-demo) | 覆盖板载外设的硬件验证与开发参考固件。 | 0 | MIT | 2026-08-24 |

## Agent、桌面与遥控集成

把工牌作为 Agent 状态终端、语音入口、审批器、遥控器或跨端提醒设备。

| 项目 | 简介 | Stars | 许可证 | 最近推送 / 状态 |
| --- | --- | ---: | --- | --- |
| [BOHUYESHAN-APB/boss-phone](https://github.com/BOHUYESHAN-APB/boss-phone) | 通过掌上终端远程指挥 Codex、Claude Code 等本地 Agent。 | 0 | MIT | 2026-08-31 |
| [zhangsan2000w-art/ai-passport-codex-buddy](https://github.com/zhangsan2000w-art/ai-passport-codex-buddy) | Codex 状态提醒、双端审批与 BLE 本地桥。 | 0 | 未声明 | 2026-09-01 |
| [bingkina/FoloToy-Codex-Buddy](https://github.com/bingkina/FoloToy-Codex-Buddy) | Codex 状态、像素宠物、声音提醒与实体按键审批。 | 2 | MIT | 2026-08-23 |
| [zhaohuaxiaoy/folo-ai-passport-voice](https://github.com/zhaohuaxiaoy/folo-ai-passport-voice) | 按住说话、桌面输入注入、Agent 工作流与物理审批。 | 4 | MIT | 2026-08-29 |
| [ihonghong/ai-passport-macos-voice-remote](https://github.com/ihonghong/ai-passport-macos-voice-remote) | macOS BLE HID 语音输入遥控器与状态界面。 | 0 | MIT | 2026-08-31 |
| [SHLcy/ai-passport-feishu](https://github.com/SHLcy/ai-passport-feishu) | 面向飞书消息与语音识别的 AI Passport 固件。 | 0 | MIT | 2026-08-27 |
| [yigeiwo/meeting-smart-minutes](https://github.com/yigeiwo/meeting-smart-minutes) | 结合飞书、多模型与 AI Passport 的会议纪要系统。 | 0 | MIT | 2026-08-30 |
| [YeatsLiao/ai-passport-ppt](https://github.com/YeatsLiao/ai-passport-ppt) | 兼容主流演示软件的 BLE 翻页笔。 | 0 | 未声明 | 2026-08-31 |
| [YeatsLiao/ai-passport-tiktok-remote](https://github.com/YeatsLiao/ai-passport-tiktok-remote) | 模拟触摸手势的短视频 BLE 遥控器。 | 0 | 未声明 | 2026-08-31 |
| [BigQ749/trae-k2-remote](https://github.com/BigQ749/trae-k2-remote) | 闪电说语音输入与 PPT 控制 BLE 遥控器。 | 1 | MIT | 2026-08-22 |
| [HwzLoveDz/folo-ai-passport-gesture-wand](https://github.com/HwzLoveDz/folo-ai-passport-gesture-wand) | 把 AI Passport 变成可编程手势控制器。 | 2 | 未声明 | 2026-08-28 |
| [KevinGong2013/esp32-ble-mac-lock](https://github.com/KevinGong2013/esp32-ble-mac-lock) | 基于 AI Passport 的一键 Mac 锁定与解锁器。 | 0 | MIT | 2026-08-27 |
| [Yijun-Linda/beminder](https://github.com/Yijun-Linda/beminder) | NFC、iPhone 计时、BLE 与实体报警的共享单车提醒系统。 | 0 | 未声明 | 2026-08-25 |
| [travelerhugo-hu/fmo-mate-for-folotoy-ai-passport](https://github.com/travelerhugo-hu/fmo-mate-for-folotoy-ai-passport) | 面向 AI Passport 的 FMO Mate 应用。 | 0 | 未声明 | 2026-08-31 |
| [SHLcy/ai-passport-stariver](https://github.com/SHLcy/ai-passport-stariver) | Stariver 桌面伴侣固件。 | 0 | MIT | 2026-08-26 |
| [Ritten1/FoloToyAIPassport](https://github.com/Ritten1/FoloToyAIPassport) | 把环境声音转化为可收集、培养的像素精灵。 | 0 | MIT | 2026-08-24 |

## 效率、信息与学习

天气、日历、专注、学习、生活信息和离线工具类固件。

| 项目 | 简介 | Stars | 许可证 | 最近推送 / 状态 |
| --- | --- | ---: | --- | --- |
| [Vitaly2026/sloth-weather](https://github.com/Vitaly2026/sloth-weather) | 随天气变化心情的树懒天气站与手机相册。 | 1 | 未声明 | 2026-09-01 |
| [yangyue1974/Niu-Weather](https://github.com/yangyue1974/Niu-Weather) | 带像素小牛的常亮天气仪表盘。 | 0 | MIT | 2026-08-25 |
| [fanquanpp/FoloToy-calendar](https://github.com/fanquanpp/FoloToy-calendar) | 月历、倒计时、纪念日、配网和低功耗日历。 | 1 | MIT | 2026-08-25 |
| [yueqiu281/TRAE_Stockscreen](https://github.com/yueqiu281/TRAE_Stockscreen) | A 股行情、交易时段刷新、时间校准与电量显示。 | 2 | 未声明 | 2026-08-26 |
| [aris659/ai-passport-GO-WORK](https://github.com/aris659/ai-passport-GO-WORK) | 像素心、CRT 动效与 SoftAP 配网的番茄钟。 | 0 | MIT | 2026-08-25 |
| [dafeng/ai-passport-timer](https://github.com/dafeng/ai-passport-timer) | 带提示音和闪屏提醒的离线倒计时器。 | 0 | MIT | 2026-08-30 |
| [dafeng/ai-passport-breath](https://github.com/dafeng/ai-passport-breath) | 带呼吸动画、背光与柔和提示音的呼吸教练。 | 0 | MIT | 2026-08-30 |
| [milkbaek022/baa-os](https://github.com/milkbaek022/baa-os) | 像素羊专注、补水与休息提醒伴侣。 | 0 | MIT | 2026-08-26 |
| [ricroad/folotoy-pipboy-living-clock](https://github.com/ricroad/folotoy-pipboy-living-clock) | Pip-Boy 风格动态时钟与任务计时器。 | 7 | MIT | 2026-08-23 |
| [elaemc0209/folotoy-ai-passport](https://github.com/elaemc0209/folotoy-ai-passport) | 课程表、GPA 助手与硬件测试页面。 | 0 | MIT | 2026-08-28 |
| [arraylee/ai-passport-answer-book](https://github.com/arraylee/ai-passport-answer-book) | 离线答案之书固件。 | 0 | 未声明 | 2026-08-31 |
| [arraylee/ai-passport-word-bear](https://github.com/arraylee/ai-passport-word-bear) | 离线单词学习与单词熊固件。 | 0 | 未声明 | 2026-08-31 |
| [joeseesun/vocab-passport](https://github.com/joeseesun/vocab-passport) | 带发音的离线词根闪卡。 | 9 | MIT | 2026-08-22 |
| [fancylk/lele-ai-passport](https://github.com/fancylk/lele-ai-passport) | 面向亲子自驾的小学生随身 AI 导游。 | 0 | 未声明 | 2026-08-29 |
| [csn6666/tianji-passport](https://github.com/csn6666/tianji-passport) | 端侧排盘与联网解读的掌心命理机。 | 0 | NOASSERTION | 2026-08-29 |
| [hyt24/ai-passport-xiaoliuren](https://github.com/hyt24/ai-passport-xiaoliuren) | 小六壬离线硬件应用。 | 1 | MIT | 2026-08-25 |
| [PhoenixZHC/folotoy_morse_trainer_blank](https://github.com/PhoenixZHC/folotoy_morse_trainer_blank) | 离线摩尔斯码输入与训练固件。 | 0 | 未声明 | 2026-08-29 |
| [BoajanQ/Today-s-mood_Folotoy_AIPassport](https://github.com/BoajanQ/Today-s-mood_Folotoy_AIPassport) | 选择并展示今日心情的简单应用。 | 1 | 未声明 | 2026-08-24 |
| [Ecparterhacs/palette-passport-ai-passport](https://github.com/Ecparterhacs/palette-passport-ai-passport) | 随身色彩记录与调色板伴侣。 | 0 | MIT | 2026-08-28 |

## 游戏、宠物与多媒体

离线游戏、虚拟宠物、音乐、图片、视频与互动体验。

| 项目 | 简介 | Stars | 许可证 | 最近推送 / 状态 |
| --- | --- | ---: | --- | --- |
| [Bagel-EW/ai-passport-games](https://github.com/Bagel-EW/ai-passport-games) | 包含派对与单人复古游戏的口袋街机。 | 0 | MIT | 2026-08-29 |
| [YeatsLiao/ai-passport-doom](https://github.com/YeatsLiao/ai-passport-doom) | 运行在 AI Passport 上的 Doom 移植实验。 | 2 | 未声明 | 2026-08-31 |
| [XFHurrican/TraeDino](https://github.com/XFHurrican/TraeDino) | Chrome 断网小恐龙复刻游戏。 | 0 | MIT | 2026-08-30 |
| [HwzLoveDz/folo-ai-passport-werewolf](https://github.com/HwzLoveDz/folo-ai-passport-werewolf) | 支持七台设备联机的离线狼人杀。 | 1 | 未声明 | 2026-08-29 |
| [JollySun/folo-ai-passport-niulai](https://github.com/JollySun/folo-ai-passport-niulai) | 牛来互动播放器、动画、录音替换与电量显示。 | 8 | MIT | 2026-08-27 |
| [Regan-Lu/niulai-ai-passport-firmware](https://github.com/Regan-Lu/niulai-ai-passport-firmware) | 《牛来快跑》可刷写固件与使用说明。 | 2 | 未声明 | 2026-08-26 |
| [PhoenixZHC/folotoy_donkeykong](https://github.com/PhoenixZHC/folotoy_donkeykong) | 原创像素攀爬游戏 Pixel Climber。 | 0 | MIT | 2026-08-29 |
| [PhoenixZHC/folotoy-badappleplayer](https://github.com/PhoenixZHC/folotoy-badappleplayer) | Bad Apple!! 全屏视频与音频播放器。 | 0 | MIT | 2026-08-23 |
| [PhoenixZHC/FoloToy-wyy-musicplayer](https://github.com/PhoenixZHC/FoloToy-wyy-musicplayer) | 网易云音乐歌单、播放控制与局域网中转。 | 1 | 未声明 | 2026-08-30 |
| [PhoenixZHC/FoloToy-EVA-musicplayer](https://github.com/PhoenixZHC/FoloToy-EVA-musicplayer) | 离线 EVA 风格音乐播放器。 | 2 | MIT | 2026-08-26 |
| [PhoenixZHC/folotoy_gallery](https://github.com/PhoenixZHC/folotoy_gallery) | 手机上传照片、GIF 与音乐的离线电子相册。 | 1 | 未声明 | 2026-08-26 |
| [PhoenixZHC/folotoy_shuangseqiu](https://github.com/PhoenixZHC/folotoy_shuangseqiu) | 纯离线双色球随机选号娱乐应用。 | 0 | MIT | 2026-08-26 |
| [linn0x/ai-passprot-aemeath](https://github.com/linn0x/ai-passprot-aemeath) | Aemeath 离线虚拟宠物。 | 0 | MIT | 2026-08-31 |
| [Ecparterhacs/talking-pet-ai-passport](https://github.com/Ecparterhacs/talking-pet-ai-passport) | 倾听并用俏皮声音复述的语音宠物。 | 1 | MIT | 2026-08-28 |
| [account-w/Voice-Flight](https://github.com/account-w/Voice-Flight) | 使用麦克风控制升降的障碍飞行游戏。 | 0 | MIT | 2026-08-27 |
| [arraylee/ai-passport-haunted-step](https://github.com/arraylee/ai-passport-haunted-step) | 三键回合制幽灵屋小游戏。 | 0 | 未声明 | 2026-08-29 |
| [azzotest/ai-passport-treasure-hunt](https://github.com/azzotest/ai-passport-treasure-hunt) | 基于 BLE 的亲子寻宝游戏。 | 1 | MIT | 2026-08-25 |
| [punkcatl/ai_passport_pokedex](https://github.com/punkcatl/ai_passport_pokedex) | 15 只宝可梦的离线动画图鉴。 | 0 | MIT | 2026-08-23 |
| [nistudyc/trae-passport-muyu](https://github.com/nistudyc/trae-passport-muyu) | 离线敲木鱼功德计数器。 | 0 | MIT | 2026-08-23 |
| [aaronluyang/music-baby](https://github.com/aaronluyang/music-baby) | 三按键互动音乐玩具。 | 0 | MIT | 2026-08-26 |
| [chenjie1129/MayDayFansInTraePassport](https://github.com/chenjie1129/MayDayFansInTraePassport) | 面向五月天歌迷的卜卜养成与附近同好体验。 | 1 | MIT | 2026-09-01 |
| [zichenli428-tech/xiaozhi-esp32](https://github.com/zichenli428-tech/xiaozhi-esp32) | 面向 AI Passport 板型的小智语音助手移植。 | 0 | MIT | 2026-08-29 |

## 平台、合集与实验性派生

多应用合集、上游基线复制、差异尚未充分说明或仍在早期阶段的仓库。

| 项目 | 简介 | Stars | 许可证 | 最近推送 / 状态 |
| --- | --- | ---: | --- | --- |
| [lululu59/FoloOS-AI-Passport-community](https://github.com/lululu59/FoloOS-AI-Passport-community) | 中文菜单、编程伴侣、番茄钟、单词熊与 Mac 桥接合集。 | 0 | 未声明 | 2026-08-30 |
| [shzh17365503/Wolf-s-AI-Passport](https://github.com/shzh17365503/Wolf-s-AI-Passport) | 包含多款游戏的 All-in-One 固件。 | 2 | 未声明 | 2026-08-28 |
| [zerob13/ai-passport](https://github.com/zerob13/ai-passport) | AI Passport 派生仓库；README 暂未说明与上游差异。 | 0 | MIT | 2026-09-01 |
| [mwm1238888/ai-passport](https://github.com/mwm1238888/ai-passport) | AI Passport 派生仓库；README 暂未说明与上游差异。 | 0 | MIT | 2026-08-31 |
| [pax-zhang/ai-passport](https://github.com/pax-zhang/ai-passport) | AI Passport 基线派生仓库。 | 3 | MIT | 2026-08-30 |
| [rvaim/ai-passport](https://github.com/rvaim/ai-passport) | TRAE AI 通行证实验仓库。 | 1 | MIT | 2026-08-28 |
| [15062106537/ai-passport](https://github.com/15062106537/ai-passport) | AI Passport 派生仓库；README 暂未说明与上游差异。 | 0 | MIT | 2026-08-28 |
| [Sher-AI-Studio/SPIDEY-AI-Passport](https://github.com/Sher-AI-Studio/SPIDEY-AI-Passport) | SPIDEY AI Passport 实验固件。 | 1 | MIT | 2026-08-24 |
| [killhello/ai-pass-port-book](https://github.com/killhello/ai-pass-port-book) | Book 方向的 AI Passport 派生实验。 | 3 | NOASSERTION | 2026-08-28 |
| [killhello/AI-pass-port-wifi](https://github.com/killhello/AI-pass-port-wifi) | 蓝牙配网方向的 AI Passport 派生实验。 | 0 | NOASSERTION | 2026-08-27 |
| [killhello/ai-pass-port-dogtag](https://github.com/killhello/ai-pass-port-dogtag) | Dogtag 方向的 AI Passport 派生实验。 | 0 | MIT | 2026-09-01 |

## FoloToy 官方生态（间接相关）

并非 AI Passport 专用，但可能提供文档、固件、服务或 Agent 集成能力。

| 项目 | 简介 | Stars | 许可证 | 最近推送 / 状态 |
| --- | --- | ---: | --- | --- |
| [FoloToy/folotoy-doc](https://github.com/FoloToy/folotoy-doc) | FoloToy 全产品文档。 | 178 | 未声明 | 2026-04-20 |
| [FoloToy/folotoy-bin](https://github.com/FoloToy/folotoy-bin) | FoloToy 产品固件与 Releases。 | 30 | 未声明 | 2025-08-13 |
| [FoloToy/folotoy-server-self-hosting](https://github.com/FoloToy/folotoy-server-self-hosting) | FoloToy 社区服务自托管配置。 | 600 | GPL-3.0 | 2026-02-01 |
| [FoloToy/folotoy-toy-role-config-skill](https://github.com/FoloToy/folotoy-toy-role-config-skill) | 安全配置角色、人设、开场白与声音的 Agent Skill。 | 1 | MIT | 2026-08-14 |
| [FoloToy/folotoy-openclaw-plugin](https://github.com/FoloToy/folotoy-openclaw-plugin) | FoloToy 的 OpenClaw 通道插件。 | 9 | 未声明 | 2026-04-28 |
| [FoloToy/folotoy-hermes-agent-plugin](https://github.com/FoloToy/folotoy-hermes-agent-plugin) | 为 FoloToy 接入 Hermes Agent 能力。 | 0 | 未声明 | 2026-04-16 |

<!-- CATALOG:END -->

## 收录口径

直接项目至少满足一项：

- 仓库描述或 README 明确写出 `FoloToy AI Passport`、`FOLOTOY MOTE` 或对应 TRAE AI 通行证硬件；
- 明确以 [`FoloToy/ai-passport`](https://github.com/FoloToy/ai-passport) 为上游、BSP 或目标板；
- 工具的主要用途是开发、模拟、刷写或连接 AI Passport。

仅名称碰巧包含“AI Passport”、但实际属于数字身份、证件识别或其他产品的仓库不会收录。没有充分说明差异的复制仓库放在“平台、合集与实验性派生”，避免与成熟项目混在一起。

## 维护方式

- `projects.json` 保存人工审核后的分类和中文摘要。
- 每周 GitHub Actions 从 GitHub API 刷新 Stars、许可证、最近推送日期和归档/失效状态。
- GitHub Pages 每次在 `main` 更新后，直接从这份 `README.md` 构建。
- 新项目、分类修正或下架建议请提交 Issue 或 Pull Request；请附仓库链接和它与 AI Passport 的直接关系。

本目录是社区导航，不隶属于 FoloToy。各项目名称、素材和代码版权归各自权利人所有。
