# ThreeUI 参考 · heroes sections（18 家族，PRO 0）

模式要点：一屏内 1 个重型 canvas 主体 + 编辑排版层叠放；指针视差/torch/parallax 是标配交互。落地：辉光色换 --lilac/--tide 低透明 box-shadow，正文 --moon。

### ASCII Page Transition（ascii-page-transition-hero）
- 运行时：Full HTML + DOM/CSS + Canvas 2D
- 模式：A stark Sable hero for agentic work, preserved unchanged with a pointer-reactive glyph field, orbiting systems vortex, tactile CTA bursts, and a full-screen ASCII transition into Field Notes.
- 渲染管线：5 Canvas 2D surfaces — hero glyph field, vortex, button bursts, ASCII transition, and Field Notes residue
- 交互：Dock and CTA hovers, pointer attraction and dispersal, vortex suction, button bursts, and Home/Field Notes ASCII page transitions
- Contract 要点：document=Complete original ascii-page-transition-v1.html, byte-for-by；sourceUrl=/landing-pages/ascii-page-transition-v1.html；layout=Original full-viewport Hero and Field Notes views inside the；interaction=Pointer + hover + click + full-screen ASCII page transition；assets=1 local Geist WOFF2 + 2 embedded WOFF2 fonts + 1 embedded SV

---

### Complete Shelf（complete-shelf-landing-page）
- 运行时：Full HTML + DOM/CSS + Three.js r165
- 模式：The complete Working Volumes bookshelf page, preserved unchanged with all seven tools, its responsive editorial interface, and authored Three.js presentation.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer, keyboard, scroll, navigation, and book interactions
- Contract 要点：document=Complete original complete-shelf-v2.html, byte-for-byte；sourceUrl=/landing-pages/complete-shelf-v2.html；headingFont=Iowan Old Style | Instrument Serif | Newsreader | Geist；bodyFont=Inter | Geist | Newsreader | Instrument Serif；headingWeight=400 | 500 | 600；bodyWeight=400 | 500 | 600；primaryColor=Hex color；typography=Heading size + body size + heading letter spacing

---

### Bestsellers Book Showcase（bestsellers-book-showcase）
- 运行时：Full HTML + DOM/CSS + embedded media
- 模式：The complete Field Manuals book showcase, preserved unchanged with its editorial layout, authored motion, interactions, and embedded media.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer, keyboard, scroll, navigation, and showcase interactions
- Contract 要点：document=Complete original bestsellers-book-showcase.html, byte-for-b；sourceUrl=/landing-pages/bestsellers-book-showcase.html；headingFont=Iowan Old Style | Instrument Serif | Newsreader | Geist；bodyFont=Iowan Old Style | Geist | Newsreader | Instrument Serif；headingWeight=400 | 500 | 600 | 700；bodyWeight=400 | 500 | 600 | 700；primaryColor=Hex color；typography=Heading size + body size + heading letter spacing

---

### Orrery（orrery-hero）
- 运行时：Full HTML + DOM/CSS + Three.js r147 + UnrealBloom
- 模式：The complete Orrery studio hero, preserved unchanged with its procedural stone plinth, luminous orbital rings, drifting debris, editorial cards, and compact dock navigation.
- 渲染管线：3-pass Three.js composer — scene render, selective UnrealBloom, and authored final composite
- 交互：Original dock and call-to-action hovers, pointer parallax, eased orrery response, card buttons, and responsive scaling
- Contract 要点：document=Complete original orrery.html, byte-for-byte；sourceUrl=/landing-pages/orrery.html；layout=Original full-screen hero inside the preview frame；interaction=Pointer + hover + card and dock controls；assets=Pinned Three.js r147 examples and Instrument Serif; all scen

---

