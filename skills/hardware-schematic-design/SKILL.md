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

按需读取当前 BOM 草稿、封装资料，以及当前连接真正需要的 Manufacturer official documentation。复杂 datasheet extraction 调用 `skills/hardware-datasheet-reading/SKILL.md`；当 exact component identity 是验证 electrical behavior、safety、thermal behavior 或 package / Layout-sensitive assumption 的必要条件，或既有关键器件需要重新评估时，对相关部分调用 `skills/hardware-component-selection/SKILL.md`。不默认读取全部 Skill、全部 datasheet、其他 Project 或全部历史记录。

## 3. Core Principles

- Module plan 按 functional boundary、power domain / power flow、signal / control flow、sequencing、protection / safety boundary、complexity 与 Layout-sensitive boundary 决定，不固定数量，禁止使用 `One IC = One Module`。
- 简单项目允许单页 schematic；复杂项目可使用 Top Sheet + Functional Sheets，但不强制 Top Sheet、固定 sheet 数量或一模块一 Markdown。
- Stage 3 entry 至少需要一个 owning `docs/module_design/*.md` record 承接当前 detailed design work；是否按模块拆分更多 records 由复杂度和追溯价值决定，不要求每个简单模块都有独立文件。
- 只核对当前连接所需的官方资料；关键连接必须有 Manufacturer documentation、计算或显式 engineering basis。
- 普通 support components 可在模块设计中按需确定，不因普通外围自动重新进入完整 Stage 2。
- Stage 3 定义全部 required components 的 electrical requirements。只有 exact identity 对当前 electrical、safety、thermal 或 package / Layout-sensitive validation 必不可少时才必须完成相应 qualification；否则可以保留充分 specification，而不虚构或提前锁定 procurement identity。
- 设计时同时明确 startup、shutdown、default 与 fault behavior，并提取 schematic-relevant Layout inputs。
- Module-specific connections、support values 与 calculations 默认记录在当前 module design context，不自动反向同步 Stage 2 selection artifacts 或 board-level documents；selection、qualification、architecture 或 requirement 实质变化时，更新对应 owner 或返回相关 Stage reevaluation。

### Proven Design Reuse

- 优先采用经过证明且适合当前需求的实现，避免不必要的重新设计。
- 适用时，Manufacturer-recommended implementation、prior field-used design 和 evidence-backed external design 可作为 design starting point 或 qualified reuse input。
- Reuse 不会转移 qualification；采用前按当前 Project 实际相关项重新核对 voltage、current、logic behavior、load、startup / default state、fault behavior、protection、thermal、package、availability 与 Layout-sensitive constraints。
- 关键参数仍以 Manufacturer official documentation 为技术权威。
- 对 Manufacturer-recommended / typical implementation，若没有必要重新推导公式，可以用 official manufacturer recommendation、当前 Project 的 applicability check、selected implementation，以及 remaining uncertainty / validation boundary 形成充分 engineering basis；不得为了满足记录规则制造没有工程价值的公式。
- 不要仅为追求原创性而重新设计本来合适的成熟实现；若当前 Project 明确要求 independent reimplementation，则该 Project requirement 优先于 Framework 的默认复用许可。

## 4. Workflow

### Determine Module Plan

从 Requirements、component decisions 和 system interfaces 确定实际需要的模块边界。为每个模块记录 responsibility、inputs / outputs、power domain、cross-module interfaces、sequencing / protection boundary 和关键 Layout sensitivity。Stage 3 至少使用一个 owning module design record 承接当前 detailed design work；additional per-module records 仅在复杂度或追溯价值需要时形成。

### Module Design Loop

每个模块执行五步：

