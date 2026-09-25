# Agent UI Kit（AI 原生界面组件包）

> 来源：BeautifulUI（beautifului.dev，AI-native 界面模式 12 类，2026-08-17 收录）
> 定位：**Agent 交互界面**——加载、思考、流式回复、人机确认、任务状态、检索上下文等
> 场景：AI 助手界面、Agent 后台、聊天应用、工作流编排页
> 使用方式：按模式文件取结构 + 关键样式，颜色一律换 wuwo token（见 SKILL.md ① 风格宣言）

## 模式速查

| # | 模式 | 文件 | 典型场景 |
|---|---|---|---|
| 01 | Pixel-grid 加载态 | `01-loading-state.md` | 等待 Agent 响应 |
| 02 | 可展开推理轨迹 | `02-thinking-traces.md` | Agent 思考过程展示 |
| 03 | 流式文本+内联来源 | `03-streaming-text.md` | AI 回答输出 |
| 04 | 人机确认卡 | `04-approval-card.md` | 执行前征求用户批准 |
| 05 | 工具调用 Chips | `05-tool-chips.md` | 代码编辑/工具调用记录 |
| 06 | 实时任务状态行 | `06-task-rows.md` | 多任务进度总览 |
| 07 | 分页聊天面板 | `07-chat-panel.md` | 多会话聊天 |
| 08 | 高级 Prompt 输入条 | `08-prompt-bar.md` | 带来源/命令/模型的输入条 |
| 09 | 推荐+置信度卡 | `09-recommendation-card.md` | Agent 决策建议 |
| 10 | 检索上下文卡 | `10-context-cards.md` | RAG/知识检索展示 |
| 11 | 表格差异预览 | `11-diff-table.md` | AI 批量改数据确认 |
| 12 | 记录网格 | `12-records-table.md` | CRM/数据管理 |

## 选用规则

- 加载中 → **01**；思考/推理中 → **02**（细分：stages=规划、traces=推理、reading=检索）
- 输出回答 → **03**（有来源加内联徽章，有后续动作加 follow-up）
- 要人拍板 → **04**（单选）或 **09**（推荐+置信度）
- 展示 Agent 干了什么 → **05**（单次动作）或 **06**（任务列表）
- 用户发指令 → **08**；多轮对话 → **07**
- 展示检索到的知识 → **10**；AI 改表格建议 → **11**；管理型数据 → **12**
