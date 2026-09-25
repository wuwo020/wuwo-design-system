# ThreeUI 参考 · ui elements css（13 家族，PRO 0）

模式要点：Canvas 2D 点阵/雕刻质感 + DOM 骨架；多数可脱离 WebGL 独立用。落地：engraved/dot 质感保留，色板换 wuwo；brand-orbs 思路可做自有品牌状态球。

### Character Carousel（character-carousel）
- 运行时：DOM + CSS
- 模式：Two authored editorial character-card carousels collected as a light filmstrip and a dark responsive wave.
- 渲染管线：1 selected responsive DOM/CSS card composition
- 交互：Pointer focus, wheel and arrow navigation, card selection, idle drift, responsive orientation, scale, speed, opacity, and palette
- 变体：character-carousel, character-filmstrip, character-wave
- Contract 要点：renderer=Sandboxed authored DOM/CSS documents；interaction=pointer + wheel + keyboard + card focus；lifecycle=responsive + visibility-aware + reduced motion；renderer=Sandboxed authored light filmstrip；interaction=pointer + wheel + keyboard + card focus；lifecycle=responsive + visibility-aware + reduced motion；renderer=Sandboxed authored dark wave；interaction=pointer + wheel + keyboard + card focus + orientation toggle

---

### Gallery（gallery）
- 运行时：Three.js r149
- 模式：The isolated Vantrix hero image ribbon: sixteen curved editorial panels orbiting a vertical cylindrical rail on a quiet paper grid.
- 渲染管线：1 live Three.js scene with 16 textured cylindrical panels
- 交互：Automatic rotation and vertical drift, responsive DPR-capped resize, reduced-motion still frame, and visibility-aware lifecycle
- Contract 要点：renderer=Extracted hero carousel only；geometry=16 curved cylindrical image panels；motion=speed + scale；lifecycle=responsive + visibility-aware + reduced motion；assets=5 authored WebP textures

---

### Genie Dock（genie-dock）
- 运行时：DOM + SVG + CSS
- 模式：A macOS-inspired application dock where live windows bend into their icons along a measured Genie curve, then restore without flattening their DOM content.
- 渲染管线：20–64 live DOM slices per moving window + 1 SVG silhouette
- 交互：Click dock icons or traffic lights to minimize and restore, drag titlebars downward to scrub the curve, move and zoom windows, and edit live form controls mid-flight
- Contract 要点：renderer=Sandboxed authored DOM/SVG document；motion=Measured Genie funnel with live DOM slices；interaction=dock + traffic lights + pointer drag + form controls；lifecycle=responsive + visibility-aware + reduced motion；assets=Lexend variable font + fjord image

---

### Engraved Certificate（engraved-certificate）
- 运行时：Canvas 2D + DOM/CSS
- 模式：A responsive engraved certificate: plate field, dual guilloche rosettes, and a drifting harmonic pass that auto-cycles through four cam states.
- 渲染管线：3 Canvas 2D engraving passes + DOM certificate
- 交互：Auto-cycled cam configurations + optional final-frame palette

---

### Performance Gauges（performance-gauges）
- 运行时：DOM + CSS
- 模式：Four layered CSS instruments — tachometer, speedometer, turbo boost, and EV power — each isolated to one full-bleed dial with polar tick geometry, scale bands, and a self-testing needle sweep.
- 渲染管线：4 layered CSS gauge compositions, one per variant
- 交互：Self-test needle sweep, settle, and idle flutter with a counting readout + optional final-frame palette
- 变体：performance-gauges, performance-gauges-boost, performance-gauges-power, performance-gauges-speedometer

---

### Uplink Loader（uplink-loader）
- 运行时：DOM + CSS + JavaScript
- 模式：A cinematic secure-uplink loader with stepped progress, illuminated telemetry ticks, neon readouts, technical corner markers, mirrored side rails, scanlines, and procedural grain.
- 渲染管线：1 DOM/CSS loader composition
- 交互：Autonomous stepped progress sequence with phase labels, completion hold, and reset glitch

---