1. **Define**：明确 module responsibility、inputs / outputs、relevant requirements 与 cross-module interfaces。
2. **Verify**：为全部 required components 定义当前电路所需的 electrical requirements；只用 Manufacturer official documentation 核对当前设计真正需要的 pin behavior、operating conditions、typical application、required peripherals、package 与 Layout 要求。复杂提取转交 datasheet-reading Skill；若这些验证依赖 exact identity，对相关部分调用 component-selection supporting method。
3. **Design**：确定 pin connections、net naming、power / ground、enable / reset / mode、feedback / sense、protection、required support components 与 unused-pin handling。
4. **Calculate**：在 schematic freeze 前，为决定关键电气行为的外围值记录可同时支持当前设计和后续 durable record 的最小可复现 engineering basis，包括适用的 datasheet basis / equation、calculated or selected value、tolerance / assumption、expected behavior 与 remaining uncertainty；不要求保存完整推导或逐步算术。适用对象包括 feedback divider、current-limit / charge-current resistor、timing capacitor、inductor、capacitor、filter、NTC 与 gain network。凡 topology / value / parameter choice 会实质影响 requirement compliance、protection / fault limit、gain / scaling、bandwidth / filtering、accuracy、ADC settling、driver stability、voltage / current margin、reference behavior、timing、thermal、power headroom、startup / shutdown 或 fault behavior，且未来改变时通常需要重新查 datasheet、计算、判断 margin 或确认 applicability，通常属于 decision-driving engineering rationale；ordinary implementation detail 不因此被强制扩写。
5. **Record**：保留可检索的 connection facts、parameter decisions、重要 assumptions、Layout-sensitive notes、open issues 与 capture status；不复制无关 Project Facts，也不把 `.SchDoc` 重写成一整份长期文本副本。对于 decision-driving electrical choice，`Calculate` 形成的关键依据不得在 Record / documentation convergence 后只剩 final value、final connection 或 final topology。Owning module record 应保留足以重新检查该决策的最小信息：engineering / manufacturer basis、relevant assumptions、适用的 equation 或 decision method、calculated / selected result、expected behavior / margin，以及 remaining uncertainty / validation boundary。这些是 information requirements，不是 mandatory section headings 或 fixed schema；简单设计可以用一两句话满足。

Support component 可随模块设计按实际影响确定，不按器件类别固定 Stage。只有新辅助器件影响 architecture、safety、critical electrical behavior、thermal 或 package / Layout boundary，或 exact identity 是验证这些假设的必要条件时，才对相关部分调用 component-selection Skill；普通低风险实际料无需因此重新执行完整 Stage 2 候选流程。

### User EDA Capture

AI/Codex 可以提供 module plan、connection plan、pin-by-pin guidance、参数计算、net naming、capture sequence 与 Layout-sensitive notes。用户负责在 Altium Designer 中实际创建 Sheet、放置 symbol、连接 wire / net、设置 value / parameter、确认 footprint、保存 `.SchDoc`、执行 ERC，并导出与当前版本对应的完整 schematic PDF 和 BOM。

Functional block diagram / signal-flow diagram 只用于 architecture、module planning 与接口流向表达。当用户正在设计具体模块、询问“怎么接”、准备 EDA capture 或要求最终接线时，不得停留在抽象框图；默认先提供可直接指导 Altium 等 EDA capture 的 **Schematic-like Connection Diagram**，再提供 **Pin-by-Pin Final Wiring**、**Component / Parameter Values**，最后列出必要的 engineering notes / open issues。

Schematic-like diagram 按适用性清楚展示 IC pin number / pin name、junction / shared node、branch connection、power / GND、net label、resistor / capacitor / support component、NC / unused handling、diode / LED / MOSFET / polarized device 的方向或 terminal identity，以及 cross-module net。不得要求用户从一串自然语言箭头自行推导实际 topology。完整 pin-by-pin wiring 主要作为 completeness cross-check，避免漏脚；只有需要 completeness audit 时才使用 pin table。

### Project Module Documentation

长期 module design record 遵循：**Diagram on ambiguity, structured text by default.** 记录应对人足够清楚、对 AI / Review 可稳定检索、不重复 authoritative `.SchDoc`，且不因 presentation 明显膨胀。默认使用简洁、无歧义的 structured connection text，例如：

```text
U6.1 EN/UVLO → EN_UVLO
R21 160kΩ: 3V3 ↔ EN_UVLO
R22 100kΩ: EN_UVLO ↔ GND
```

只有 shared node / wired-AND / wired-OR、多处分支 junction、MOSFET / transistor control、diode / polarity-sensitive path、divider + switch / comparator combination、多器件共同驱动一个 control net，或纯文字容易产生 topology 歧义的 cross-module control path，才建议附 compact schematic-like textual diagram。简单 power、GND、单一 pin-to-net connection 不要求额外 diagram。

Diagram 用于表达 topology / ambiguity；structured connection record 用于保存长期可检索事实；pin table 只在 completeness 需要时使用。不得机械地把同一连接同时复制到 diagram、pin table、net table、component table 与 prose。Project documentation 只保存真正具有长期追溯价值的 design intent、connections、key values、cross-module interface、open issue 与 evidence boundary。

Documentation concision 可以删除重复表达，避免复制 `.SchDoc`、datasheet 或相同的 diagram / table / prose，但不得删除 decision-driving engineering rationale。尤其不得把有 engineering basis 的 selected value 压缩成只有 final value、无法追溯选择原因的记录。

