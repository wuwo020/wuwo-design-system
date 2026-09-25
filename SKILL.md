---
name: wuwo-design-system
description: 机主独有设计系统（暗夜梦核基底+亮色变体）。设计/做页面/UI/组件/动效/配色/字体/HTML/Logo 动画交付时用。承接原 ui-component-bundles、popular-web-designs、claude-design、frontend-design、sketch、transitions-dev、design-md、pretext，并集成 Pixel2Motion。
license: MIT
version: 1.0.0
tags: [design, css, html, ui, design-system, wuwo, 暗夜梦核, transitions, tokens, web-design, sketch, pretext]
platforms: [linux, macos, windows]
---

# WUWO Design System

机主（无我）的独有设计系统。所有设计类任务的第一入口——做页面、改 UI、选组件、加动效、定配色、写 DESIGN.md、出变体方案，一律先看本 skill。

> 本 skill 由 2026-08-16 合并 8 个设计类 skill 而成：
> `ui-component-bundles`（组件层）+ `popular-web-designs`（风格库 54 体系）+ `claude-design`（设计流程/反 slop）+
> `frontend-design`（设计原则）+ `sketch`（变体工作流）+ `transitions-dev`（动效层 27 过渡）+
> `design-md`（token 规范层）+ `pretext`（文本排版创意）+ `pixel2motion`（像素 Logo → SVG → 品牌动效）。功能不丢失，索引见文末「来源映射」。

---

## ① 风格宣言（机主审美特征）

### 基底：暗夜梦核（Dark Dream-core）——默认主题

机主历史作品（qi544xi 人物志、lamb 故事、online 页、梦境记录系统）全部验证的视觉语言：

| Token | 值 | 用途 |
|---|---|---|
| `--ink` | `#0B1020` | 深蓝黑底（页面主背景） |
| `--moon` | `#F2F4FA` | 月光白（正文/主文字） |
| `--mist` | `#93A0C2` | 雾蓝（次要文字/说明） |
| `--dim` | `#5D6889` | 更暗的蓝灰（占位/禁用） |
| `--lilac` | `#B9A7FF` | 丁香紫（主点缀/链接/强调） |
| `--rose` | `#FFA8BE` | 玫瑰粉（次级点缀/直播感/女性向） |
| `--tide` | `#7DDCC4` | 潮青（第三点缀/成功/状态） |
| `--amber` | `#E89B5A` | 琥珀（暖调替代点缀/故事感） |

风格特征：
- **暗色优先**：深蓝黑底是默认，所有交付物默认暗色。
- **月光白文字**：正文用 `#F2F4FA` 级亮度，避免纯白刺眼。
- **粉紫青三色点缀**：紫为主、粉和青为辅，琥珀做暖调变体。**一次只用 1-2 个点缀色**，不彩虹。
- **圆润圆角**：默认 `--radius-md: 12px`，卡片 `16px`，按钮 `10px`，胶囊 `999px`。不用尖锐直角（除非内容明确是工业/终端风）。
- **玻璃拟态微光**：卡片常用 `rgba(255,255,255,0.04~0.08)` 半透明底 + `backdrop-filter: blur(12-20px)` + `1px rgba(255,255,255,0.08)` 描边；发光用同色系低透明度 box-shadow（紫光 `0 0 20px rgba(185,167,255,0.25)`）。
- **渐变克制**：渐变只用于关键视觉点（hero 标题文字、CTA 按钮、发光装饰），用 `--lilac→--rose` 或 `--tide→--lilac` 双色，不用蓝紫靛三色渐变（AI 味重灾区）。
- **梦幻/直播/深夜氛围**：适合梦境记录、直播内容、人物故事、个人品牌。参考梦境——暗夜、星云、月光、微光粒子。

### 变体：亮色暖调（Light Warm）——可选主题

支持整套亮色变体，通过 `html[data-theme="light"]` 或 `.light` 切换（token 双套）：

| Token | 值 | 用途 |
|---|---|---|
| `--bg` | `#F7F4EF` | 奶油底（亮色主背景） |
| `--ink` | `#1A1A1A` | 深墨（亮色主文字） |
| `--muted` | `#6E635B` | 暖灰（次要文字） |
| `--accent` | `#E89B5A` | 琥珀（亮色主点缀，暖调） |
| `--accent2` | `#B98A6E` | 深琥珀（hover/强调） |

亮色场景：白天阅读、杂志/编辑风、需要清爽的对外交付。**默认仍暗色**，亮色是变体，不是替代。

### 审美红线（机主明确不喜欢 / AI 味判定）

1. **不彩虹**：一次最多 2 个点缀色。
2. **不蓝紫靛三色渐变堆叠**（AI slop 头号特征）。
3. **不用默认 Indigo/Violet**（模型默认色）当强调色——用上面的 wuwo 色板。
4. **不玻璃拟态滥用**：玻璃只用在「有内容叠在内容上」的场景（导航栏、浮层、卡片叠底图），纯色底上不强行玻璃。
5. **圆角不能三种以上混用**：一套页面 radius 保持 2-3 档。
6. **不堆 emoji**（品牌本身不用则不用）。
7. **不假数据/假指标**：装饰性数字、fake stats、空话标签（Insights/Growth/Optimize）直接砍。
8. **不居中堆叠当默认布局**：先想 surface 再定布局（见 ⑥ 工作流）。

---

## ② 风格库（54 个真实设计体系）

