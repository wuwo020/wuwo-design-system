# 05 工具调用 Chips（Tool Chips）

组合效果：Agent 的代码编辑/工具调用显示为紧凑 chip：图标 + 动作摘要 + 可展开差异预览。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Tool chips | AI 界面模式 | BeautifulUI（beautifului.dev，Tool Chips） |
| 折叠展开 | 过渡 | transitions-dev（21-accordion） |

---

## 💻 结构示例

```html
<div class="tool-chip">
  <div class="chip-head">
    <span class="chip-icon">✎</span>
    <span class="chip-title">Write 204 lines</span>
    <code class="chip-file">ChurnSchedule.tsx</code>
    <span class="chip-status ok">✓ built in 1.2s</span>
  </div>
  <pre class="chip-diff">+ const windows = slots.filter(s => s.temp <= -12)
+ return schedule(windows, { hero: "pistachio" })</pre>
</div>
```

---

## 🎨 关键样式（可复用）

```css
.tool-chip {
  border-radius: var(--radius-md);
  border: 1px solid rgba(255,255,255,.07);
  background: rgba(255,255,255,.03);
  overflow: hidden;
}
.chip-head { display: flex; align-items: center; gap: 8px; padding: 8px 12px; }
.chip-file { font-family: var(--font-mono); font-size: 12px; color: var(--mist); }
.chip-status { margin-left: auto; font-size: 12px; }
.chip-status.ok { color: var(--tide); }
.chip-diff {
  padding: 10px 12px; margin: 0; border-top: 1px solid rgba(255,255,255,.05);
  font-family: var(--font-mono); font-size: 12px; line-height: 1.6;
  background: rgba(0,0,0,.2); overflow-x: auto;
}
.chip-diff .add { color: var(--tide); } .chip-diff .del { color: var(--rose); }
```

---

## 🎯 与 wuwo 结合

- Chip 是「一次动作」的档案卡：做了什么、改了哪个文件、结果如何，三行内讲完。
- diff 行用等宽字体 + 语义色（+潮青/-玫瑰），暗底上够亮不刺眼。
- 多 chips 纵向堆叠成操作流；横向放不下就选 06 任务行列表。
