# 组件库 / 素材库引用指南（v2）

> 机主的要求：「给各种组件库或者类似素材库那种东西，做详细的 skill 说明，让 skill 引用的时候，有方向和参考。」
> 所以本文件是**选型手册**：每个库写清「它是什么 / 什么时候用 / 什么时候别用 / 怎么装 / 落地要点 / 坑 / 许可」。
> **通用纪律**：
> 1. **一个项目里的同类库只选 1 个**（不要 shadcn + HeroUI + daisyUI 一起上）。
> 2. **库只提供骨架，皮肤永远来自 `aesthetic-directions.md` 的 token**——套用默认主题 = 立刻 AI 味。
> 3. 库自带的花哨演示（粒子、光晕、渐变）**默认不开**。
> 4. 商用前看许可；下表已标，未标的一律先查。

## 0. 30 秒选型

| 我要做… | 首选 | 备选 |
|---|---|---|
| 团播/品牌/活动页（营销向） | 手写 HTML + **GSAP** + **Lenis**（PC） | Astro / 原生 Vite |
| 后台/管理端（AI 秒聘这类） | **shadcn/ui** + Radix | **HeroUI**、coss UI、daisyUI |
| React 应用里的动效 | **Motion**（`motion/react`） | GSAP（复杂时间线时） |
| 需要现成花哨组件（光效、粒子、动画卡片） | **Magic UI** | Aceternity UI、React Bits |
| 手机网页手势（抽屉、拖拽、滑动） | 原生 Pointer Events + **GSAP Draggable** | Vaul（React 抽屉）、Embla（轮播） |
| 图标 | **Lucide** | Phosphor、Tabler |
| 中文字体 | 系统字体栈兜底 + 按需子集化的 **Noto Sans/Serif SC** | 霞鹜文楷、MiSans |
| 配图 | 真实照片（自有素材优先） | Unsplash / Pexels |

---

## 1. 动效库

### 1.1 GSAP（核心 + ScrollTrigger + Observer + Draggable）
- **是什么**：工业标准 JS 动画引擎。核心免费；**ScrollTrigger / Observer / Draggable / InertiaPlugin / Flip / SplitText 自 2025 年起全部免费**（Webflow 收购后放开）。
- **什么时候用**：滚动跟手叙事（`scrub`）、`pin` 分区、整屏翻页（Observer）、拖拽惯性（Draggable）、复杂时间线。
- **什么时候别用**：只是让按钮变色、卡片淡入——用 CSS 就够，别为一个微交互加载 100KB。
- **怎么装**：
  ```html
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrollTrigger.min.js"></script>
  ```
  ```bash
  npm i gsap            # React 项目建议 @gsap/react 的 useGSAP
  npm i @gsap/react
  ```
- **落地要点**：只用官方 `transform` 别名（`x/y/scale/rotation`）；`ease:"none"` 是 scrub 横向滚动的硬要求；用 `gsap.matchMedia()` 做双端差异（自动 revert）。
- **坑**：`scrub` 值过大显得迟钝；`pin` 分段太短沉浸感消失；SPA 卸载不 `kill()` 会泄漏；手机地址栏伸缩要 `ScrollTrigger.config({ignoreMobileResize:true})`。
- **国内**：jsDelivr 偶有抽风，可换 `https://registry.npmmirror.com/gsap/3.15.0/files/dist/gsap.min.js` 或自托管。
- **许可**：标准 GSAP 免费许可（含商用），禁止把 GSAP 本身当产品转卖。
- **配套读**：`references/scroll-gesture-motion.md`（配方与纪律）。

### 1.2 Motion（前 Framer Motion）
- **是什么**：React 动画库，现在也支持原生 JS（`motion` 包）。弹簧/布局动画/手势一体。
- **什么时候用**：React 项目里的组件入场、布局切换（`layout`）、拖拽（`drag`）、滚动（`useScroll`）。
- **别用**：纯 HTML 静态页（为它上 React 不划算）。
- **装**：`npm i motion` → `import { motion, useScroll, useTransform } from "motion/react"`。
- **坑**：**不要同时装 `framer-motion` 和 `motion`**；`AnimatePresence` 需要稳定的 `key`；频繁用 `layout` 会有布局抖动。
- **许可**：MIT。

