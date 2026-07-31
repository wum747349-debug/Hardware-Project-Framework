# 硬件项目模板使用指南

> 文档状态：当前有效
> 适用阶段：新项目初始化、模板维护与旧项目迁移
> 适用对象：新项目初始化、模板维护与旧项目迁移
> 最后核对依据：项目结构标准、八阶段流程和当前硬件项目模板

## 1. 模板适用范围

`templates/hardware_project_template/` 默认适用于：

- 低压嵌入式硬件；
- MCU 控制板；
- 传感器采集板；
- 电源管理板；
- 模拟前端；
- 通信接口扩展板。

模板提供必要目录、状态头、事实源入口、阶段文档和父目录说明；按需输出与图片子目录在实际产生内容时创建。模板不提供任何项目的器件、网络、板框、线宽、孔径或板厂下单默认值。

## 2. 不直接适用的复杂项目

以下项目可复用基础目录，但不能仅凭本模板完成设计和放行：

- 高压；
- 射频；
- 高速数字与复杂受控阻抗；
- 隔离电源；
- 汽车电子；
- 医疗电子；
- 安规认证；
- HDI、刚挠结合或其他特殊制造工艺。

这些项目必须增加专项 Skill、checklist、标准依据和具备相应能力的审查。

## 3. 权威文档

- 项目目录、文件职责、命名和迁移：`docs/Project_Structure_Standard.md`
- 八阶段顺序、阶段门和职责：`docs/08_Project_Workflow.md`
- AI 最小读取范围：`docs/AI_Context_Guide.md`
- 仓库稳定原则：`PROJECT_RULES.md`
- PCB 执行方法：`skills/hardware-pcb-layout-review/SKILL.md`
- PCB Layout 前置清单：`checklists/pcb_layout_preflight_checklist.md`
- PCB 制造放行清单：`checklists/pcb_release_checklist.md`

本指南只说明模板操作，不复制上述规则正文。

## 4. 从模板创建项目

1. 确认项目适用范围；复杂项目先补专项方法和检查项。
2. 在 `projects/` 下确定下一个稳定编号。
3. 将 `templates/hardware_project_template/` 复制为 `projects/XX_Project_Name/`。
4. 将项目根 `README.md` 标题、当前项目阶段和当前硬件版本占位符替换为项目实际信息。
5. 填写 `requirements.md` 的目标、第一版边界、验收边界和待确认制造基线。
6. 更新 `block_diagram.md`、`design_notes.md` 和 `references.md` 的初始内容。
7. 在 `docs/README.md` 标记各阶段文件为“未启用”“草稿”“当前有效”或“历史归档”，不在其中重复维护当前项目阶段。
8. 检查模板内链接、占位符和项目目录命名。
9. 只提交本次新项目文件，不把缓存、日志、二进制临时文件或其他项目改动混入提交。

复制模板只完成项目初始化，不表示需求、选型、原理图、PCB、DRC 或制造已经完成。

## 5. 项目命名

项目目录使用：

```text
XX_Project_Name
```

- `XX`：两位稳定顺序号；
- `Project_Name`：英文单词和下划线组成的功能名称；
- 不用临时器件型号绑定目录名；
- 公开引用后不因优先级变化重排编号。

示例只说明格式：

```text
04_Sensor_Interface_Board
```

## 6. 八阶段工作方式

| 阶段 | 主阶段 | 主要启用文件 |
|---|---|---|
| 1 | 需求确认阶段 | `requirements.md`、`block_diagram.md`、`design_notes.md` |
| 2 | 关键器件选型阶段 | `docs/component_selection_plan.md`、`references.md` |
| 3 | 原理图模块设计和绘制阶段 | `docs/module_design/*.md`、BOM 草稿、原理图输出 |
| 4 | 原理图审查阶段 | `docs/schematic_review.md` |
| 5 | PCB 布局阶段 | `docs/pcb_design_rules.md`、Layout Preflight |
| 6 | 布线和铺铜阶段 | 当前 PCB 实现证据、中间 DRC 记录 |
| 7 | PCB 审查阶段 | `docs/pcb_review.md`、Batch DRC、制造输出 |
| 8 | 焊接和硬件调试阶段 | `docs/bringup_log.md`、`docs/test_report.md`、`docs/revision_history.md` |

完整进入、退出和回退条件以八阶段流程为准。

## 7. 必需、阶段性和可选内容

### 创建时必需

- 项目根五个事实入口：`README.md`、`requirements.md`、`block_diagram.md`、`design_notes.md`、`references.md`；
- `docs/README.md`；
- `hardware/README.md`；
- `firmware/README.md`；
- 标准目录说明文件。

这些文件可以是草稿，但不得虚构事实。

### 阶段性文件

进入相应阶段时启用：

- `docs/component_selection_plan.md`
- `docs/module_design/*.md`
- `docs/schematic_review.md`
- `docs/pcb_design_rules.md`
- `docs/pcb_review.md`
- `docs/bringup_log.md`
- `docs/test_report.md`
- `docs/revision_history.md`

文件可以提前存在；只有状态头、内容和阶段门满足时才表示已启用或完成。

### 按需目录

- `docs/user/`
- `hardware/outputs/schematic_pdf/`
- `hardware/outputs/bom/`
- `hardware/outputs/netlist/`
- `hardware/outputs/erc/`
- `hardware/outputs/component_reports/`
- `hardware/outputs/footprint_reports/`
- `hardware/outputs/gerber/`
- `hardware/outputs/drill/`
- `hardware/outputs/pick_place/`
- `hardware/outputs/fabrication_package/`
- `hardware/images/pcb/`
- `hardware/images/assembly/`
- `hardware/images/bringup/`
- `hardware/images/test/`
- 按模块创建的 `references/datasheets/<module>/`