完整模板在 `templates/web-designs/`（54 个 .md，每个含配色/字体/组件/间距/阴影/响应式 + 可直接粘贴的 Google Fonts link）。
读取方式：`skill_view(name="wuwo-design-system", file_path="templates/web-designs/<site>.md")`

### 选型速查

- **开发者工具/后台**：Linear、Vercel、Supabase、Raycast、Sentry、Cursor
- **文档/内容站**：Mintlify、Notion、Sanity、MongoDB
- **营销/落地页**：Stripe、Framer、Apple、SpaceX
- **暗色 UI**：Linear、Cursor、ElevenLabs、Warp、Superhuman
- **亮色/干净**：Vercel、Stripe、Notion、Cal.com、Replicate
- **活泼/友好**：PostHog、Figma、Lovable、Zapier、Miro
- **高端/奢侈**：Apple、BMW、Stripe、Superhuman、Revolut
- **数据密集/仪表盘**：Sentry、Kraken、Cohere、ClickHouse
- **等宽/终端风**：Ollama、OpenCode、x.ai、VoltAgent

### 54 体系完整清单

**AI 与机器学习（12）**：claude(Anthropic 暖陶土编辑风)、cohere(活力渐变数据风)、elevenlabs(暗色电影感)、minimax(暗色霓虹)、mistral.ai(法式极简紫调)、ollama(终端单色)、opencode.ai(开发者暗色全等宽)、replicate(白底代码向)、runwayml(暗色电影媒体)、together.ai(技术蓝图风)、voltagent(虚空黑+翠绿终端)、x.ai(极简全等宽)

**开发者工具与平台（14）**：cursor(暗色渐变)、expo(暗色紧字距)、linear.app(极简暗色紫调)、lovable(俏皮渐变)、mintlify(绿色阅读优化)、posthog(俏皮暗色)、raycast(暗色炫彩)、resend(极简暗色等宽)、sentry(数据密集粉紫)、supabase(暗色翠绿)、superhuman(高级暗紫光)、vercel(黑白精确 Geist)、warp(暗色 IDE 块状)、zapier(暖橙友好)

**基础设施与云（6）**：clickhouse(黄调技术文档)、composio(暗色多彩集成图标)、hashicorp(企业黑白)、mongodb(绿叶文档)、sanity(红调编辑)、stripe(紫渐变 w300 优雅)

**设计与效率（10）**：airtable(彩色友好数据)、cal(干净中性)、clay(有机形状柔和渐变)、figma(多彩俏皮专业)、framer(黑蓝动效向)、intercom(友好蓝对话)、miro(亮黄无限画布)、notion(暖极简衬线标题)、pinterest(红调瀑布流)、webflow(蓝调营销)

**金融科技与加密（4）**：coinbase(干净蓝信任)、kraken(紫调暗色数据密集)、revolut(暗色渐变卡)、wise(亮绿友好清晰)

**企业与消费（8）**：airbnb(暖珊瑚照片圆润)、apple(高级白空间 SF Pro)、bmw(暗色精密工程)、ibm(carbon 结构蓝)、nvidia(绿黑能量)、spacex(黑白全幅未来)、spotify(暗色亮绿粗字)、uber(黑白紧凑都市)

### 字体替换速查（专有字体 → Google Fonts CDN 替代）

| 专有字体 | CDN 替代 | 特征 |
|---|---|---|
| Geist / Geist Sans | Geist (Google Fonts) | 几何压缩字距 |
| sohne-var (Stripe) | Source Sans 3 | 轻量优雅 |
| Berkeley Mono | JetBrains Mono | 技术等宽 |
| Airbnb Cereal VF | DM Sans | 圆润友好几何 |
| Circular (Spotify) | DM Sans | 几何温暖 |
| figmaSans | Inter | 干净人文 |
| Pin Sans (Pinterest) | DM Sans | 友好圆润 |
| CoinbaseDisplay/Sans | DM Sans | 几何可信 |
| UberMove | DM Sans | 粗紧 |
| waldenburgNormal (Sanity) | Space Grotesk | 几何微窄 |
| IBM Plex Sans/Mono | IBM Plex Sans/Mono | Google Fonts 有 |
| Rubik (Sentry) | Rubik | Google Fonts 有 |

**字体规则**：替代字体时严格沿用原模板的字重/字号/字距（这些比字体本身更承载视觉身份）。等宽只做点缀，不全文等宽。

### 组件实例参考（component.gallery，2026-08-17 收录）

