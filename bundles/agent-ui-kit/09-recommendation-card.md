# 09 推荐+置信度卡（Recommendation Card）

组合效果：Agent 建议 + 置信度条 + 主操作 + 「替代方案」折叠区。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Recommendation card | AI 界面模式 | BeautifulUI（beautifului.dev，Recommendation Card） |
| 卡片 hover | 过渡 | transitions-dev（19-card-tilt 可选） |

---

## 💻 结构示例

```html
<div class="rec-card">
  <div class="rec-head">
    <h4>Want me to place this restock order?</h4>
    <span class="rec-confidence">High confidence</span>
  </div>
  <p class="rec-body">Reorder waffle cones from <code>cone_king</code> with lead time <code>7_days</code>.</p>
  <div class="rec-meter"><span style="width:82%"></span></div>
  <div class="rec-actions">
    <button class="btn-primary">Accept</button>
    <button class="btn-ghost">Alternatives</button>
  </div>
  <details class="rec-alts"><summary>Other options</summary>
    <p>Switch to vanilla_madagascar · <em>Needs review</em></p>
    <p>Full restock across every SKU · <em>No signal</em></p>
  </details>
</div>
```

---

## 🎨 关键样式（可复用）

```css
.rec-meter { height: 4px; border-radius: 999px; background: rgba(255,255,255,.08); overflow: hidden; }
.rec-meter span {
  display: block; height: 100%; border-radius: 999px;
  background: linear-gradient(90deg, var(--lilac), var(--tide));
}
.rec-confidence { font-size: 12px; padding: 3px 10px; border-radius: 999px;
  background: rgba(125,220,196,.12); color: var(--tide); }
.rec-alts summary { color: var(--dim); font-size: 13px; cursor: pointer; }
.rec-alts em { color: var(--amber); font-style: normal; font-size: 12px; }
```

---

## 🎯 与 wuwo 结合

- 置信度等级三档：高=潮青、中=琥珀、低=玫瑰；渐变只在进度条用（紫→青，克制）。
- 主操作=接受（-lilac 实底），次级=替代方案（ghost）；「需复核」标记用琥珀。
- 建议正文要可执行：对象+动作+参数用 `<code>` 强化，不写模糊空话。
