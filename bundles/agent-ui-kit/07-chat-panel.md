# 07 分页聊天面板（Chat Panel）

组合效果：Tab 切换会话主题的聊天面板：会话列表 + 消息流（含推理折叠）+ 底部输入。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Tabbed chat panel | AI 界面模式 | BeautifulUI（beautifului.dev，Chat） |
| Tab 滑动 | 过渡 | transitions-dev（16-tabs-sliding） |

---

## 💻 结构示例

```html
<div class="chat-panel">
  <div class="chat-tabs" role="tablist">
    <button role="tab" aria-selected="true">Flavors</button>
    <button role="tab">Suppliers</button>
  </div>
  <div class="chat-thread">
    <div class="msg user">Compare mint chip to last summer</div>
    <div class="msg agent">
      <details class="msg-reasoning"><summary>Reasoning · 2s</summary><p>…</p></details>
      <p>Mint chip is up 12% with stronger weekend peaks.</p>
    </div>
  </div>
  <div class="composer"><textarea placeholder="Ask anything…"></textarea></div>
</div>
```

---

## 🎨 关键样式（可复用）

```css
.chat-tabs { display: flex; gap: 4px; padding: 6px; border-radius: 999px;
  background: rgba(255,255,255,.04); width: fit-content; }
.chat-tabs button { padding: 6px 14px; border-radius: 999px; color: var(--mist); font-size: 13px; }
.chat-tabs button[aria-selected="true"] { background: rgba(185,167,255,.15); color: var(--lilac); }
.msg { max-width: 78%; padding: 10px 14px; border-radius: var(--radius-lg); line-height: 1.7; }
.msg.user { align-self: flex-end; background: rgba(185,167,255,.14); color: var(--moon); }
.msg.agent { align-self: flex-start; background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.06); }
.msg-reasoning summary { color: var(--dim); font-size: 12px; cursor: pointer; }
```

---

## 🎯 与 wuwo 结合

- 面板级组件，配合 08 输入条组成完整聊天工作区；Tab 药丸滑动用 16-tabs-sliding。
- 用户/Agent 气泡立场分明：用户紫底右对齐、Agent 玻璃底左对齐。
- 推理折叠默认收起（--dim 小字），保留「信任但不可少」的透明度。