这些标准路径不在模板中全部预建；进入相应阶段并实际产生内容时再创建。目录存在不表示输出已经生成，父目录 `README.md` 统一说明用途和启用时机。

## 8. 文档状态头

项目根 `README.md` 是当前项目阶段的唯一主事实源，建议使用：

```text
> 文档状态：<草稿 / 当前有效 / 历史归档>
> 当前项目阶段：<八阶段名称>
> 当前硬件版本：<版本>
> 最后核对依据：<文件、证据或待填写>
```

其他项目文档使用：

```text
> 文档状态：<草稿 / 待核对 / 当前有效 / 历史归档>
> 适用阶段：<一个或多个八阶段名称>
> 适用对象：<项目名称与硬件版本>
> 最后核对依据：<文件、资料、证据或待填写>
```

使用规则：

- 初始化时使用“草稿”，不要直接标记“当前有效”；
- 关键依据不足时使用“待核对”；
- 只有在所列依据与适用版本范围内有效时使用“当前有效”；
- 历史记录保留为“历史归档”，不要伪装成当前事实；
- `docs/README.md` 只维护职责、启用时机和导航，不重复项目根 README 的当前阶段；
- 审查、测试或调试日期写在正文，不维护统一的“最近更新”字段；
- 状态头不能替代 EDA、DRC、制造或实测证据。

## 9. 什么时候创建或启用阶段文档

- 在关键器件需要正式比较时启用选型计划。
- 在模块进入连接、计算和专项布局设计时创建对应模块文档。
- 在首次正式原理图审查时启用原理图审查记录。
- 在 PCB Layout Preflight 前必须完成项目 PCB 规则文档。
- 在首次布局/布线审查时启用 PCB 审查记录。
- 在准备焊接和首次上电时启用 bringup 记录。
- 在开始正式测试时启用测试报告。
- 在确定首个硬件版本或出现重要变更时启用改版记录。

不要为了目录整齐而一次性填写所有阶段结果。

## 10. 填写 PCB 规则模板

1. 从 `requirements.md` 读取目标板厂和基础 PCB 规格摘要。
2. 使用目标板厂当前官方能力核对相关制造边界与日期。
3. 区分制造能力、项目设计默认值和制造极限。
4. 根据项目需求定义网络分类、Net Class 或明确网络 Scope。
5. 填写 Clearance、Width、Via、Hole、Annular Ring、Mask、Silkscreen、Board Outline 和 Polygon 等适用类别。
6. 只在项目确实需要时增加差分、阻抗、长度、高速、模拟或大电流专项规则。
7. 明确每条规则的 Scope、Priority 和默认/专项覆盖关系。
8. 由用户在 Altium Designer 中实际配置规则，并分别确认配置、Scope 和 Priority 状态。
9. Layout 前运行初始 DRC；制造放行前运行完整 Batch DRC。
10. 将实际问题、DRC 结果和制造门禁写入 `docs/pcb_review.md`，不要写回规则定义。

## 11. 项目事实与通用模板

- 模板描述“需要填写什么”，不保存任何项目答案。
- `requirements.md` 保存本项目需求和基础制造摘要。
- `design_notes.md` 保存本项目整板设计意图、Pin Map 和接口。
- 模块文档保存本项目连接、计算和专项布局要求。
- `docs/pcb_design_rules.md` 保存本项目具体规则值。
- 审查记录保存实际问题、证据、状态和结论。

不得把另一个项目的参数复制到模板后再作为新项目默认值。

## 12. 项目 1 参考边界

项目 1 可用于理解文档分层、规则与审查分工、证据记录和输出目录组织，但不是可原样复制的模板。

新项目必须基于自己的需求、目标板厂官方能力、关键器件资料、封装、装配方式和实际 EDA 实现重新设计。不得继承项目 1 的器件、网络名、规则值、板框、制造参数、问题编号、DRC 结果或放行结论。

## 13. 初始化验收清单

- [ ] 项目目录名称符合 `XX_Project_Name`。
- [ ] 创建时必需文件与目录齐全。
- [ ] 核心项目文档包含统一状态头。
- [ ] 根 README 的导航链接有效。
- [ ] 第一版目标、不做内容和验收边界已记录。
- [ ] PCB 制造基线字段均已填写占位或确认值。
- [ ] 阶段文件未被误标记为已完成。
- [ ] 空输出目录未被描述为已有输出。
- [ ] 模板占位符未被虚构值替换。
- [ ] 不包含其他项目的器件、网络、尺寸、规则或审查状态。
- [ ] `git diff --check` 和 Markdown 链接检查通过。

## 14. 旧项目迁移

- 先按项目结构标准确定现有事实源，不机械重写全部文件。
- 优先补项目入口、状态头、`docs/README.md` 和 `hardware/README.md`。
- 只在进入相关阶段时补齐阶段文档和输出目录。
- 旧阶段编号可保留为历史，后续更新逐步映射到八阶段。
- 不为满足模板外观移动或改写 Altium 二进制源文件。
- 文件重命名或移动前检查链接和历史引用。

## 15. AI 最小上下文

新增项目或模板维护时读取：

- `PROJECT_RULES.md`
- `AGENTS.md`
- `docs/AI_Context_Guide.md`
- `docs/Project_Structure_Standard.md`
- 本指南
- `templates/hardware_project_template/`

只有需要判断阶段门时读取完整八阶段流程；不默认加载其他项目、全部 Skill、全部 datasheet 或项目 1。