### Trochil Hero（trochil-hero）
- 运行时：Full HTML + DOM/CSS + Three.js r149 + raw WebGL 2
- 模式：A configurable Trochil hero with its complete procedural halftone hummingbird, pointer flight choreography, measured editorial grid, and liquid metal calls to action.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer flight, hover, reveal choreography, responsive layout, and liquid metal controls with pointer drag and press ripples
- Contract 要点：document=Complete original trochil-hero.html, byte-for-byte；sourceUrl=/landing-pages/trochil-hero.html；headingFont=Instrument Serif | Newsreader | Geist；bodyFont=Geist | Newsreader | Instrument Serif；headingWeight=400 | 500 | 600 | 700；bodyWeight=400 | 500 | 600 | 700；primaryColor=Hex color；typography=Heading size + body size + heading letter spacing

---

### Cortexa Hero（cortexa-hero）
- 运行时：Full HTML + DOM/CSS + Three.js r149
- 模式：The complete Cortexa intelligence-platform hero, preserved unchanged with its procedural point-cloud bust, silhouette bloom, data haze, and pointer-following torch interaction.
- 渲染管线：1 sandboxed full-document renderer with a multilevel bloom composite
- 交互：Original intro dolly, pointer torch, particle extraction, CTA and navigation hover states, and responsive layout
- Contract 要点：document=Complete original cortexa-hero.html, byte-for-byte；sourceUrl=/landing-pages/cortexa-hero.html；headingFont=Instrument Serif | Newsreader | Geist；bodyFont=Geist | Newsreader | Instrument Serif；headingWeight=300 | 400 | 500 | 600；bodyWeight=300 | 400 | 500 | 600；primaryColor=Hex color；typography=Heading size + body size + heading letter spacing

---

### Cathode Hero（cathode-hero）
- 运行时：Full HTML + DOM/CSS + Three.js r149
- 模式：The complete Cathode workstation hero, preserved unchanged with its procedural isometric CRT, keyboard light chase, screen glow, film grain, and pointer-driven orbit.
- 渲染管线：3 authored WebGL passes — graded ground, workstation geometry, and grain
- 交互：Original pointer orbit, keyboard light chase, CTA and navigation hover states, and responsive layout
- Contract 要点：document=Complete original cathode.html, byte-for-byte；sourceUrl=/landing-pages/cathode.html；headingFont=Inter | Instrument Serif | Newsreader | Geist；bodyFont=Inter | Geist | Newsreader | Instrument Serif；headingWeight=300 | 400 | 500 | 600；bodyWeight=300 | 400 | 500 | 600；primaryColor=Hex color；typography=Heading size + body size + heading letter spacing

---

### Cadence Hero（cadence-hero）
- 运行时：Full HTML + DOM/CSS + inlined Three.js r149 + embedded media
- 模式：The complete Cadence finance landing page with a responsive hero grid, an orderly bundled radial hero field, content-fit gradient pill navigation, compact dark glass CTAs, three WebGL scenes, cohesive GPT Image 2 editorial media, scroll reveals, and portfolio sequence.
- 渲染管线：3 authored WebGL scenes — centered radial loom, chain network, and heart field
- 交互：Original section-by-section scroll reveals, pointer response, CTA and navigation hover states, and responsive layout
- Contract 要点：document=Complete packaged cadence.html with 10 owner-requested GPT I；sourceUrl=/landing-pages/cadence.html；headingFont=Geist | Instrument Serif | Newsreader；bodyFont=Geist | Newsreader | Instrument Serif；headingWeight=300 | 400 | 500 | 600 | 700；bodyWeight=300 | 400 | 500 | 600；primaryColor=Hex color；typography=Heading size + body size + heading letter spacing

---

### Attune Hero（attune-hero）
- 运行时：Full HTML + DOM/CSS + inlined Three.js r149
- 模式：The complete attune hero page, preserved unchanged with its procedural Three.js Mars, orbital telemetry, dust haze, and full-bleed product layout.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original reveal choreography, pointer, hover, and responsive layout
- Contract 要点：document=Complete original attune-hero.html, byte-for-byte；sourceUrl=/landing-pages/attune-hero.html；headingFont=Instrument Serif | Newsreader | Geist；bodyFont=Inter | Geist | Newsreader | Instrument Serif；headingWeight=400 | 500 | 600 | 700；bodyWeight=300 | 400 | 500 | 600 | 700；primaryColor=Hex color — the accent, its two tints, and the warm hairline；typography=Heading size 40–96px ceiling + body size + heading tracking,

