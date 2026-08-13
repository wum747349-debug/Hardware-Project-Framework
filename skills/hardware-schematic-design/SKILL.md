# Hardware Schematic Design Skill

## 1. Purpose / Applicable Tasks

本 Skill 服务 Stage 3 — Schematic Module Design and Capture，回答“已经确定的关键器件，应该如何组成实际模块电路？”。用于按需规划 schematic module、设计连接与关键外围参数、指导用户完成 EDA capture、执行轻量 Cross-Module Integration Check，并判断是否达到 `READY FOR SCHEMATIC REVIEW`。

本 Skill 不承担 Stage 4 正式 Schematic Review，也不批准进入 PCB Layout。

## 2. Minimum Context

默认读取：

1. Layer 0/1：Project `FRAMEWORK.md`、`PROJECT_RULES.md` 与绑定 Framework 的 `docs/AI_Context_Guide.md`
2. 本 Skill
3. 当前 Project 的 `requirements.md`、`design_notes.md`、`references.md`
4. 当前任务涉及的器件决策和已有模块文档

按需读取当前 BOM 草稿、封装资料，以及当前连接真正需要的 Manufacturer official documentation。复杂 datasheet extraction 调用 `skills/hardware-datasheet-reading/SKILL.md`；关键器件需要重新评估时才调用 `skills/hardware-component-selection/SKILL.md`。不默认读取全部 Skill、全部 datasheet、其他 Project 或全部历史记录。

## 3. Core Principles

- Module plan 按 functional boundary、power domain / power flow、signal / control flow、sequencing、protection / safety boundary、complexity 与 Layout-sensitive boundary 决定，不固定数量，禁止使用 `One IC = One Module`。
- 简单项目允许单页 schematic；复杂项目可使用 Top Sheet + Functional Sheets，但不强制 Top Sheet、固定 sheet 数量或一模块一 Markdown。
- `docs/module_design/*.md` 只在复杂度或追溯价值需要时创建，不要求每个简单模块都有独立文件。
- 只核对当前连接所需的官方资料；关键连接必须有 Manufacturer documentation、计算或显式 engineering basis。
- 普通 support components 可在模块设计中按需确定，不因普通外围自动重新进入完整 Stage 2。
- 设计时同时明确 startup、shutdown、default 与 fault behavior，并提取 schematic-relevant Layout inputs。

## 4. Workflow

### Determine Module Plan

从 Requirements、component decisions 和 system interfaces 确定实际需要的模块边界。为每个模块记录 responsibility、inputs / outputs、power domain、cross-module interfaces、sequencing / protection boundary 和关键 Layout sensitivity；仅在有追溯价值时形成模块文档。

### Module Design Loop

每个模块执行五步：

1. **Define**：明确 module responsibility、inputs / outputs、relevant requirements 与 cross-module interfaces。
2. **Verify**：只用 Manufacturer official documentation 核对当前设计真正需要的 pin behavior、operating conditions、typical application、required peripherals、package 与 Layout 要求；复杂提取转交 datasheet-reading Skill。
3. **Design**：确定 pin connections、net naming、power / ground、enable / reset / mode、feedback / sense、protection、required support components 与 unused-pin handling。
4. **Calculate**：在 schematic freeze 前，为决定关键电气行为的外围值记录 datasheet basis / equation、calculated or selected value、tolerance / assumption、expected behavior 与 remaining uncertainty。适用对象包括 feedback divider、current-limit / charge-current resistor、timing capacitor、inductor、capacitor、filter、NTC 与 gain network。
5. **Record**：保留 connection plan、parameter decisions、重要 assumptions、Layout-sensitive notes、open issues 与 capture status；不复制无关 Project Facts。

普通 resistor、capacitor、diode、LED、test point、jumper、small MOSFET、small logic gate 与 analog switch 可随模块设计确定。只有新辅助器件影响 architecture、safety、critical electrical behavior、thermal 或 package / Layout boundary 时，才对相关部分调用 component-selection Skill 或重新评估关键器件。

