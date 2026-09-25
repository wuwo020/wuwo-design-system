# 滚动与手势驱动的动效（拇指跟手 · 双端）

> 这是 v1 最缺的一块，也是机主明确要的：**画面跟着拇指的滑动实时变化，读起来有沉浸感**。
> 核心原则一句话：**滚动是输入设备**——页面不是「滚到某处播一段动画」，而是「滚动进度 = 动画进度」，手指动多少，画面就动多少。

## 1. 跟手（scrub）而非触发（trigger）

| | 播放式（少用） | 跟手式（默认用这个） |
|---|---|---|
| 行为 | 滚到某位置，动画自己播完 | 动画进度 = 滚动进度，实时映射 |
| 感觉 | 「放了段视频」 | 「我在拨动这个世界」 |
| 用法 | 只用于「揭示」类一次性入场（≤600ms） | 叙事、画廊、图层、文字排版、进度 |

- 跟手动效**不要有缓动惯性以外的「表演」**：`scrub: 0.6`（或 `scrub: true` 最紧）让 GSAP 用少量缓动追上滚动，手感顺滑又不脱节。数值越大越"软"，会上瘾但会显得迟钝，超过 1 就会明显滞后。
- 跟手期间**不要同时做淡入淡出式的 opacity 0→1 整段**，那会让跟手感消失；用位移、缩放、`clip-path`、`filter` 的变化来表达进度。

## 2. 技术选型（按「能不用 JS 就不用」排序）

| 需求 | 首选 | 说明 |
|---|---|---|
| 简单滚入揭示（淡入上移、进度条） | **CSS `animation-timeline: view()` / `scroll()`** | 浏览器原生，跑在合成器线程，手机最省电。Chrome/Edge 支持；Safari/Firefox 用 `@supports (animation-timeline: view())` 兜底 → 不支持就直接显示（不要留白） |
| 复杂叙事（pin + scrub + 分层） | **GSAP ScrollTrigger** | 生态最成熟，`pin`/`scrub`/`snap`/`containerAnimation`/`matchMedia` 齐全 |
| 整屏竖向翻页（类 TikTok 沉浸） | **GSAP Observer** | 归一化 pointer/触屏/滚轮，`onUp/onDown` + `tolerance`，比手写手势稳 |
| 卡片拖拽/滑动删除/惯性 | **GSAP Draggable + InertiaPlugin**（3.13 起免费） | 惯性、边界回弹、吸附都内置 |
| 全局顺滑滚动（PC） | **Lenis**（3KB，MIT） | 只在 `(hover:hover) and (pointer:fine)` 启用；手机保留原生滚动（原生惯性手感更好） |
| 简单跟手（一句话级） | **原生 Pointer Events + `transform`** | 例如底部抽屉、卡片翻转，不必上库 |

**CDN（实测 200）**：
```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/Observer.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.3.26/dist/lenis.min.js"></script>
```
国内访问不稳定时换 `registry.npmmirror.com` 镜像或自托管（见 `library-guide.md` §动效库）。

## 3. 六个可复用配方

### 3.1 文字 scrub 揭示（首屏标题，手机 PC 通用）
```js
// 每行文字随滚动从下方滑入并"擦出"，进度完全跟手
gsap.to(".hero-line", {
  yPercent: 0, opacity: 1, ease: "none", stagger: 0.08,
  scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom 60%", scrub: 0.5 }
});
// 想更"读出来"的感觉：clip-path 从 100% 收到 0
gsap.fromTo(".reveal", { clipPath: "inset(0 0 100% 0)" },
  { clipPath: "inset(0 0 0% 0)", ease: "none",
    scrollTrigger: { trigger: ".reveal", start: "top 85%", end: "top 35%", scrub: 0.4 } });
```

### 3.2 影像视差 + 暗角（沉浸感的主要来源，零成本）
```js
gsap.to(".hero-img", { yPercent: -12, scale: 1.12, ease: "none",
  scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true } });
```
深浅两层的速度差（0.08 / 0.2 / 0.35）就够，**不要超过 3 层**，手机 GPU 顶不住。

### 3.3 横向画廊：手机横滑，PC 滚轮驱动横移（同一份内容）
```js
const mm = gsap.matchMedia();
mm.add("(min-width: 1024px)", () => {          // PC：pin 住，滚轮推动横向
  const track = document.querySelector(".gallery-track");
  const scrollTween = gsap.to(track, {
    x: () => -(track.scrollWidth - window.innerWidth),
    ease: "none",                                  // 必须 none，否则滚动位置对不上
    scrollTrigger: { trigger: ".gallery", pin: true, scrub: 1,
      start: "top top", end: () => "+=" + (track.scrollWidth - window.innerWidth) }
  });
  return () => gsap.set(track, { clearProps: "x" });   // 切回手机时清干净
});
// 手机什么都不做：交给原生横滑 + scroll-snap（拇指手感最好）
```

### 3.4 整屏翻页（Observer，两端都能用）
```js
Observer.create({ target: window, type: "wheel,touch,pointer", tolerance: 40,
  onDown: () => goTo(current + 1), onUp: () => goTo(current - 1) });
```
翻页用 `gsap.to(container, {yPercent: -100 * i})` + `snap`；**必须给「跳过动画」出口**（reduced-motion 或用户连按两次时直接跳，不排队）。

