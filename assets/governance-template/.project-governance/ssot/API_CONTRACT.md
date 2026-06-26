# API Contract

跨组件的接口契约 SSOT，是契约消费方（前端 / Mock / 测试 / 集成方）与契约提供方（后端 / SDK / CLI / 服务端）的共同标准。任何接口变化都必须更新本文件并留痕。

不涉及对外接口的项目（如纯文档站、单体桌面工具）可将 `Status` 设为 `n/a` 并在 `Content` 区写一句"本项目无外部接口"，仍需保留文件以满足校验。

- Status: draft   （允许值：`draft` / `confirmed` / `superseded` / `n/a`）

## Change History

`Version` 列填项目版本号（如 `v1.0`、`v1.1`），与 `ssot/PROJECT_STATE.md` 的 `Versions` 段对应。

| Date | Version | Change | Reason | Decision |
|---|---|---|---|---|

## Content

- Base URL:
- Auth:
- Error format:
- Pagination:
- Endpoints:
- Mock data rules:
