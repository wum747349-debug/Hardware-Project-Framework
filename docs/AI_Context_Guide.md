# AI 上下文读取指南

## 1. 文件定位

本文用于规定 AI 在协助本仓库时的最小必要上下文读取规则，避免随着项目数量、Skill 数量和历史记录增加而出现上下文膨胀。

AI 默认只读取“仓库基础规则 + 当前项目文件 + 当前阶段 Skill”，不默认读取所有项目、所有 Skill、所有模板和所有历史记录。

## 2. 核心原则

- 默认只读取当前任务所需的最小上下文。
- 当前任务只涉及一个项目时，只读取当前项目目录下的相关文件。
- 当前任务只涉及一个阶段时，只读取当前阶段对应 Skill。
- 不应为了“保险”读取所有项目、所有 Skill、所有历史记录。
- `templates/` 只在新增项目或维护模板时读取。
- `references/open_source_hardware_projects.md` 只在涉及开源参考、结构借鉴或用户明确要求时读取。
- 历史审查记录、测试记录和改版记录只在继续同一问题、追踪历史问题或总结项目时读取。
- 涉及关键硬件参数时，必须回到 datasheet、reference manual 或 application note 核对。

## 3. 渐进式硬件设计阶段

本仓库采用以下阶段划分：

1. 需求整理
2. 模块方案拆分
3. 关键器件候选选型
4. 关键 datasheet 阅读
5. 模块电路设计说明
6. 外围器件反推 / BOM 草稿
7. 原理图设计
8. 原理图审查
9. PCB Layout
10. PCB 审查
11. 打样、焊接、上电、测试、改版和简历整理

资料收集不是独立的一次性前置阶段，而是嵌入“关键器件候选”“关键 datasheet 阅读”和“模块电路设计说明”的过程。

## 4. 上下文分层

| 层级 | 说明 | 示例 |
|---|---|---|
| 基础上下文 | 仓库级协作规则 | `PROJECT_RULES.md`、`AGENTS.md`、`docs/AI_Context_Guide.md` |
| 阶段上下文 | 当前任务阶段对应方法 | datasheet 阅读、器件选型、原理图审查 Skill |
| 当前项目上下文 | 当前项目相关文件 | 当前项目 `requirements.md`、`design_notes.md`、`references.md` |
| 扩展上下文 | 只有任务明确需要时读取 | `templates/`、开源参考索引、历史记录、专项 checklist |

## 5. 任务类型与读取范围

