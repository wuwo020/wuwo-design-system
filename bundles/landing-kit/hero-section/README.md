# Hero Section Bundle

组合效果：滚动入场标题 + 渐变 CTA Button + Glassmorphism 介绍卡片。

---

## 📦 组件来源

| 组件 | 类型 | 来源 |
|------|------|------|
| Hero Title Scroll Reveal | Animation | Originkit (Scroll-reveal-01) |
| CTA Button Glow Effect | CSS/Micro | Uiverse (Buttons/48291) |
| Intro Card Glassmorphism | Micro | Uiverse (Cards/57286) |

---

## 💻 Tailwind / HTML 示例

```html
<!-- Hero Title with Scroll Reveal -->
<div class="hero-title">
  <h1>Build Faster With<br><span class="highlight">Smart UI Kits</span></h1>
</div>

<!-- CTA Button -->
<a href="#" class="btn-glow">Get Started →</a>

<!-- Glassmorphism Intro Card -->
<div class="glass-card">
  <p>Drag-and-drop components for landing pages, dashboards, and AI interfaces.</p>
</div>
```

---

## 🎨 关键样式（可复用）

```css
/* Glassmorphism Card */
.glass-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 1.5rem;
  border-radius: 1rem;
}

/* CTA Button Glow */
.btn-glow {
  background: linear-gradient(135deg, #667eea, #764ba2);
  box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
  transition: all 0.3s ease;
}
.btn-glow:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
}

/* Scroll Reveal Animation */
.hero-title {
  opacity: 0;
  transform: translateY(30px);
  animation: slideUp 0.8s ease-out forwards;
}
@keyframes slideUp {
  to { opacity: 1; transform: translateY(0); }
}
```

---

**关联 Skill**：`frontend-design`（配色与排版指导）、`hyperframes-video`（视频中嵌入动画）  
**适用场景**：Landing Page、产品首页、个人作品集