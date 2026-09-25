# ThreeUI 参考 · backgrounds fields（16 家族，PRO 4）

模式要点：低干扰氛围层——单 pass 优先、pointer 响应平滑（smoothed）、visibility-aware 暂停。落地：粒子/线条色一律换 --tide 或 --lilac 单色系，透明度压到 0.3-0.5 避免抢内容。

### Cross Beam（cross-beam） 🔒PRO
- 运行时：WebGL2
- 模式：Three cross-fading beams diffused through blue-noise atmosphere and a reactive glyph field.
- 渲染管线：3 — beam, atmosphere, glyph
- 交互：Smoothed pointer chaos + 4 click ripples + customizable hue
- Contract 要点：speed=1；beamWidth=1；dither=0.11；glyphSize=4；glyphAmount=0.45；noiseScale=1；hue=0；renderPasses=3

---

### Predictive Arc（predictive-arc）
- 运行时：Canvas 2D + Raw WebGL + Three.js r128
- 模式：Eight animated arc, signal, ribbon, void, and halftone scenes collected in one Canvas 2D, raw-WebGL, and Three.js family.
- 渲染管线：1 selected Canvas 2D, raw-WebGL, or Three.js field pass
- 交互：Variant selection plus customizable mode, speed, color, and brightness
- 变体：amber-halftone, data-pixel-arc, halftone-flow, override-grid, predictive-arc, ribbon-field, signal-particles, void-field
- Contract 要点：renderer=Canvas 2D + Raw WebGL + Three.js；variants=Predictive + Data Pixel + Signal + Override + Ribbon + Void ；mode=dark | light；pixelRatio=≤ 2；assets=None

---

### Liquid Form（liquid-form）
- 运行时：Raw WebGL
- 模式：A centered silver ray-marched liquid form with authored studio reflections and pointer-responsive camera drift.
- 渲染管线：1 raw WebGL ray-march pass
- 交互：Smoothed pointer look-at plus customizable material, morph, and tint
- Contract 要点：renderer=Raw WebGL；steps=70；pixelRatio=≤ 1.5

---

### CRT（crt）
- 运行时：Raw WebGL + Canvas 2D
- 模式：A complete Matrix-era boot terminal rendered to an offscreen text texture and passed through the exact authored curved CRT shader.
- 渲染管线：2 — Canvas 2D boot texture + raw WebGL CRT composite
- 交互：Customizable boot speed, CRT motion, hue, brightness, and opacity
- Contract 要点：renderer=Raw WebGL + Canvas 2D；boot=19 authored terminal rows；assets=None

---

### Globe（energy-orb） 🔒PRO
- 运行时：Raw WebGL + Canvas 2D
- 模式：Three interactive globe treatments: a smoky procedural energy sphere, a monochrome constellation sculpture, and a dusk network world with live flight arcs.
- 渲染管线：1–2 — Canvas 2D globe or Canvas 2D stars + raw WebGL energy sphere
- 交互：Drag with inertia, pointer collision or node hover, click-launched arcs, plus customizable motion, scale, palette, and opacity
- 变体：energy-orb, network-globe, tangled-constellations
- Contract 要点：renderer=Raw WebGL or Canvas 2D；variants=Energy | Tangled | Network；interaction=Drag + pointer + visibility；assets=Baked land-mask data only；renderer=Canvas 2D；source=Byte-exact local document；motion=Visibility + reduced motion；renderer=Canvas 2D

---

### Spark Badge（spark-badge） 🔒PRO
- 运行时：Canvas 2D
- 模式：A luminous credential badge held together by curl-noise embers, carved typography, rain occlusion, waterline sparks, and an adaptive particle field.
- 渲染管线：3 — rear rain, figure embers + waterline, foreground rain
- 交互：Ambient 17-second dissolve/reform cycle with reduced-motion and adaptive load governor
- 变体：spark-badge, spark-browser, spark-iphone, spark-studio-display
- Contract 要点：renderer=Canvas 2D；particles=17,600 + rain + water；passes=3；motion=Visibility + reduced motion；assets=None

---

### Hypnotic Loops（hypnotic-loops）
- 运行时：Raw WebGL + Canvas 2D
- 模式：Four supersampled loop studies—Lines, Dots, Rays, and Type—folded across a centered surface in an orange-to-sunset palette.
- 渲染管线：7 — scene, brightness, four separable blur passes, composite
- 交互：Live shape deformation with four authored pattern modes, custom background color, and reduced-motion support
- 变体：hypnotic-loops, hypnotic-loops-dots, hypnotic-loops-rays, hypnotic-loops-type
- Contract 要点：renderer=Raw WebGL + Canvas 2D；mesh=63,571 polar vertices；patterns=Lines | Dots | Rays | Type；palette=Orange + Sunset；passes=7；motion=Visibility + reduced motion

---

