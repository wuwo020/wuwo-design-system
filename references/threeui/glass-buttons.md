# ThreeUI 参考 · glass buttons（4 家族，PRO 0）

模式要点：玻璃拟态=半透明底+blur+1px 描边+hover 辉光；shader 按钮是重特效生产慎用。落地：玻璃底 rgba(255,255,255,0.05)、描边 rgba(255,255,255,0.08)、hover 辉光 --lilac 0.25。

### Shader Buttons（star-portal）
- 运行时：Raw WebGL + Canvas 2D + CSS
- 模式：Six authored shader and canvas button treatments collected into one interactive family.
- 渲染管线：1 selected shader, canvas, and CSS button composition
- 交互：Variant selection with authored pointer, hover, motion, and palette behavior
- 变体：ignition-button, induction-button, plasma-button, star-portal, tactile-button, uploading-button
- Contract 要点：variants=Star Portal + Ignition + Induction + Plasma + Tactile + Thin

---

### Rectangle Buttons（maccess-glass-button）
- 运行时：DOM + CSS
- 模式：Thirteen authored rectangle-button and animated CTA treatments collected into one family.
- 渲染管线：1 selected DOM/CSS button composition
- 交互：Variant selection with authored hover, focus, motion, and palette behavior
- 变体：dot-border-button, floating-dots-cta, generate-button, glassmorphism-cta, gradient-beam-cta, gradient-cta, gradient-pill-button, launch-button, lumen-cta, lumen-cta-ghost, maccess-glass-button, sliding-text-cta, spinning-border-button
- Contract 要点：variants=Dark Glass + Launch + Dot Border + Floating Dots + Sliding T

---

### Circle Buttons（circle-buttons）
- 运行时：DOM + CSS
- 模式：Three compact circular icon controls using the exact Dark Glass, Launch, and Dot Border material systems.
- 渲染管线：1 layered DOM/CSS circle composition
- 交互：Source-faithful hover and press behavior, focus-visible ring, reduced-motion fallback, and adaptive light/dark palette
- 变体：circle-buttons, circle-buttons-mail, circle-buttons-plus
- Contract 要点：renderer=Semantic button + scoped layered CSS；variants=Play + Plus + Mail；materials=Dark Glass + Launch + Dot Border；size=56–72px diameter；theme=Dark (default) | Light；interaction=Hover | Focus | Press | Disabled | Reduced motion；assets=Three inline SVG icons

---

### Liquid Metal Button（liquid-metal-button）
- 运行时：Raw WebGL 2 + DOM/CSS
- 模式：A prismatic liquid-metal control in Sign up pill, Liquid Orb, and configurable Play Circle variants, with pointer-following bloom and press ripples.
- 渲染管线：Up to 20 — metal, crisp rim, adaptive softening, multi-radius bloom, and composite
- 交互：Hover, focus, pointer-dragged metal, faceted press ripples, and Enter/Space activation
- 变体：liquid-metal-button, liquid-metal-button-circle, liquid-metal-play-button, lumen-cta
- Contract 要点：renderer=DOM + CSS；variant=Primary | Ghost；geometry=45px tall, 999px radius, 30px side padding, 10px gap；gradient=90deg, six authored stops from #050014 to #9470d9；ring=7px open circle at 1.3px, trailing the label；mode=Dark | Light backdrop；palette=Hue, saturation, and brightness at the boundary；motion=Reduced motion removes the hover transition
