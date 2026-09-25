---
name: wuwo-design-system
description: 无我网页设计系统 v2（手机网页优先 + PC 兼顾）。做网页/落地页/活动页/后台界面/组件/动效/配色/字体时用：先声明审美方向，再按双端规则搭结构，用滚动与手势跟手动效做沉浸感，守住去 AI 味底线；含组件库与素材库选型手册、滚动叙事起始模板、双端验收脚本。承接原 ui-component-bundles、popular-web-designs、claude-design、frontend-design、sketch、transitions-dev、design-md、pretext、pixel2motion。
license: MIT
version: 2.0.0
tags: [design, css, html, ui, design-system, wuwo, mobile-web, responsive, scroll-animation, gsap, anti-ai-slop, tokens, web-design]
platforms: [linux, macos, windows]
---

# 无我网页设计系统 v2

机主（无我）的设计系统。**所有网页/UI 类任务的第一入口**：做页面、改界面、选组件、加动效、定配色、写 DESIGN.md、出变体方案。

> **v2 相对 v1 改了什么**（v1 = 素材仓库，v2 = 有立场的设计系统）：
> ① 新增**三套审美方向**，先声明方向再动手，不再从 54 个外站风格里随机拼；
> ② 新增**手机网页优先 + PC 网页兼顾**的成文规则（v1 只有一句「移动优先」，且实际只按手机写）；
> ③ 新增**滚动与手势跟手动效**章节（v1 几乎没写，而这正是机主要的效果）；
> ④ 新增**组件库/素材库选型手册**（references/library-guide.md）；
> ⑤ 删掉不合理内容：`bundles/landing-kit`（紫蓝渐变 CTA + 毛玻璃 + emoji 标题 + 悬停翻卡）、悬空的 `dashboard-kit`/`mobile-onboarding-kit` 引用、把玻璃/渐变字当默认值的规定；
> ⑥ 新增可跑的**滚动叙事起始模板**与**双端验收脚本**。

## 0. 怎么用（30 秒）

1. **声明方向**（一句话）→ 读 `references/aesthetic-directions.md`，从 A/B/C 里选一套，写出「这是 <方向>，主角是 <主体>」。
2. **读两条硬规则**：双端适配 `references/responsive-dual.md` + 滚动手势 `references/scroll-gesture-motion.md`（要动效时必读）。
3. **选库**（需要组件/图标/字体/音乐时）→ `references/library-guide.md`，一个项目同类库只选一个。
4. 动手写页面 → 交付前跑 `scripts/dual-screenshot.py <文件>` 看双端截图 + 过一遍 `references/anti-ai-slop.md` 自检。

## 1. 硬规则（不可协商）

1. **一套方向，一个项目**：方向未声明不动手；声明后所有颜色/字体/动效/图片处理都从该方向的 token 推导，**不许临时加色或混搭两套方向**。
2. **手机网页优先，PC 网页同等对待**：两个断点各写自己的构图（手机竖屏叙事 / PC 分栏 + 悬停 + 键盘），PC 绝不是「手机版拉宽」。
3. **滚动/手势跟手**：滚动进度 = 动画进度（scrub），不是「滚到某处播一段」。
4. **0 进度可读**：首屏文字绝不用 JS/滚动门控（否则第一眼是空白）；JS 全挂、`prefers-reduced-motion` 下，全部内容静态可读。
5. **去 AI 味**：禁渐变文字、禁毛玻璃默认、禁 emoji 当图标、禁「居中大标题 + 两行灰字 + 三张一样的卡」；文案不许写「赋能/一站式/在当今」这类正确的废话。
6. **交付=成品 + 双端证据**：贴出手机与 PC 的真实截图；几何检查（无溢出）不算验收。

## 2. 审美方向（细节见 `references/aesthetic-directions.md`）

| | A 沉浸暗场 | B 仪器极简 | C 暖调编辑 |
|---|---|---|---|
| 用于 | 活动页、直播叙事、品牌页 | 后台、数据、工具、AI 界面 | 长文、报告、公司故事 |
| 底/字 | 深蓝黑 + 月光白 | 纯灰阶三档 | 奶油底 + 深墨 |
| 感觉 | 影像说话、跟手叙事 | 克制、无装饰、信息密度高 | 纸感、衬线、可长读 |

**默认 token（方向 A，直接抄）**