---

### Betawise（betawise-landing-page）
- 运行时：Full HTML + DOM/CSS + Three.js r149 + WebGL2
- 模式：The complete Betawise attribution page, preserved unchanged with its normal-extruded stroke globe in Three.js, its starfield and orbital arcs, and the authored WebGL2 liquid-metal CTAs.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer, hover, press, and responsive scaling
- Contract 要点：document=Complete original betawise.html, byte-for-byte；sourceUrl=/landing-pages/betawise.html；headingFont=Questrial | Instrument Serif | Newsreader | Geist；bodyFont=Questrial | Geist | Newsreader | Instrument Serif；headingWeight=400 | 500 | 600 | 700；bodyWeight=400 | 500 | 600 | 700；primaryColor=Hex color — carried onto the stroke globe through the canvas；typography=Heading size 26–60u + body size + heading tracking, on the p

---

### Betawise Hero（betawise-hero）
- 运行时：Full HTML + DOM/CSS + Three.js r149
- 模式：The complete Betawise particle-bust hero page, preserved unchanged with its Three.js point-cloud bust and pointer response. Betawise is the later full page built from the same brand.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer, hover, and responsive scaling
- Contract 要点：document=Complete original betawise-hero.html, byte-for-byte；sourceUrl=/landing-pages/betawise-hero.html；headingFont=Outfit | Instrument Serif | Newsreader | Geist；bodyFont=Outfit | Geist | Newsreader | Instrument Serif；headingWeight=400 | 500 | 600 | 700；bodyWeight=300 | 400 | 500 | 600；primaryColor=Hex color — carried onto the point cloud through the canvas；typography=Heading size 32–76px + body size + heading tracking, narrow-

---

### Axonis（axonis-landing-page）
- 运行时：Full HTML + DOM/CSS + Three.js 0.160 module
- 模式：The complete Axonis infrastructure page, preserved unchanged with its Three.js module field, entrance choreography, and the two locally hosted liquid-metal button frames it embeds.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original entrance choreography, pointer, hover, and reduced-motion fallback
- Contract 要点：document=Complete original axonis.html, byte-for-byte；sourceUrl=/landing-pages/axonis.html；headingFont=Space Grotesk | Instrument Serif | Newsreader | Geist；bodyFont=Space Grotesk | Geist | Newsreader | Instrument Serif；headingWeight=320 | 400 | 500 | 600 | 700；bodyWeight=400 | 500 | 600 | 700；primaryColor=Hex color — the accent pair, the wordmark ramp, and the modu；typography=Wordmark size 14–34vw + body size + wordmark tracking, optic

---

### Tidecrest Hero（tidecrest-hero）
- 运行时：Full HTML + DOM/CSS + Three.js r147 + UnrealBloom
- 模式：The complete Tidecrest hero page, preserved unchanged with its Three.js terrain and the authored EffectComposer and UnrealBloom post-processing chain.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer, hover, and responsive scaling
- Contract 要点：document=Complete original tidecrest-hero.html, byte-for-byte；sourceUrl=/landing-pages/tidecrest-hero.html；headingFont=Figtree | Instrument Serif | Newsreader | Geist；bodyFont=Hanken Grotesk | Geist | Newsreader | Instrument Serif；headingWeight=300 | 400 | 500 | 600；bodyWeight=300 | 400 | 500 | 600；primaryColor=Hex color；typography=Heading size + body size + heading letter spacing

---

