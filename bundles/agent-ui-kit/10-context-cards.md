# 10 检索上下文卡（Context Cards）

组合效果：检索到的知识块卡片：类型图标 + 标题 + 摘要 + 文件来源 + 字数。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Context cards | AI 界面模式 | BeautifulUI（beautifului.dev，Context Cards） |
| 卡片堆叠展开 | 过渡 | transitions-dev（01-card-resize） |

---

## 💻 结构示例

```html
<div class="context-stack">
  <article class="context-card" data-type="pdf">
    <span class="ctx-badge">PDF</span>
    <h5>Vendor onboarding rule</h5>
    <p class="ctx-snippet">Cold-chain certification must be verified before a new dairy…</p>
    <footer class="ctx-src">Dairy Onboarding SOP.pdf · 290 chars</footer>
  </article>
  <article class="context-card" data-type="csv">
    <span class="ctx-badge">CSV</span>
    <h5>Seasonal demand row</h5>
    <p class="ctx-snippet">Q4 velocity table: pistachio +18%, vanilla +6%…</p>
    <footer class="ctx-src">Sales Velocity Export.csv · 1,250 chars</footer>
  </article>
</div>
```

---

## 🎨 关键样式（可复用）

```css
.context-card {
  padding: 14px 16px; border-radius: var(--radius-md);
  background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.07);
  border-left: 3px solid var(--lilac);
}
.context-card[data-type="csv"] { border-left-color: var(--tide); }
.ctx-badge { font-size: 11px; padding: 2px 8px; border-radius: 999px;
  background: rgba(255,255,255,.07); color: var(--mist); letter-spacing: .04em; }
.ctx-snippet { color: var(--mist); font-size: 13px; line-height: 1.6; }
.ctx-src { color: var(--dim); font-size: 12px; font-variant-numeric: tabular-nums; }
```

---

## 🎯 与 wuwo 结合

- 左侧类型色条是唯一的强标识（紫=文档、青=数据、琥珀=其他），主体克制。
- 卡片句柄显示真实字符数（tabular-nums），信息密度透明。
- 堆叠多时支持「展开/收起全部」，用 card-resize 过渡避免跳动。
