# 硬件项目结构标准

> 文档状态：当前有效
> 适用阶段：全部八阶段
> 适用对象：本仓库硬件项目与项目模板
> 最后核对依据：`PROJECT_RULES.md`、`docs/08_Project_Workflow.md`、当前项目模板与项目 1 文档结构

## 1. 文档定位

本文规定本仓库硬件项目的目录结构、文件职责、事实源、状态、命名、版本、初始化验收和旧项目迁移方式。

规则层级如下：

```text
PROJECT_RULES.md
    ↓
docs/Project_Structure_Standard.md
    ↓
docs/08_Project_Workflow.md
    ↓
skills/*/SKILL.md
    ↓
checklists/*.md
    ↓
项目级事实文件
    ↓
审查、DRC、调试和测试证据
```

`PROJECT_RULES.md` 保存所有项目共同遵守的稳定原则；本文回答“项目文件放在哪里、每个文件负责什么”；工作流程回答“何时创建或更新这些文件”；Skill 回答“如何执行某类任务”；checklist 回答“逐项检查什么”；项目文件和证据保存本项目的实际事实与结果。

## 2. 适用范围

本标准默认适用于：

- 低压嵌入式硬件；
- MCU 控制板；
- 传感器采集板；
- 电源管理板；
- 模拟前端；
- 通信接口扩展板。

高压、射频、高速数字、隔离电源、汽车电子、医疗电子或涉及安规认证的项目仍使用本标准管理基础文件，但必须增加专项 Skill、checklist、证据和合规要求，不能仅凭通用模板完成设计或放行。

## 3. 标准项目目录

```text
projects/XX_Project_Name/
├─ README.md
├─ requirements.md
├─ block_diagram.md
├─ design_notes.md
├─ references.md
├─ docs/
│  ├─ README.md
│  ├─ component_selection_plan.md
│  ├─ module_design/
│  ├─ schematic_review.md
│  ├─ pcb_design_rules.md
│  ├─ pcb_review.md
│  ├─ bringup_log.md
│  ├─ test_report.md
│  ├─ revision_history.md
│  └─ user/
├─ hardware/
│  ├─ README.md
│  ├─ altium_project/
│  ├─ outputs/
│  └─ images/
├─ firmware/
│  └─ README.md
└─ references/
   ├─ datasheets/
   └─ lcsc_parts/
```

目录树表示标准路径，不表示模板会预建全部子目录，也不表示空输出目录已经产生对应输出。

## 4. 文件启用级别

### 4.1 创建项目时必须存在

新项目初始化时必须创建：

- `README.md`；
- `requirements.md`；
- `block_diagram.md`；
- `design_notes.md`；
- `references.md`；
- `docs/README.md`；
- `hardware/README.md`；
- `firmware/README.md`；
- `docs/module_design/`；
- `hardware/altium_project/`；
- `hardware/outputs/`；
- `hardware/images/`；
- `references/datasheets/`；
- `references/lcsc_parts/`。

模板只预建上述入口文件和父目录说明。`hardware/outputs/`、`hardware/images/` 等父目录通过各自 `README.md` 说明按需子目录，不预建尚未产生内容的输出或图片分类目录。

这些文件可以处于“草稿”或“待确认”状态，但必须说明用途、当前事实边界和待补信息。不得为了满足初始化格式而虚构器件、参数、规则或验证结果。

### 4.2 进入阶段时启用

阶段文件在首次进入相关工作时创建或从模板启用：

| 文件 | 首次启用时机 |
|---|---|
| `docs/component_selection_plan.md` | 开始关键器件候选与选型记录时 |
| `docs/module_design/*.md` | 某模块进入详细电路设计、参数反推或专项布局要求整理时 |
| `docs/schematic_review.md` | 开始正式原理图审查时 |
| `docs/pcb_design_rules.md` | PCB Layout Preflight 前，形成项目级 PCB 规则基线时 |
| `docs/pcb_review.md` | 开始 PCB 布局、布线或制造放行审查记录时 |
| `docs/bringup_log.md` | 准备焊接检查或首次上电时 |
| `docs/test_report.md` | 开始正式功能、性能或边界测试时 |
| `docs/revision_history.md` | 确立首个硬件版本或发生重要设计变更时 |

阶段文件可以提前以空模板存在，但不得把“文件存在”解释为该阶段已完成。

### 4.3 按需启用

以下内容仅在项目实际需要时创建：

