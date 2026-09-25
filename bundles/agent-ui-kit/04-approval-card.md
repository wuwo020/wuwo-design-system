# 04 人机确认卡（Approval Card）

组合效果：Agent 执行前向人确认的问题卡：问题 + 单选选项 + 次级操作。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Approval card | AI 界面模式 | BeautifulUI（beautifului.dev，Approval Card） |
| 卡片入场 | 过渡 | transitions-dev（07-panel-reveal） |

---

## 💻 结构示例

```html
<div class="approval-card" role="dialog" aria-labelledby="appr-q">
  <p id="appr-q">How many flavors should we launch?</p>
  <div class="appr-options" role="radiogroup">
    <label><input type="radio" name="flavors"> Three (core line)</label>
    <label><input type="radio" name="flavors"> Five (full case)</label>
    <label><input type="radio" name="flavors"> Just one hero</label>
  </div>
  <div class="appr-actions">
    <button class="btn-primary">Continue</button>
    <button class="btn-ghost">Ask again</button>
  </div>
</div>
```

---

## 🎨 关键样式（可复用）

```css
.approval-card {
  padding: 20px; border-radius: var(--radius-lg);
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.08);
  backdrop-filter: blur(12px);
  max-width: 420px;
}
.appr-options label {
  display: flex; align-items: center; gap: 10px;
  padding: 10px 12px; border-radius: var(--radius-md);
  border: 1px solid rgba(255,255,255,.08); cursor: pointer;
}
.appr-options label:has(input:checked) {
  border-color: rgba(125,220,196,.5);
  background: rgba(125,220,196,.08);
}
```

---

## 🎯 与 wuwo 结合

- 确认卡是「Agent 的谨慎时刻」，视觉要点：不抢主流程、但一眼可读选项。
- 选中态用--tide（成功语义），禁用项用 --dim；按钮主次分明（primary 紫、ghost 透明）。
- 供「仅此一次/总是允许」的常驻选项可放卡片底部，用 --mist 小字。
