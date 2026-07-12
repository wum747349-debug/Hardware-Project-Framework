# AI 上下文读取指南

## 1. 文件定位

本文用于规定 AI 在协助本仓库时的最小必要上下文读取规则，避免随着项目数量、Skill 数量和历史记录增加而出现上下文膨胀。

AI 默认只读取“仓库基础规则 + 当前项目文件 + 当前阶段 Skill”，不默认读取所有项目、所有 Skill、所有模板和所有历史记录。

新聊天接手仓库时，默认读取：

- `PROJECT_RULES.md`
- `AGENTS.md`
- `docs/AI_Context_Guide.md`
- `README.md`

`docs/08_Project_Workflow.md` 是仓库标准执行流程和阶段边界规则，只在需要判断完整流程、当前阶段、阶段权限或维护流程文档时按需读取。`prompts/硬件项目工作流程总结.md` 是面向用户的学习、复盘和任务布置参考文档，只在用户明确需要流程总结、阶段复盘或生成提示词时按需读取。

## 2. 核心原则

- 默认只读取当前任务所需的最小上下文。
- 当前任务只涉及一个项目时，只读取当前项目目录下的相关文件。
- 当前任务只涉及一个阶段时，只读取当前阶段对应 Skill。
- 不应为了“保险”读取所有项目、所有 Skill、所有历史记录。
- 普通任务不默认读取 `docs/08_Project_Workflow.md` 和 `prompts/硬件项目工作流程总结.md`。
- `templates/` 只在新增项目或维护模板时读取。
- `references/open_source_hardware_projects.md` 只在涉及开源参考、结构借鉴或用户明确要求时读取。
- 历史审查记录、测试记录和改版记录只在继续同一问题、追踪历史问题或总结项目时读取。
- 涉及关键硬件参数时，必须回到 datasheet、reference manual 或 application note 核对。

## 3. 上下文分层

| 层级      | 说明          | 示例                                                        |
| ------- | ----------- | --------------------------------------------------------- |
| 基础上下文   | 仓库级协作规则     | `PROJECT_RULES.md`、`AGENTS.md`、`docs/AI_Context_Guide.md` |
| 阶段上下文   | 当前任务阶段对应方法  | datasheet 阅读、器件选型、原理图审查 Skill                             |
| 当前项目上下文 | 当前项目相关文件    | 当前项目 `requirements.md`、`design_notes.md`、`references.md`  |
| 扩展上下文   | 只有任务明确需要时读取 | `templates/`、开源参考索引、历史记录、专项 checklist                     |

## 4. 任务类型与读取范围

