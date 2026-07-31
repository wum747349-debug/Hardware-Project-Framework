# AI 上下文读取指南

> 文档状态：当前有效
> 适用阶段：全部八阶段
> 适用对象：本仓库 AI/Codex 协作任务
> 最后核对依据：八阶段工作流程、项目结构标准与当前 Skill 路由

## 1. 文件定位

本文规定 AI 协助本仓库时的最小必要上下文，避免随项目、Skill、checklist 和历史记录增加而无边界加载。

新聊天接手仓库时默认读取：

- `PROJECT_RULES.md`
- `AGENTS.md`
- `docs/AI_Context_Guide.md`
- `README.md`

仅在判断完整流程、当前阶段、阶段权限、回退条件或维护流程时读取 `docs/08_Project_Workflow.md`。仅在新项目初始化、旧项目迁移或模板维护时读取 `docs/Project_Structure_Standard.md`、`docs/Project_Template_Guide.md` 和模板。

## 2. 核心原则

- 默认只读取“仓库基础规则 + 当前项目事实文件 + 当前阶段 Skill + 当前任务证据”。
- 一个项目任务只读取该项目相关内容；不默认加载其他项目。
- 一个阶段任务只读取该阶段 Skill；跨阶段任务才按需读取上游 Skill。
- 不默认加载全部 datasheet，只读取当前决策、问题或关键器件所需资料。
- 不默认加载项目 1，也不把项目 1 的器件、网络、板框、规则值或板厂参数当作通用参数。
- 不为“保险”读取全部历史审查、调试、测试或改版记录。
- 涉及关键硬件参数时，回到官方 datasheet、reference manual 或 application note 核对。
- 涉及制造能力时，使用目标板厂当前官方资料；商品页、报价和促销不能替代官方工艺能力。
- 文档变更只更新相应事实源，不机械同步全部项目文件。

## 3. 上下文分层

| 层级 | 内容 | 示例 |
|---|---|---|
| 基础上下文 | 仓库稳定规则与读取规则 | `PROJECT_RULES.md`、`AGENTS.md`、本文 |
| 阶段上下文 | 当前任务的执行方法 | 当前阶段 `skills/*/SKILL.md` |
| 当前项目上下文 | 当前项目事实与设计意图 | `requirements.md`、`design_notes.md`、`references.md` |
| 实现证据 | 支撑 EDA、DRC、制造或实测结论的输入 | PDF、BOM、图片、报告、输出、测量记录 |
| 扩展上下文 | 条件触发资料 | 模块文档、checklist、板厂能力、历史记录、模板、开源索引 |

## 4. 八阶段任务读取范围

| 主阶段 / 任务 | 默认读取 | 按需读取 | 不应默认读取 |
|---|---|---|---|
| 阶段 1：需求确认 | 基础上下文 + 当前项目 `requirements.md`、`block_diagram.md` | 项目 `README.md`、结构标准、模板指南（仅初始化/迁移） | 其他项目、全部 datasheet、全部 Skill |
| 阶段 2：关键器件选型 | 基础上下文 + 器件选型 Skill + 当前项目 `requirements.md`、`design_notes.md`、`references.md` | 当前候选 datasheet、datasheet Skill、专项 checklist | 原理图/PCB 审查 Skill、无关器件资料 |
| 阶段 3：模块设计与原理图绘制协作 | 基础上下文 + 当前项目需求、设计说明、资料索引、当前模块文档和关键资料 | 选型 Skill、datasheet Skill、BOM 草稿、封装资料 | 其他项目、全部历史记录 |
| 阶段 4：原理图审查 | 基础上下文 + 原理图审查 Skill + 当前项目需求、设计说明、资料索引、完整原理图 PDF、当前 BOM、`docs/schematic_review.md` | 当前模块文档；网表、ERC、元件报告、映射报告、截图仅按具体问题触发 | 其他项目、模板、全部 Skill |
| 阶段 5：Layout Preflight | 基础上下文 + PCB Skill + 当前项目 `requirements.md`、`design_notes.md`、`references.md`、`docs/schematic_review.md`、`docs/pcb_design_rules.md` 和关键器件 Layout 资料 | 原理图 PDF、BOM、模块文档、目标板厂官方能力、机械约束 | `docs/pcb_review.md`、DRC 报告、制造输出、其他项目 |
| 阶段 5～6：Layout / Routing Review | 基础上下文 + PCB Skill + 当前项目 `requirements.md`、`design_notes.md`、`docs/pcb_design_rules.md` 和当前 PCB 图片/实现证据 | 相关模块文档、关键 datasheet、`docs/schematic_review.md`；继续已有问题时读取 `docs/pcb_review.md` | 全部 `references/`、全部 datasheet、完整流程、Release Checklist、制造输出、DRC 结果 |
| 阶段 7：PCB Release Review | 基础上下文 + PCB Skill + 当前项目 `requirements.md`、`docs/pcb_design_rules.md`、`docs/pcb_review.md`、当前 PCB 实现证据、当前 BOM、用户对话中的完整 Batch DRC 结果、制造输出清单/实际输出和 Release Checklist | 目标板厂官方能力、Gerber、Drill、Pick and Place、装配图、制造说明、局部截图 | 其他项目、未关联的历史输出、全部 datasheet |
| 阶段 8：焊接和硬件调试 | 基础上下文 + 当前项目 `bringup_log.md`、`test_report.md`、原理图和接口说明 | PCB 审查记录、关键 datasheet、专项安全 checklist、`revision_history.md` | 其他项目历史记录、模板 |

## 5. 常见维护任务

| 任务 | 默认读取 | 按需读取 | 不应默认读取 |
|---|---|---|---|
| 新增项目 | 基础上下文 + 结构标准 + 模板指南 + 硬件项目模板 | 八阶段流程 | 其他项目历史记录 |
| 模板维护 | 基础上下文 + 结构标准 + 模板指南 + 模板 | 一个明确的参考项目结构 | 所有项目内容、全部 datasheet |
| 旧项目迁移 | 基础上下文 + 结构标准 + 当前项目入口与目录说明 | 当前阶段文件、八阶段流程 | 机械重写全部历史记录 |
| README / 通用文档维护 | 基础上下文 + 被修改文档 | 与引用关系直接相关的权威文档 | 当前项目全部硬件细节 |
| 开源项目参考分析 | 基础上下文 + 仓库开源参考索引 | 当前项目 `references.md`、需求与设计说明 | 其他无关项目 |
| 历史问题追踪 | 基础上下文 + 当前问题所在审查/调试/测试记录 | 与该问题直接关联的证据和资料 | 全部历史输出 |

## 6. PCB 三种模式最小上下文

PCB Layout Preflight、布局审查、布线铺铜审查、PCB Review 和制造放行默认读取 `skills/hardware-pcb-layout-review/SKILL.md`。

### Layout Preflight

- 当前项目 `requirements.md`
- 当前项目 `design_notes.md`
- 当前项目 `references.md`
- 当前项目 `docs/schematic_review.md`
- 当前项目 `docs/pcb_design_rules.md`
- 关键器件 Layout 资料

原理图 PDF、BOM、模块文档、板厂官方能力和机械约束按需读取；不默认读取 `pcb_review.md`、DRC 报告或制造输出。

### Layout / Routing Review

- 当前项目 `requirements.md`
- 当前项目 `design_notes.md`
- 当前项目 `docs/pcb_design_rules.md`
- 当前 PCB 图片或用户提供的实现证据

模块文档、关键 datasheet、原理图审查记录和已有 PCB 问题按需读取；不默认读取全部资料索引、全部 datasheet、完整流程、Release Checklist、制造输出或 DRC 结果。

### PCB Release Review

- 当前项目 `requirements.md`
- 当前项目 `docs/pcb_design_rules.md`
- 当前项目 `docs/pcb_review.md`
- 当前 PCB 实现证据和当前 BOM
- 用户在对话中提供的完整 Batch DRC 结果
- 制造输出清单或待放行的实际输出
- `checklists/pcb_release_checklist.md`

Gerber、Drill、Pick and Place、装配图、制造说明和局部截图按具体问题读取。DRC 摘要默认来自用户对话，不要求专门报告或完整截图。

### 条件触发原则

- 目标板厂官方能力：制造基线、设计规则、制造规则或下单核对任务；
- 相关关键器件 PCB Layout 要求：布局、布线、散热、回流或专项规则依赖器件要求时；
- 原理图 PDF 与 BOM：问题涉及网络、封装、极性、接口或原理图审查追溯时；
- DRC 局部截图或报告片段：用户摘要不足以判断具体违规、规则问题或豁免时；
- Gerber、钻孔、坐标和装配输出：制造放行时。

不因一般 PCB 视觉审查自动浏览板厂资料；只有判断制造能力、规则值、裕量或下单参数时才读取目标板厂官方能力。

## 7. Altium 与证据边界

- `.SchDoc` 与 `.PcbDoc` 是权威实现源文件，但只有当前环境具备可靠解析器、脚本或自动化接口时，AI 才能直接读取相应内部对象。
- 无可靠 `.SchDoc` 解析能力时，原理图审查默认使用可追溯的完整原理图 PDF 和当前 BOM。
- 无可靠 `.PcbDoc` 解析能力时，只使用用户提供的 PCB 图片、规则摘要、DRC 对话结果、报告、截图和制造输出等实现证据。
- PCB 图片只能支持视觉审查，不能证明网络、间距、线宽、孔径、环宽、规则命中、铺铜状态或 DRC 通过。
- AI 只有在用户提供 ERC 或 DRC 结果时才分析实际结果，不得声称自行运行 Altium、Repour、ERC 或 Batch DRC。
- 缺少 DRC 报告文件不自动阻断审查；缺少版本、规则基线或关键类别时，只能给出受限结论。
- 无法由现有证据确认的实现事项，标记“待 EDA 核对”，不得据此关闭问题或制造放行。

## 8. 完整流程读取规则

仅在以下情况读取完整 `docs/08_Project_Workflow.md`：

- 判断项目处于哪个主阶段；
- 判断进入、退出、回退或阶段权限；
- 执行新项目初始化或旧项目迁移；
- 维护流程、结构、模板或跨阶段门禁；
- 用户明确要求完整流程说明。

普通 datasheet 阅读、单次器件选型、单次原理图审查、单次 PCB 审查、调试记录或小幅文档维护不默认读取完整流程。
