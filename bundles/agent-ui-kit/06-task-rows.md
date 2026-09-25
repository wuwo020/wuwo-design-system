# 06 实时任务状态行（Task Rows）

组合效果：Agent 并行任务列表——running / completed / failed 状态、步骤计数、结果摘要。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Task rows | AI 界面模式 | BeautifulUI（beautifului.dev，Task Rows） |
| 状态点动效 | 组件源 | Thinking Orbs 语义色灵感 |

---

## 💻 结构示例

```html
<ul class="task-list">
  <li class="task-row done">
    <span class="task-state"></span>
    <span class="task-name">Verified vendor records</span>
    <span class="task-meta">12 suppliers</span>
    <span class="task-result">Completed</span>
  </li>
  <li class="task-row running">
    <span class="task-state"></span>
    <span class="task-name">Scoring stockout risk</span>
    <span class="task-meta">68%</span>
    <span class="task-result">…</span>
  </li>
  <li class="task-row failed">
    <span class="task-state"></span>
    <span class="task-name">Flagged stale records</span>
    <span class="task-meta">0</span>
    <span class="task-result">Failed</span>
  </li>
</ul>
```

---

## 🎨 关键样式（可复用）

```css
.task-row { display: flex; align-items: center; gap: 10px; padding: 9px 12px; }
.task-row + .task-row { border-top: 1px solid rgba(255,255,255,.05); }
.task-state { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
.task-row.running .task-state { background: var(--amber); animation: breathe 1.4s infinite; }
.task-row.done   .task-state { background: var(--tide); }
.task-row.failed .task-state { background: var(--rose); }
.task-name { flex: 1; color: var(--moon); }
.task-meta { color: var(--mist); font-variant-numeric: tabular-nums; font-size: 13px; }
.task-result { font-size: 13px; }
.task-row.done .task-result { color: var(--tide); }
.task-row.failed .task-result { color: var(--rose); }
@keyframes breathe { 50% { opacity: .35; } }
```

---

## 🎯 与 wuwo 结合

- 状态语义严格三档：运行=琥珀呼吸、完成=潮青、失败=玫瑰——这是状态色，不是装饰色。
- 计数用 tabular-nums 对齐；「完成 ×/×」用真实进度，不用假百分比。
- 单任务进度细节沉到 02 trace 或 05 chip，列表只留一行摘要。
