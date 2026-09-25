# ThreeUI 参考 · threejs scenes（22 家族，PRO 0）

模式要点：程序化几何 + PMREM 环境烘焙 + instancing；交互统一为 pointer orbit/drag inertia/raycast hover。落地：材质 tint 换 wuwo 点缀色系，背景换 --ink。

### Noema Bloom（noema-bloom）
- 运行时：Three.js r149
- 模式：An interactive blue particle flower that unfurls from a closed bud into a luminous bloom across a starry, atmospheric field.
- 渲染管线：1 live Three.js particle scene render + 6 bloom and grain post passes
- 交互：Pointer petal push, drag rotation with inertia, auto return, and double-click or Escape reset
- Contract 要点：renderer=Three.js r149 + custom bloom；presentation=Background only; landing-page UI hidden；subject=Particle flower bud-to-bloom morph；interaction=Push + orbit + inertial return；motion=Visibility + reduced-motion still；pixelRatio=Source governor up to 2x；assets=No binary scene assets

---

### Receipt Printer（receipt-printer）
- 运行时：Three.js r160 + Canvas 2D + DOM/CSS
- 模式：An interactive checkout card that prints a textured membership receipt as simulated Three.js cloth, lets the paper react to pointer wind and pulling, and shreds it when the order is cancelled.
- 渲染管线：1 live Three.js cloth render + 1 Canvas 2D receipt-artwork pass
- 交互：Automatic print cycle, replay, cancel-to-shred, pointer wind, and drag-to-pull cloth physics
- Contract 要点：renderer=Three.js r160 + Canvas 2D + DOM/CSS；source=Complete self-contained HTML focused on the printer；surface=Receipt texture + cloth and shred physics on a flat charcoal；interaction=Wind + pull + replay + cancel；motion=Visibility suspension + reduced-motion still；layout=Responsive isolated printer stage at the original 1x present；assets=Hosted fonts + Three.js r160; no binary scene files

---

### Heatmap Badge（heatmap-badge）
- 运行时：Canvas 2D + DOM/CSS
- 模式：A suspended conference credential with a pointer-painted thermal face, relit vinyl sleeve, and a lanyard that bends, swings, and settles under a compact rigid-body simulation.
- 渲染管线：2 visible Canvas 2D passes plus offscreen heat, crinkle-normal, gloss, and print buffers
- 交互：Pointer-painted heat, tilt and relighting, plus grab-and-drag rigid-body swing on a dual-cord Verlet lanyard
- Contract 要点：renderer=Canvas 2D + DOM/CSS；source=Complete self-contained authored HTML；surface=Heat field + crinkle normals + gloss composite；physics=Dual Verlet cords + rigid badge body；interaction=Heat paint + tilt + drag + swing；motion=Visibility suspension + reduced-motion still；assets=Self-contained fonts and procedural scene

---

### Hourglass Loader（hourglass-loader）
- 运行时：Three.js r149 + Canvas 2D + DOM/CSS
- 模式：A tactile wooden hourglass that drains, glides, and tips over through a seamless ten-second loop, with pointer-driven lighting, spring wobble, and light and dark themes.
- 渲染管线：1 live Three.js render with runtime-generated albedo, normal, roughness, environment, and backdrop textures plus a DOM progress capsule
- 交互：Pointer camera parallax, surface-tracked spotlight, spring-driven hourglass wobble, and an animated light/dark theme switch
- Contract 要点：renderer=Three.js r149 + Canvas 2D textures；source=Complete authored HTML preserved unchanged；loop=10-second drain + physical tip-over；interaction=Parallax + spotlight + spring wobble + theme toggle；motion=Visibility suspension + reduced-motion still；layout=Settled desk composition with adaptive camera framing；assets=4 material swatches + local Three.js r149

---

### 3D Lego（skills-plugins）
- 运行时：Three.js r149 + Canvas 2D
- 模式：A crisp Three.js keyboard family: a compact knobbed keyboard leads the authored blue four-stud brick, a narrow remote control, and a four-colour game pad, all built from the brick's own lofted fillets, ring-stamped connectors, and lighting.
- 渲染管线：1 live Three.js scene render
- 交互：Pointer-following isometric tilt, responsive orthographic framing, raycast hover and press feedback on every control, and knobs that turn under the cursor
- 变体：skills-plugins, skills-plugins-gamepad, skills-plugins-keyboard, skills-plugins-remote-control
- Contract 要点：renderer=Sandboxed source + direct Three.js；source=Owner HTML, connectors restamped；variant=brick | keyboard | remote-control | gamepad；geometry=Lofted rounded-profile product bodies；interaction=Tilt + button hover and press；lifecycle=Visibility + reduced motion；assets=None

