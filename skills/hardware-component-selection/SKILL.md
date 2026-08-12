# Hardware Component Selection Skill

## 适用场景

当需要进行关键器件候选选型、替代料选择、候选方案比较、BOM 草稿依据整理或采购风险分析时，使用本 Skill。

本 Skill 服务于渐进式硬件设计流程：关键器件优先，外围器件后置。第一轮只做关键器件候选，不生成最终 BOM。

## 最小读取上下文

默认读取：

1. `PROJECT_RULES.md`
2. `AGENTS.md`
3. `docs/AI_Context_Guide.md`
4. `skills/hardware-component-selection/SKILL.md`
5. 当前项目 `requirements.md`
6. 当前项目 `design_notes.md`
7. 当前项目 `references.md`

按需读取：

- `skills/hardware-datasheet-reading/SKILL.md`，仅在需要提取或核对已下载 datasheet 参数时读取。
- 当前模块相关 datasheet。
- 相关 checklist。

不默认读取：

- 所有项目目录。
- 所有 Skill。
- 所有 datasheet。
- 模板目录。
- 历史审查记录。

## 核心原则

- 第一轮只关注关键器件候选，不生成完整最终 BOM。
- 关键器件优先，普通外围器件后置。器件何时确定取决于 architecture impact、safety / risk impact、critical parameter dependency 与 Layout / thermal impact，不按 MOSFET、TVS、NTC、inductor 等器件类别硬编码 Stage；不影响架构的普通阻容、LED 等仍可后置。
- 默认工作流是 `Requirements → JLCPCB / LCSC-first candidate discovery → Manufacturer datasheet qualification → Primary + Alternate decision → purchase-time availability recheck`。
- `JLCPCB/LCSC-first` 是现实采购候选池的优先级，不是 `JLCPCB/LCSC-only`。只有满足工程 Hard Requirements 的器件才是有效候选；不得为满足采购优先级而选择明显技术更差或不满足要求的器件。
- 当前执行环境具备公开 Web/Search 能力时，AI/Codex 可以且应优先搜索公开的 JLCPCB、LCSC 或 JLCPCB Parts 信息进行候选发现；不声明所有环境都具备公网或商城访问能力，也不默认进行受限访问、爬取或批量下载。
- 当前环境没有相关搜索能力时，由用户提供 C 编号、MPN、candidate 或商品页信息，再继续 qualification。
- 默认筛出约 2–4 个 realistic candidates，正常结果优先形成 `Primary` 与 `Alternate`；只有确有工程意义时增加 `Conditional` 或 `Rejected`，不为填满类别制造低质量候选。
- JLCPCB/LCSC 没有合理候选时，可扩大到 Manufacturer、Mouser、DigiKey 或其他适当 distributor / sourcing channel。
- 禁止一上来生成完整最终 BOM。

## Evidence 边界

### Procurement evidence

JLCPCB/LCSC、JLCPCB Parts、marketplace 或 distributor 信息主要用于确认：

- JLC C-number
- Manufacturer 与 MPN
- listed package
- current availability 与 price
- procurement convenience
- 适用时的公开 SMT / sourcing information

库存、价格与商城 availability 是 `point-in-time procurement evidence`，不是永久 Project Fact。Availability 使用 `Good / Limited / Unavailable / Unknown`；必要时记录 `checked date`，不默认长期保存具体库存数字。

### Technical evidence

Manufacturer official datasheet、reference manual、application note 与其他官方 documentation 是技术 qualification 的权威依据，用于核对：

- functionality、operating voltage/current
- Recommended Operating Conditions、Absolute Maximum Ratings 与 electrical characteristics
- thermal、pinout、state machine / control behavior
- required external components、typical application
- package drawing、Layout requirements 与 safety-critical parameters

Marketplace data cannot replace manufacturer datasheet / official documentation for critical technical qualification. 商品页的 listed package 也必须与 Manufacturer official package information 一致后才能完成技术确认。

## 选型流程

### 1. 明确需求和模块

从当前项目 `requirements.md` 和 `design_notes.md` 确认：

