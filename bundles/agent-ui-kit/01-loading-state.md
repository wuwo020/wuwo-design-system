# 01 Pixel-grid 加载态

组合效果：像素网格方块随机微抖动+亮度闪烁 + 状态文案 + 已耗时计时（Churning/DriveDots/OrbitSurfer 三种变体）。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Pixel-grid Loader | AI 界面模式 | BeautifulUI（beautifului.dev，Loading State） |
| 加载中 ThinkingOrb | 组件源 | Thinking Orbs（agent 加载态首选） |

---

## 💻 结构示例

```html
<div class="ai-loading" data-variant="churning">
  <div class="loader-grid" aria-hidden="true"></div>
  <div class="loader-label">Churning…</div>
  <div class="loader-elapsed">2.3s</div>
</div>
```

grid 方块由 JS 生成：容器 `display:grid`，N×N 个小方块，随机 `--delay` 与 `--phase`，跑抖动/闪烁 keyframes。

---

## 🎨 关键样式（可复用）

```css
.loader-grid {
  display: grid;
  grid-template-columns: repeat(10, 8px);
  gap: 3px;
}
.loader-grid span {
  width: 8px; height: 8px; border-radius: 2px;
  background: var(--lilac); opacity: .15;
  animation: grid-pulse 1.2s var(--delay) infinite;
}
@keyframes grid-pulse {
  0%, 100% { opacity: .12; transform: translateY(0); }
  50%      { opacity: .55; transform: translateY(-2px); }
}
.loader-label { color: var(--mist); font-size: 14px; }
.loader-elapsed { color: var(--dim); font-variant-numeric: tabular-nums; }
```

---

## 🎯 与 wuwo 结合

- 暗底默认：方块用 `--lilac`/`--tide` 低透明度，勿用彩虹。
- 加载文案用真实动词（Churning/整理中），不建议假百分比；耗时计时真实渲染。
- 比 ThinkingOrb 更「数据感」；纯装饰性微交互用 ThinkingOrb，等待本质是「状态展示」用本模式。