### Koi Studies（koi-studies）
- 运行时：DOM + CSS 3D + Canvas 2D + WebGL
- 模式：A tactile stack of three Japanese koi studies with CSS 3D depth, pointer tilt, drag and keyboard navigation, pixel-mask reveals, and animated halftone imagery.
- 渲染管线：3 Canvas 2D halftone card faces + 1 CSS 3D stack + 1 ambient shader canvas
- 交互：Drag, tap, or use the arrow keys to cycle cards, with pointer tilt, reveal trails, responsive layout, and reduced-motion behavior
- Contract 要点：renderer=Sandboxed authored DOM/CSS/Canvas document；cards=Kōhaku + Shūsui + Utsuri；interaction=pointer drag + tap + keyboard + hover tilt；halftone=300-frame inline pixel mask at 30 fps；assets=3 JPEGs + 3 MP4 clips + inline mask；fallback=CSS field when the optional remote shader is unavailable；motion=Reduced motion, reduced transparency, visibility, and focus 

---

### Animated Top Dock（animated-top-dock）
- 运行时：DOM + CSS
- 模式：Sable’s top navigation dock with its authored downward spring expansion, proximity field, glass layers, focus behavior, and active menu state.
- 渲染管线：1 spring layout pass across 6 dock items
- 交互：Pointer proximity, keyboard focus, active selection, reduced motion, and mobile static mode
- Contract 要点：renderer=DOM + CSS；items=1 logo + 5 menu items；proximity=122 px；spring=0.19 / 0.70；motion=Pointer + focus + reduced motion

---

### Sketchbook（sketchbook）
- 运行时：DOM + CSS 3D
- 模式：The exact Singapore paper sketchbook with nested-strip page curls, direct dragging, tilt, zoom, a movable magnifying glass, and its complete authored plate set.
- 渲染管线：18 nested CSS 3D strips per turning leaf
- 交互：Drag or tap pages, arrows, keyboard, cursor tilt, zoom, and draggable loupe
- Contract 要点：renderer=DOM + CSS 3D；pageCurl=18 nested strips；interaction=Drag + zoom + loupe；motion=Reduced-motion aware；assetBaseUrl=/sketchbook/；assets=17 exact local files

---

### Diagnostics Panel（diagnostics-panel）
- 运行时：Canvas 2D
- 模式：Three diagnostic illustration variants — layered planes, node cubes, and a flowing mesh — each isolated without page chrome or copy.
- 渲染管线：1 active isolated Canvas 2D illustration
- 交互：Variant selection plus customizable speed, size, opacity, and palette
- 变体：diagnostics-panel, diagnostics-panel-flow, diagnostics-panel-nodes

---

### Skeuomorphic Toggle（skeuomorphic-toggle）
- 运行时：DOM/CSS
- 模式：A tactile skeuomorphic toggle with a sliding on/off thumb that automatically matches light and dark appearances, isolated without the surrounding card.
- 渲染管线：1 isolated source pass
- 交互：Automatic site/system appearance with explicit light and dark overrides, plus customizable size, opacity, and palette

---

### Wireframe Forms（wireframe-forms）
- 运行时：Canvas 2D
- 模式：A family of rotating wireframe forms, with the cube, crossed cylinders, and nested sphere isolated as individual variants.
- 渲染管线：1 isolated source pass
- 交互：Three selectable shape variants with customizable speed, size, length, density, opacity, and palette
- 变体：defense-lines, topo-field, wireframe-forms, wireframe-forms-cylinders, wireframe-forms-sphere
- Contract 要点：variant=Cube | Cylinders | Sphere

---

### Brand Orbs（brand-orbs）
- 运行时：Canvas 2D
- 模式：Twenty-three animated brand marks rebuilt as small and medium dimensional dot orbs for AI status, product activity, and compact loading states.
- 渲染管线：1 transparent Canvas 2D dot-lattice pass
- 交互：Twenty-three variants, small and medium presets, dark-first theme, speed, pause, reduced motion, visibility pause, and deterministic restart
- 变体：brand-orbs, brand-orbs-aura, brand-orbs-codex, brand-orbs-css, brand-orbs-cursor, brand-orbs-designcode, brand-orbs-dreamcut, brand-orbs-email, brand-orbs-figma, brand-orbs-framer, brand-orbs-gemini, brand-orbs-github, brand-orbs-instagram, brand-orbs-ios, brand-orbs-linkedin, brand-orbs-neuform, brand-orbs-openai, brand-orbs-react, brand-orbs-swift, brand-orbs-threads, brand-orbs-ui, brand-orbs-ux, brand-orbs-x
- Contract 要点：renderer=Sandboxed authored Canvas 2D engine；variants=23 brand marks；size=Small 20px | Medium 56px (default)；theme=Dark (default) | Light；motion=Speed | Pause | Reduced motion | Visibility；assets=Vector paths + procedural dots
