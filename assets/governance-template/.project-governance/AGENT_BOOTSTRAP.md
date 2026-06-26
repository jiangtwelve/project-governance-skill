# Agent Bootstrap

除非 `AGENTS.md` 中 project-governance block 为 `Status: disabled`，否则所有 agent 必须遵守本文件。

## 启动顺序

1. 读 `ssot/PROJECT_STATE.md`。
2. 读 `rules/GRILLING_PROTOCOL.md`、`rules/DEVELOPMENT_PROCESS.md`、`rules/DOCUMENTATION_RULES.md`、`rules/LOGGING_RULES.md`。
3. 按任务读取相关 SSOT、流程、验收、导入或决策文件。
4. 默认只读 `decisions/INDEX.md`；需要追溯原因时再读单个决策文件。

## 强制规则

- 不允许“快速开始写代码，文档以后再补”。
- PRD、架构、阶段状态确认前，不得进入代码实现。
- 有需求、交互、架构、接口、数据模型、流程阶段歧义时，必须执行追问协议。
- 需求或交互变化必须更新 `ssot/PRD.md`；架构、接口、数据模型、部署变化必须更新对应 SSOT。
- 主文档更新后，按影响范围重走流程；跳过不受影响阶段必须由用户明确确认。
- 验收和关键确认只能来自用户明确表达，agent 不得自行推断。
- 开始前读取 `PROJECT_STATE.md`，结束后仅在实质状态变化时更新。

## 索引

- SSOT：`ssot/PRD.md`、`ssot/ARCHITECTURE.md`、`ssot/API_CONTRACT.md`、`ssot/PROJECT_STATE.md`
- 规则：`rules/GRILLING_PROTOCOL.md`、`rules/DEVELOPMENT_PROCESS.md`、`rules/UPGRADE_RULES.md`
- 追溯：`decisions/INDEX.md`、`imports/SOURCE_INDEX.md`
