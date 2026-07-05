# 硬件项目模板使用说明

## 1. 仓库定位

本仓库可以作为低压嵌入式硬件项目工作区模板，用于管理硬件项目的需求、资料、器件选型、原理图、PCB、打样、调试、测试和改版记录。

## 2. 适用项目类型

适用于：

- MCU 控制板
- STM32 实战板
- 传感器采集板
- 电源管理板
- 单节锂电池供电项目
- 模拟前端板
- ADC / DAC 扩展板
- MOSFET 驱动板
- 通信接口扩展板
- 低压嵌入式硬件项目

## 3. 不直接覆盖的项目类型

以下项目不建议直接套用本模板，需要新增专项规则、专项 Skill 和专项 checklist：

- 高压电源
- 市电 AC-DC
- 射频
- 高速数字
- DDR
- 大电流功率板
- 医疗电子
- 汽车电子
- 强安规认证项目

## 4. 新增项目步骤

1. 从 `templates/hardware_project_template/` 复制项目模板。
2. 放入 `projects/XX_Project_Name/`。
3. 修改项目 `README.md`。
4. 填写 `requirements.md`。
5. 整理 `block_diagram.md`。
6. 收集官方资料并更新 `references.md`。
7. 使用 `skills/hardware-datasheet-reading/SKILL.md` 提取关键资料。
8. 使用 `skills/hardware-component-selection/SKILL.md` 进行器件选型。
9. 将选型依据写入 `design_notes.md`。
10. 绘制原理图。
11. 使用 `skills/hardware-schematic-review/SKILL.md` 审查原理图。
12. 将审查结果写入 `docs/schematic_review.md`。
13. 后续进入 PCB、打样、调试和测试阶段时，继续按照 `docs/08_Project_Workflow.md` 执行。

## 5. 新项目命名建议

建议使用：

```text
projects/04_Project_Name/
projects/05_Project_Name/
```

项目名建议包含功能关键词，例如：

```text
04_RS485_Sensor_Node
05_STM32_Motor_Driver_Board
06_Battery_Powered_Data_Logger
```

## 6. AI 协作建议

新增项目的具体上下文读取范围以 `docs/AI_Context_Guide.md` 中“新增项目”任务类型为准。

新增项目时，应让 AI 先读取：

1. `PROJECT_RULES.md`
2. `AGENTS.md`
3. `docs/08_Project_Workflow.md`
4. `docs/Project_Template_Guide.md`
5. `templates/hardware_project_template/`

然后再根据具体项目需求初始化项目目录。