| 任务类型 | 默认读取 | 按需读取 | 不应默认读取 |
|---|---|---|---|
| 新聊天接手仓库 | `PROJECT_RULES.md`、`AGENTS.md`、`docs/AI_Context_Guide.md`、`README.md` | `docs/08_Project_Workflow.md` | 所有项目、所有 Skill、`templates/` |
| 需求整理 | 基础上下文 + 当前项目 `requirements.md` | 当前项目 `README.md`、`block_diagram.md` | 其他项目目录、所有 datasheet |
| 模块方案拆分 | 基础上下文 + 当前项目 `requirements.md`、`block_diagram.md`、`design_notes.md` | 当前项目 `references.md` | 所有 datasheet、所有 Skill、普通外围器件资料 |
| 关键器件候选选型 | 基础上下文 + `skills/hardware-component-selection/SKILL.md` + 当前项目 `requirements.md`、`design_notes.md`、`references.md` | datasheet Skill，仅在需要提取已下载资料时读取 | 原理图审查 Skill、其他项目、`templates/` |
| 关键 datasheet 阅读 | 基础上下文 + `skills/hardware-datasheet-reading/SKILL.md` + 当前项目 `requirements.md`、`references.md` + 当前模块相关 datasheet | 当前项目 `design_notes.md` | 与当前模块无关的 PDF、所有项目、所有 Skill |
| 模块电路设计说明 | 基础上下文 + 当前项目 `requirements.md`、`design_notes.md`、`references.md` + 当前模块关键资料 | 器件选型 Skill / datasheet Skill | 所有历史记录、所有外围器件资料 |
| 外围器件反推 / BOM 草稿 | 基础上下文 + 器件选型 Skill + 当前项目 `requirements.md`、`design_notes.md`、`references.md` | 当前模块 datasheet、相关 checklist | 最终 BOM、无关模块资料 |
| 原理图设计 | 基础上下文 + 当前项目需求、设计说明、关键 datasheet 和候选记录 | 器件选型 Skill / datasheet Skill | PCB 审查记录、其他项目 |
| 原理图审查 | 基础上下文 + `skills/hardware-schematic-review/SKILL.md` + 当前项目需求、设计说明、资料和原理图文件 | datasheet Skill / 器件选型 Skill，仅在追溯依据时读取 | 所有 Skill、所有项目、`templates/` |
| PCB Layout / PCB 审查 | 基础上下文 + 当前项目原理图、PCB 相关文件和 PCB checklist | datasheet / 原理图审查记录 | 其他项目目录、模板目录 |
| 调试测试 | 基础上下文 + 当前项目 `docs/bringup_log.md` / `docs/test_report.md` | 原理图审查记录、PCB 审查记录、关键 datasheet | 其他项目历史记录 |
| 新增项目 | 基础上下文 + `docs/Project_Template_Guide.md` + `templates/hardware_project_template/` | `docs/08_Project_Workflow.md` | 其他项目历史记录 |
| 模板维护 | 基础上下文 + `docs/Project_Template_Guide.md` + `templates/` | 一个已有项目结构作为参考 | 所有项目内容 |
| README / 通用文档维护 | 基础上下文 + 被修改文档 | 相关 docs | 当前项目硬件细节文件 |
| 开源项目参考分析 | 基础上下文 + `references/open_source_hardware_projects.md` | 当前项目 `references.md` / `design_notes.md` | 其他无关项目目录 |

## 6. 阶段补充规则

- 模块方案拆分阶段不需要读取所有 datasheet。
- 关键器件候选阶段只读取当前项目 `requirements.md`、`design_notes.md`、`references.md` 和器件选型 Skill。
- datasheet 阅读阶段只针对当前模块和当前候选器件。
- 不应为了“保险”读取所有项目、所有 Skill、所有历史记录。
- 不应把普通阻容、LED、排针、测试点、普通按键等外围器件作为第一轮重点资料收集对象。
- 立创商城资料由用户手动搜索和下载；AI/Codex 只整理、分析和核对用户提供的资料。

## 7. templates/ 读取规则

`templates/` 目录只在以下场景读取：

- 新增硬件项目；
- 修改或维护项目模板；
- 检查模板目录结构是否完整；
- 用户明确要求查看模板内容。

普通 datasheet 阅读、器件选型、原理图审查、PCB 审查、调试记录整理时，不应读取 `templates/`。

## 8. Skill 读取规则

- 一个任务默认只读取当前阶段对应的一个 Skill。
- 跨阶段任务才允许读取多个 Skill。
- 读取上游 Skill 应有明确原因，例如选型需要 datasheet 参数，原理图审查需要追溯选型依据。
- Skill 只保留阶段方法、输入、输出格式和关键风险提醒。
- 更细的检查项应优先沉淀到 `checklists/`。

## 9. 当前项目读取规则

当任务明确属于某一个项目时，只读取该项目目录下与任务相关的文件。

例如当前任务属于：

`projects/01_STM32_DAQ_Control_Board/`

则不应默认读取：

- `projects/02_LiIon_Charger_Protection_Board/`
- `projects/03_STM32_OpAmp_ADC_Acquisition_Board/`
- 后续新增的其他项目目录

除非用户明确要求跨项目对比、复用经验或总结所有项目。

## 10. 历史记录读取规则

以下文件只在需要追踪历史问题、继续审查、总结项目或准备简历材料时读取：

- `docs/schematic_review.md`
- `docs/pcb_review.md`
- `docs/bringup_log.md`
- `docs/test_report.md`
- `docs/revision_history.md`

普通需求整理、datasheet 阅读和初步选型时，不应默认读取全部历史记录。
