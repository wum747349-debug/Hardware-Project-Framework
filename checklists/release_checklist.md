# Project Stage Deliverable Checklist

本表只检查当前 Stage 交付覆盖；生命周期与转换条件见 [Workflow](../docs/08_Project_Workflow.md)，适用 Core 与项目专属范围按 [AI Context Guide](../docs/AI_Context_Guide.md) 选择。

- [ ] 根 `README.md` 的当前阶段与交付范围真实。
- [ ] 本次 Stage 的 Project Facts 与 Stage-enabled 文档已更新。
- [ ] 未启用的 Conditional / Stage-enabled 内容没有被当作缺失项。
- [ ] 所有已声明结论都有当前 Project 的可追溯证据。
- [ ] AI/Codex 未声称自行运行 EDA、ERC、DRC、制造输出或实测。
- [ ] 只有本阶段实际产生的输出被列为交付物。
- [ ] Framework binding 未被无意改为 `main` 或其他漂移版本。
- [ ] Project Validator 与当前 Stage 对应的 checklist 已运行。
- [ ] Git diff 只包含本次交付文件，commit 信息清楚。

制造放行使用 [PCB Release Checklist](pcb_release_checklist.md)；Bootstrap / Stage 1 使用 [Initialization Checklist](project_initialization_checklist.md)。本 checklist 不要求所有项目预建或更新 firmware、EDA、BOM、Gerber、Bring-up、Test 或 Revision 文件。