| Token | 值 | 用途 |
|---|---|---|
| `--ink` | `#0B1020` | 主背景（深蓝黑） |
| `--ink-2` | `#121829` | 抬升面（卡片/分区） |
| `--line` | `rgba(242,244,250,.08)` | 描边/分隔线（1px 为准） |
| `--moon` | `#F2F4FA` | 主文字 |
| `--mist` | `#93A0C2` | 次要文字 |
| `--dim` | `#5D6889` | 占位/禁用 |
| `--accent` | 见下 | **全页只有一个强调色** |

强调色按主体选**一个**：`--rose #FFA8BE`（人/主播/女性向）、`--amber #E89B5A`（故事/暖调）、`--tide #7DDCC4`（数据/状态）、`--lilac #B9A7FF`（品牌需要时才用）。v1 的错误是四色齐上 + 紫色发光当氛围——**紫不是禁忌，滥用才是**。

方向 C（亮色暖调）token：`--bg #F7F4EF`／`--ink #1A1A1A`／`--muted #6E635B`／`--accent #E89B5A`。

**形状与节奏**：圆角只用两档（`8–10px` 内容件 / `999px` 胶囊），**不要** 16–24px 全套大圆角；阴影克制（深色底下用亮度分层，不用辉光）；间距用一套数：`8 / 14 / 22 / 34 / 56 / 88`；正文 17px/1.8（手机）、18px/1.7（PC）；中文标题行高压到 1.1–1.2。

## 3. 双端适配（细节见 `references/responsive-dual.md`）

| 项 | 手机网页 | PC 网页 |
|---|---|---|
| 断点 | 单列起步，`@media (min-width:1024px)` 再增强 | 版心 1200px，出血层用 `100vw` |
| 首屏 | 竖屏叙事，`min-height:100svh`，标题竖排式分行 | **分栏**（左文右图/右影像位），`align-content:center` |
| 导航 | 底部拇指区固定条 + `env(safe-area-inset-bottom)` | 顶部横向导航 + 键盘可达 |
| 触达 | 点击区 ≥44×44px，`padding` 撑开 | 悬停态包在 `@media (hover:hover) and (pointer:fine)` |
| 输入 | `font-size ≥16px`（否则 iOS 自动放大） | 可加 `:focus-visible` 描边 |
| 单位 | `svh/dvh` 替 `vh`；`clamp()` 做流体字号 | 允许固定 px + 更宽行距 |
| 动效 | 手势/滚动驱动，不用 hover 承担信息 | 可用 hover/光标/键盘，横向用滚轮驱动 |
| 必守 | `viewport-fit=cover` + 安全区；微信内 `playsinline muted` 视频 | 不用 `100vw` 宽度配滚动条导致横向溢出 |

## 4. 滚动与手势（细节 + 可抄代码见 `references/scroll-gesture-motion.md`）

**技术阶梯（先用上面的）**：① 纯 CSS `animation-timeline: scroll()/view()`（能上合成器、最省电）→ ② GSAP ScrollTrigger（`scrub` 跟手、`pin` 叙事、`matchMedia` 分端）→ ③ 手势：Observer（滑动翻页）/ Draggable+Inertia（拖拽惯性）/ 手写 Pointer Events（底部抽屉）→ ④ Lenis 平滑滚动（**只给 PC**，手机原生滚动更跟手）。

**必守**：跟手动画用 `ease:'none'`（进度即进度，别叠缓动）；进场动画 150–400ms、`power3.out`；反馈类 <120ms；手机开 `ScrollTrigger.config({ignoreMobileResize:true})`；`pin` 必须给 `invalidateOnRefresh:true`；横向位移算 `scrollWidth - innerWidth`，保证尽头停整卡；CDN 用三源兜底或自托管（实测单源会偶发失败）。

## 5. 组件库 / 素材库（选型手册见 `references/library-guide.md`）

**纪律**：一个项目同类库只选 1 个；不为展示技术而引库；能用 CSS 写的微交互不引库；引库先看许可与体积；**库给你零件，方向给你长相**——库里默认的长相（紫色渐变/毛玻璃/发光）一律按方向 token 重刷。

速查：底座 `shadcn/ui`（React 复制式）+ 原语 Radix/Base UI；非 React 用 `daisyUI`/纯 CSS；动效 `Motion`（React）、`GSAP`（滚动叙事）、`dotlottie-web`（AE 动效落地）、`Lenis`（PC 平滑）；特效组件 `Magic UI`/`Aceternity`（挑 1–2 个用，别整页堆）；图标 `Lucide`/`Phosphor`/`Tabler`；中文字体 `Noto Serif/Sans SC`、`LXGW WenKai`、`MiSans`（CDN 地址与坑见手册）。

## 6. 去 AI 味（20 条禁项 + 文案纪律见 `references/anti-ai-slop.md`）