- `docs/user/`：面向使用者的接口说明、快速开始、接线说明和安全提示；
- `hardware/outputs/schematic_pdf/`：用户实际导出可追溯原理图 PDF 时；
- `hardware/outputs/bom/`：用户实际导出 BOM 时；
- `hardware/outputs/netlist/`：需要网表核对或归档时；
- `hardware/outputs/erc/`：用户实际导出 ERC、Messages 或相关证据时；
- `hardware/outputs/component_reports/`：需要补充元件属性证据时；
- `hardware/outputs/footprint_reports/`：需要核对引脚、焊盘或封装映射时；
- `hardware/outputs/gerber/`：进入制造输出且用户实际导出 Gerber 时；
- `hardware/outputs/drill/`：用户实际导出 PTH/NPTH 钻孔文件时；
- `hardware/outputs/pick_place/`：需要 SMT 装配且用户实际导出坐标时；
- `hardware/outputs/fabrication_package/`：制造放行后整理同版制造归档包时；
- `hardware/images/pcb/`：需要视觉审查、机械沟通或项目展示时；
- `hardware/images/assembly/`：需要记录装配过程或结果时；
- `hardware/images/bringup/`：需要记录上电调试现象时；
- `hardware/images/test/`：需要记录测试环境、波形或结果时；
- `references/datasheets/<module>/`：当前决策需要读取相应模块资料时；
- `references/lcsc_parts/`：使用立创商城进行候选搜索和采购记录时。

按需目录默认不存在，在进入相应阶段并实际产生内容时创建。低信息量子目录不单独放置 README；说明统一维护在父目录 `README.md`。只有子目录确有独立使用规则时才增加说明文件。

## 5. 文件唯一职责

| 文件或目录 | 唯一职责 |
|---|---|
| `README.md` | 项目入口：说明目标、范围、当前阶段、硬件版本、关键导航和下一步，不维护详细规则或审查问题 |
| `requirements.md` | 保存需求、功能边界、验收边界和基础制造规格摘要 |
| `block_diagram.md` | 保存系统模块、能量流、信号流和模块边界 |
| `design_notes.md` | 保存整板当前设计意图、主选方案、Pin Map、接口定义和跨模块约定 |
| `references.md` | 保存资料索引、来源、用途、阅读状态和待核对项 |
| `docs/README.md` | 说明项目 `docs/` 内文件状态、职责和导航 |
| `docs/component_selection_plan.md` | 保存关键器件候选、筛选依据、主选与备选决策过程 |
| `docs/module_design/*.md` | 保存单个模块的连接、计算、器件依据、风险和专项布局要求 |
| `docs/schematic_review.md` | 保存实际原理图问题、证据、状态和进入 PCB Layout 的结论 |
| `docs/pcb_design_rules.md` | 保存本项目具体 PCB 规则值、Scope、Priority、DRC 类别、配置状态和规则豁免 |
| `docs/pcb_review.md` | 保存实际 PCB 问题、证据、关闭状态、DRC 结果引用和制造门禁结论 |
| `docs/bringup_log.md` | 保存焊接检查、首次上电、测量数据、现象和调试过程 |
| `docs/test_report.md` | 保存测试条件、预期、实测结果、偏差和验收结论 |
| `docs/revision_history.md` | 保存硬件版本、重要改版原因、影响范围和复验要求 |
| `docs/user/` | 保存面向使用者的操作、接线、接口和安全说明 |
| `hardware/README.md` | 说明硬件源文件、实现证据、输出目录、命名和能力边界 |
| `hardware/altium_project/` | 保存 Altium 权威工程源文件；`.SchDoc` 和 `.PcbDoc` 分别是原理图和 PCB 的权威实现源 |
| `hardware/outputs/` | 保存 EDA 和制造输出，不保存设计意图或通用规则 |
| `hardware/images/` | 保存审查、装配、调试和展示所需图片 |
| `firmware/` | 保存固件源码、配置、构建和烧录说明 |
| `references/datasheets/` | 保存官方 datasheet、reference manual、application note 及其模块分类 |
| `references/lcsc_parts/` | 保存供应商搜索记录、候选入口和采购辅助信息，不作为关键参数唯一依据 |

## 6. 事实源与禁止重复维护

### 6.1 事实源规则

同一事实只指定一个主维护位置，其他文件仅保留摘要并链接主事实源：

| 事实 | 主事实源 | 允许的摘要位置 |
|---|---|---|
| 当前项目阶段 | 项目根 `README.md` | 其他文档不重复维护，只声明自身适用阶段 |
| 功能边界与验收要求 | `requirements.md` | 项目 `README.md` |
| 基础制造规格 | `requirements.md` | `docs/pcb_design_rules.md` 引用或展开规则依据 |
| 整板设计意图、Pin Map、接口定义 | `design_notes.md` | 模块文档和用户说明按需引用 |
| 模块连接、计算和专项布局要求 | `docs/module_design/*.md` | `design_notes.md` 仅保留整板级摘要 |
| 资料来源和阅读状态 | `references.md` | 设计文档引用具体条目 |
| PCB 具体规则、Scope、Priority | `docs/pcb_design_rules.md` | `requirements.md` 只保留制造基线摘要 |
| 原理图审查状态 | `docs/schematic_review.md` | 项目 `README.md` 只保留当前阶段摘要 |
| PCB 问题、DRC 证据和制造门禁 | `docs/pcb_review.md` | 项目 `README.md` 只保留结论摘要 |
| 调试过程与测量原始记录 | `docs/bringup_log.md` | `docs/test_report.md` 引用相关记录 |
| 正式测试结论 | `docs/test_report.md` | 项目 `README.md` 只保留结论摘要 |
| 硬件版本和改版原因 | `docs/revision_history.md` | 各文档状态头填写适用版本 |
| EDA 实际实现 | `.SchDoc` / `.PcbDoc` | PDF、BOM、图片和报告作为可追溯实现证据 |

