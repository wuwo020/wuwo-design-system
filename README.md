> **WUWO Design System** — 个人/团队设计系统 Skill，可直接装进 AI 编码助手（Codex / Claude Code / Hermes / Pi 等任何支持 `SKILL.md` 的工具）使用。

---

## 这是什么

一套**完整的设计系统技能包**：给 AI 助手一份可执行的视觉规范，让它在做页面、改 UI、选组件、加动效、定配色、写 `DESIGN.md` 时，产出统一、不"AI 味"的成品。

它不是一个组件库，也不是一个网站模板——它是**给 AI 看的设计说明书 + 可直接复用的资产**。

## 两大主题

| 主题 | 说明 |
|---|---|
| **暗夜梦核 Dark Dream-core**（默认） | 深蓝黑底 `#0B1020` + 月光白文字 + 粉/紫/青三色点缀，玻璃拟态微光，适合个人品牌、内容站、直播氛围页 |
| **亮色暖调 Light Warm**（变体） | 奶油底 `#F7F4EF` + 琥珀点缀，适合白天阅读、杂志/编辑风、对外交付 |

两套 token 通过 `html[data-theme="light"]` 切换，同一份代码平滑换肤。

## 目录结构

```
SKILL.md              技能主文档（501 行）—— 风格宣言、token、组件规范、动效、流程、反 AI 味清单
bundles/              可直接用的组件组合包
  ├── landing-kit/      落地页套件（hero、特性卡…）
  └── agent-ui-kit/     AI 应用界面套件
references/           参考与规范
  ├── transitions/      27 种过渡动效
  ├── threeui/          三维界面参考
  └── pretext/          文本排版创意
templates/            模板库
  ├── web-designs/      54 个知名网站风格拆解（Stripe / Linear / Vercel / Apple …）
  ├── design-md/        DESIGN.md 起步模板
  └── pretext/          排版创意示例页
scripts/              辅助脚本
```

## 安装

把整个仓库放到你所用助手的技能目录即可。

**Codex**
```bash
git clone https://github.com/wuwo020/wuwo-design-system.git ~/.codex/skills/wuwo-design-system
```

**Claude Code**
```bash
git clone https://github.com/wuwo020/wuwo-design-system.git ~/.claude/skills/wuwo-design-system
```

**Hermes**
```bash
git clone https://github.com/wuwo020/wuwo-design-system.git ~/.hermes/skills/wuwo-design-system
```

装好后开新会话，直接说需求即可，例如：

> 用 `wuwo-design-system` 做一个产品落地页，暗色主题，三个特性卡，要有微光玻璃质感。

## 包含哪些能力

- **风格宣言**：8 个核心 token + 使用铁律（一次只用 1–2 个点缀色、不用三色渐变、圆角规范、玻璃拟态参数）
- **组件层**：按钮、卡片、导航、表单、弹窗、表格、空状态等
- **动效层**：27 种过渡、滚动叙事、微交互、`reduced-motion` 降级
- **风格库**：54 个知名网站的设计体系拆解，可作参考或混搭
- **流程层**：从需求到交付的设计流程 + 反 slop（去 AI 味）检查清单
- **变体工作流**：一次产出多套方案供挑选
- **文本排版创意**：文字驱动的视觉实验
- **像素 Logo → SVG → 品牌动效**工作流

## 设计原则（节选）

- 暗色优先，纯白文字要避免（用 `#F2F4FA` 级月光白）
- 点缀色克制：紫为主，粉/青为辅，琥珀做暖调变体
- 渐变只用在关键视觉点，双色即可
- 不用尖锐直角，除非内容明确是工业/终端风
- 发光用同色系低透明度阴影，不用外发光贴纸感

---

## 许可

MIT
