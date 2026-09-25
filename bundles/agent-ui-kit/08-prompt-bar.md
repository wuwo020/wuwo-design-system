# 08 高级 Prompt 输入条（Prompt Bar）

组合效果：带 @来源、/命令、模型选择、附件/听写按钮的输入条。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Prompt bar | AI 界面模式 | BeautifulUI（beautifului.dev，Prompt Bar） |
| 输入清空 | 过渡 | transitions-dev（13-input-clear-dissolve） |

---

## 💻 结构示例

```html
<div class="prompt-bar">
  <div class="pb-chips">
    <span class="pb-chip" data-kind="source">@ Scoop Data</span>
    <span class="pb-chip" data-kind="command">/ web-search</span>
  </div>
  <textarea class="pb-input" placeholder="Type to search sources & files…"></textarea>
  <div class="pb-actions">
    <button aria-label="Attach">＋</button>
    <button aria-label="Dictate">🎤</button>
    <button class="pb-send" aria-label="Send">➤</button>
  </div>
</div>
```

---

## 🎨 关键样式（可复用）

```css
.prompt-bar {
  display: flex; flex-direction: column; gap: 8px;
  padding: 12px; border-radius: 20px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(255,255,255,.09);
  transition: border-color var(--duration-fast), box-shadow var(--duration-fast);
}
.prompt-bar:focus-within {
  border-color: rgba(185,167,255,.45);
  box-shadow: 0 0 0 3px rgba(185,167,255,.12);
}
.pb-chip {
  padding: 3px 10px; border-radius: 999px; font-size: 12px;
  background: rgba(147,160,194,.12); color: var(--mist);
  border: 1px solid rgba(147,160,194,.2);
}
.pb-input { background: transparent; border: 0; resize: none; min-height: 22px;
  color: var(--moon); outline: none; }
.pb-send { border-radius: 999px; padding: 8px 14px; background: var(--fg); color: var(--bg); }
```

---

## 🎯 与 wuwo 结合

- 聚焦态是唯一的强反馈点：紫光描边（非彩虹渐变），其余保持低对比。
- 来源/命令 chip 用 --mist 系弱化，让输入文本保持主角地位。
- 听写/附件属于低频操作，图标按钮放右侧，勿抢发送键（--lilac 实底）。