### 6.2 禁止重复维护

- 不在 `requirements.md` 和 `docs/pcb_design_rules.md` 各自维护两套具体 PCB 规则；前者保存制造基线摘要，后者保存可执行规则。
- 不在规则文档记录实际问题是否已关闭；实际状态写入相应审查记录。
- 不在 checklist 写入某项目当前是否通过；项目状态写入项目审查记录。
- 不在 Skill、checklist、模板或仓库级规则写入单个项目的器件、网络名、板框、规则值或板厂下单参数。
- 不把审查记录中的 DRC 摘要反向当作已配置规则的权威定义。
- 不把图片、PDF 或文字设计意图当作 `.SchDoc` / `.PcbDoc` 内部实现已经同步的证明。

规则文件描述“应该是什么”，审查记录描述“实际是否做到”。

## 7. 标准文档状态头

项目根 `README.md` 是当前项目阶段的唯一主事实源，建议使用：

```text
> 文档状态：<草稿 / 当前有效 / 历史归档>
> 当前项目阶段：<八阶段名称>
> 当前硬件版本：<版本>
> 最后核对依据：<文件、证据或待填写>
```

其他项目 Markdown 文档默认使用：

```text
> 文档状态：<草稿 / 待核对 / 当前有效 / 历史归档>
> 适用阶段：<一个或多个八阶段名称>
> 适用对象：<项目名称与硬件版本>
> 最后核对依据：<文件、资料、证据或待填写>
```

`docs/README.md` 只维护文件职责、启用时机和文档导航，可以使用“未启用”“草稿”“当前有效”“历史归档”等简化状态，但不得维护另一套当前项目阶段。

审查、测试和调试记录如需日期，在正文中使用“审查日期”“测试日期”或“记录日期”，不在所有文件中统一维护“最近更新”。状态含义：

- `草稿`：结构已建立，内容尚未完成；
- `待核对`：已有内容，但关键依据或实现证据不足；
- `当前有效`：在所列依据和适用版本范围内有效；
- `历史归档`：仅用于追溯，不再代表当前设计。

状态头不能替代证据，也不能凭模板自动填写为“当前有效”。旧项目的历史状态头可以保留，后续迁移时再逐步调整，不为统一外观机械重写。

## 8. 命名规范

### 8.1 Markdown 文件

- 固定职责文件使用本标准规定的英文小写蛇形命名，例如 `design_notes.md`、`pcb_review.md`。
- 不在文件名中使用空格、临时编号、日期或“最终版”等含义不稳定的词。
- 同一职责不创建 `pcb_review_new.md`、`pcb_review_final.md` 等并行文件；历史通过 Git 和版本字段追溯。
- 用户交付文档可在 `docs/user/` 内使用清晰的英文小写蛇形名称。

### 8.2 项目目录

项目目录使用：

```text
XX_Project_Name
```

- `XX` 为两位顺序号；
- `Project_Name` 使用有意义的英文单词和下划线；
- 名称表达功能定位，不绑定临时器件料号；
- 目录编号一旦公开引用，不因优先级变化而重排。

示例仅表示格式：

```text
04_Sensor_Interface_Board
```

### 8.3 模块文档

模块文档位于 `docs/module_design/`，推荐：

```text
NN_<module_name>.md
```

- `NN` 只用于稳定阅读顺序；
- `<module_name>` 使用英文小写蛇形名称；
- 一个文件负责一个清晰模块或跨模块专项；
- 模块拆分变化时优先更新索引和链接，不机械重编号历史文件。

### 8.4 硬件版本

- 正式硬件版本使用 `Rev A`、`Rev B`、`Rev C`。
- 设计尚未形成首个可制造版本时可使用 `Draft 01`、`Draft 02`。
- 同一次硬件改版必须在 `docs/revision_history.md` 记录原因、影响范围和需要回退复验的阶段。
- 固件版本、文档状态和硬件版本分别管理，不相互替代。

### 8.5 输出文件版本

正式输出推荐：

```text
<Project>_<OutputType>_<HardwareRevision>_<YYYYMMDD>.<ext>
```

