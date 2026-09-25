# ThreeUI 参考层（threeui.com，2026-08-22 收录）

ThreeUI（by DesignCode / Meng To）= Three.js 组件 + 交互式 shader + 完整落地页库，每项提供**提示词模板 + React 组件（npm `@designcodeio/threeui`）+ 源 HTML**。本目录收录其 **96 个组件家族的全量模式卡**（约 300+ 可视变体），作为 wuwo-design-system 的 **3D/WebGL/落地页特效参考层**——不照搬配色与代码，提炼「场景→结构→技术要点→提示词写法」，落地时一律换算 wuwo token。

## 数据来源与获取方式（实测）

- **全量元数据**：主站 SPA bundle `https://threeui.com/assets/index-*.js` 内嵌完整 catalog（96 家族 × 描述/runtime/passes/交互/变体/contract），一次抓取即得全部，无需逐页爬。
- **详情页提示词模板**（Copy Prompt 按钮）核心结构：
  > "You are working in an existing application. Use the following ThreeUI example as a visual, interaction, and implementation reference for the requested experience. ### Component: {importName} … ### Runtime: … ### Reference brief: {description} — Review the linked source before making changes. Study its structure, styling, composition, motion, interactions… Adapt the relevant ideas to the destination project's existing stack, content, and design language."
- **源 HTML**：`https://threeui.com/<category-path>.html` 直接可取（免费项完整源码；PRO 项返回的是预览壳+外链资产，无实现细节）。示例：`https://threeui.com/landing-pages/kage.html`（244KB 完整 Kage 页）。
- **MCP 端点** `https://threeui.com/api/mcp`：需 Pro 认证（免费不可用）。
- PRO 判定：browse 页 🔒 标记为准。**PRO 共 5 家族**（cross-beam / energy-orb globe / spark-badge / terrain-plume / meng-timeline），只记「存在什么能力」不收录实现。

## 分类速查表

| 分类 | 免费家族 | 免费条目 id | PRO（只记存在） |
|---|---|---|---|
| Landing Pages 整页 | 15 | kage、sekitei、noctiluca、understory、agent-arcana、kairo、volta-atelier、halfwave、centra、meridian、sketchbook(meng-to)、echo-vale、inkbound-river-story、renderlab、aurello | — |
| Hero 首屏 | 16 | ascii-page-transition、orrery、trochil、cortexa、cathode、cadence、attune、betawise×2、axonis、tidecrest、sylva、nocturne、veyra、complete-shelf、bestsellers | — |
| Sections 区块 | 2 | maccess-workflow（3 暗色产品区块）、volta-atelier-hero（拼贴 hero） | — |
| Three.js 场景 | 22 | noema-bloom、receipt-printer、heatmap-badge、hourglass-loader、3D lego(skills-plugins)、wood-icons、sylva-living-world、sunset-valley、temple-night、sakura-branch、landscape(7 天气)、country towers、bookshelf、wallet 系列、iso-motion-grid、iso-charging-dock、365-shapes、iso-mail-lightshafts、scalability-bricks、structure-flow(13 变体)、warp-field、woven-cloth | — |
| Backgrounds 背景 | 12 | predictive-arc(8)、liquid-form、crt、hypnotic-loops(4)、noise-flow(at-the-horizon)、elements(5 元素)、particle-orb、recursive-erosion、quantera-trading、constellation-field(9)、portal-field(5)、laser(matrix-field 4) | cross-beam、globe(energy-orb 3)、spark-badge(4)、terrain-plume |
| UI Elements | 8 | character-carousel、gallery、genie-dock、engraved-certificate、diagnostics-panel(3)、skeuomorphic-toggle、wireframe-forms(3)、brand-orbs(23 品牌) | — |
| Buttons 按钮 | 4 | rectangle glass 系(13 变体)、circle buttons(3)、shader buttons star-portal(6)、liquid-metal button(3) | — |
| CSS 纯 CSS | 5 | performance-gauges(4 表盘)、uplink-loader、koi-studies、animated-top-dock、sketchbook(书页) | — |
| Text Animation 文字动效 | 5 | typography-vortex、semantic-bloom、text-path studies(6)、gradient-collection(4)、article-headings(3) | — |
| Motion Design 定帧动效 | 2 | understory sting、sylva sting | meng-timeline |

