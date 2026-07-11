# docs 目录说明

> 文档状态：当前有效
> 当前阶段：整板原理图系统审查
> 适用对象：STM32 DAQ Control Board Rev A
> 最后核对依据：当前 docs 目录结构

本目录保存 `01_STM32_DAQ_Control_Board` 的阶段文档、模块设计依据和后续审查/调试记录。

| 路径 | 用途 |
|---|---|
| `module_design/` | 当前有效的模块详细设计依据，承接 `design_notes.md` 中不展开的计算、连接和风险细节 |
| `user/` | 面向展示、学习复盘和项目说明的文档 |
| `schematic_review.md` | 当前进行中的原理图系统审查记录，重点维护问题清单和关闭状态 |
| `component_selection_plan.md` | 历史选型记录，保留第一轮关键器件搜索关键词、筛选维度和候选记录模板 |
| `pcb_review.md` | 尚未开始的 PCB 审查记录 |
| `bringup_log.md` | 尚未开始的焊接和上电调试记录 |
| `test_report.md` | 尚未开始的测试报告 |
| `revision_history.md` | 当前有效的问题追踪和改版记录入口 |

当前项目阶段：模块原理图设计说明和设计文档已完成，AD 原理图中补充的 I2C、SPI、UART2、公用电源 + GPIO、用户 LED 和用户按键连接规划已同步到文档；下一步进入原理图系统审查 / PCB Layout 前检查。当前不代表原理图已审查通过，也不代表可以直接 PCB Layout 或打样。

## 文档职责分工

- 需求和验收边界维护在 [../requirements.md](../requirements.md)。
- 当前整板实现摘要、Pin Map 和接口定义维护在 [../design_notes.md](../design_notes.md)。
- 模块级参数、计算、连接依据和 PCB 检查项维护在 [module_design/](module_design/)。
- datasheet 路径、阅读状态和来源备注维护在 [../references.md](../references.md)。
- 历史选型过程维护在 [component_selection_plan.md](component_selection_plan.md)，不作为最终 BOM。
- 原理图问题、风险等级、修改建议和关闭状态维护在 [schematic_review.md](schematic_review.md)。
