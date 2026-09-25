# 03 流式文本+内联来源（Streaming Text）

组合效果：AI 回答逐字流式输出、句内嵌来源徽章（favicon+域名）、结尾附带 follow-up 建议按钮。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Streamed answer + sources | AI 界面模式 | BeautifulUI（beautifului.dev，Streaming Text） |
| 光标闪烁 | 过渡 | transitions-dev（15-shimmer-text 变体） |

---

## 💻 结构示例

```html
<div class="stream-text">
  <p>Pistachio is your fastest-growing flavor — sales are up 23%…</p>
  <a class="inline-source" href="…">
    <img src="favicon.png" alt="" width="16" height="16"> scoopdata.io
  </a>
</div>
<div class="follow-ups">
  <button>Which flavors sell best in winter</button>
  <button>Compare gelato and soft serve margins</button>
</div>
```

流式输出：JS 按 token 追加文本；每追加完一个来源就渲染一个 `inline-source` 徽章；句子结束光标隐藏。

---

## 🎨 关键样式（可复用）

```css
.stream-text { line-height: 1.8; color: var(--moon); }
.stream-caret { display: inline-block; width: 2px; height: 1em;
  background: var(--lilac); animation: caret 0.9s steps(1) infinite; vertical-align: -0.15em; }
@keyframes caret { 50% { opacity: 0; } }
.inline-source {
  display: inline-flex; align-items: center; gap: 5px;
  padding: 2px 8px; border-radius: 999px; font-size: 12px;
  background: rgba(185,167,255,.1); border: 1px solid rgba(185,167,255,.25);
  color: var(--mist); vertical-align: baseline;
}
.follow-ups { display: flex; gap: 8px; flex-wrap: wrap; }
.follow-ups button {
  padding: 6px 12px; border-radius: 999px; font-size: 13px;
  border: 1px solid rgba(255,255,255,.1); color: var(--mist);
}
```

---

## 🎯 与 wuwo 结合

- 来源徽章用紫系（--lilac 低透明度），数量多时（>3）折叠成「+N sources」。
- 流式进度在源卡片上显示真实验证：✓ 首屏加载、来源可点即可追溯——内容真实优先。
- follow-up 按钮是「把对话往下推」的入口，文案用用户视角疑问句。
