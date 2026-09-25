# 02 可展开推理轨迹（Thinking Traces）

组合效果：Agent 思考时逐条展示步骤轨迹（steps/reasoning/search/coding 四类），每条可展开看细节。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Expandable traces | AI 界面模式 | BeautifulUI（beautifului.dev，Thinking） |
| Trace 展开动效 | 过渡 | transitions-dev（21-accordion / 09-icon-swap） |

---

## 💻 结构示例

```html
<div class="trace-list">
  <button class="trace-item" aria-expanded="false">
    <span class="trace-dot state-progress"></span>
    <span class="trace-title">Reading flavor briefs</span>
    <span class="trace-time">1.2s</span>
    <span class="trace-chevron"></span>
  </button>
  <div class="trace-detail">…展开后的推理摘要…</div>
</div>
```

轨迹类型：`steps`（步骤）、`reasoning`（推理）、`search`（检索）、`coding`（编码），用 `data-kind` 区分徽章文案。

---

## 🎨 关键样式（可复用）

```css
.trace-item {
  display: flex; align-items: center; gap: 10px;
  width: 100%; padding: 10px 12px; border-radius: var(--radius-md);
  background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.06);
}
.trace-dot { width: 8px; height: 8px; border-radius: 50%; }
.state-progress { background: var(--amber); animation: breathe 1.4s ease-in-out infinite; }
.state-idle     { background: var(--dim); }
.state-done     { background: var(--tide); }
.trace-detail {
  display: grid; grid-template-rows: 0fr; transition: grid-template-rows var(--duration-medium);
}
.trace-item[aria-expanded="true"] + .trace-detail { grid-template-rows: 1fr; }
```

---

## 🎯 与 wuwo 结合

- 状态点语义：进行中=琥珀呼吸、完成=潮青、等待=暗灰；不彩虹。
- 展开用 accordion 过渡（21-accordion），chevron 用 `scaleY(-1)` 翻转。
- 轨迹是给用户「信任 Agent」用的，文案要真实步骤，不写空话进度。
