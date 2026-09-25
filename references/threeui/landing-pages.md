# ThreeUI 参考 · landing pages（15 家族，PRO 0）

模式要点：连续 3D 世界 + 章节滚动编排（scroll choreography）+ 单一贯穿叙事主题。落地 wuwo 化：底色换 --ink、章节标题用 --lilac 渐变字、保留 reduced-motion 静帧回退。

### Agent Arcana（agent-arcana-landing-page）
- 运行时：Full HTML + DOM/CSS + Canvas 2D + WebGL2
- 模式：The complete Agent Arcana deck, preserved unchanged with three richly illustrated agent cards, dynamically derived relief maps, pointer-steered WebGL2 lighting, card draws, and an editorial field guide.
- 渲染管线：2 sandboxed WebGL2 card-lighting planes over the complete document
- 交互：Original Draw CTA and navigation hovers, card tilt and relighting, previous/next deck controls, section-by-section scroll, and responsive layout
- Contract 要点：document=Complete original agent-arcana.html, byte-for-byte；sourceUrl=/landing-pages/agent-arcana.html；layout=Original full landing page inside the preview frame；interaction=Scroll + pointer + hover + card draw；assets=3 WOFF2 fonts + 14 WebP paintings + 1 SVG mark; no external 

---

### Understory（understory-landing-page）
- 运行时：Full HTML + DOM/CSS + inlined Three.js r149
- 模式：The complete Understory mental-health practice page, preserved unchanged with its embedded Outfit face, thirteen embedded portraits, procedural Three.js glass hands and planting, responsive editorial layout, and soft specular pointer response.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original CTA and navigation hovers, section-by-section scroll, pointer-reactive planting, press-triggered pollen, and responsive layout
- Contract 要点：document=Complete original cogniwave.html, byte-for-byte；sourceUrl=/landing-pages/cogniwave.html；layout=Original full landing page inside the preview frame；interaction=Scroll + pointer + hover + press；assets=Inlined Three.js r149, Outfit font, portraits, and procedura

---

### Noctiluca（noctiluca-landing-page）
- 运行时：Full HTML + DOM/CSS + local Three.js r149
- 模式：The complete Noctiluca slow-media descent, preserved unchanged with its bioluminescent Three.js water volume, looping jellyfish study, live depth ruler, stratified transect, and six cursor-lit specimen plates.
- 渲染管线：2 sandboxed Three.js renderers — fixed water volume and cursor-lit specimen deck
- 交互：Original CTA and navigation hovers, section-by-section scroll, pointer parallax, specimen lighting, and responsive scaling
- Contract 要点：document=Complete original noctiluca.html, byte-for-byte；sourceUrl=/landing-pages/noctiluca.html；layout=Original full landing page inside the preview frame；interaction=Scroll + pointer + hover；assets=noctiluca-assets kept at its authored relative path; no exte

---

### Kage（kage-landing-page）
- 运行时：Full HTML + DOM/CSS + Three.js
- 模式：The complete authored Kage temple experience, preserved as an interactive full-page document with its original navigation, scroll scenes, and local Three.js world.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer, keyboard, scroll, and navigation interactions
- Contract 要点：document=Complete packaged kage.html with audio removed；sourceUrl=/landing-pages/kage.html；headingFont=Onest | Instrument Serif | Newsreader | Geist；bodyFont=Onest | Geist | Newsreader | Instrument Serif；headingWeight=400 | 500 | 600 | 700；bodyWeight=300 | 400 | 500 | 600；primaryColor=Hex color — the vermilion accent and the ember tint it drive；typography=Heading size 30–72px ceiling + body size + heading tracking

---

### Inkbound River Story（inkbound-river-story）
- 运行时：Full HTML + DOM/CSS + embedded media
- 模式：The complete Inkbound river narrative, preserved unchanged with its cinematic chapters, scroll choreography, interactions, and embedded media.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer, keyboard, scroll, navigation, and narrative interactions
- Contract 要点：document=Complete original inkbound-river-story.html, byte-for-byte；sourceUrl=/landing-pages/inkbound-river-story.html；layout=Original full landing page inside the preview frame；interaction=Scroll + pointer + keyboard + media controls；assets=Original embedded media

---

### Kairo（kairo-landing-page）
- 运行时：Full HTML + DOM/CSS + WebGL2 + GSAP ScrollTrigger + Lenis
- 模式：The complete KAIRO culinary product page with its WebGL2 flame-wrapped hero, Lenis smooth scroll, GSAP ScrollTrigger reveals, pinned editorial sections, and remote product photography.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original smooth scroll, scroll-triggered reveals, WebGL flame motion, pointer, and hover
- Contract 要点：document=Complete updated KAIRO template with only its final newline ；sourceUrl=/landing-pages/kairo-culinary.html；layout=Original full landing page inside the preview frame；interaction=WebGL2 flame + Lenis smooth scroll + ScrollTrigger reveals +；assets=Original remote imagery and CDN runtimes; the page needs net

---

### Volta Atelier（volta-atelier-landing-page）
- 运行时：Full HTML + DOM/CSS + Three.js r128
- 模式：The complete Volta Atelier studio page — services, work, process, team, pricing, FAQ, and footer as authored — with an owner-requested hero revision: the collage is respaced into a clean two-row band and the fixed corner registration marks are gone. Use Volta Atelier Hero for the isolated opening section with locally owned portraits.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer repulsion, idle float, scroll choreography, and navigation
- Contract 要点：document=Complete Volta Atelier template; hero collage respaced and c；sourceUrl=/landing-pages/volta-atelier.html；layout=Full landing page inside the preview frame; the hero collage；interaction=Pointer repulsion + idle float + scroll + navigation；assets=Original remote imagery and CDN runtimes; the page needs net

---

