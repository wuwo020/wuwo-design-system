# WUWO Design System v2

**无我网页设计系统** —— 一套可直接装进 AI 编码助手（Codex / Claude Code / Hermes / Pi 等任何读 `SKILL.md` 的工具）的设计 skill。
给 AI 一份可执行的视觉立场：先定审美方向，再按手机优先/PC 兼顾的规则搭页面，用滚动与手势跟手动效做沉浸感，并守住去 AI 味底线。

## v2 改了什么

v1 是「素材仓库」：54 个站点风格、5 个组件来源、27 个过渡效果，任 AI 挑选拼凑，结果是哪都像、哪都不是，而且默认长相正好是 AI 最容易产出的那一种（紫蓝渐变 + 毛玻璃 + 居中大标题 + 三张一样的卡）。
v2 换成**有立场的系统**：

| | v1 | v2 |
|---|---|---|
| 审美 | 54 个风格随便挑 | **三套方向**，一个项目声明一套（沉浸暗场 / 仪器极简 / 暖调编辑） |
| 端 | 只写了「移动优先」，实际只按手机写 | **手机网页优先 + PC 网页各自构图**（PC 不是放大的手机页） |
| 动效 | 触发式微交互为主 | **滚动/手势跟手**：滚动进度 = 动画进度，含 GSAP / CSS 时间轴 / 手势库阶梯 |
| 去 AI 味 | 一段红线 | 独立参考文件：视觉 + 文案 + 动效三层禁项与自检 |
| 组件库 | 5 个来源清单 | **选型手册**：什么时候用、什么时候别用、坑、许可、一个项目一个库 |
| 可验证 | 无 | 起始模板 + `scripts/dual-screenshot.py` 双端截图验收 |
| 删除 | — | `bundles/landing-kit`（四项禁项全踩）、悬空引用、玻璃/渐变字当默认值 |

## 目录

```
SKILL.md                  主文档：硬规则、方向 token、双端表、滚动手势阶梯、工作流
references/
  aesthetic-directions.md 三套审美方向（配色/字体/动效/图像处理）
  responsive-dual.md      手机网页 + PC 网页成文规则（断点、安全区、悬停门控、双击）
  scroll-gesture-motion.md 滚动与拇指手势跟手动效（技术阶梯 + 可抄代码 + 已知坑）
  anti-ai-slop.md         去 AI 味：视觉/文案/动效三层禁项与自检清单
  library-guide.md        组件库、图标、字体、素材库选型手册（何时用/坑/许可）
  transitions/            27 个微交互过渡 + motion token（_root.css）
  threeui/ pretext/       ThreeUI 组件族、中文创意排版
templates/
  story-scroll/           滚动叙事起始模板（手机竖屏 + PC 分栏 + 滚轮驱动横移，含降级）
  design-md/              DESIGN.md 起手式（带方向声明与禁用清单）
  web-designs/            54 个站点结构拆解（只借结构，不换皮）
bundles/agent-ui-kit/     AI 应用界面 12 件（状态行、工具调用卡、审批卡、记录表…）
scripts/
  dual-screenshot.py      双端截图验收（390×844 与 1440×900；查溢出、报错、GSAP 是否真加载）
  list-assets.sh          列出资产
```

## 三套方向

| | A 沉浸暗场 | B 仪器极简 | C 暖调编辑 |
|---|---|---|---|
| 用于 | 活动页、直播叙事、品牌页 | 后台、数据、工具、AI 界面 | 长文、报告、公司故事 |
| 底/字 | 深蓝黑 `#0B1020` + 月光白 | 纯灰阶三档 | 奶油 `#F7F4EF` + 深墨 |
| 强调色 | 全页只一个：rose/amber/tide/lilac 择一 | 近乎不用色 | 琥珀 `#E89B5A` |

## 用法

```bash
# 装进你的 AI 助手：把本仓库放到其 skill 目录，或直接读 SKILL.md
python3 scripts/dual-screenshot.py path/to/page.html out/   # 双端截图验收
bash scripts/list-assets.sh                                # 列出资产
```

## 来源与许可

MIT。吸收并改写自 impeccable（craft-floor / adapt）、Emil Kowalski skills（emil-design-eng / pick-ui-library）、nothing-design-skill、uizze/anti-ui-slop、taste-skill、gsap skill，均为 MIT/Apache-2.0 许可，出处已在 `SKILL.md` 标注。
