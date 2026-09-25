# 双端适配：手机网页优先，PC 网页同等对待

> 机主的场景：做的主要是**网页**（不是 App），手机访问多，但 PC 也有人看（后台、招聘方、电脑上打开链接）。
> 所以原则是 **mobile-first 写 CSS，但 PC 不是「手机版拉宽」**：两端各自有自己的构图，共享同一套内容和 token。

## 1. 断点与布局切换

```css
/* 从手机写起，向上增强。只用 3 个断点，别更多 */
/* 默认 <640px：手机竖屏 */
@media (min-width: 640px)  { /* 大屏手机横屏 / 小平板 */ }
@media (min-width: 1024px) { /* PC：布局换形态 */ }
@media (min-width: 1440px) { /* 大屏：只加留白和最大宽度，不再加列 */ }
```

- **按内容断，不按设备断**：哪里挤了就在哪里断。组件级适配优先用 **container query**（`container-type: inline-size` + `@container (min-width: 480px)`），这样同一张卡在侧栏和主栏里各自正确。
- 流体字号/间距用 `clamp()`：`font-size: clamp(32px, 7vw + 8px, 96px)`，一条规则同时管两端，减少断点。
- 内容最大宽度：正文 `36em`（中文）/ 版心 `1200–1320px`，大屏两侧留白，**不无限拉宽**。

## 2. 两端的构图差异（同一内容，不同形态）

| 模块 | 手机网页 | PC 网页 |
|---|---|---|
| 首屏 | 竖向满屏，主角占 60–75% 高，标题压在影像下缘 | 左右分栏（文 5 : 图 7）或全宽影像 + 左下标题 |
| 滚动叙事 | 单列，pin 住一屏让内容在里面换 | 左侧文字滚动、右侧画面 sticky 跟随换帧 |
| 横向画廊 | 原生横滑 + `scroll-snap`（拇指天然会左右滑） | 竖向滚轮驱动横移（ScrollTrigger + pin），或显示箭头+拖拽 |
| 导航 | 底部固定栏或右上菜单，主操作在拇指区 | 顶部横排导航，hover 有反馈 |
| 列表/卡片 | 单列大卡，整卡可点 | 2–3 列，或表格（后台） |
| 弹层 | **底部抽屉**（可下滑关闭） | 居中 modal 或右侧面板 |
| 表单 | 单列，大输入框，键盘不遮挡提交按钮 | 两列分组，Tab 键顺序正确 |
| 目录 | 顶部可折叠 / 阅读进度条 | 左侧或右侧 sticky 目录，当前节高亮 |

**判断标准**：把手机截图和 PC 截图并排，如果 PC 看起来像「手机页面放大并居中」，就是没做 PC 适配。

## 3. 输入方式：触摸与鼠标分开对待

```css
/* hover 效果只给真有鼠标的设备，否则手机点击会「粘住」hover 态 */
@media (hover: hover) and (pointer: fine) {
  .card:hover { transform: translateY(-4px); }
}
/* 按下反馈两端都给——手机上这是唯一的触觉替代 */
.btn:active { transform: scale(.97); }
```

- **触摸目标 ≥ 44×44px**；PC 密集界面可以 ≥ 32px，但用伪元素扩大可点区域，不放大视觉。
- 手机**反馈要在手指按下时立刻出现**（`pointerdown` / `:active`），不要等 `click`。
- 手机上没有 hover，所以 **hover 里藏的信息必须有别的途径拿到**（点击展开、直接显示）。
- PC 专属增强：hover 预览、键盘快捷键、`cursor` 样式、滚轮横移、拖拽。手机专属增强：滑动手势、下拉关闭、`scroll-snap`。

## 4. 手机网页的坑（必查清单）

- **视口高度**：全屏区块用 `min-height: 100svh`（小视口，地址栏展开时）或 `100dvh`（动态），**禁止裸 `100vh`**——iOS Safari 地址栏伸缩会让内容跳动或被遮。pin 叙事的段落高度用 `svh` 算，避免滚动中跳。
- **安全区**：底部固定栏 `padding-bottom: max(12px, env(safe-area-inset-bottom))`，并在 `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">`。
- **不要禁止缩放**（`user-scalable=no` 伤无障碍）。
- **输入框字号 ≥ 16px**，否则 iOS 聚焦时自动放大页面。
- **滚动穿透**：打开抽屉/弹层时锁背景滚动（`overflow: hidden` 放 `html`，或 `overscroll-behavior: contain` 放弹层）。
- **地址栏伸缩触发 resize**：ScrollTrigger 设 `ScrollTrigger.config({ ignoreMobileResize: true })`，否则每次地址栏动都会重算、画面闪。
- **横向溢出**：任何元素宽度超出屏幕都会导致整页左右晃。交付前在 375px 下检查 `document.documentElement.scrollWidth === innerWidth`。
- **图片**：`srcset` + `sizes` 给手机小图；首屏图 `fetchpriority="high"`，其它 `loading="lazy"`。
- **字体**：中文字体很大，只加载用到的字重；首屏用系统字体兜底（`font-display: swap`），避免白屏。
- 微信内置浏览器：视频自动播放要 `muted playsinline`，`position: sticky` 在旧版 X5 内核可能失效——关键 pin 效果用 ScrollTrigger 的 `pin`（transform/fixed 方案）而不是纯 CSS sticky。

## 5. 性能预算（手机是瓶颈）

- 中端安卓机上滚动必须 55fps 以上。**只动 `transform` 和 `opacity`**；`filter: blur`、`backdrop-filter`、大面积 `box-shadow` 在手机上最贵，滚动中不要动画它们。
- 同屏持续动画的元素 ≤ 3 个；离开视口的动画暂停（IntersectionObserver / ScrollTrigger `toggleActions`）。
- WebGL/Three.js 背景：手机上降级（降分辨率 `setPixelRatio(Math.min(devicePixelRatio, 1.5))` 或换成静态图/视频）。
- 用 `gsap.matchMedia()` 给手机和 PC 注册**不同强度**的动画，而不是一套动画硬跑两端（见 `scroll-gesture-motion.md` §5）。

## 6. 验收（两端都要真截图看）

交付前用 Playwright（本机有 chromium）分别截：
- **手机** 390×844（`isMobile: true, hasTouch: true, deviceScaleFactor: 3`）：首屏、滚动 30%/60%/90% 各一张。
- **PC** 1440×900：同样位置各一张。
- 检查：无横向溢出、文字不被影像吃掉、首屏主角明确、PC 不是「放大的手机页」、reduced-motion 下内容完整可读。
- 验收脚本模板：`scripts/dual-screenshot.py`。