### Sylva（sylva-hero）
- 运行时：Full HTML + DOM/CSS + local Three.js
- 模式：The complete Sylva page, preserved unchanged with its living-world Three.js scene, local Lexend type, card imagery, and the two liquid-metal buttons it embeds — plus three derived variants that re-dress the scene and retone the page chrome around it. Sylva Living World is the scene-only Three.js entry.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer, hover, scroll, and responsive scaling
- 变体：sylva-hero, sylva-hero-maple-autumn, sylva-hero-sakura-sunset, sylva-hero-sequoia-mist
- Contract 要点：document=Complete original inner-green-3d.html, byte-for-byte；sourceUrl=/landing-pages/inner-green-3d.html；variant=Living Green | Sakura Sunset | Maple Autumn | Sequoia Mist；derived=The byte-exact page with a scene transformation applied, its；headingFont=Lexend | Instrument Serif | Newsreader | Geist；bodyFont=Lexend | Geist | Newsreader | Instrument Serif；headingWeight=200 | 300 | 400 | 500 | 600；bodyWeight=200 | 300 | 400 | 500

---

### Nocturne（nocturne-hero）
- 运行时：Full HTML + DOM/CSS + Three.js r149
- 模式：The complete Nocturne hero, preserved unchanged with its shaded midnight sky, the floating debit card carried by its own halo and glow passes, and the still sea reflecting both. The authored file is named lumen.html.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer parallax, hover, and reduced-motion fallback
- Contract 要点：document=Complete original lumen.html, byte-for-byte；sourceUrl=/landing-pages/lumen.html；headingFont=Mulish | Instrument Serif | Newsreader | Geist；bodyFont=Mulish | Geist | Newsreader | Instrument Serif；headingWeight=300 | 400 | 600；bodyWeight=300 | 400 | 600；primaryColor=Hex color；typography=Heading size + body size + heading letter spacing

---

### Veyra Hero（veyra-hero）
- 运行时：Full HTML + DOM/CSS + inlined Three.js r149
- 模式：The complete Veyra fine-jewellery hero, preserved unchanged with its chrome hands, turning star-cut stone, violet glass, pointer-driven orbit, editorial typography, and responsive navigation.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer orbit, CTA and navigation hover states, reveal choreography, and responsive layout
- Contract 要点：document=Complete original veyra-fullbleed.html, byte-for-byte；sourceUrl=/landing-pages/veyra-fullbleed.html；headingFont=DM Sans | Instrument Serif | Newsreader | Geist；bodyFont=DM Sans | Geist | Newsreader | Instrument Serif；headingWeight=300 | 400 | 500 | 600；bodyWeight=300 | 400 | 500 | 600；primaryColor=Hex color；typography=Heading size + body size + heading letter spacing

---

### Sections（maccess-workflow）
- 运行时：DOM + CSS
- 模式：Three reusable dark product sections collected into one responsive family.
- 渲染管线：1 selected responsive DOM/SVG composition
- 交互：Variant selection with authored motion, native form behavior, and reduced-motion fallback
- 变体：maccess-newsletter-footer, maccess-testimonial-intro, maccess-workflow
- Contract 要点：identity=Neutral, unbranded copy；variants=Onboarding Steps + Editorial Intro + Newsletter Footer

---

### Volta Atelier Hero（volta-atelier-hero）
- 运行时：DOM + CSS + Canvas 2D
- 模式：The isolated Volta Atelier opening section: an oversized typographic frame around an eleven-card, pointer-reactive studio collage with ambient dust and producer details.
- 渲染管线：1 sandboxed DOM/CSS hero composition + 1 ambient Canvas 2D dust pass
- 交互：Pointer-repulsive portrait collage, idle float, producer bubble, live Porto clock, responsive layout, reduced motion, scale, speed, opacity, and palette
- 变体：cloud-field, void-field, volta-atelier-hero
- Contract 要点：renderer=Extracted hero section only；collage=11 overlapping portrait tiles；motion=speed + collage scale；lifecycle=responsive + visibility-aware + reduced motion；assets=10 authored WebP portraits
