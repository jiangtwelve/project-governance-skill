# Agent Bootstrap

除非 `AGENTS.md` 中 project-governance block 为 `Status: disabled`，否则所有 agent 必须遵守本文件。

Metadata: governance_skill=project-governance; governance_version=1.0.0; initialized_at=TBD; project_type=TBD

## 启动

1. 先读 `ssot/PROJECT_STATE.md`，确认当前 `Current Version`、骨架四段状态、`Active Process`、`Backlog` 与 `Stage Regressions`。
2. 再读 `rules/GRILLING_PROTOCOL.md`、`rules/DEVELOPMENT_PROCESS.md`、`rules/VERSION_RULES.md`、`rules/DOCUMENTATION_RULES.md`、`ssot/GLOSSARY.md`。
3. 按任务读取相关 SSOT、流程、验收、导入或决策文件；默认只读 `.project-governance/decisions/INDEX.md`，需追溯时再读单个决策文件。

## 强制规则

### 项目骨架红线（永远不可省）

- 项目骨架固定四段（需求确认、技术栈确认、实际开发、验收测试）跨项目不可变，不允许重命名、合并、跳过。
- 第一段、第二段未 `Confirmed` 不得进入第三段；第四段未 `Confirmed` 不得结束当前版本、不得启动新版本。
- 当前版本未完成时禁止升版本；用户硬升必须按 `rules/VERSION_RULES.md` 的"硬升应对"处理。

### 实际开发段内部流程

- 实际开发段内部流程在第二段商定，确定后写入 `.project-governance/processes/active.md`。
- 流程改动允许加 / 删 / 重排 / 改内容，逐条按追问协议确认；单次改动超过 `Process Mutation Threshold`（默认 3）时，agent 必须先反问"是否换流程而不是改"。
- 流程改动确认后，本段从新流程第一个阶段重新开始；新旧重叠产物必须逐条研判（复用 / 局部修补 / 重做），结果写入决策记录。
- 阶段级红线：任何 `acceptance_required: true` 的阶段，未经用户明确确认不得推进。

### 文档与回归

- 不允许"快速开始写代码，文档以后再补"。
- 需求/交互变化更新 `ssot/PRD.md`；架构/接口/数据模型/部署变化更新对应 SSOT。
- 主文档更新后按影响范围回归对应骨架段（参见 `rules/DEVELOPMENT_PROCESS.md` 的回归规则），跳过不受影响阶段必须由用户确认。
- 验收和关键确认只能来自用户明确表达；`PROJECT_STATE.md` 仅在实质状态变化时更新。

### 双语对照

- 用户或 agent 引入任何新概念前，必须先在 `ssot/GLOSSARY.md` 登记并对齐含义。
- 与用户对话用 `User Term` 列的词；写入文档前反翻译成 `Doc Term` 列的词。
- 同一术语含义跨版本变化时追加 `Revisions`，不覆盖旧含义。

### 流程库

- 流程库位置：`~/.claude/process-library/`（用户本机私有）。
- 第二段开始时 agent 必须检索流程库；库为空或无合适模板时现场起草，逐条与用户对齐。
- 沉淀触发：首版第四段 `Confirmed` 时强制询问；后续版本改过流程并完成一轮时再询问。沉淀写入由 agent 与用户共同完成。

## 索引

- SSOT：`ssot/PRD.md`、`ssot/ARCHITECTURE.md`、`ssot/API_CONTRACT.md`、`ssot/PROJECT_STATE.md`、`ssot/GLOSSARY.md`
- 规则：`rules/GRILLING_PROTOCOL.md`、`rules/DEVELOPMENT_PROCESS.md`、`rules/VERSION_RULES.md`、`rules/DOCUMENTATION_RULES.md`、`rules/UPGRADE_RULES.md`
- 流程：`.project-governance/processes/active.md`（本项目本版本流程）、`~/.claude/process-library/`（用户私有流程库）
- 追溯：`.project-governance/decisions/INDEX.md`、`.project-governance/imports/SOURCE_INDEX.md`
