# docs 目录说明

本目录保存 `01_STM32_DAQ_Control_Board` 的阶段文档、模块设计依据和后续审查/调试记录。

| 路径 | 用途 |
|---|---|
| `module_design/` | 模块详细设计依据，用于承接 `design_notes.md` 中迁出的模块细节 |
| `user/` | 面向展示、学习复盘和项目说明的文档 |
| `schematic_review.md` | 原理图系统审查记录，当前为待审查模板 |
| `component_selection_plan.md` | 第一轮关键器件选型历史依据、搜索关键词、筛选维度和候选记录模板 |
| `pcb_review.md` | 后续 PCB 审查记录 |
| `bringup_log.md` | 后续焊接和上电调试记录 |
| `test_report.md` | 后续测试报告 |
| `revision_history.md` | 后续问题追踪和改版记录 |

当前项目阶段：模块原理图设计说明和设计文档已完成，AD 原理图中补充的 I2C、SPI、UART2、公用电源 + GPIO、用户 LED 和用户按键连接规划已同步到文档；下一步进入原理图系统审查 / PCB Layout 前检查。当前不代表原理图已审查通过，也不代表可以直接 PCB Layout 或打样。