### 1.3 Lenis
- **是什么**：3KB 平滑滚动库（MIT）。
- **什么时候用**：**PC 网页**想让滚轮顺滑、配合 scrub 更「顺」。
- **别用**：手机上——原生惯性滚动手感最好，Lenis 只会增加掉帧风险。用 `@media (hover:hover) and (pointer:fine)` 包起来。
- **装**：`npm i lenis`；CDN `https://cdn.jsdelivr.net/npm/lenis@1.3.26/dist/lenis.min.js`。
- **配套**：与 GSAP 联动 `lenis.on('scroll', ScrollTrigger.update)` + `gsap.ticker.add(t => lenis.raf(t*1000))`。
- **坑**：`position: fixed` 的元素和 `overflow: hidden` 的弹层容易打架；会让浏览器原生「回到顶部」失效，需要额外处理。

### 1.4 CSS 原生滚动动画（`animation-timeline`）
- **是什么**：`scroll()` / `view()` 时间线，滚动驱动动画不必写 JS，跑在合成器线程。
- **什么时候用**：简单揭示、进度条、视差初稿——**优先于 JS**。
- **别用**：需要 pin、需要精确 scrub 控制、需要按窗口宽度变化重算时。
- **写法**：
  ```css
  @supports (animation-timeline: view()) {
    .fade { animation: fade linear both; animation-timeline: view(); animation-range: entry 20% cover 40%; }
    @keyframes fade { from { opacity: 0; translate: 0 24px } to { opacity: 1; translate: 0 } }
  }
  ```
- **坑**：Safari/Firefox 支持较慢，必须 `@supports` 兜底（不支持时直接显示最终态，不要留白）。

### 1.5 dotlottie-web（LottieFiles 官方）
- **是什么**：矢量/JSON 动画播放器（`.lottie` 格式比 `.json` 体积小）。
- **什么时候用**：需要**精细的插画动画**（成功反馈、加载、空状态）。
- **别用**：当主视觉——Lottie 是「小动画」，放大到全屏会糊且有廉价感。手机首屏慎用（解码耗电）。
- **装**：`npm i @lottiefiles/dotlottie-web`（React: `@lottiefiles/dotlottie-react`）。
- **许可**：MIT（播放器）；**单个动画素材的许可要看来源**（LottieFiles 市场有免费/付费之分）。

### 1.6 Rive
- **是什么**：状态机式交互动画（可响应 hover/点击/滚动输入），作者用 Rive 编辑器做。
- **什么时候用**：需要「可交互角色/图标」且愿意在编辑器里做资产时。
- **别用**：没人做资产、或只是普通图标动画（Lottie 更省事）。
- **许可**：运行时免费，编辑器有免费档。

### 1.7 Three.js / React Three Fiber
- **是什么**：WebGL 3D。
- **什么时候用**：PC 优先的强视觉场景（首屏 3D、产品旋转），且团队能承担性能成本。
- **别用**：手机为主的页面——除非降级方案齐备。**手机默认替换成视频或静态图**。
- **装**：`npm i three`（React：`@react-three/fiber`）。
- **坑**：`setPixelRatio(Math.min(devicePixelRatio, 1.5))` 控制开销；卸载时必须 `dispose()` 几何体/纹理/渲染器，否则内存不释放。
- **参考库**：本 skill `references/threeui/`（96 个 ThreeUI 组件的模式卡，只用来看「场景→结构→技术要点」，不照抄）。

---

## 2. UI 组件库

### 2.1 shadcn/ui（后台默认）
- **是什么**：不是依赖包，而是**代码分发式**组件集（CLI 把组件源码拷进你的项目），建在 Radix primitives + Tailwind 上。
- **什么时候用**：中后台、需要无障碍和键盘操作的密集界面。**默认选它**。
- **装**：`npx shadcn@latest init` → `npx shadcn@latest add button dialog table`。
- **落地要点**：组件进项目后**必须改主题变量**（`--radius`、色板映射到方向 token）；默认 `rounded-lg + shadow` 就是我们禁止的「AI 组件默认值」。
- **坑**：它是「拿代码」不是「装包」，升级要手动合；别在同一个项目混装多套 primitive。
- **许可**：MIT。

### 2.2 Radix Primitives / Base UI
- **是什么**：无样式、可访问的交互原语（弹层、下拉、Tabs…），管行为不管外观。
- **什么时候用**：自己造组件、或 shadcn 没有的部件。
- **坑**：`Dialog`/`Popover` 的 portal 与 z-index 层级要规划；动画用 `data-state` 属性驱动。
- **许可**：MIT。