- 输入/输出电压
- 最大电流或负载边界
- 通信接口
- ADC 通道和输入范围
- MOSFET 负载类型和电流
- PCB 层数、尺寸和可焊接性
- 调试方式
- 成本、采购和封装约束

需求不完整时，标注“不确定项”，不要强行确定最终器件。

### 2. 识别第一轮关键器件与后置外围

优先识别会影响模块架构、外围参数、供电、散热、保护和 PCB Layout，或存在关键参数依赖与安全风险的器件，例如：

- MCU
- USB 转 UART 芯片
- 3.3V LDO / DC-DC
- USB-C 连接器
- 晶振
- MOSFET
- 关键保护器件
- 运放、ADC、参考电压源等模拟关键器件

这些示例不是固定 Stage 分类。普通不影响架构的阻容、LED、按键、排针、测试点和跳帽等，可等模块电路参数明确后再选；任何外围一旦影响 architecture、safety、critical parameter、Layout 或 thermal，应前移处理。

### 3. JLCPCB / LCSC-first 候选发现

先从公开的 JLCPCB/LCSC/JLCPCB Parts 信息发现约 2–4 个 realistic candidates，并记录搜索时点。AI/Codex 应使用当前环境实际具备的公开 Web/Search 能力；若不可用，则给用户输出：

- 搜索关键词
- 筛选条件
- 需要重点查看的参数
- 建议候选数量
- 需要返回的 C 编号、MPN、candidate 或商品页信息

先应用工程 Hard Requirements；不满足者不因库存好、价格低或 SMT 便利而进入有效候选。如果首选采购池没有合理结果，再扩大到 Manufacturer、Mouser、DigiKey 或其他适当渠道。

### 4. 建立候选记录

AI/Codex 根据公开搜索结果或用户提供的信息建立精简候选表，区分 procurement evidence 与 technical evidence，并标注：

- Availability：`Good / Limited / Unavailable / Unknown`
- Datasheet verified：是否已依据 Manufacturer official documentation 完成关键参数核对
- Decision：`Primary / Alternate / Conditional / Rejected`
- 尚未满足的 Hard Requirement、风险或待核对项

### 5. Manufacturer datasheet qualification

器件成为 `Primary` 或 `Alternate` 前，必须用 Manufacturer official documentation 核对：

- functionality、工作电压/电流与 Recommended Operating Conditions
- Absolute Maximum Ratings、electrical characteristics 与 safety-critical parameters
- 功耗、温升与 thermal limits
- pinout、state machine / control behavior
- required external components 与 typical application
- package drawing 与 PCB Layout requirements

资料不足时保留为 `Conditional` 或 `Rejected`，不得仅凭 marketplace data 完成关键技术 qualification。

### 6. Primary / Alternate 决策与采购前复核

综合 Hard Requirements、Manufacturer qualification、架构与风险影响、采购便利性形成 `Primary` 和 `Alternate`。只有确有条件约束或明确淘汰依据时才保留 `Conditional` / `Rejected`。

在真正 purchasing、ordering 或 PCBA BOM submission 前，对 Primary 与 Alternate 执行一次 lightweight availability recheck，更新 Availability，必要时记录 `checked date`。这不是新 Stage、Gate 或专门 approval；如果状态变为 `Limited`、`Unavailable` 或无法核对，则重新评估 Primary / Alternate，不把旧库存或价格记录当作当前事实。

## 输出格式

### 1. 候选器件记录表

| Module | Function | JLC C# | Manufacturer | MPN | Package | Availability | Key requirements | Datasheet verified | Decision | Notes |
|---|---|---|---|---|---|---|---|---|---|---|

`Availability` 统一使用 `Good / Limited / Unavailable / Unknown`；`Decision` 统一使用 `Primary / Alternate / Conditional / Rejected`。需要记录时，将 availability checked date 写入 `Notes`，不默认保存长期具体库存数字。

### 2. 关键参数比较表

| 模块 | 器件类别 | MPN | 参数 | 项目需求 | 器件规格 | 是否满足 | 备注 |
|---|---|---|---|---|---|---|---|

### 3. 选型风险表

