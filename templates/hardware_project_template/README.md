# Hardware Project Template

本目录是硬件项目模板。新增项目时，可复制本目录到 `projects/XX_Project_Name/`。

## 项目目标

请在这里填写本项目要实现的功能、应用场景和第一版边界。

## 工具链

- EDA：Altium Designer
- MCU 配置：STM32CubeMX，如适用
- 固件开发：Keil MDK，如适用
- 文档：Markdown
- 版本管理：Git / GitHub

## 推荐流程

1. 填写 `requirements.md`
2. 绘制或整理 `block_diagram.md`
3. 收集资料并更新 `references.md`
4. 进行器件选型并更新 `design_notes.md`
5. 绘制原理图
6. 审查原理图并更新 `docs/schematic_review.md`
7. PCB Layout
8. PCB 审查并更新 `docs/pcb_review.md`
9. 打样、焊接、上电调试
10. 更新 `docs/bringup_log.md`
11. 完成测试并更新 `docs/test_report.md`
12. 如有改版，更新 `docs/revision_history.md`