| 任务类型                | 默认读取                                                                                                              | 按需读取                                     | 不应默认读取                         |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------ |
| 新聊天接手仓库             | `PROJECT_RULES.md`、`AGENTS.md`、`docs/AI_Context_Guide.md`、`README.md`                                             | `docs/08_Project_Workflow.md`、`prompts/硬件项目工作流程总结.md`，仅在下方规则命中时读取 | 所有项目、所有 Skill、`templates/`、所有历史记录 |
| 需求整理                | 基础上下文 + 当前项目 `requirements.md`                                                                                    | 当前项目 `README.md`、`block_diagram.md`      | 其他项目目录、所有 datasheet            |
| 模块方案拆分              | 基础上下文 + 当前项目 `requirements.md`、`block_diagram.md`、`design_notes.md`                                               | 当前项目 `references.md`                     | 所有 datasheet、所有 Skill、普通外围器件资料 |
| 关键器件候选选型            | 基础上下文 + `skills/hardware-component-selection/SKILL.md` + 当前项目 `requirements.md`、`design_notes.md`、`references.md` | datasheet Skill，仅在需要提取已下载资料时读取           | 原理图审查 Skill、其他项目、`templates/`  |
| 关键 datasheet 阅读     | 基础上下文 + `skills/hardware-datasheet-reading/SKILL.md` + 当前项目 `requirements.md`、`references.md` + 当前模块相关 datasheet  | 当前项目 `design_notes.md`                   | 与当前模块无关的 PDF、所有项目、所有 Skill     |
| 模块电路设计说明            | 基础上下文 + 当前项目 `requirements.md`、`design_notes.md`、`references.md` + 当前模块关键资料                                       | 器件选型 Skill / datasheet Skill             | 所有历史记录、所有外围器件资料                |
| 外围器件反推 / BOM 草稿     | 基础上下文 + 器件选型 Skill + 当前项目 `requirements.md`、`design_notes.md`、`references.md`                                     | 当前模块 datasheet、相关 checklist              | 最终 BOM、无关模块资料                  |
| 原理图设计               | 基础上下文 + 当前项目需求、设计说明、关键 datasheet 和候选记录                                                                            | 器件选型 Skill / datasheet Skill             | PCB 审查记录、其他项目                  |
| 原理图审查               | 基础上下文 + `skills/hardware-schematic-review/SKILL.md` + 当前项目需求、设计说明、资料和当前可解析的实现证据，如原理图 PDF、网表、ERC 报告、BOM、元件报告或截图；`.SchDoc` 仅在当前环境具备可靠解析能力时作为 AI 读取输入 | datasheet Skill / 器件选型 Skill，仅在追溯依据时读取   | 所有 Skill、所有项目、`templates/`     |
| 原理图变更后的文档同步        | 基础上下文 + 当前可解析的实现证据，如原理图 PDF、网表、ERC 报告、BOM、元件报告或截图 + 当前项目 `design_notes.md` + 与变更相关的 `module_design` 文档 + `docs/schematic_review.md`；`.SchDoc` 仅在当前环境具备可靠解析能力时作为 AI 读取输入 | `requirements.md`，仅当功能边界或验收标准受到影响；`references.md`，仅当器件或参数依据发生变化；`docs/revision_history.md`，记录重要设计决定或硬件版本变化；datasheet Skill，仅当需要核对关键器件参数 | 其他项目、全部 Skill、全部 datasheet、无关历史记录、`templates/` |
| PCB Layout / PCB 审查 | 基础上下文 + 当前项目原理图、PCB 相关文件和 PCB checklist                                                                           | datasheet / 原理图审查记录                      | 其他项目目录、模板目录                    |
| 调试测试                | 基础上下文 + 当前项目 `docs/bringup_log.md` / `docs/test_report.md`                                                        | 原理图审查记录、PCB 审查记录、关键 datasheet            | 其他项目历史记录                       |
| 新增项目                | 基础上下文 + `docs/Project_Template_Guide.md` + `templates/hardware_project_template/`                                 | `docs/08_Project_Workflow.md`            | 其他项目历史记录                       |
| 模板维护                | 基础上下文 + `docs/Project_Template_Guide.md` + `templates/`                                                           | 一个已有项目结构作为参考                             | 所有项目内容                         |
| README / 通用文档维护     | 基础上下文 + 被修改文档                                                                                                     | 相关 docs                                  | 当前项目硬件细节文件                     |
| 开源项目参考分析            | 基础上下文 + `references/open_source_hardware_projects.md`                                                             | 当前项目 `references.md` / `design_notes.md` | 其他无关项目目录                       |

## 5. 特殊读取规则

- `docs/08_Project_Workflow.md` 只在用户询问完整流程、需要判断阶段边界或权限、新项目初始化、维护流程文档时读取。
- `prompts/硬件项目工作流程总结.md` 只在用户要求流程总结、阶段复盘、生成提示词或学习完整流程时读取。
- `templates/` 只在新增硬件项目、维护模板、检查模板结构或用户明确要求时读取。
- 一个任务默认只读取当前阶段对应的一个 Skill；跨阶段任务才按需读取上游 Skill。
- 当前任务明确属于某个项目时，只读取该项目目录下与任务相关的文件；跨项目对比、经验复用或总结所有项目时才读取其他项目。
- 历史审查、PCB 审查、bringup、测试报告和改版记录只在追踪历史问题、继续审查、总结项目或准备简历材料时读取。
- 原理图变更后的文档同步必须以用户在 Altium 中修改后的实现输出为依据；AI 通过更新后的 PDF、网表、ERC、BOM、报告或截图核对实现，无可靠证据时标记“待 EDA 核对”。
- `.SchDoc` 是权威源文件，但只有在当前环境具备可靠 Altium 解析器、脚本或自动化接口时，才能作为 AI 直接读取和核对的实现输入。
- 文档变更只影响相关事实源，不应机械修改所有项目文档。