| 编号 | 模块 | 器件 | 风险描述 | 风险等级 | 建议处理 |
|---|---|---|---|---|---|

### 4. 待核对 datasheet 项

| 模块 | 器件 | 需要核对的参数 | 原因 | 当前状态 |
|---|---|---|---|---|

### 5. 后置外围器件清单

| 模块 | 外围器件 | 后置原因 | 需要等待的关键参数 |
|---|---|---|---|

## 常见模块检查重点

### MCU

- 工作电压
- Flash / RAM
- GPIO 数量
- ADC 通道和分辨率
- UART / I2C / SPI 数量
- SWD 调试
- 时钟、复位、BOOT、去耦要求
- 封装和焊接难度

### USB-C 与 USB 转 UART

- USB-C 仅供电还是包含 USB2.0 数据
- CC 电阻配置
- VBUS 电压范围
- D+ / D- 连接关系
- UART 逻辑电平
- 驱动支持
- 封装焊接难度
- ESD/TVS 需求

### LDO / DC-DC

- 输入电压范围
- 输出电压
- 输出电流
- 压差或效率
- 静态电流
- 输入/输出电容要求
- EN / PG / FB 引脚
- 热耗散风险

### MOSFET

- N 沟道 / P 沟道
- Vds
- Id
- Rds(on)
- Vgs(th)
- Rds(on) 对应的测试 Vgs，尤其是 2.5V / 4.5V 条件
- MCU 3.3V GPIO 是否能可靠驱动
- 栅极电阻、下拉电阻
- 感性负载续流路径
- 封装散热能力

### ADC 输入保护

- 输入电压范围
- 分压比例
- 输入阻抗
- RC 滤波
- 钳位或 TVS 漏电
- STM32 ADC 采样时间
- 过压和误接风险

### 运放

- 供电电压范围与单电源适用性
- 输入共模范围和输出摆幅是否覆盖实际信号边界
- Gain-bandwidth、带宽、压摆率与稳定性要求
- 输入失调电压、输入偏置电流和噪声对误差预算的影响
- 容性负载、输出驱动、去耦和 Layout 要求
- 封装、散热、可焊接性与替代风险

### 独立 ADC 与参考电压

- 分辨率、采样率、输入范围和接口类型
- 参考电压来源、精度、温漂、噪声与去耦要求
- 输入阻抗、采样保持时间、驱动能力和前端稳定时间
- INL / DNL、offset、gain error、有效位数和噪声是否满足验收边界
- 供电、数字电平、时钟、数据吞吐与 MCU 资源是否匹配
- 官方 Layout、接地、参考与输入滤波要求

## 风险等级

- 高风险：可能损坏芯片、电源、电池，可能导致无法上电，或存在明显安全风险。
- 中风险：可能影响稳定性、精度、温升、寿命、调试难度或后续改版。
- 低风险：主要影响成本、封装、采购、文档一致性或可维护性。

## 禁止事项

- 不要直接照抄开源项目 BOM。
- 不要只给型号，不说明依据。
- 不要在没有 datasheet 依据时确认关键参数。
- 不要推荐采购困难、封装过难或资料不完整的器件作为第一版主选。
- 不要忽略替代料。
- 不要忽略电源、MOSFET、ADC、运放、参考电压等高风险模块。
- 不要把普通阻容、LED、排针、测试点、普通按键作为第一轮重点资料收集对象。
- 不要生成未经核对的最终 BOM。
- 不要把 JLCPCB/LCSC 或其他 marketplace data 当作关键技术 qualification authority。
- 不要为了形成固定数量或分类而制造低质量候选。
- 不要把 point-in-time 库存、价格或 availability 固化为永久 Project Fact。

## 本 Skill 的流程边界

本 Skill 不增加 EDA Library Acceptance、新 Gate、新 Stage、symbol approval workflow、footprint acceptance workflow、mandatory footprint documentation、supplier-specific Framework lifecycle 或 mandatory inventory database。

Package、pin / pad mapping、polarity、Pin 1 与 mechanical fit 继续在正常设计及 Schematic / PCB Review 生命周期中核对；候选选型记录不构成 EDA symbol 或 footprint acceptance。
