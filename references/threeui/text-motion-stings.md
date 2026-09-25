# ThreeUI 参考 · text motion stings（8 家族，PRO 1）

模式要点：文字是画布主角——粒子组成字、旋涡排字、渐变轨道环绕；全部带 pointer dissolve/suction。落地：文字色 --moon、粒子 --lilac→--rose 渐变、禁蓝紫靛。

### Typography Vortex（typography-vortex）
- 运行时：Canvas 2D
- 模式：Sable’s complete rotating typography vortex with crisp prerendered rings, drifting glyphs, pointer dissolution, particle dust, and click suction — with dark and light surfaces.
- 渲染管线：2 Canvas 2D passes — text layer + particle composite
- 交互：Mode, pointer dissolve, ambient dust, click suction, responsive rings, and reduced motion
- Contract 要点：renderer=Canvas 2D；mode=dark | light；rings=1.21 growth；interaction=Dissolve + suction；pixelRatio=≤ 2；asset=Fragment Mono

---

### Semantic Bloom（semantic-bloom）
- 运行时：Canvas 2D + DOM/CSS
- 模式：A customizable Codex wordmark that draws a viscous particle organism toward its letters, illuminating the text as the network searches and reconnects.
- 渲染管线：1 filtered Canvas 2D particle network over a DOM wordmark
- 交互：Pointer attraction, live text and size controls, synchronized light/dark mode, visibility pausing, and reduced-motion still frame
- Contract 要点：source=Exact owner-selected HTML；focus=Centered semantic wordmark；text=Codex；mode=dark | light；size=0.55–1.6；motion=Pointer + reduced-motion still；assets=None

---

### Text Path Studies（globe-study）
- 运行时：Canvas 2D
- 模式：Six interactive Canvas 2D typography studies spanning a globe, flowing outlines, morphing glyphs, cloth physics, ripples, and a particle sphere.
- 渲染管线：1 selected sandboxed Canvas 2D study
- 交互：Variant-specific drag, zoom, hover, click, morph, cloth, ripple, and particle interactions
- 变体：audio-wordmark, ball-study, cloth-study, globe-study, morphing-glyph-cloud, outline-typeflow, particle-wordmark, ripple-study, threeui-intro
- Contract 要点：source=Six exact authored figures across two documents；renderer=Canvas 2D；mode=dark | light；variant=Six text-path studies；pixelRatio=≤ 2.5；assets=None；source=Exact FIG 07 document；renderer=Canvas 2D

---

### Gradient Collection（gradient-collection）
- 运行时：Canvas 2D
- 模式：Four directional twelve-tile gradient carousels orbiting kinetic ThreeUI headlines, with preserved perspective, shadows, and a synchronized light/dark canvas.
- 渲染管线：1 Canvas 2D typographic carousel
- 交互：Four rising, falling, horizontal, and vertical compositions complete one orbit every 15 seconds with synchronized light/dark mode
- 变体：gradient-collection, gradient-collection-falling-diagonal, gradient-collection-horizontal-sweep, gradient-collection-vertical-loop

---

### Article Headings（article-headings）
- 运行时：DOM/CSS + Canvas 2D
- 模式：Three expressive text treatments collected in one family: a chromatic intro, a particle wordmark, and an audio-reactive identity lockup.
- 渲染管线：Variant-dependent DOM/CSS or one to two Canvas 2D passes
- 交互：Authored text motion with responsive presentation, reduced-motion handling, and synchronized light/dark mode
- 变体：article-headings, audio-wordmark, particle-wordmark, threeui-intro
- Contract 要点：renderer=DOM/CSS or Canvas 2D；variants=Intro | Particle | Audio；mode=dark | light；motion=Reduced-motion aware；assets=Fragment Mono + inline source documents

---

### Understory Sting（understory-motion）
- 运行时：Three.js r149
- 模式：A four-second motion frame carrying one statement beside a marble hand that holds a refracting glass block of hydrangeas.
- 渲染管线：1 live Three.js scene render plus a transmission pass for the glass block
- 交互：None — a fixed, seekable timeline; every visible value is a pure function of scene time
- Contract 要点：renderer=Three.js r149；variant=understory；message=One statement, newline separated；format=16:9 | 1:1 | 4:5 | 9:16；duration=4s, seamless loop；time=Freeze one deterministic frame；motion=Visibility + reduced motion；assets=No binary scene assets

---

### Sylva Sting（sylva-motion）
- 运行时：Three.js r149
- 模式：A five-second motion frame in which a survey pulse draws a moss root in behind its own wireframe, then one statement lands in the air above it.
- 渲染管线：1 live Three.js scene render with procedural ShaderMaterials, CanvasTextures, and instancing
- 交互：None — a fixed, seekable timeline; every visible value is a pure function of scene time
- Contract 要点：renderer=Three.js r149；variant=sylva；message=One statement, newline separated；format=16:9 | 1:1 | 4:5 | 9:16；duration=5s, seamless loop；time=Freeze one deterministic frame；motion=Visibility + reduced motion；assets=No binary scene assets

---

### Meng Timeline（meng-timeline） 🔒PRO
- 运行时：Full HTML + DOM/CSS + embedded MP4
- 模式：A scroll-driven horizontal timeline of Meng To's 17 highest-reach posts from June through August 2026, composed as perspective-scaled post cards with synchronized date markers, rays, embedded clips, and like reveals.
- 渲染管线：1 sandboxed full-document renderer
- 交互：Automatic progression, pointer drag, neighboring-card click, wheel, arrow keys, and Home
- Contract 要点：document=Complete original meng-timeline.html, byte-for-byte；layout=1920x1080 authored stage scaled into the preview frame；interaction=Autoplay + drag + neighboring-card click + wheel + keyboard；motion=Reduced-motion still states and visibility-aware playback；assets=10 WebP avatars + 16 MP4 clips; no network request