---

### Wood Icons（wood-icons）
- 运行时：Three.js r149
- 模式：A tactile Three.js object family pairing carved timber with blue glass: a handheld console, a compact keyboard, and a translucent popsicle, each with its own procedural geometry and shared material language.
- 渲染管线：Two scene passes plus a six-level bloom and final composite pipeline
- 交互：Pointer orbit, drag-to-spin inertia, responsive DPR control, plus raycast buttons and keys on the handheld and keyboard
- 变体：wood-icons, wood-icons-keyboard, wood-icons-popsicle
- Contract 要点：renderer=Three.js r149 + custom postprocessing；variant=gameboy | keyboard | popsicle；materials=Procedural wood + two-shell refractive glass；interaction=Hover orbit + inertial drag + controls；motion=Visibility + reduced-motion still；pixelRatio=Source governor up to 1.75x；assets=No binary assets

---

### Sylva Living World（sylva-living-world）
- 运行时：Three.js r149
- 模式：A scene-only procedural world that shifts from living green moss roots into mossy boughs in Sakura blossom, Maple autumn leaf, or Sequoia foliage — each in its own light.
- 渲染管线：1 live Three.js scene render with procedural ShaderMaterials, CanvasTextures, and instancing
- 交互：Pointer-driven moss parting, camera parallax, pollen trails, scan-light entrance, and butterfly flight
- 变体：sylva-living-world, sylva-living-world-maple-autumn, sylva-living-world-sakura-sunset, sylva-living-world-sequoia-mist
- Contract 要点：renderer=Three.js r149；variant=Living Green | Sakura Sunset | Maple Autumn | Sequoia Mist；scene=Moss roots | one shared bough world in Sakura, Maple, or Seq；presentation=Scene only; source page UI removed；interaction=Moss response + pollen + parallax；motion=Visibility + reduced motion；pixelRatio=≤ 2；assets=No binary scene assets

---

### Sunset Valley（sunset-valley）
- 运行时：Three.js r149
- 模式：An interactive procedural valley that moves from its authored sunset into a fern-banked forest morning, a starry aurora night with layered wisps, or the blue hour after the sun has gone.
- 渲染管线：1 live scene render + PMREM environment bake + optional instanced fern understory or five-curtain aurora layer
- 交互：Pointer cloud flow, grass parting, sand scuffs, river ripples, dust, and stone physics
- 变体：sunset-valley, sunset-valley-aurora, sunset-valley-blue-hour, sunset-valley-forest
- Contract 要点：renderer=Three.js r149；scene=Sunset / Forest / Aurora / Blue Hour；environment=PMREM sky probe；interaction=Terrain + atmosphere；pixelRatio=≤ 1.7；assets=4 owned environment fallbacks

---

### Temple Night（temple-night）
- 运行时：Three.js r149
- 模式：One procedural world engine pointed at four places: Kage’s Kyoto mountain temple after dark, Yosemite Valley under alpenglow, a Presidio park above the Golden Gate, and Lake Louise at dusk — same rig, same foreground plates, same bloom pipeline.
- 渲染管线：17 — scene + 16-pass bloom/composite pipeline
- 交互：Pointer parallax and world-space cursor wisps
- 变体：lake-louise, presidio-sunset, temple-night, yosemite-sunset
- Contract 要点：renderer=Three.js r149；variant=temple-night | yosemite-sunset | presidio-sunset | lake-loui；scene=Procedural temple, valley, headland, or lake world；post=16 authored passes；interaction=Parallax + motes；pixelRatio=≤ 1.8；assets=None；renderer=Three.js r149

---

### Sakura Branch（sakura-branch）
- 运行时：Three.js r160
- 模式：Two procedural cherry boughs at sunset: the lush pink Sakura scene and the sharper, ember-orange Sentra branch from learnme.html.
- 渲染管线：1 live Three.js scene render with procedural ShaderMaterials and CanvasTextures
- 交互：Pointer-driven canopy wind, drifting petals, and animated blossoms; the Sakura preset also includes butterfly flight
- 变体：sakura-branch, sakura-branch-sentra
- Contract 要点：renderer=Three.js r160；variant=sakura | sentra；scene=Cherry bough + blossom canopy；interaction=World-space wind response；motion=Reduced-motion aware；pixelRatio=≤ 2；assets=No external scene assets

---