需要看「某个通用组件（Tabs/Accordion/Pagination/Popover/Rating/Tree view 等）在真实设计系统里怎么实现」时，去 [component.gallery](https://component.gallery)（60 组件 × 95 设计系统 × 2,671 实例，含 Shopify Polaris、Elastic EUI、Red Hat、HeroUI、Ariakit、Web Awesome 等）——与本地 54 模板互补：54 模板给「整套风格」，gallery 给「单组件的跨系统对照」。用法：查组件最佳实践/无障碍模式/签名差异时引用其代码与说明。

---

## ③ 组件层（5 大组件源）

### 组件源总览

| 源 | 内容 | 定位 | 技术栈 |
|---|---|---|---|
| **Uiverse / galaxy** | >3000 个 CSS/Tailwind 微组件（按钮/卡片/输入/Toggle/Tooltip/Loading） | 静态通用元件 | 纯 CSS/Tailwind，可复制 |
| **Originkit** | ~45+ 动画组件（Loader/Scroll Reveal/Hover/Skeleton/Frame Transitions） | 入场动效 | 动画组件 |
| **Thinking Orbs** | 9 种点阵「思考球」加载态（working/searching/solving/listening/connecting/weaving/composing/breathing/shaping） | **Agent UI 加载态首选** | 纯 2D canvas，npm `thinking-orbs`，SSR 安全，跟随 `.dark` |
| **Amicro** | React 微交互（按钮 morph/卡片展开/3D Carousel/Dither Charts/Text Reveal/Magnetic Field/Expand Ring） | 交互反馈层（鼠标/点击/状态微动画） | React + Motion，[amicro.vercel.app](https://amicro.vercel.app/) |
| **Appica UI** | 70+ 生产级组件 6 类（Actions&Inputs 30/Data Display 13/Decoration 4/Menus&Nav 9/Overlays 6/Status&Feedback 8） | **完整体系层**（复杂组件首选） | React 19 + Tailwind v4，npm `@appica/ui-react`，可访问性内建，CSS 变量主题化含 light/dark，配套 appica-icons ~5000 SVG |
| **BeautifulUI**（beautifului.dev，旧域名 beautiful-ui-five.vercel.app） | AI 原生界面模式 12 类（Pixel-grid 加载/可展开推理轨迹/流式文本+内联来源/人机确认卡/工具 Chips/任务状态行/分页聊天/高级 Prompt 条/推荐+置信度卡/检索上下文卡/表格差异/记录网格） | **Agent 界面层**（AI 交互模式首选） | 模式整理在 `bundles/agent-ui-kit/`（12 个 README，含结构+关键样式+wuwo token 映射） |
| **Aceternity UI**（ui.aceternity.com） | 200+ 生产级组件/block：Bento Grid、Spotlight、Aurora 背景、3D Globe、Text Reveal、Marquee、Glare Card、Mesh Gradient、Animated Beams 等 | **营销落地页特效层**（hero/背景/卡片特效） | React + Tailwind + Motion，免费组件 MIT 可复制，[ui.aceternity.com/components](https://ui.aceternity.com/components) |
| **21st.dev** | 12,000+ 社区 React 组件 + shadcn 主题 + 2,000+ 营销板块（hero/background/shader/footer） | **大库索引层**（按需抓取，不整库收录） | 分类 URL：`21st.dev/community/components/s/{button|ai-chat|card|carousel|navigation-menu|sign-in|hero|animated-hero|shader|background|gradient|footer}`，无账号可浏览，部分组件需注册 |
| **Pixel2Motion**（nolangz/pixel2motion，MIT） | Raster Logo → 低复杂度平滑 SVG → 可复核品牌动效 HTML；含语义部件拆分、Logo reveal、ribbon fitting、确定性 motion QA | **Logo-to-Motion 专用工作流**（品牌片头、splash、loading/hover logo、SVG 动效） | 参考流程见 `references/pixel2motion.md`；上游脚本按需使用，不把生成物/缓存/整仓库复制进设计 Skill |
| **ThreeUI**（threeui.com，2026-08-22 收录） | 96 个组件家族（约 300+ 变体）：整页落地页 15 / Hero 18 / Three.js 场景 22 / 背景场域 16 / UI 元件+CSS 13 / 按钮 4 / 文字动效+sting 8；每项含提示词模板+源 HTML | **3D/WebGL 落地页特效层**（整页叙事、hero 冲击、氛围背景、shader 按钮） | 模式卡整理在 `references/threeui/`（含选型路由 + wuwo token 强制换算表）；免费 91 家族可学源码结构，PRO 5 家族只记存在 |
| **shadcn/ui**（ui.shadcn.com，2026-08-28 收录） | React 代码复制式组件底座：Radix 原语 + Tailwind，CLI 把代码拷进项目（无运行时依赖、无版本升级包袱），CSS 变量主题化 | **React 项目组件底座**（React 交付默认从这起步；wuwo token 直接映射到其 CSS 变量；也是第三方组件的统一分发通道） | 官网 [ui.shadcn.com](https://ui.shadcn.com)，MIT；`bunx shadcn init` 后 `npx shadcn add <component>`；BeUI/Rare UI/21st.dev 大量组件都走 `shadcn add <registry>/<component>` 安装 |
| **BeUI**（beui.dev，GitHub starc007/ui-components，2026-08-28 收录） | 111 个动画组件：Morphing Modal、Animated Toast Stack、Tilt Card、Magnetic/Metallic/Stateful Button、File Tree、Expandable Control、Animated CTA Buttons 等 | **动画组件库**（比 Amicro 覆盖面宽：CTA/模态/吐司/文件树/表单动效；按钮微交互反馈层仍以 Amicro 为第一顺位，两者按场景分流） | React 19 + Tailwind 4 + Framer Motion，开源免费，`bunx shadcn add @beui/<component>`，分类浏览 [beui.dev/components/motion](https://beui.dev/components/motion)；粘贴后配色按 wuwo token 过反 slop 审查 |
| **Rare UI**（rareui.com，2026-08-28 收录） | 14 个"稀有精品"动画组件：Fluid Orb、Gravity Letters、Step player、Code Block、GitHub activity、Notification bell、Grid Reveal、Folder component、OTP Input、Duration Picker 等，含 AI kit 分类 | **稀有特效层**（小而精，hero/品牌页记忆点首选；AI kit 的 Fluid Orb 可与 ThinkingOrb 搭配做 Agent 氛围） | 开源免费，shadcn CLI 安装，浏览 [rareui.com/components](https://www.rareui.com/components)；组件少，按需抓单件不整库收录 |

### 场景速查（先定场景再选源）

**Landing 页**（`bundles/landing-kit/`）：Hero=Originkit scroll-reveal + CTA glow；Feature Cards=Uiverse 玻璃卡/3D flip；Testimonials=Uiverse 星级评分；CTA=渐变按钮。**暗夜梦核风**：hero 标题渐变字（`--lilac→--rose`）+ 背景星云光晕 + 卡片玻璃拟态。**品牌记忆点/稀有特效**（Fluid Orb、Gravity Letters 类）=Rare UI 按需抓单件；**动画 CTA/模态/吐司**=BeUI。

**Dashboard 后台**（`bundles/dashboard-kit/`）：Side Nav=Appica Navigation 或 Uiverse；KPI Cards=数字滚动+发光描边；**复杂表单/日历/日期/Combobox/OTP/数据表格=Appica 首选**；Status Badge=Appica Status & Feedback。

**React 交付底座**：React 项目组件地基默认 **shadcn/ui**（`npx shadcn init` + `add`），wuwo token 映射到其 CSS 变量后再叠上层源；BeUI/Rare UI/21st.dev 组件统一走 `shadcn add <registry>/<component>` 安装。

**Agent UI**（`bundles/agent-ui-kit/`）：Chat Bubble=Uiverse；**Agent 加载态=ThinkingOrb 首选**（按动作选 state：检索=searching、推理=solving、写作=composing、联网=connecting、规划=weaving、待机=breathing）；**按钮微交互=Amicro 首选**（morph/like/send）；**模态/吐司/表单动效=BeUI**（Morphing Modal、Animated Toast Stack、Expandable Control）；**表单/输入=Appica 首选**；状态过渡=Amicro Expand Ring/Text Reveal；**整页 AI 交互模式（加载/推理轨迹/流式回复/人机确认/任务状态/检索卡等）=BeautifulUI 首选**，模式清单与代码见 `bundles/agent-ui-kit/README.md`。

**移动端引导**（`bundles/mobile-onboarding-kit/`）：Progress Steps + Interactive Cards + Gesture Animations。

### ThinkingOrb 状态速查

```jsx
import { ThinkingOrb } from 'thinking-orbs';
<ThinkingOrb state="searching" size={64} />  {/* 64px 聊天头像级 */}
<ThinkingOrb state="working" size={20} />    {/* 20px 行内文本级 */}
<ThinkingOrb theme="dark" speed={1.5} paused={false} />
```

| state | 语义 | 场景 |
|---|---|---|
| working | 粒子绕倾斜轨道 | 默认干活中 |
| searching | 扫描子午线 | 搜索/检索 |
| solving | 带状混乱后拼合 | 解题/推理 |
| listening | 波形穿过圆环 | 语音输入 |
| connecting | 星座自行接线 | 网络/连接 |
| weaving | 三股绳编织成球 | 规划/编排 |
| composing | 起伏绶带 | 写作/生成 |
| breathing | 圆环缓慢形变 | 待机/空闲 |
| shaping | 圆→三角→方块 | 塑形/建模 |

### Amicro 微交互速查（React + Motion）

| 类别 | 组件 | 场景 |
|---|---|---|
| Buttons | morph/rotate/shake/pulse/ring/glare | 发送/点赞/删除反馈 |
| Card Spreads | 卡片展开过渡 | 工具结果卡展开 |
| Text Reveal | 文字揭示 | 生成结果逐字浮现 |
| Magnetic Field | 磁吸跟随鼠标 | Hero CTA 悬浮 |
| Dither Charts | 抖动图表 | Agent 数据可视化 |
| 3D Carousel | 3D 轮播 | 多结果浏览 |

```jsx
import { motion } from 'motion/react';
<motion.button whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>Send</motion.button>
```

### 许可

Uiverse/ThinkingOrbs/Amicro/Appica 均 MIT；Originkit 免费商用遵守官网条款。仅做代码片段整理，不声明组件所有权。

---

## ④ 动效层（27 个 CSS 过渡 + Amicro + ThinkingOrbs）

### Pixel2Motion：Logo-to-Motion 专用分支

当输入是 Logo 图片或截图，目标是品牌片头、Logo reveal、splash、loading/idle/hover 标记或可交付的 SVG 动效时，**先走 Pixel2Motion**，再决定是否进入 HyperFrames 视频栈。它的顺序固定为：像素源分析与 `motion_spec.md` → 最低复杂度平滑 SVG → overlay/IoU/路径审计 → 语义部件动效 → 独立 showcase HTML → 确定性帧捕获、easing probe、连续性检查与 Final Frame Contract。详细命令和门槛见 `references/pixel2motion.md`。

- 设计系统负责最终的 Wuwo 色彩、字体、构图和反 slop 判断；Pixel2Motion 负责 Logo 拟合、可动效 SVG 结构和 motion QA，不能用高 IoU 掩盖锯齿 trace。
- 复杂自交 ribbon / ∞ 标记使用 split-fill 与路径审计；`@keyframes` 的 timing-function 写字面量 cubic-bezier，不使用会在 Chromium 中静默失效的 `var()`。
- 交付到 HyperFrames、透明视频或更长品牌叙事时，复用 Pixel2Motion 的 `logo.svg` 和 `motion_spec.md`，不重新描 Logo。

### 补充动效来源（2026-08-17 收录）

- **Aceternity 特效组件**（React+Motion）：Bento Grid、Spotlight Card、Aurora 背景、3D/2D Globe、Text Reveal、Marquee、Glare Card、Lens/Flip Cards、Animated Beams、Mesh Gradient、Meteor、Particles——营销落地页 hero/背景特效需求直接去 [ui.aceternity.com/components](https://ui.aceternity.com/components) 按需复制（免费组件 MIT）。**注意**：粘贴后配色必须换成 wuwo token，Aceternity 默认色偏彩虹渐变/霓虹，过 AI 味审查（见 ⑥ 反 slop 自检 1/2 条）。
- **loader-buttons.appllama.io**（@jaimintf 实验集）：25 款 WebGL2 shader 加载按钮（Fibonacci Breather/Glass Tide/Chladni Whisper/Voronoi Lantern 等），纯灵感参考——WebGL2 开销大，生产慎用；只吸收「加载态与动作语义文案绑定」的设计思路（如 Focusing/Merging/Weaving/Polishing）。
- **ThreeUI 动效/场景模式**（`references/threeui/`）：文字动效 5 家族（typography-vortex 粒子旋涡、particle wordmark、gradient carousel）、定帧 motion sting 2 家族（seekable timeline，每个可见值都是场景时间的纯函数）、背景场域 16 家族（constellation 粒子网络/CRT/liquid-form/elements）。做 hero 背景、标题动效、品牌 sting 先查该目录；ThreeUI 默认色（emerald/amber/纯黑）必须按 README 的 wuwo token 换算表转换后才可用。

### 27 过渡速查表（完整代码在 `references/transitions/`）

每个过渡是 `t-*` 命名空间 + 语义 CSS 变量，无框架依赖，内置 `prefers-reduced-motion` 守卫。安装：复制对应文件 CSS 粘贴 + 接好 HTML hooks + 保留 reduced-motion 块 + 需要 JS 的复制编排片段。

| # | 过渡 | 用在哪 | 文件 |
|---|---|---|---|
| 01 | Card resize | 容器宽高随布局状态变化 | `01-card-resize.md` |
| 02 | Number pop-in | 数字更新逐位模糊滑入 | `02-number-pop-in.md` |
| 03 | Notification badge | 小徽章滑入+圆点弹出 | `03-notification-badge.md` |
| 04 | Text states swap | 文字原地模糊上下切换 | `04-text-states-swap.md` |
| 05 | Menu dropdown | 从触发器原点生长的下拉 | `05-menu-dropdown.md` |
| 06 | Modal open/close | 缩放弹窗（关闭更柔） | `06-modal.md` |
| 07 | Panel reveal | 面板滑入区域+交叉模糊 | `07-panel-reveal.md` |
| 08 | Page side-by-side | 列表↔详情/步骤 1↔2 滑动 | `08-page-side-by-side.md` |
| 09 | Icon swap | 同槽双图标交叉淡入 | `09-icon-swap.md` |
| 10 | Success check | 淡入+旋转+描边绘制庆祝成功 | `10-success-check.md` |
| 11 | Avatar group hover | 行内项距离衰减浮起+回弹 | `11-avatar-group-hover.md` |
| 12 | Error state shake | 分段抖动+自动恢复边框提示 | `12-error-state-shake.md` |
| 13 | Input clear dissolve | 清空输入逐词飞散 | `13-input-clear-dissolve.md` |
| 14 | Skeleton reveal | 占位脉冲→交叉淡入真实内容 | `14-skeleton-reveal.md` |
| 15 | Shimmer text | 高光扫过灰字（纯 CSS） | `15-shimmer-text.md` |
| 16 | Tabs sliding | 分段控件活动药丸滑动 | `16-tabs-sliding.md` |
| 17 | Tooltip | 延迟淡入缩放、瞬时关闭（纯 CSS） | `17-tooltip.md` |
| 18 | Texts reveal | 文本行交错模糊升起 | `18-texts-reveal.md` |
| 19 | Card hover tilt | 3D 倾斜+光标跟踪辉光 | `19-card-tilt.md` |
| 20 | Plus to menu morph | 圆形触发器变形为菜单 | `20-plus-menu-morph.md` |
| 21 | Accordion | grid-rows 伸缩+箭头翻转 | `21-accordion.md` |
| 22 | Toast | 底部升起+淡入，慢进快出 | `22-toast.md` |
| 23 | Like button | 爱心填充+粒子迸发 | `23-like-button.md` |
| 24 | Learn more hover | 箭头滑动张开 | `24-learn-more-hover.md` |
| 25 | Checkbox check | 填充+勾描边绘制 | `25-checkbox-check.md` |
| 26 | Spinning counter | 老虎机数字转轮+垂直模糊 | `26-spinning-counter.md` |
| 27 | Toggle | 开关滑块双弹过冲 | `27-toggle.md` |

### 决策规则（用户说要动效时先匹配）

- 触发器+表面从它生长 → **dropdown**；居中无锚 → **modal**
- 表面滑入页面区域 → **panel reveal**；两屏切换 → **page side-by-side**
- 元素变宽高 → **card resize**；文本原地变 → **text swap**；双图标同槽 → **icon swap**；数字更新 → **number pop-in**
- 成功/完成瞬间（勾、付款、上传）→ **success check**
- 悬停水平堆叠项（头像/标签/分段按钮）→ **avatar group hover**
- 表单校验错误 → **error state shake**；清空搜索框 → **input clear**
- 占位加载→真实内容 → **skeleton reveal**；进行中文字 → **shimmer text**
- 互斥小选项+移动高亮 → **tabs sliding**；悬停提示 → **tooltip**
- 标题+副文交错进入 → **texts reveal**；卡片 3D 响应 → **card hover tilt**
- 圆形触发器变面板 → **plus to menu morph**；可折叠头部 → **accordion**
- 匹配不到 → `transitions reveal` 列清单让用户选，不瞎猜

**优先级**：两个都合适时选开销低的（card resize < panel reveal，dropdown < modal，success check < 完整弹窗庆祝）。

### Motion tokens（动效节奏基准，`references/transitions/_root.css` 顶部）

**Durations**：`--duration-stagger 40ms` / `--duration-micro 80ms`（tooltip 延迟、shake 段）/ `--duration-quick 150ms`（modal/dropdown 关、text swap）/ `--duration-fast 250ms`（icon swap、dropdown/modal 开、tabs、page slide）/ `--duration-medium 350ms`（panel/toast 关）/ `--duration-slow 400ms`（panel 开、skeleton reveal）/ `--duration-very-slow 500ms`（强调、badge、text reveal、success check）

**Easings**：`--ease-smooth-out cubic-bezier(0.22,1,0.36,1)`（面板/弹窗开关、页面滑动）/ `--ease-in-out ease-in-out`（icon/text swap、reveal）/ `--ease-out ease-out`（tooltip）/ `--ease-linear linear`（shimmer、skeleton、spinner）/ `--ease-bounce cubic-bezier(0.34,1.36,0.64,1)`（badge pop）/ `--ease-bounce-strong cubic-bezier(0.34,3.85,0.64,1)`（avatar 回弹）

**Distances**：`--distance-micro 4px` / `--distance-small 6px` / `--distance-base 8px` / `--distance-medium 12px` / `--distance-large 30px`

**Scales**：`--scale-large 0.96`（modal）/ `--scale-medium 0.97`（dropdown 开）/ `--scale-small 0.98`（tooltip）/ `--scale-tiny 0.99`（dropdown 关）

**Blur**：`--blur-small 2px` / `--blur-medium 3px` / `--blur-large 8px`（success check）

> `transitions refine` 工作流：扫全项目找硬编码 `ms/s`/`cubic-bezier`，按**用途**（不是数字）映射到 token——300ms modal close 也映射 `--duration-quick`。用途不匹配的不强换。

### 已知坑（动效必看）

- **不要删 close-state class 清理**（dropdown/modal 的 `.is-closing` setTimeout 没了，下次打开从关闭态跳变）
- **重放动画必须 reflow**：`void el.offsetWidth` 夹在 class 移除/重加之间
- **动内件不动容器**：badge 动圆点、page slide 动页面段
- **不用 `transition: all`**：精确枚举属性
- **success check 的 stroke-dasharray 别硬编码 20**：用 `path.getTotalLength()` 向上取整
- **card tilt 的 pointermove 绑外层 wrapper**，不绑卡片本体
- **accordion 内边距放 `.t-acc-panel-inner`**，不放 track（0fr 轨道残留高度）
- **accordion 箭头用 `transform: scaleY(-1)` 翻转**，不用 CSS `d:` 路径插值（Chromium-only）
- **暗色模式 input clear 辉光**：`mix-blend-mode` 用 `screen`、`--glow-opacity ~0.85`、白色渐变用 JS 画

---

## ⑤ 规范层（DESIGN.md token 规范）

正式设计系统用 Google 的 **DESIGN.md** 规范（Apache-2.0，`google-labs-code/design.md`）：YAML front matter 写机器可读 token，Markdown 正文写人读 rationale。CLI：`npx @google/design.md`。

### wuwo 默认 token 模板（暗夜梦核基底）

```md
---
version: alpha
name: wuwo-dark-dream
description: 暗夜梦核——深蓝黑底、月光白文字、粉紫青点缀、圆润圆角、玻璃微光。
colors:
  primary: "#0B1020"      # ink 深蓝黑
  secondary: "#93A0C2"    # mist 雾蓝
  tertiary: "#B9A7FF"     # lilac 丁香紫（主点缀）
  accent: "#FFA8BE"       # rose 玫瑰粉（次级点缀）
  success: "#7DDCC4"      # tide 潮青
  neutral: "#F2F4FA"      # moon 月光白（文字）
typography:
  h1:
    fontFamily: "Noto Serif SC"
    fontSize: 2.5rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  body-md:
    fontFamily: "Noto Sans SC"
    fontSize: 1rem
    lineHeight: 1.7
rounded:
  sm: 10px
  md: 12px
  lg: 16px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
shadows:
  glow-lilac: "0 0 20px rgba(185,167,255,0.25)"
  glass: "0 8px 32px rgba(0,0,0,0.35)"
components:
  card-glass:
    backgroundColor: "rgba(255,255,255,0.05)"
    textColor: "{colors.neutral}"
    rounded: "{rounded.lg}"
    padding: 24px
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "#0B1020"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.accent}"
---
```

### 关键规范

- **Token 类型**：颜色（hex/oklch/rgb）、尺寸（数字+单位）、引用 `{path.to.token}`、排版对象（fontFamily/fontSize/fontWeight/lineHeight/letterSpacing/fontFeature/fontVariation）。
- **组件属性白名单**：backgroundColor、textColor、typography、rounded、padding、size、height、width。**变体是兄弟键**（`button-primary-hover`），不嵌套（`button-primary.hover` 错误）。
- **规范章节顺序**：Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts（linter 警告乱序，照此写）。
- **坑**：hex 必须带引号（YAML 吃 `#`）；负尺寸带引号（`letterSpacing: "-0.02em"`）；`version: alpha` 是当前版本；引用必须点路径 `{colors.primary}` 不是 `{primary}`；排版子属性拼写错会静默丢弃（fontwight 不报错）。

### CLI 工作流

```bash
npx -y @google/design.md lint DESIGN.md              # 结构+引用+WCAG 对比度（exit 1=错误）
npx -y @google/design.md diff DESIGN.md DESIGN-v2.md # 版本对比，回归 exit 1
npx -y @google/design.md export --format json-tailwind DESIGN.md > tailwind.theme.json
npx -y @google/design.md export --format css-tailwind DESIGN.md > theme.css   # Tailwind v4 @theme
npx -y @google/design.md export --format dtcg DESIGN.md > tokens.json         # W3C DTCG
```

9 条 lint 规则：broken-ref(error)、contrast-ratio(WCAG AA 4.5:1 warning)、missing-primary、missing-typography、orphaned-tokens、section-order、unknown-key、token-summary、missing-sections。**用户在意无障碍时明确点出 WCAG 发现**。

---

## ⑥ 工作流（设计流程 + 变体对比 + 交付规范）

### Step 0：先定 Surface（反 slop 第一法则）

动手写任何颜色/字体前，**先口头承诺一个 surface 原型**。AI 设计 slop 是构图问题不是配色问题——默认居中 hero + 三张等重卡片是错的开始。

七种 surface：

1. **Monitor** — 用户在看状态变化（仪表盘/状态页）：密度、扫读层次，无营销框架。仪表盘是 Monitor 不是 Decide，别给它居中 hero。
2. **Operate** — 用户在操作事物（控制台/后台/队列/收件箱）：动作 affordance 和选择态主导。
3. **Compare** — 用户在对选项权衡（定价/套餐/规格/搜索结果）：对齐列、结构对等、突出一个差异点。
4. **Configure** — 用户在设置（设置/表单/向导/引导）：渐进披露、清晰保存/校验态、低装饰。
5. **Decide / Learn** — 用户在被说服或被教（落地页/文档/营销）：每节一个想法。**唯一 hero 通常正确的 surface**。
6. **Explore** — 用户在浏览开放空间（画廊/地图/搜索筛选/目录）：筛选器、结果网格、缩放/窥视。
7. **Command / Inspect** — 用户键盘驱动或深入单对象（命令栏/检查器/详情面板）：速度与焦点优先。

规则：一行字先声明 surface（「这是 Monitor surface，密度和可扫读性优先于 hero」）；一个屏跨两个 surface 就命名主次，不平均成糊。

### Step 1：设计计划（两遍法）

第一遍在思考里做紧凑 token 系统：**颜色**（4-6 个命名 hex）、**字体**（2+ 角色：有性格的 display 面 + 互补正文 + 工具/数据小字）、**布局**（一句话散文 + ASCII wireframe 对比）、**签名元素**（这页唯一的记忆点）。

第二遍对着 brief 复查：**哪部分读起来像任何同类页面的通用默认**？像就改，说明改了什么为什么。确认相对独特后才写代码，每个颜色/字体决策都从计划推导。

### Step 2：变体对比（sketch 工作流）

用户要看方向时出 **2-3 个变体**（不是 1 个，很少 4+），每个是完整独立 HTML 文件，**不同设计立场**（密度/强调/审美/布局/落地方式里选一个轴拉开），不是不同像素值——只换强调色的两个变体是浪费。

- 变体命名用立场不用编号：`001-calm-editorial/`、`001-utilitarian-dense/`
- 单文件自包含：内联 `<style>`、系统字体或一个 Google Font、Tailwind CDN 可以、**真实假内容**（真句子真名字，不 Lorem ipsum）、至少一个状态过渡（开/关、筛选、切换）
- 每个变体用浏览器打开目检（截图/vision 检查布局 bug），坏了先修再展示
- 对比表要**有观点**：「我的看法：X 给重度用户，Y 给内容向受众，Z 最弱——两头都想做都没做成」
- 用户选定后**收敛**，不留一堆选项
- 有现成主题就把共享 token 放 `sketches/themes/tokens.css` 统一 `@import`

### Step 3：反 slop 自检（交付前必跑）

按 10 条打分（每条命中 +1，越低越好），**先诊断后修复**，修完重打：

1. Tech gradient——蓝紫靛渐变糊满
2. Generic tech hue——默认 indigo/violet 强调
3. Feature-tile grid——图标+标题+一句话×3 等重
4. Accent rail——卡片左侧彩色条假装组织
5. Unearned blur——玻璃拟态没有纵深体系支撑
6. Monument stat——巨数字填空间
7. Icon topper——每个标题上方圆角方块图标
8. Center stack——没构图所以全居中
9. Default type——Inter/system-ui 默认而非选择
10. Wrong surface——构图与 surface 不匹配（根源）

修复对应：3/8/10 → **重构图**（换 surface 选择，不换色）；1/2/9 → **重配色/重排版**；4/5/6/7 → **删装饰**，用真正的层次（字号/字重/间距）替代。3/8/10 还在响就不算完。

### Step 4：内容纪律

- 文字是设计材料不是装饰：从用户侧命名（「管理通知」不是「配置 webhook」）、主动语态（「保存更改」不是「提交」）、动作全流程同名（按钮「发布」→ toast「已发布」）
- 错误不说教、不模糊：说清什么坏了怎么修；空状态是行动邀请
- 不填假内容：假指标、装饰性统计、通用特征网格、占位证言、AI 味段落全砍
- 需要真实素材但缺失时用干净占位/排版/抽象纹理，不画华丽假 SVG 插图

### Step 5：交付规范

- 默认**单个自包含 HTML 文件**（内嵌 CSS/JS、浏览器双击可开、避免远程依赖除非稳定有用、含响应式）
- 除非用户要 repo 实现，不进构建链
- 文件名描述性：`Landing Page.html`、`Design System Board.html`
- 大改保留旧版：`Name v2.html`、`Name v3.html`（或页内 Toggle 做变体探索）
- 移动端点击目标 ≥44px；1920×1080 deck 文字 ≥24px；打印 ≥12pt
- deck：1920×1080 16:9 固定画布缩放适配、键盘导航、可见页码、localStorage 记住当前页、1-2 个背景色上限、不把 markdown 要点当 deck
- prototype：主路径可点、关键状态齐（default/hover/focus/loading/empty/error/success）、有用时加页内 `Tweaks` 控制（theme/layout/density/accent/type scale/motion on-off）、localStorage 持久化
- React 才用 CDN：钉死版本、避免 `react@18` 式未钉 URL、全局 style 对象起特定名（`commandPaletteStyles`）
- 键盘焦点可见、`prefers-reduced-motion` 尊重
- **验证才算完成**：文件存在、浏览器打开无 console 错、截图看主视口；验证受限就明说哪些没验证。从不说「done」如果文件没真写出来
- 版权：提取设计原则可以，克隆专有布局/品牌表面不行；参考要转化姿态和原则成原创设计
- 最终回复短：产物路径 + 内容 + 验证状态 + 下一步建议

### 创意文本排版（pretext 工作流）

用户要「文本变几何」类创意 demo（文字绕障碍物、文字打砖块、逐字碎裂、ASCII 障碍排版、动态多栏、动力学排版、最小包裹 UI）时用 `@chenglou/pretext`（DOM-free 文本测量，esm.sh CDN）：

```js
import { prepare, layout, prepareWithSegments, layoutWithLines,
         layoutNextLineRange, materializeLineRange, measureLineStats, walkLineRanges }
  from "https://esm.sh/@chenglou/pretext@0.0.6";
```

- 核心模式：`layoutNextLineRange` + 每行宽度函数 = 文字绕活动精灵流动（最出圈 demo）
- 模板：`templates/pretext/hello-orb-flow.html`（起步）、`templates/pretext/donut-orbit.html`（进阶）；模式库 `references/pretext/patterns.md`
- 创意标准：暗底暖核、比例字体是重点（Iowan Old Style/Inter/JetBrains Mono/可变字体，不默认无衬线）、真实文案不 Lorem、首帧即成品
- 性能：`prepare()` 每 text+font 只调一次；每帧只跑 `layout*`；canvas font 每帧设一次
- 坑：CSS/Canvas 字体串必须一致（Inter 404 会漂 5-20%）；grapheme 切分用 `Intl.Segmenter`；`break:'never'` 芯片要 `extraWidth`；用 esm.sh 不用 unpkg（TS-only entry）；走廊太窄**跳行**别传超小 maxWidth；交付前加 vignette/scanline/空闲自运动/一个交互响应

---

## 来源映射（合并后功能索引）

| 原 skill | 合并去向 |
|---|---|
| ui-component-bundles | ③ 组件层 + `bundles/` + `scripts/list-bundles.sh` |
| popular-web-designs | ② 风格库 + `templates/web-designs/`（54 模板） |
| claude-design | ⑥ 工作流（surface 七原型/反 slop/交付规范） |
| frontend-design | ⑥ 工作流（两遍法/内容纪律）+ ① 风格宣言红线 |
| sketch | ⑥ 变体对比工作流 |
| transitions-dev | ④ 动效层 + `references/transitions/`（27 参考 + `_root.css`） |
| design-md | ⑤ 规范层 + `templates/design-md/starter.md` |
| pretext | ⑥ 创意文本排版 + `templates/pretext/` + `references/pretext/` |
| ThreeUI（2026-08-22 新吸收） | ③ 组件层（3D/WebGL 特效行）+ ④ 动效层补充 + `references/threeui/`（96 家族模式卡） |
| Pixel2Motion（2026-08-27 收录） | ④ Logo-to-Motion 专用分支 + `references/pixel2motion.md`（像素拟合、SVG 结构、品牌动效、Motion QA） |

## 目录结构

```
wuwo-design-system/
├── SKILL.md                     # 本文件（六层：宣言/风格库/组件/动效/规范/工作流）
├── bundles/                     # 组件套装（landing-kit/agent-ui-kit）
├── bundles/agent-ui-kit/        # AI 界面模式 12 类（BeautifulUI 整理：加载/轨迹/流式/确认/工具/任务/聊天/输入/推荐/上下文/差异/记录）
├── scripts/list-bundles.sh      # 列出可用 bundle
├── references/
│   ├── transitions/             # 27 个 CSS 过渡参考 + _root.css（含 motion tokens）
│   ├── threeui/                 # ThreeUI 96 家族模式卡（README 含选型路由+wuwo token 换算表）
│   ├── pixel2motion.md          # Pixel2Motion Logo-to-Motion 集成参考
│   └── pretext/patterns.md      # pretext 社区模式库
└── templates/
    ├── web-designs/             # 54 个真实设计体系模板
    ├── design-md/starter.md     # DESIGN.md 起始模板
    └── pretext/                 # hello-orb-flow.html / donut-orbit.html
```
