# docs 目录说明

> 文档状态：当前有效
> 适用阶段：阶段 1 至阶段 8
> 适用对象：STM32 DAQ Control Board Rev A 的阶段文档与导航
> 最后核对依据：当前 docs 目录结构

本目录保存 `01_STM32_DAQ_Control_Board` 的阶段文档、模块设计依据和后续审查/调试记录。

| 路径                            | 用途                                                                                     |
| ----------------------------- | -------------------------------------------------------------------------------------- |
| `module_design/`              | 当前有效的模块详细设计依据，承接 `design_notes.md` 中不展开的计算、连接和风险细节                                     |
| `user/`                       | 面向展示和使用者的稳定项目说明                                                                         |
| `schematic_review.md`         | 原理图系统审查记录，维护已关闭问题和与 PCB 审查关联的实现依据                                                        |
| `component_selection_plan.md` | 历史选型记录，保留第一轮关键器件候选、比较、替代关系、资料来源和风险边界                                                  |
| `pcb_design_rules.md`         | 当前有效的 PCB 制造基线和 Altium Designer 人工配置规则；尚未在实际 `.PcbDoc` 中配置和验证，不代表 PCB Review 或 DRC 已完成 |
| `pcb_review.md`               | 阶段 5 至阶段 7 的 PCB 审查问题、关闭依据和制造门禁主记录                                                          |
| `bringup_log.md`              | 尚未开始的焊接和上电调试记录                                                                         |
| `test_report.md`              | 尚未开始的测试报告                                                                              |
| `revision_history.md`         | 当前有效的问题追踪和改版记录入口                                                                       |

当前项目阶段以项目根 [README.md](../README.md) 的状态头为准。当前不代表 PCB、DRC 或制造输出已经通过；剩余门禁以 [pcb_review.md](pcb_review.md) 为准。阶段 7 完成并确认制造、装配准备就绪后，才进入阶段 8：焊接和硬件调试阶段。

## 文档职责分工

- 需求和验收边界维护在 [../requirements.md](../requirements.md)。
- 当前整板设计意图、主选方案摘要、Pin Map 和接口定义维护在 [../design_notes.md](../design_notes.md)。
- 实际电气实现以当前 Altium 原理图、对应审查版 PDF 和必要时导出的网表为准；若与文档不一致，应记录到 [schematic_review.md](schematic_review.md)。
- 模块级参数、计算、连接依据和 PCB 检查项维护在 [module_design/](module_design/)。
- datasheet 路径、阅读状态和来源备注维护在 [../references.md](../references.md)。
- 历史选型过程维护在 [component_selection_plan.md](component_selection_plan.md)，不作为最终 BOM。
- 原理图问题、风险等级、修改建议和关闭状态维护在 [schematic_review.md](schematic_review.md)。
- PCB 制造基线、规则值、Scope、优先级和 DRC 应检查项维护在 [pcb_design_rules.md](pcb_design_rules.md)。
- 阶段 5 至阶段 7 的 PCB 问题、关闭依据、风险统计和制造门禁维护在 [pcb_review.md](pcb_review.md)。