### 2.3 HeroUI（原 NextUI）
- **是什么**：成品 React 组件库（Tailwind v4 + React Aria），开箱即用的观感。
- **什么时候用**：想快、没有强设计约束的内部工具。
- **别用**：品牌页——它的默认风格辨识度太强（一眼「HeroUI 味」）。
- **装**：`npm i @heroui/react`；官方 skill：`curl -fsSL https://heroui.com/install | bash -s heroui-react`。
- **许可**：MIT。

### 2.4 coss UI（原 Origin UI）
- **是什么**：shadcn 兼容的组件/区块集合，风格更克制。
- **什么时候用**：需要一个「比 shadcn 更完整、比 HeroUI 更中性」的后台。
- **许可**：MIT。

### 2.5 daisyUI
- **是什么**：Tailwind 的纯 CSS 组件类库（无需 JS 组件）。
- **什么时候用**：非 React 后端模板、快速原型、服务端渲染页面。
- **别用**：需要精细控制交互行为时（它不提供行为逻辑）。
- **坑**：自带主题（`data-theme`）一大堆，**必须自定义主题**否则一眼 daisyUI。
- **许可**：MIT。

### 2.6 Magic UI
- **是什么**：shadcn 兼容的「动效组件」集（Marquee、Particles、Animated Beam、Number Ticker…）。
- **什么时候用**：营销页确实需要一个「有说法」的动效组件，且 React/Next 项目。
- **别用**：整页用它——**它是点缀，不是骨架**；也**不要用在后台**。
- **装**：`npx shadcn@latest add "https://magicui.design/r/<component>.json"`（官方 skill 走 `@magicui/*` 注册表）。
- **坑**：粒子/星空/光效类组件是 AI 味重灾区，选「数字滚动、逐字淡入、滚动进度」这类**信息型**动效，别选装饰型。
- **许可**：MIT。

### 2.7 Aceternity UI / React Bits / Uiverse.io
- **是什么**：创意组件/特效市场（大量花哨动效、纯 CSS 片段）。
- **什么时候用**：**取材与灵感**——看它们怎么实现一个效果，然后用自己的 token 重写。
- **别用**：直接贴进项目（配色、动画曲线、层次都不一致，拼起来就是「AI 拼贴感」）。
- **许可**：各自不同（Uiverse 多为免费社区片段），商用前确认。

### 2.8 手机交互专用
| 库 | 用途 | 要点 |
|---|---|---|
| **Vaul**（React） | 底部抽屉（drawer） | 自带拖拽关闭、`snapPoints`；正是手机网页最需要的交互；MIT |
| **Embla Carousel** | 拖拽轮播 | 轻、`dragFree` + `align` 控制；手机上比自己写 swipe 稳 |
| **Sonner** | Toast | React 生态最省事的通知；手机上**只出现在顶部或拇指区上方** |
| **cmdk** | 命令面板 | PC 后台的 `⌘K` 面板；手机上退化为搜索框 |
| **NumberFlow** | 数字滚动 | 业绩/工资数字变化的跟手动效，有质感不花哨 |

---

## 3. 图标库

| 库 | 风格 | 什么时候用 | 许可 |
|---|---|---|---|
| **Lucide**（lucide.dev） | 1.5px 线性、一致性好 | **默认选它**（ICON 首选） | ISC |
| **Phosphor**（phosphoricons.com） | 6 种字重，可粗细呼应排版 | 需要「同一图标不同粗细」时 | MIT |
| **Tabler Icons** | 2px 线性、数量多 | 后台密集界面 | MIT |
| **Iconify / icones.js.org** | 聚合 150+ 图标集 | 快速找图标（**落地时挑一个主库**，别混 5 套风格） | 各自 |
| **Simple Icons** | 品牌 logo（含抖音、B站、小红书） | 平台标识 | CC0 |

- **纪律**：一个项目**只用一个主图标库**；描边粗细与文字粗细匹配；图标尺寸只用 2–3 档（16/20/24）；**不用 emoji 当图标**。
- **手机**：图标可点区域 ≥44px，视觉尺寸可以小，用 padding 撑开。

## 4. 字体

### 4.1 中文（重点：中文字体文件大，必须节制）
| 字体 | 气质 | 用途 | 许可 |
|---|---|---|---|
| 系统栈（PingFang SC / 微软雅黑 / Noto Sans CJK） | 中性 | **正文默认**——零加载成本 | 随系统 |
| **Noto Sans SC** / **Noto Serif SC** | 中性无衬线 / 阅读衬线 | 需要统一跨端观感时；衬线用于 C 方向标题 | OFL |
| **霞鹜文楷 LXGW WenKai** | 手写楷体、有人味 | 叙事标题、引文（**正文不用**，笔画太细长文易累） | OFL |
| **思源黑体/宋体**（同 Noto CJK 家族） | 万能 | 印刷感需求 | OFL |
| **MiSans / HarmonyOS Sans** | 现代、笔画干净 | 界面标题 | 各自免费商用（小米/华为授权，需确认条款） |
| **得意黑 Smiley Sans** | 张扬、倾斜 | 海报级标题（**只在 C 方向大字用**） | OFL |
| 站酷高端黑/快乐体、阿里巴巴普惠体 | 品牌感 | 活动页标题 | 免费商用（阿里/站酷授权） |