### 3.5 卡片拖拽/左滑忽略（Draggable + 惯性）
```js
Draggable.create(".card", { type: "x", inertia: true,
  bounds: { minX: -320, maxX: 0 },
  onDragEnd() { if (this.x < -120 || this.getVelocityX() < -600) dismiss(this.target); else gsap.to(this.target,{x:0}); }
});
```
判定阈值用「位移 1/3 或速度 600px/s」，两个条件满足其一即视为意图——只看位移会让人觉得「不够狠不动」，只看速度会误触。

### 3.6 底部抽屉（手机主交互，PC 变 modal）
```js
// pointerdown 记录起点 → pointermove 实时 set y（跟手）→ pointerup 按位移/速度决定吸附
sheet.addEventListener("pointerdown", e => { startY = e.clientY; sheet.setPointerCapture(e.pointerId); });
sheet.addEventListener("pointermove", e => { if (startY == null) return;
  const dy = Math.max(0, e.clientY - startY); sheet.style.transform = `translateY(${dy}px)`;
  backdrop.style.opacity = 1 - dy / sheet.offsetHeight * .6; });   // 背景跟着变暗 = 跟手的关键
sheet.addEventListener("pointerup", e => { const dy = e.clientY - startY;
  const close = dy > sheet.offsetHeight * .3 || velocity > 600;
  gsap.to(sheet, { y: close ? sheet.offsetHeight : 0, duration: .35, ease: "power2.out", onComplete: reset }); });
```
注意：`touch-action: none` 只加在把手区域，否则整页滚不动。

## 4. 手势/滚动的硬性纪律

- **跟手元素必须 `will-change: transform` 或用 GSAP 自动管理**；连续动画结束后清掉（`clearProps`），长期挂着会吃内存。
- **不要在 `scroll` 事件里写逻辑**（手机每帧都触发）：交给 ScrollTrigger / IntersectionObserver / CSS 时间线。
- **pin 的分段要够长**：`end: "+=150%"` 起步，短了会「嗖」一下过去，沉浸感全无。手机建筑 pin 段落用 `svh` 计算高度。
- **pin + 地址栏伸缩**：`ScrollTrigger.config({ ignoreMobileResize: true })`。
- **滚动条与刷新**：动态内容（图片加载、字体）加载完后 `ScrollTrigger.refresh()`；SPA 切页/组件卸载时 `mm.revert()` 或 `ScrollTrigger.getAll().forEach(t => t.kill())`，否则监听器泄漏、页面越用越卡。
- **`prefers-reduced-motion: reduce` 必须真的降级**：不是「动画变快」，而是**取消 pin/scrub、跳到终态**，内容完整可读。
  ```js
  mm.add({ reduce: "(prefers-reduced-motion: reduce)", ok: "(prefers-reduced-motion: no-preference)" }, (ctx) => {
    if (ctx.conditions.reduce) { gsap.set(".hero-line", { yPercent: 0, opacity: 1 }); return; }
    /* 正常动画 */
  });
  ```
- **别把关键内容做成动画才有**：动画只是加分，JS 失败/被拦也要能读到全部文字（SEO 和弱网都靠这个）。
- **0 进度 = 可读终态**：首屏第一行标题绝不交给 scrub——ScrubTrigger 在页面顶部进度为 0，隐藏式揭示会让首屏变成一块黑屏（实测踩过）。只让**第二行标题、引言、影像位**跟手揭示。同理，任何「滚动到 X 才出现」的东西，用户停在顶部时必须已经能看到关键信息。
- **验收必须滚到 100%**：底部 4% 是事故高发区（安全区、页脚、按钮贴边）。截图清单里 0% / 33% / 66% / 100% 四个位置都不能省。

## 5. 双端差异（同内容不同强度）

```js
const mm = gsap.matchMedia();
mm.add("(max-width: 639px)", () => {   // 手机：短、轻、竖屏叙事
  gsap.to(".figure", { yPercent: -8, ease: "none", scrollTrigger: { trigger: ".figure", scrub: true } });
});
mm.add("(min-width: 1024px)", () => {  // PC：pin + 横向 + 多层视差
  /* 3.3 的横向画廊等 */
});
```
- 手机：视差 ≤2 层、位移 ≤10%、竖向叙事、不加载 WebGL、不加全局 smooth scroll。
- PC：可以上 pin + 横向 + Lenis + 鼠标跟随，但**所有效果都要有非 hover 的等价表达**（手机用户也是客户）。
- `gsap.matchMedia()` 在条件不再匹配时会**自动 revert** 该块创建的动画和 ScrollTrigger，是双端差异唯一正确的做法。

## 6. 性能与验证

- 只动 `transform` / `opacity` / `clip-path`；**滚动中禁止**动画 `filter: blur`、`backdrop-filter`、`box-shadow`、`width/height`。
- 真机验证（不要只看 DevTools 模拟器）：本机有 chromium，用 Playwright 设备模拟截图（`scripts/dual-screenshot.py`），或让机主手机打开链接。
- 检查项：滚动是否掉帧、跟手是否滞后（`scrub` 值）、地址栏伸缩是否跳、横屏是否错位、reduced-motion 下内容是否齐全、关掉 JS 是否还能读到内容。