### User EDA Capture

AI/Codex 可以提供 module plan、connection plan、pin-by-pin guidance、参数计算、net naming、capture sequence 与 Layout-sensitive notes。用户负责在 Altium Designer 中实际创建 Sheet、放置 symbol、连接 wire / net、设置 value / parameter、确认 footprint、保存 `.SchDoc`、执行 ERC，并导出与当前版本对应的完整 schematic PDF 和 BOM。

### Cross-Module Integration

所有主要模块完成设计与 capture 后，在 Stage 3 执行一次轻量 Cross-Module Integration Check，确认模块能够组成完整且自洽的设计，至少覆盖：

1. Power Flow
2. Signal / Control Flow
3. Voltage / Logic Compatibility
4. Startup / Shutdown / Fault State
5. Cross-sheet Net Consistency
6. Missing / Conflicting Responsibility

该检查不重复 Stage 4 的完整 schematic checklist、完整 BOM review、全部 pin audit、全部 protection review 或 PCB-layout-entry approval。

### Stage 3 Readiness

只有同时满足以下条件，才可报告 `READY FOR SCHEMATIC REVIEW`：

- 主要模块设计完成；
- 关键连接具有 Manufacturer documentation、计算或显式 engineering basis；
- 必要关键外围参数已确定，或未决项边界清晰且不阻止审查；
- startup / default / fault behavior 已分析；
- Cross-Module Integration Check 已完成；
- 用户已完成当前版本 EDA capture；
- 已有与当前 `.SchDoc` 对应的完整 schematic PDF；
- 已有当前版本 BOM。

`READY FOR SCHEMATIC REVIEW` 不等于 `ERC PASS`、Stage 4 PASS 或 PCB Layout approved。

## 5. Evidence Boundary

`.SchDoc` 是 authoritative schematic implementation source。没有可靠 EDA parser 或 Altium automation 时，不得声称已读取 `.SchDoc` 内部对象、已完成 schematic capture、已验证实际 pin mapping、已运行 ERC、已确认所有跨页网络或已确认 footprint mapping。AI/Codex 只分析用户提供的 PDF、BOM、截图、报告或其他实际 EDA evidence，并明确结论限制。

## 6. Return / Escalation Rules

- 若关键器件不满足 electrical requirement、功能 / pin behavior 不成立、thermal / package 不可接受，或 procurement condition 失效且无合理替代，只将相关部分返回 Stage 2 reevaluation。
- 若必须修改 confirmed functional requirement、safety boundary、system interface 或 architecture-level requirement，返回 Stage 1 / relevant Gate 处理。
- 普通外围参数调整不触发 Stage rollback；不得自动修改 Project `README.md` 的 Current Project Stage。

## 7. Output

输出保持精简并可直接指导 capture：

1. Module Plan：模块责任、接口、边界和设计顺序
2. Module Design Record：Define / Verify / Design / Calculate / Record 的关键结果
3. EDA Capture Guidance：net naming、pin / connection plan、capture sequence 和待用户确认项
4. Cross-Module Integration：六类检查的结论、冲突和 open issues
5. Stage 3 Readiness：`READY FOR SCHEMATIC REVIEW` 或明确列出尚未满足的条件

## 8. Prohibited Actions

- 不把 Stage 3 扩展为 Stage 4 正式 Schematic Review。
- 不输出 `SCHEMATIC PASS`、`ERC PASS`、`STAGE 4 PASS` 或 `PCB LAYOUT APPROVED`，除非存在对应真实 Evidence 和后续 Stage 结果。
- 不强制固定 module / sheet 数量、Top Sheet 或一模块一文档。
- 不复制 datasheet-reading、component-selection 或 schematic checklist 的完整方法。
- 不用商品页、教程、博客或开源项目替代关键参数的 Manufacturer official documentation。
- 不伪造 EDA capture、ERC、pin mapping、cross-sheet net 或 footprint mapping 结果。