视觉：渐变文字、毛玻璃默认、紫色辉光氛围、emoji 当图标、居中大标题 + 两行灰字 + 三张一样的卡、整页 16–24px 大圆角、无意义的编号 /01 /02、hover 翻卡承担信息、库存图凑数、层层嵌套卡片。
文案：赋能/一站式/在当今数字化时代/开启新篇章；排比三连的正确废话；形容词堆叠（极致、震撼、颠覆）；没有主语的「致力于」。
动效：万物淡入上浮、均匀 `ease-in-out` 满屏 0.6s、滚动劫持、光标跟随满屏。

## 7. 动效资产 `references/transitions/`

27 个过渡（含完整代码 + `_root.css` 里的 motion token）：
卡片与容器 `01-card-resize` `07-panel-reveal` `08-page-side-by-side` `21-accordion`；
文字与数字 `04-text-states-swap` `15-shimmer-text` `18-texts-reveal` `26-spinning-counter` `02-number-pop-in`；
反馈与状态 `03-notification-badge` `10-success-check` `12-error-state-shake` `14-skeleton-reveal` `22-toast` `23-like-button`；
控件与菜单 `05-menu-dropdown` `06-modal` `09-icon-swap` `16-tabs-sliding` `17-tooltip` `20-plus-menu-morph` `24-learn-more-hover` `25-checkbox-check` `27-toggle`；
指针类 `11-avatar-group-hover` `19-card-tilt` `13-input-clear-dissolve`。
motion token：`--dur-fast 120ms / --dur-base 220ms / --dur-slow 420ms`，缓动 `cubic-bezier(.2,.8,.2,1)`（进）、`cubic-bezier(.4,0,1,1)`（出）。

## 8. 规范层（DESIGN.md token）

写页面时先落一份 `DESIGN.md`：方向声明（A/B/C）+ 上表 token 值 + 强调色用途 + 圆角/间距/字号三套数 + 动效节奏 + 图像处理规则（裁剪比、暗角/去饱和口径）。**页面里出现的颜色必须能在 DESIGN.md 找到出处**。

## 9. 资产清单

- `references/`：`aesthetic-directions.md` 三套方向 · `responsive-dual.md` 双端 · `scroll-gesture-motion.md` 滚动手势 · `anti-ai-slop.md` 去 AI 味 · `library-guide.md` 选型手册 · `transitions/` 27 个过渡 · `threeui/` ThreeUI 组件族 · `pretext/` 创意文本排版。
- `templates/story-scroll/index.html`：**滚动叙事起始模板**（手机竖屏叙事 + PC 分栏 + 滚轮驱动横移，含 0 进度可读与 reduced-motion 降级，已双端截图验收）。
- `templates/design-md/starter.md`：DESIGN.md 起手式。
- `bundles/agent-ui-kit/`：AI/后台界面 12 件（状态行、工具调用卡、审批卡、引用、空态、错误、进度、推荐卡、会话列表、设置、记录表、组件索引）。
- `scripts/`: `dual-screenshot.py` 双端截图验收（390×844 与 1440×900，顺带查横向溢出/控制台报错/GSAP 是否真加载）；`list-assets.sh` 列资产。

## 10. 工作流

- **Step 0 定 Surface**：先说清是「手机为主的活动页 / PC 为主的后台 / 双端都要的官网」，因为方向与断点策略跟着它变。
- **Step 1 两遍法**：第一遍只做结构与内容（无动效），第二遍才加跟手动效；不许一遍里层叠。
- **Step 2 变体**：机主要对比时给 2–3 个变体，差异必须落在**方向或结构**上（不是换配色），每版一句话说明取舍。
- **Step 3 自检**：过 `anti-ai-slop.md` 清单；跑 `scripts/dual-screenshot.py`，手机 + PC 各看真实截图（首屏必须有字、底部有安全区、无重叠裁切）。
- **Step 4 交付**：文件 + DESIGN.md + 双端截图 + 一句「方向/断点/动效降级怎么做的」。

## 来源与许可

吸收并改写（均为 MIT/公开许可，保留出处）：impeccable `craft-floor` / `adapt`（质量底线与双端适配基线）、Emil Kowalski `emil-design-eng` / `pick-ui-library`（动效手感与选库方法论）、`nothing-design-skill`（仪器极简）、`uizze/anti-ui-slop`、`taste-skill`（去 AI 味）、gsap skill（ScrollTrigger/Observer 用法）。外部站点仅作**原则参考**（54 个站点拆解在 `templates/web-designs/`，只借结构与信息密度，不换皮）。
