# Active Process

本文件记录**当前项目当前版本商定的开发流程**。在骨架第二段（技术栈确认）由 agent 与用户共同填写。本文件只服务于实际开发段；启动新版本时按需重新填写或继承。

字段定义、改动规则与可裁剪边界见 `rules/DEVELOPMENT_PROCESS.md`，沉淀规则见 `rules/VERSION_RULES.md`。

> **Task Plan 红线**：本流程中任何 `acceptance_required: true` 的阶段在编码前必须先产出 `processes/tasks/<stage_id>.md` 颗粒级 task plan 并经用户明确确认。模板见 `templates/RECORD_TEMPLATES.md` 的 `Task Plan` 段，规则见 `rules/DEVELOPMENT_PROCESS.md` 的 "Task Plan 前置" 段。

## Metadata

- Name: TBD（建议格式 `<product-type>-<variant>-vN`）
- Applicable To: TBD
- Source: TBD（`library:<name>` 或 `drafted-in-project`）
- Applied To Version: TBD
- Confirmed At: TBD

## Stages

按 `rules/DEVELOPMENT_PROCESS.md` 的字段顺序逐条填写：

### Example Stage（占位，请删除并替换为真实阶段）

- id: example_stage
- name_zh: 示例阶段
- goal: 描述这一步要达成的目标
- done_when: 描述可验证的完成条件
- acceptance_required: false
- optional: false
- typical_pitfalls:
  - 列出这一步容易踩的坑

## Lessons Learned

沉淀时由用户口述、agent 整理。当前版本走完一轮前可留空。

## Mutation Log

记录本流程在当前版本内的改动历史。改动规则见 `rules/DEVELOPMENT_PROCESS.md`。

| Date | Change Type | Detail | Reason | User Confirmed |
|---|---|---|---|---|
