# Feature Cards Bundle

组合效果：带悬停翻转的玻璃拟态卡片网格，展示产品特性。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Glassmorphism Card | Micro | Uiverse (Cards/57286) |
| 3D Flip on Hover | Animation | Originkit (Card-flip-03) |
| Icon Pulse Effect | Micro/Uiverse | Checkboxes/Radios with pulse |

---

## 💻 Tailwind / HTML 示例

```html
<div class="feature-grid">
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="flip-card-front glass-card">
        <h3>🚀 Fast</h3>
        <p>Built with vanilla CSS & Tailwind</p>
      </div>
      <div class="flip-card-back glass-card">
        <p>No heavy frameworks needed.</p>
      </div>
    </div>
  </div>
  
  <!-- Repeat for more cards -->
</div>
```

---

## 🎨 关键样式（可复用）

```css
/* Flip Container */
.flip-card {
  perspective: 1000px;
  width: 100%;
  max-width: 280px;
}
.flip-card-inner {
  position: relative;
  width: 100%;
  transition: transform 0.6s;
  transform-style: preserve-3d;
}
.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}
.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  backface-visibility: hidden;
  border-radius: 1rem;
}
.flip-card-back {
  transform: rotateY(180deg);
}
```

**关联 Skill**：`frontend-design`（卡片布局规范）、`hyperframes-animation`（视频内展示翻转效果）  
**适用场景**：Feature Section、产品展示页、服务介绍页