## 选型路由（按需求找模式）

1. **整页叙事落地页**（滚动章节驱动一个连续 3D 世界）→ `landing-pages.md`：kage（夜路京都）、sekitei（枯山水七章）、noctiluca（深海下潜）
2. **Hero 一屏冲击** → `heroes-sections.md`：产品实物=cathode/isometric；抽象科技=cortexa 点云胸像/orrery 轨道仪；文字主导=ascii-page-transition
3. **背景场域（低干扰氛围）** → `backgrounds-fields.md`：粒子网络=constellation-field；终端/CRT=crt；流体金属=liquid-form；元素系=elements
4. **3D 小场景/加载态/图标** → `threejs-scenes.md`：hourglass-loader 加载、brand-orbs 品牌球、receipt-printer 出票交互
5. **按钮/CTA 特效** → `glass-buttons.md`：玻璃拟态系=rectangle/circle buttons；重特效=shader/liquid-metal（生产慎用）
6. **标题文字动效** → `text-motion-stings.md`：vortex 旋涡、particle wordmark、gradient carousel
7. **纯 CSS 无 WebGL** → `ui-elements-css.md`：gauges 表盘、dock、koi 卡片堆、uplink loader

## wuwo token 映射（强制换算表）

ThreeUI 原作大量用青绿(emerald)/琥珀/银灰/纯黑底，直接照搬违反机主审美红线。落地时按下表换算：

| ThreeUI 常见色 | 用途 | 换算到 wuwo token（v2.1） |
|---|---|---|
| Emerald / Amber / Violet / Rose 等彩色主色 | 粒子/streak/强调 | 全部收敛为当前调色板的**唯一** `--accent`（香槟 `#C9A96E` / 胭脂 `#A8544A` / 青瓷 `#93BBAA` 三选一） |
| Silver/chrome（liquid metal） | 材质高光 | 保留材质，tint 到 `--fg` 骨白，**不加彩色辉光** |
| Pure black `#000` 底 | 场景底色 | 换 `--bg`（石墨 `#0C0C0D` / 暖墨 `#0F0E0D` / 深岩 `#0B0F12`），并叠颗粒层 |
| White text `#FFF` | 正文 | `--fg` 骨白；次要用 `--fg-2`（同色 .74 透明），**不换成蓝灰** |

其他红线执行：一次只用 1 个点缀色（structure-flow 13 变体只挑一个色系）；玻璃拟态仅用于内容叠内容场景；圆角按方向 A：媒体 4px、控件胶囊。

## 使用纪律

1. **版权**：免费项源 HTML 结构/技术可学习借鉴；交付物必须是转化后的原创实现（换 token、换字体、换构图姿态），不逐字节拷贝专有文件。PRO 项零实现细节。
2. **性能**：多数场景是 3–17 个渲染 pass + bloom 后处理，生产页面最多保留 1 个重型 canvas；加载态/背景类选单 pass 方案。
3. **Reduced motion**：原作全部内建 `prefers-reduced-motion` 与 visibility-pause，我们的实现必须同样带上。
4. **提示词复用**：给 AI 编码器描述目标效果时，按「Component 场景一句话 + Runtime 技术栈 + Reference brief 行为清单」三段式写，比泛泛说"做个炫酷 hero"成功率高得多。

## 文件索引

- `landing-pages.md` — 整页叙事模式（15）
- `heroes-sections.md` — Hero 首屏 + 区块（18）
- `threejs-scenes.md` — Three.js 交互场景（22）
- `backgrounds-fields.md` — 背景/场域（16）
- `ui-elements-css.md` — UI 元件 + 纯 CSS（13）
- `glass-buttons.md` — 按钮系统（4）
- `text-motion-stings.md` — 文字动效 + 定帧 sting（8）
