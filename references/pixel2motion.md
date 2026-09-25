# Pixel2Motion 集成参考

- 上游仓库：https://github.com/nolangz/pixel2motion
- 当前核对版本：`e9faedb28930df0da2acf17da00c80730a78cfe8`（MIT）
- 定位：把 PNG/JPG/WebP/截图 Logo 变成低复杂度、可编辑、可动效的 SVG，再交付独立 HTML 动效与可复核 QA 证据。

## 何时使用

触发词包括：Logo 动画、品牌片头、Logo reveal、splash screen、SVG 动效、像素 Logo 转矢量、加载/待机/hover 品牌标记、品牌 motion。它是 `wuwo-design-system` 的 Logo-to-Motion 专用分支；普通页面转场、产品 UI 动效仍走本 skill 的 transitions / Amicro / ThinkingOrbs。

## 核心工作流

1. **先写 `motion_spec.md`**：品牌动势词、使用场景、语义部件清单、编排草图。
2. **先做最低复杂度拟合**：原语 → 原语组合 → 少量 Bézier → 平滑轮廓；像素追踪只作测量/起点，不能自动当最终艺术稿。
3. **静态矢量 QA**：渲染 `logo.svg`，生成 overlay 与 IoU/像素差报告；平滑度、端点、宽度、负空间、结构优先于盲目追求 IoU。
4. **为动效结构化 SVG**：每个语义部件有稳定 id（如 `#mark`、`#wordmark`、`#dot`）；需要 draw-on 的路径设 `pathLength="1"`；动画部件不要依赖 `nth-child`。
5. **再编排动效**：依据 Disney 12 原则，默认 anticipation/action/follow-through = 20/50/30；按使用场景选时长，所有部件共享可复核时钟。
6. **用 showcase HTML 交付**：主动画、至少 3 个 atomic motion、Replay/slow/speed 控制、`prefers-reduced-motion`、`?t=<ms>`、`?static=1`、`window.__p2mReady`。
7. **做确定性 Motion QA**：关键时间帧、交叉点/部件交接风险帧、easing probe、ink-delta continuity sweep，以及最终帧与静态渲染的 Final Frame Contract。

## 常用命令

```bash
python3 scripts/raster_logo_trace.py source.png --out outputs
python3 scripts/render_overlay.py logo.svg source.png \
  --out outputs/fit_iterations/02_refined_overlay.png \
  --render-out outputs/final_render.png --report outputs/fit_metrics.json
python3 scripts/svg_path_audit.py logo.svg --out-svg outputs/bezier_segments.svg \
  --report outputs/bezier_audit.json
python3 scripts/animate_svg_showcase.py logo.svg --css motion.css \
  --out logo_motion.html --title "Logo Motion" --duration-hint 1500
python3 scripts/capture_motion_frames.py logo_motion.html \
  --times 0,300,700,1000,1250,1500 --out outputs/motion_frames \
  --strip outputs/motion_strip.png --compare-final outputs/final_render.png
python3 scripts/probe_motion_continuity.py logo_motion.html \
  --times 500,700,900 --probe "#draw-stroke:stroke-dashoffset"
```

复杂的自交宽 ribbon / ∞ 标记先读上游 `references/ribbon-fitting.md` 与 `reveal-patterns.md` 的 split-fill 方案。不要让高 IoU 的锯齿 trace 通过平滑度门；不要在 `@keyframes` 里用 `var()` 作为 timing-function，写字面量 cubic-bezier 并用 probe 验证。

## 与本设计系统/视频栈的衔接

- Logo fitting、SVG 语义拆分、独立 HTML 动效：优先 Pixel2Motion。
- Wuwo 设计系统仍拥有最终视觉决策：把上游默认色替换为 wuwo token，保持暗夜梦核/亮色变体与反 slop 红线。
- 需要进入 HyperFrames、透明视频、品牌片头或更长叙事：先用 Pixel2Motion 产出静态 SVG + motion spec + QA 证据，再交给 `video/hyperframes` 或 `video/motion-graphics`；不要重新描一套 Logo。
- 最终交付至少保留 `logo.svg`、`motion_spec.md`、`logo_motion.html`、`final_render.png` 与 `motion_strip.png`（若某项未做，明确标注原因）。