同一制造批次的 Gerber、钻孔、坐标、BOM、装配图和制造说明必须能追溯到同一 `.PcbDoc` 与硬件版本。草稿输出可增加 `DraftNN`，但不得使用 `final`、`latest` 等无法长期追溯的词。

## 9. 输出目录职责

`hardware/outputs/` 只保存由 EDA 或制造准备过程产生的文件：

| 目录 | 内容 |
|---|---|
| `schematic_pdf/` | 可追溯到当前 `.SchDoc` 的完整原理图 PDF |
| `bom/` | 当前版本 BOM 与制造/装配所需物料输出 |
| `netlist/` | 条件触发的网表输出 |
| `erc/` | 用户实际导出的 ERC、Messages 或相关证据 |
| `component_reports/` | 条件触发的元件属性报告 |
| `footprint_reports/` | 条件触发的封装、引脚或焊盘映射报告 |
| `gerber/` | Gerber 层文件 |
| `drill/` | PTH、NPTH 与相关钻孔输出 |
| `pick_place/` | SMT 贴片坐标 |
| `fabrication_package/` | 已批准制造批次的同版归档包 |

目录存在、文件已导出和制造已放行是三个不同状态。制造输出必须由用户在 EDA 中实际生成并确认，AI/Codex 只能检查用户提供的输出完整性、版本和文档一致性。

## 10. 新项目初始化验收

新项目初始化完成时逐项确认：

- [ ] 项目目录符合 `XX_Project_Name` 命名；
- [ ] 创建时必需文件和目录齐全；
- [ ] 每个必需 Markdown 文件包含统一状态头；
- [ ] `README.md` 能导航到五个项目事实入口；
- [ ] `requirements.md` 已列出第一版目标、不做内容、验收边界和待确认制造基线；
- [ ] `block_diagram.md` 已建立模块占位和主要能量流、信号流；
- [ ] `design_notes.md` 已建立整板设计意图、Pin Map 和接口定义入口；
- [ ] `references.md` 能记录来源、用途、阅读状态和本地路径；
- [ ] `docs/README.md` 区分未启用、草稿、当前有效和历史归档文件；
- [ ] `hardware/README.md` 说明源文件、实现证据和输出目录边界；
- [ ] 阶段性文件没有被误标记为已完成；
- [ ] 空输出目录没有被描述为已有输出；
- [ ] 模板占位符未被虚构值替代；
- [ ] Markdown 相对链接有效；
- [ ] 没有复制其他项目的器件、网络、板框、规则值、审查状态或制造参数。

初始化验收只证明项目框架可用，不证明需求、原理图、PCB、DRC 或制造已经完成。

## 11. 旧项目迁移

旧项目按使用频率和当前阶段渐进迁移，不为统一外观机械重写全部历史：

1. 先建立现有文件到标准职责的映射，确定每类事实的权威源。
2. 优先补齐项目入口、状态头、`docs/README.md` 和 `hardware/README.md`。
3. 将重复事实收敛到主事实源；其他文件改为摘要和链接，保留有追溯价值的历史说明。
4. 项目进入相应阶段时，再补齐阶段文件和输出目录，不要求一次创建并填写全部文件。
5. 旧项目历史阶段编号可以保留；后续更新时逐步映射到仓库八阶段模型。
6. 文件移动或重命名前先检查仓库内链接和外部引用；无明确收益时保留原路径。
7. 不移动、重写或解析 Altium 二进制源文件来满足目录外观。
8. 迁移完成后检查相对链接、职责重复、版本字段和实现证据追溯关系。

## 12. 项目 1 参考实现边界

`projects/01_STM32_DAQ_Control_Board/` 是仓库当前参考实现，用于学习：

- 项目文档如何导航；
- 整板说明与模块说明如何分层；
- 项目级 PCB 规则与 PCB 审查记录如何分工；
- 实现证据、问题状态和制造门禁如何记录；
- Altium 源文件、输出和图片如何组织。

项目 1 不是可原样复制的模板。新项目不得直接继承项目 1 的：

- 器件与位号；
- 网络名与接口定义；
- PCB 规则值与规则 Scope；
- 板框、安装孔和机械约束；
- 板厂、层叠、板厚、铜厚和下单参数；
- 审查问题、DRC 结果、规则豁免或制造结论。

复用项目 1 的方法时，必须回到新项目需求、目标板厂官方能力、关键器件 datasheet、封装、装配方式和实际 EDA 实现重新确认。

## 13. 相关文档

- [仓库通用规则](../PROJECT_RULES.md)
- [八阶段项目流程](08_Project_Workflow.md)
- [AI 上下文读取指南](AI_Context_Guide.md)
- [项目模板使用说明](Project_Template_Guide.md)
- [硬件项目模板](../templates/hardware_project_template/README.md)
- [项目 1 参考实现](../projects/01_STM32_DAQ_Control_Board/README.md)
