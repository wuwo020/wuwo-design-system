# 11 表格差异预览（Diff Table）

组合效果：AI 对表格数据的批量修改建议：行级新增/删除高亮、点击 toggle 应用、底部汇总条。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Diff table | AI 界面模式 | BeautifulUI（beautifului.dev，Diff Table） |
| 行高亮过渡 | 过渡 | transitions-dev（01-card-resize / 09-icon-swap） |

---

## 💻 结构示例

```html
<div class="diff-table">
  <table>
    <thead><tr><th>Flavor</th><th>Category</th><th>Supplier</th><th></th></tr></thead>
    <tbody>
      <tr class="row-del"><td>Rocky Road</td><td>Classic</td><td>aurora-scoops</td><td>✕</td></tr>
      <tr class="row-add"><td>Pistachio</td><td>Seasonal</td><td>maple-orbit</td><td>＋</td></tr>
    </tbody>
  </table>
  <footer class="diff-summary">
    <span>2 removals · 1 addition</span>
    <button class="btn-primary">Apply 3 changes</button>
  </footer>
</div>
```

---

## 🎨 关键样式（可复用）

```css
.diff-table { border: 1px solid rgba(255,255,255,.08); border-radius: var(--radius-md); overflow: hidden; }
.diff-table th { text-align: left; padding: 8px 12px; font-size: 12px; color: var(--dim);
  background: rgba(255,255,255,.04); }
.diff-table td { padding: 10px 12px; border-top: 1px solid rgba(255,255,255,.05); font-size: 14px; }
.row-del { background: rgba(255,168,190,.08); }
.row-add { background: rgba(125,220,196,.08); }
.row-del td:first-child { text-decoration: line-through; color: var(--rose); }
.diff-summary {
  display: flex; justify-content: space-between; align-items: center;
  padding: 10px 12px; border-top: 1px solid rgba(255,255,255,.08);
  font-size: 13px; color: var(--mist);
}
```

---

## 🎯 与 wuwo 结合

- 增删语义色严格：+潮青底、-玫瑰底+删除线；**不并行出现第三种高亮**。
- 「点击行切换是否应用」是本模式核心交互：选中行右侧出现勾，汇总条实时更新。
- 批量操作必须配「Apply N changes」汇总，改前让人看清总量。