大型 error budget、noise analysis、stability simulation、thermal model、timing budget、parameter sweep、spreadsheet 或 simulation result 等复杂分析，可在确有必要时放入 supporting analysis artifact；这不是默认 Stage 3 artifact，也不得成为第二个 selected-design authority。Owning module record 仍须保留 assumptions、selected result、decision conclusion、remaining uncertainty 与 supporting analysis reference 的最小摘要：**Complex analysis may be externalized; the design decision must remain recoverable from the owning module record.**

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
- 至少一个 owning module design record 已承接当前 detailed design work，additional records 的拆分与复杂度和追溯需求相称；
- 全部 required components 的 electrical requirements 已定义；尚未确定的 exact procurement identity 不阻断当前 electrical、safety、thermal 或 package / Layout-sensitive validation；
- 关键连接和 decision-driving electrical choices 具有 durable and traceable 的 Manufacturer documentation、计算或显式 engineering basis，可从 owning module record 或其明确引用的 supporting analysis 中恢复；
- 必要关键外围参数已确定，或未决项边界清晰且不阻止审查；
- startup / default / fault behavior 已分析；
- Cross-Module Integration Check 已完成；
- 用户已完成当前版本 EDA capture；
- 已有与当前 `.SchDoc` 对应的完整 schematic PDF；
- 已有当前版本 BOM。

`READY FOR SCHEMATIC REVIEW` 不等于 `ERC PASS`、Stage 4 PASS 或 PCB Layout approved。

`Electrical design selected` 表示相应 electrical decision 已有足够且可追溯的 engineering basis；simulation、PCB implementation 或 hardware validation 可以仍然 pending。不得为了记录 selected design 而假称这些后续验证已经完成，也不为未收敛项新增正式 lifecycle state；继续使用现有自然语言、open issues 与 evidence / validation boundary 表达。

## 5. Evidence Boundary

`.SchDoc` 是 authoritative schematic implementation source。没有可靠 EDA parser 或 Altium automation 时，不得声称已读取 `.SchDoc` 内部对象、已完成 schematic capture、已验证实际 pin mapping、已运行 ERC、已确认所有跨页网络或已确认 footprint mapping。AI/Codex 只分析用户提供的 PDF、BOM、截图、报告或其他实际 EDA evidence，并明确结论限制。

## 6. Return / Escalation Rules

- 只有建立 architecture / module direction 所依赖的关键 component identity 或 qualification 不成立时，才将相关部分返回 Stage 2 reevaluation。
- 若必须修改 confirmed functional requirement、safety boundary、system interface 或 architecture-level requirement，返回 Stage 1 / relevant Gate 处理。
- Topology、connection、electrical requirement 与 calculated-value issue 在 Stage 3 处理；普通 actual-part、supplier-part、library、footprint mapping 或外围参数调整若不否定上游 electrical design，不触发 Stage 2 rollback。不得自动修改 Project `README.md` 的 Current Project Stage。

## 7. Output

输出保持精简并可直接指导 capture：

1. Module Plan：模块责任、接口、边界和设计顺序
2. Module Design Record：Define / Verify / Design / Calculate / Record 的关键结果
3. EDA Capture Guidance：默认依次给出 Schematic-like Connection Diagram、Pin-by-Pin Final Wiring、Component / Parameter Values，以及必要的 engineering notes / open issues；另列 net naming、capture sequence 和待用户确认项
4. Cross-Module Integration：六类检查的结论、冲突和 open issues
5. Stage 3 Readiness：`READY FOR SCHEMATIC REVIEW` 或明确列出尚未满足的条件

## 8. Prohibited Actions

- 不把 Stage 3 扩展为 Stage 4 正式 Schematic Review。
- 不输出 `SCHEMATIC PASS`、`ERC PASS`、`STAGE 4 PASS` 或 `PCB LAYOUT APPROVED`，除非存在对应真实 Evidence 和后续 Stage 结果。
- 不强制固定 module / sheet 数量、Top Sheet 或一模块一文档。
- 不复制 datasheet-reading、component-selection 或 schematic checklist 的完整方法。
- 不用商品页、教程、博客或开源项目替代关键参数的 Manufacturer official documentation。
- 不伪造 EDA capture、ERC、pin mapping、cross-sheet net 或 footprint mapping 结果。
- 当任务目标是实际 schematic capture guidance 时，不得仅用 functional block diagram、signal-flow arrows、abstract text chain、prose-only connection summary 或 incomplete pin table 替代具体接线指导。
- 不把所有 module documentation 强制变成完整 ASCII schematic，也不为 presentation 重复保存第二份原理图。
