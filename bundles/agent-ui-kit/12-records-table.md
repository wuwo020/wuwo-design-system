# 12 记录网格（Records Table）

组合效果：CRM 式数据网格：列排序、行内标签、关系强度、操作列。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Records table | AI 界面模式 | BeautifulUI（beautifului.dev，Records Table） |
| 表格/排序 | 组件源 | Appica UI（Data Display） |

---

## 💻 结构示例

```html
<table class="records-table">
  <thead>
    <tr><th><button class="th-sort" data-sort="company">Company ▾</button></th>
        <th>Categories</th><th>Last interaction</th>
        <th>Connection</th><th></th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="#">Alpine Churn — Zürich</a></td>
      <td><span class="tag">B2B</span><span class="tag">Gelato</span></td>
      <td>4 days ago</td>
      <td><span class="strength strong">Very strong</span></td>
      <td><button aria-label="更多">⋯</button></td>
    </tr>
  </tbody>
</table>
```

---

## 🎨 关键样式（可复用）

```css
.records-table { width: 100%; border-collapse: collapse; }
.records-table th { position: sticky; top: 0; text-align: left; padding: 8px 12px;
  font-size: 12px; color: var(--dim); background: var(--ink); }   /* 实色，不用玻璃 */
.records-table td { padding: 11px 12px; border-top: 1px solid rgba(255,255,255,.05); font-size: 14px; }
.records-table tbody tr:hover { background: rgba(255,255,255,.03); }
.tag { display: inline-block; padding: 2px 8px; margin-right: 4px; border-radius: 999px;
  background: rgba(147,160,194,.12); color: var(--mist); font-size: 12px; }
.strength { font-size: 12px; }
.strength.strong { color: var(--tide); } .strength.weak { color: var(--amber); }
.strength.none  { color: var(--dim); }
```

---

## 🎯 与 wuwo 结合

- 网格是回读区（Monitor surface）：表头 sticky、行 hover 微光、排序箭头状态清晰。
- 标签/徽章最多两档色（mist 中性 + 语义色），不做彩虹分类。
- 关系强度用文字+色阶（强=潮青/弱=琥珀/无=暗灰），不用表情符号。