### Landscape（landscape）
- 运行时：Three.js r149
- 模式：A tower-free procedural terrain whose light, sky, fog, stars, rain, lightning, snow, grass, and stones move through seven authored environment states.
- 渲染管线：1 live Three.js render with a polar heightfield, instanced grass and stones, gradient sky, stars, and layered weather
- 交互：Pointer parallax, drag-to-orbit, wheel and pinch zoom, with cross-fading time and weather systems
- 变体：landscape-night, landscape-noon, landscape-rain, landscape-snow, landscape-storm, landscape-sunrise, landscape-sunset
- Contract 要点：renderer=Three.js r149；variant=Sunrise / Noon / Sunset / Night / Rain / Storm / Snow；structure=Tower-free terrain, grass, stones, sky, stars, and weather；time=Morning / Noon / Sunset / Night；weather=Clear / Rain / Storm / Snow；camera=Orbit + parallax + zoom；pixelRatio=≤ 2；assets=No external scene assets

---

### Country Towers（japanese-tower）
- 运行时：Three.js r149 + Canvas 2D
- 模式：Six country-specific towers assembling above a procedural landscape: Japanese, Chinese, Vietnamese, Thai, Khmer, and Ottoman.
- 渲染管线：1 live Three.js scene render with six authored architecture builders and procedural CanvasTexture generation
- 交互：Country selection, automatic 4.4-second construction, pointer orbit, hover parallax, pinch and wheel zoom, and camera reset
- 变体：japanese-tower, tower-cambodia, tower-china, tower-thailand, tower-turkey, tower-vietnam
- Contract 要点：renderer=Three.js r149；country=Japan / China / Vietnam / Thailand / Cambodia / Turkey；structure=Six authored procedural architectures；landscape=Terrain + mountains + grass + stones；camera=Orbit + parallax + zoom；pixelRatio=≤ 2；assets=Runtime + texture set

---

### Bookshelf（bookshelf）
- 运行时：Three.js r165
- 模式：The exact seven-volume Bookshelf collection with its authored room, carousel shelf, individual cover artwork, foil, pages, inspection, opening, and page-turn system.
- 渲染管线：1 live scene render + PMREM environment bake
- 交互：Shelf navigation, volume selection, click-to-inspect, cover drag, paginated leaf drag, orbit, pan, and reset
- Contract 要点：renderer=Three.js r165；collection=7 authored volumes；environment=PMREM room；interaction=Inspect + cover + pages；pixelRatio=≤ 2；assets=2 exact owned atlases

---

### Wallet（mechanical-keyboard）
- 运行时：Three.js r149
- 模式：An isometric product collection led by a leather bifold standing open on its fold, with the authored keyboard, a sculpted wireless mouse, and a remote firing its emitter alongside it — each on the same camera, environment, light rig and material language, and each detailed for what it actually is.
- 渲染管线：1 live Three.js scene render + shared PMREM environment bake per document
- 交互：Pointer orbit plus card-draw, key, click-plate, wheel, DPI, and remote button feedback
- 变体：mechanical-keyboard, mechanical-mouse, mechanical-remote, mechanical-wallet
- Contract 要点：renderer=Three.js r149；camera=Orthographic isometric；object=Wallet / Keyboard / Mouse / Remote；interaction=Orbit + product controls；pixelRatio=≤ 2；assets=Font + exact runtime

---

### Isometric Motion Grid（isometric-motion-grid）
- 运行时：SVG + JavaScript
- 模式：Six animated product scenes arranged as a dark isometric SVG grid, with live orthographic azimuth and elevation responding independently to each pointer.
- 渲染管线：6 live SVG illustration passes
- 交互：Independent pointer-driven azimuth and elevation with ambient timeline animation
- Contract 要点：renderer=SVG DOM；figures=6；camera=Azimuth + elevation；motion=requestAnimationFrame；assets=None

---

### Isometric Charging Dock（isometric-charging-dock）
- 运行时：Three.js r149
- 模式：A monochrome isometric charging dock whose puck, capsule, lid indicators, badge, and weighted ink outlines move through a precisely authored 172-frame loop.
- 渲染管线：1 scene render with instanced screen-space outline geometry
- 交互：Autonomous 172-frame loop with deterministic frame and playback hooks
- Contract 要点：renderer=Three.js r149；camera=Orthographic true-isometric；motion=172 frames at 60 fps；outlines=Instanced screen-space fat lines；assets=Pinned Three.js r149 runtime only

---