- **加载策略**：正文走系统字体栈（`-apple-system, "PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif`）；只在**标题**用 Web 字体，且用 `fonttools` 子集化 + `woff2`（`font-display: swap` 或 `optional`）。
- **渠道**：Google Fonts 直连不稳定，用 `fonts.loli.net` / `fonts.googleapis.cn` 镜像，或从 jsDelivr/自托管取 `@fontsource/noto-sans-sc`。
- **纪律**：一个页面**最多 2 个字族**；中文标题不要用纯英文无衬线（Space Grotesk）硬排——中英混排要单独设定间距与字号。

### 4.2 西文
| 字体 | 气质 | 用途 |
|---|---|---|
| Inter / Geist | 中性 UI | 界面数字与英文正文 |
| **Space Grotesk + Space Mono** | 仪器感 | B 方向（Nothing 式）标题/标签 |
| Instrument Serif / Playfair | 编辑感 | C 方向标题 |
| JetBrains Mono / IBM Plex Mono | 代码 | 数据、代码、标签 |

## 5. 图片与插画

| 来源 | 用途 | 要点 / 许可 |
|---|---|---|
| **自有素材**（团播直播照、主播写真） | 首选 | 有版权、有真人物，是去 AI 味最强武器 |
| **Unsplash / Pexels** | 通用配图 | 免费商用；**避免「商务握手」「团队围桌」这类库存感图** |
| **Pixabay** | 补充 | 同上，质量参差 |
| **unDraw / Storyset** | 插画 | ⚠️ 默认「扁平人物插画」是 AI 味重灾区，**尽量不用**；非要插画优先线性几何图 |
| 自绘 SVG 几何 | 装饰 | 一条线、一个圆、一组刻度就够，比插画高级 |
| 生成式图片 | 主视觉概念图 | 只用抽象/材质/光影类（**不要生成人物**，容易假） |

- 图片处理：`object-fit: cover` + 暗角渐变保证文字可读；手机上 `srcset` 给 1x/2x；**首屏图压缩到 200KB 内**。
- **不要用带水印或来源不明的图**（尤其人物照）。

## 6. 参考与风格库（借用原则，不换皮）

- `templates/web-designs/`（54 个知名站点拆解：Stripe / Linear / Vercel / Apple …）：看**结构、信息密度、层级处理**，不看配色。
- `references/threeui/`：3D/WebGL/落地页的首屏与背景模式库（96 家族）；手机慎用，PC 参考。
- `references/transitions/`：27 个 UI 微交互过渡的 token 与实现（含 `_root.css` 动效 token）——**微交互直接用这里**，不要每页重发明。
- `references/pretext/`、`templates/pretext/`：中文排版创意（大字、竖排、字距玩法）——**A/C 方向的标题可用**。
- `bundles/agent-ui-kit/`：AI 应用界面（会话流、工具调用卡、审批卡、记录表）——做 AI 产品后台直接用。
- `bundles/landing-kit/`：**v2 已删除**（其 hero/特性卡默认是紫蓝渐变 + 毛玻璃 + emoji 标题 + 悬停翻卡，四项都踩本版禁项）。落地页结构请用 `templates/story-scroll/index.html`，或从 `templates/web-designs/` 借骨架后按方向 token 重刷。

## 7. 外部 skill 参考（可吸收，注明出处）

| 来源 | 拿什么 | 许可 |
|---|---|---|
| Emil Kowalski `skills`（emil-design-eng / apple-design / pick-ui-library） | 动效手感（时长、缓动、可中断）、iOS 手感、选库判断 | MIT |
| Paul Bakaus `impeccable` | `craft-floor` 质量底线、反 slop 清单、放大招思路 | Apache-2.0 |
| Dominik Martin `nothing-design-skill` | 减法立场、三层法则、单色体系 | MIT |
| 明哥 `前端优化Skills`（398 skill） | 组件库/动效库官方 skill 的具体用法与坑（本文件 §1–§4 的一手来源） | 各库原许可 |