### Noise Flow（at-the-horizon）
- 运行时：Raw WebGL + Canvas 2D
- 模式：A traced encounter between a luminous figure and a vast dissolving profile, rendered entirely in directional threshold grain.
- 渲染管线：2 — Canvas 2D plate bake + animated WebGL threshold-dither composite
- 交互：Responsive uncropped fit, 25 FPS grain drift, reduced-motion still frame, and visibility-aware preview lifecycle
- 变体：at-the-horizon, bell-field, flow-field, stream-convergence
- Contract 要点：renderer=Raw WebGL + Canvas 2D；plate=Authored figure and portrait；grain=Directional threshold dither；motion=25 FPS | reduced-motion still；layout=Uncropped square center fit；assets=Base64 fields + vector traces；renderer=Raw WebGL adapter；source=Exact authored GLSL

---

### Elements（elements）
- 运行时：Raw WebGL2 + Canvas 2D
- 模式：Water, lightning, fire, condensation, and a painterly generative tree collected as one elemental family across WebGL2 and Canvas 2D.
- 渲染管线：1 selected composition — up to 3 WebGL2 passes or 1 Canvas 2D pass
- 交互：Variant selection, pointer-reactive marks and tree wind, speed, scale, particles, palette, and opacity
- 变体：condensation, elemental-flame, elemental-lightning, elemental-water, elements, generative-tree, ribbon-field
- Contract 要点：renderer=Sandboxed WebGL2 or Canvas 2D；variants=Water + Lightning + Fire + Condensation + Generative Tree；source=Complete authored Elemental Marks + Generative Tree document；assets=Three vector mark paths; no external tree assets；variant=water；renderer=Sandboxed raw WebGL2；assets=OpenAI vector path；variant=lightning

---

### Terrain Plume（terrain-plume） 🔒PRO
- 运行时：Raw WebGL + Canvas 2D
- 模式：DesignCode 5’s monochrome plume behind its exact engraved mountain range, foreground firs, grain, and dithered reveal.
- 渲染管线：1 WebGL plume + engraved terrain + reveal
- 交互：Pointer parallax, dithered entry, visibility-aware playback, and customizable plume geometry, strength, softness, speed, opacity, and palette
- Contract 要点：renderPasses=1；renderer=Raw WebGL；terrain=Owned Canvas 2D；reveal=Dithered Canvas 2D；speed=1；size=1；thickness=1；strength=1

---

### Particle Orb（particle-orb）
- 运行时：Canvas 2D
- 模式：The exact autonomous-system particle orb and connective field isolated from its source page.
- 渲染管线：1 Canvas 2D particle-network pass
- 交互：Autonomous particle motion + optional final-frame palette
- 变体：dot-border-button, floating-dots-cta, generate-button, glassmorphism-cta, gradient-beam-cta, gradient-cta, gradient-pill-button, ignition-button, induction-button, launch-button, particle-orb, plasma-button, sliding-text-cta, spinning-border-button, tactile-button, uploading-button

---

### Recursive Erosion（recursive-erosion）
- 运行时：Raw WebGL + Canvas 2D
- 模式：A looping particle sphere that recursively erodes into holes while luminous trails crawl across its surface.
- 渲染管线：3 WebGL particle passes + 1 Canvas 2D grain composite
- 交互：Authored four-second seamless loop + optional final-frame palette

---

### Quantera Trading Background（quantera-trading-background）
- 运行时：Three.js r165 + postprocessing
- 模式：A deep green trading field with volumetric light shafts, drifting chalk equations, sparkling dust, subtle bloom, and pointer parallax.
- 渲染管线：1 Three.js scene render + UnrealBloom postprocessing
- 交互：Pointer-driven light, equation, particle, and camera-space parallax
- Contract 要点：renderer=Three.js r165 + bloom；presentation=Background only; page UI hidden；layers=Light shafts + equations + particles；interaction=Parallax + light response；motion=Visibility + reduced motion；pixelRatio=≤ 1.75；assets=No binary scene assets

---

### Constellation Field（constellation-field）
- 运行时：Canvas 2D + Raw WebGL
- 模式：A family of particle networks, gateways, interface lines, defense traces, and topographic fields gathered into one configurable collection.
- 渲染管线：1 active isolated source pass
- 交互：Variant selection plus customizable mode, speed, size, stroke width, length, density, opacity, and palette
- 变体：connectivity-graph, constellation-field, defense-lines, flux-vortex, gateway-flow, interface-lines, particle-drift, particle-network, topo-field

---

### Portal Field（portal-field）
- 运行时：Three.js r134 + Raw WebGL + Canvas 2D
- 模式：Five ambient field backgrounds collected across Three.js, raw WebGL, and Canvas 2D renderers.
- 渲染管线：1 selected ambient field composition
- 交互：Variant selection plus customizable motion, geometry, opacity, and palette
- 变体：amber-halftone, bell-field, cloud-field, flow-field, portal-field, stream-convergence
- Contract 要点：variants=Portal + Flow + Cloud + Bell + Stream Convergence

---

### Laser（matrix-field）
- 运行时：Raw WebGL
- 模式：Four pointer-reactive laser scenes spanning a preserved matrix junction, atmospheric blade, vanishing array, and halftone relay.
- 渲染管线：1 selected raw-WebGL laser pass
- 交互：Variant selection, smoothed pointer response, reduced-motion stills, and customizable motion, geometry, opacity, and palette
- 变体：connectivity-graph, gateway-flow, interface-lines, laser-atmospheric-blade, laser-halftone-relay, laser-vanishing-array, matrix-field