### 365 Shapes（365-tetrahedron）
- 运行时：Raw WebGL 2
- 模式：Four monochrome 365 studies pairing a tumbling refractive solid with its matching pixel-built shape word, bloom, radial light shafts, and tactile drag inertia.
- 渲染管线：11 — scene, bright extraction, downsample, six blur passes, radial rays, and composite
- 交互：Pointer orbit plus drag-to-throw inertia, responsive DPR-capped resize, and visibility-aware preview lifecycle
- 变体：365-cube, 365-hexagon, 365-pentagon, 365-tetrahedron, 365-triangle
- Contract 要点：renderer=Raw WebGL 2；geometry=Cube | Triangle | Hexagon | Pentagon；wordmark=Shape name follows selected geometry；post=Bloom + radial rays + grain；interaction=Orbit + drag inertia；pixelRatio=≤ 2；assets=Glyph paths only

---

### Isometric Mail Light Shafts（iso-mail-lightshafts）
- 运行时：Canvas 2D
- 模式：Five flat-vector isometric scenes under the same animated light shafts: opening mail, a keyboard with an Apple Magic Mouse, a mirrorless camera with a hovering drone, a condenser microphone desk, and a spiral notepad with coffee.
- 渲染管线：5 — light curtain, shadows, painter-sorted solids, foreground props, and glow composite
- 交互：Pointer-driven orbit with coin physics, proximity-reactive keys and mouse, a lens wake-up and drone hover, a microphone that hears the pointer, or a notepad sheet that lifts under it
- 变体：iso-mail-lightshafts, iso-mail-lightshafts-camera-drone, iso-mail-lightshafts-keyboard, iso-mail-lightshafts-microphone, iso-mail-lightshafts-notepad
- Contract 要点：renderer=Canvas 2D；camera=Orthographic orbit；variants=Mail + Keyboard + Camera & Drone + Microphone + Notepad；geometry=3D painter sort；framing=Shared 999 x 619 design footprint；interaction=Coins, keys, mouse, lens, hover, level, and paper；pixelRatio=≤ 2；motion=Reduced-motion still

---

### Scalability Bricks（scalability-bricks）
- 运行时：Three.js r147 + Cannon.js
- 模式：An interactive isometric brick massif with falling illuminated pieces, physics-driven collisions, five accent palettes, three material styles, and adaptive light and dark surfaces.
- 渲染管线：4 — faceted bricks, edge lines, additive halos, and impact particles
- 交互：Orbit, zoom, throwable bricks, double-click reset, theme, material style, and accent palette
- Contract 要点：renderer=Three.js r147 + Cannon.js 0.6.2；camera=Orthographic orbit + zoom；physics=Throw + collision + reset；pixelRatio=≤ 2；assets=3 pinned runtime scripts + Geist

---

### Structure Flow（structure-flow）
- 运行时：Three.js r128–r160
- 模式：Thirteen authored Three.js field studies collected as one family, spanning particle domes, horizons, orbital systems, matrices, topology, fluid fields, embers, and vortexes.
- 渲染管线：1–2 Three.js scene, point-cloud, or ShaderMaterial passes
- 交互：Variant-specific pointer, motion, geometry, opacity, mask, and palette controls
- 变体：data-field, dimensional-field, dot-matrix, ember-storm, emerald-horizon, expanse-field, fluid-field, flux-vortex, logic-core, nebula, orbital-sphere, structure-flow, topology-field
- Contract 要点：renderer=Three.js r128–r160；variants=13 field studies；controls=Renderer-specific；assets=None；renderer=Three.js r128；geometry=Fullscreen plane；assets=None；renderer=Three.js r128

---

### Warp Field（warp-field）
- 运行时：Three.js r128
- 模式：Nexus’s focused hero warp: 400 emerald additive streaks and 40 luminous tiles streaming through an authored deep-space fog field.
- 渲染管线：1 Three.js scene render
- 交互：Customizable speed, streaks, tiles, color, camera, and brightness
- 变体：data-field, dimensional-field, expanse-field, halftone-flow, logic-core, neon-sign, topology-field, warp-field
- Contract 要点：renderer=Three.js r128；streaks=400；tiles=40；assets=None

---

### Woven Cloth（woven-cloth）
- 运行时：Three.js r160
- 模式：A Three.js woven-cloth simulation with Woven Cloth typography printed into its procedural textile so every letter deforms with the fabric.
- 渲染管线：1 Three.js cloth scene pass
- 交互：Typography deforms with the authored textile motion + optional final-frame palette
- 变体：ember-storm, fluid-field, nebula, woven-cloth