### Halfwave（halfwave-landing-page）
- 运行时：Full HTML + DOM/CSS + Three.js r149
- 模式：The complete Halfwave studio page with a wall of analogue CRT monitors, original screen artwork and team portraits, per-screen static and colour bars, film grain, and serif display typography. The authored file is named codescan.html.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original pointer, hover, scroll, and responsive scaling
- Contract 要点：document=Complete authored codescan.html with an external original me；sourceUrl=/landing-pages/codescan.html；layout=Original full landing page inside the preview frame；interaction=Scroll + pointer + hover；assets=12 images in public/landing-pages/halfwave-assets/; procedur

---

### Centra（centra-landing-page）
- 运行时：Full HTML + DOM/CSS + Three.js r147 + Three.js 0.160 module
- 模式：The complete Centra control-plane page, preserved unchanged with its recursively grown cherry bough on the ES-module Three.js build, the pointer-tracking mechanical eye beneath it, and the three module cards that build their own trace-chain, guard-crystal, and fleet-cluster objects the first time a pointer enters them.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original scroll choreography, pointer tracking, hover, and responsive scaling
- Contract 要点：document=Complete original centra.html, byte-for-byte；sourceUrl=/landing-pages/centra.html；layout=Original full landing page inside the preview frame；interaction=Scroll + pointer + hover；assets=Procedural bough, eye, and module objects, no binary assets

---

### Meridian（meridian-landing-page）
- 运行时：Full HTML + DOM/CSS + inlined Three.js r155 module
- 模式：The complete Meridian revenue-platform page, preserved unchanged with the whole Three.js r155 module inlined into the document, so the page renders its Earth-from-orbit scene without making a single network request. The authored file is named ascend.html.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original scroll choreography, pointer, hover, and responsive scaling
- Contract 要点：document=Complete original ascend.html, byte-for-byte；sourceUrl=/landing-pages/ascend.html；layout=Original full landing page inside the preview frame；interaction=Scroll + pointer + hover；assets=Inlined Three.js runtime and procedural scene, no external r

---

### Sketchbook（meng-to-sketchbook-landing-page）
- 运行时：Full HTML + DOM/CSS + JavaScript
- 模式：A tactile personal portfolio built as a Singapore sketchbook, with nine illustrated plates, curled page turns, a draggable magnifying glass, zoom controls, a botanical paper atmosphere, and an editorial index.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original page turns, pointer tilt, draggable magnifier, zoom controls, navigation, scroll, keyboard, and responsive layout
- Contract 要点：document=Complete original meng-to-sketchbook.html, byte-for-byte；sourceUrl=/landing-pages/meng-to-sketchbook.html；layout=Original full landing page inside the preview frame；interaction=Page turns + magnifier drag + zoom + pointer tilt + scroll +；assets=17 packaged files in public/landing-pages/meng-to-sketchbook

---

### Sekitei（sekitei-landing-page）
- 运行时：Full HTML + DOM/CSS + local Three.js r149
- 模式：The complete Sekitei scroll journey through a Japanese dry garden from first grey to dusk, preserved unchanged with its continuous Three.js world, seven chapter camera landings, local imagery, and authored typography switcher.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original chapter-by-chapter scroll choreography, pointer, navigation, typography switcher, and responsive layout
- Contract 要点：document=Complete original sekitei-world.html, byte-for-byte；sourceUrl=/landing-pages/sekitei.html；layout=Original seven-chapter landing page inside the preview frame；interaction=Chapter scroll + pointer + navigation + typography switcher；assets=35 packaged runtime files in public/landing-pages/sekitei-as

---

### RenderLab（renderlab-landing-page）
- 运行时：Full HTML + DOM/CSS + Tailwind Play CDN
- 模式：The complete RenderLab motion-house page, preserved unchanged with its ruled column overlay, tracking cursor label, scroll progress bar, light and dark toggle, marquee bands, and the twenty remote stills and one remote loop the original page references.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original scroll progress, cursor label, theme toggle, pointer, and hover
- Contract 要点：document=Complete original renderlab-motion-house.html, byte-for-byte；sourceUrl=/landing-pages/renderlab-motion-house.html；layout=Original full landing page inside the preview frame；interaction=Scroll + pointer + hover + theme toggle；assets=Twenty images, one video, and the Tailwind runtime fetched f

---

### Echo Vale（echo-vale-landing-page）
- 运行时：Full HTML + DOM/CSS + Three.js r128 + Tailwind Play CDN
- 模式：The complete Echo Vale travel page with its Three.js point-cloud drift, horizontal journey scroller, and fourteen image placements served from a responsive local WebP package sized for true 2x display coverage.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original entrance counter, scroll choreography, pointer, and hover
- Contract 要点：document=Complete Echo Vale document with its original layout and int；sourceUrl=/landing-pages/echo-vale.html；layout=Original full landing page inside the preview frame；interaction=Entrance + scroll + pointer + hover；assets=Thirty-two responsive WebP image files; Three.js, Tailwind, 

---

### Aurello（aurello-landing-page）
- 运行时：Full HTML + DOM/CSS + GSAP 3.12.5 with ScrollTrigger + Tailwind Play CDN
- 模式：The complete Aurello beverage page, preserved unchanged with its GSAP ScrollTrigger can choreography, the pinned journey can that travels the length of the page, the flavour selector, and the sixteen remote product renders the original page references.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Original scroll-scrubbed can choreography, flavour selector, pointer, hover, and reduced-motion fallback
- Contract 要点：document=Complete original aurello-beverage.html, byte-for-byte；sourceUrl=/landing-pages/aurello-beverage.html；layout=Original full landing page inside the preview frame；interaction=Scroll + pointer + hover；assets=Sixteen images and the GSAP, ScrollTrigger, and Tailwind run
