# PCB 辅助审查记录

> 文档状态：首轮 PCB 辅助审查记录完成，存在未关闭问题，未批准制造输出
> 当前阶段：阶段 11：PCB 审查问题修正与关闭
> 审查对象：STM32 DAQ Control Board Rev A
> 审查日期：2026-07-29
> 审查输入基线：当前本地工作树；初次审查对应 `main` HEAD `49462616d00875fa011b27f3276eecddc76c6d80`

## 1. 文档定位与事实边界

本轮是基于完整原理图 PDF、当前 BOM、顶层、底层和无铺铜 PCB 视图进行的 PCB 辅助审查。

- 未直接解析、打开或修改 `.PcbDoc`。
- 未运行或控制 Altium Designer。
- AI/Codex 未运行 Batch DRC，也未配置实际 PCB 规则。
- 未生成 Gerber、钻孔、贴片坐标、装配图或正式制造包。
- 视觉审查不能替代 Batch DRC、封装与焊盘映射、实际机械尺寸和制造文件检查。
- 图片只能支持可见布局事实，不能量化证明网络连接、间距、孔径、环宽、阻焊或规则命中情况；这些项目统一保留为待 EDA/人工核对。

用户提供的 DRC 摘要可作为本轮审查输入。其结果为 `Warnings=0`、`Rule Violations=0`，但所用规则参数与 [PCB 设计规则](pcb_design_rules.md) 的当前基线不一致，因此不能关闭制造门禁。DRC 的追溯要求和可接受记录方式见第 6 节。

## 2. 审查输入与版本一致性

### 2.1 硬件实现输入

| 输入 | 路径 | Git blob | 用途 |
| --- | --- | --- | --- |
| 原理图 PDF | [STM32_DAQ_Control_Board_Schematic.pdf](../hardware/outputs/schematic_pdf/STM32_DAQ_Control_Board_Schematic.pdf) | `600b20539e8e5461e105329a2daa77df38323a13` | 核对模块、位号、接口和网络意图 |
| BOM | [STM32_DAQ_Control_Board.xlsx](../hardware/outputs/bom/STM32_DAQ_Control_Board.xlsx) | `3eb4d0be6174fdbb1981c2f917ea44c8e2c6459d` | 核对器件集合、位号、数量和参数 |
| 顶层视图 | [顶层.png](../hardware/images/pcb/顶层.png) | `f5f4704908553e6b0eb1bd772a773b96269540b1` | 顶层布局、走线、铺铜和丝印 |
| 底层视图 | [底层.png](../hardware/images/pcb/底层.png) | `754d883c7296e6917b2364d24dad4a96678d7188` | 底层铺铜、换层和底面装配 |
| 无铺铜视图 | [无铺铜视图.png](../hardware/images/pcb/无铺铜视图.png) | `0146ceee386bc217830e386e9beb77742f1d32e3` | 走线、过孔、换层和密集区域 |

设计意图和规则依据：

- [requirements.md](../requirements.md)
- [design_notes.md](../design_notes.md)
- [pcb_design_rules.md](pcb_design_rules.md)
- [MCU 最小系统](module_design/01_mcu_minimum_system.md)
- [USB-C 供电与 AP2112](module_design/02_usb_c_power_ap2112.md)
- [USB 转 UART / CH340C](module_design/03_usb_uart_ch340c.md)
- [ADC 输入保护](module_design/04_adc_input_protection.md)
- [MOSFET 低边输出](module_design/05_mosfet_low_side_output.md)
- [接口、测试点与丝印](module_design/06_interfaces_testpoints.md)

项目文档用于确认设计意图和风险边界，不替代实际 PCB 实现证据。

### 2.2 一致性结论与限制

- 三张 PCB 图片的板框、安装孔、器件坐标、接口位置和主要走线相互对应，可判断为同一版布局的不同显示模式。
- 图片中可辨认的 `U1`、`X1`、`U6`、`U7`、`U8`、`Q1/Q2`、`D1-D5`、USB-C、SWD、SPI、I2C、UART2、两路 ADC 和两路 MOSFET 接口，与 PDF、BOM 的总体功能结构一致。
- Git blob 可追溯五个输入文件，但不能证明它们由完全相同的 `.PcbDoc` 保存状态一次性导出。
- 当前 DRC 摘要缺少完整版本和规则追溯信息。该限制不妨碍本轮视觉辅助审查，但阻断制造放行。

## 3. 总体结论

关键模块布局总体合理：MCU 最小系统集中，USB、ADC、MOSFET 和电源区域分区清楚，接口与测试点总体可访问；顶底层存在大面积铺铜和较多地过孔。

视觉上未发现明显短路、明显未布线飞线或严重布局失控；无铺铜视图中也未见明显反复换层或大电流网络长距离细线。该结论仅限视觉审查，不代表 PCB、DRC 或制造输出已经通过。

| 风险等级 | 数量 |
| --- | ---: |
| 高风险 | 2 |
| 中风险 | 4 |
| 低风险 | 2 |
| 合计 | 8 |

当前两个高风险门禁为：DRC 规则基线不一致、关键接口安全边界未完整落实。`PCB-002` USB-C 型号冲突和 `PCB-004` Shield 策略冲突已经关闭，不再计入未关闭风险统计。

**当前不允许生成正式制造文件或投产。**

## 4. 视觉审查结果

### 4.1 板框与机械

- 板框在三张图片中均为规则闭合的圆角矩形，未见异常折线；四角安装孔数量和分布对称，孔体内未见走线。
- USB-C 位于左侧板边且朝向板外；SPI、UART2、ADC、BOOT、SWD、I2C 和 MOSFET 接口均靠近板边。
- SW3 可从顶面操作，但开关高度、拨动范围、外壳开孔，以及 USB-C 与左下安装孔的机械间隙需 3D 或实物尺寸核对。
- 用户已在 Altium 中确认当前板框外接尺寸为 `59.563 mm × 60.000 mm`。尺寸子项已确认；圆角、四个安装孔的孔位/孔径、孔到板边/铜的间距，以及 SW3、USB-C 与安装孔的机械间隙仍需继续核对。

### 4.2 器件布局

- MCU、晶振、VDDA 和数字去耦集中在板中央，布局紧凑。
- USB-C、U6 ESD 和 U7 CH340C 位于左下同一区域；电源入口、SW3 和 U8 沿底边形成清楚的电源流向。
- 两路 ADC 位于上部并保持相似布局；两路 MOSFET 输出在左侧形成上下对称的局部区域。
- 接口、按键、LED 和测试点大多位于边缘或器件间空白区，未见明显遮挡或器件压入安装孔区域。

### 4.3 MCU、晶振与去耦

- `X1` 紧靠 U1 的 `OSC_IN/OSC_OUT` 一侧，`C3/C4` 就近放置。
- 晶振走线短、局部近似对称，视觉上未见晶振网络过孔，也未见强干扰走线穿过晶振区域。
- `C2/C5/C9`、`C1` 分布在 U1 相应电源侧附近；`R5/C7/C8` 集中在 VDDA/VSSA 附近。
- MCU 和晶振下方底层以大面积铺铜为主，未见明显贯穿式地分割。

### 4.4 USB-C、USB ESD 与 CH340C

- U6 紧邻 USB-C 数据引脚，USB_DP/USB_DM 主要限制在 USB-C、U6 和 U7 之间的小区域内。
- 两条数据线在 U6 附近有局部交叉/绕行，但总体路径短，未见明显多次换层或跨越 MCU、ADC、MOSFET 区。
- 本项目不建立 USB 差分对、不要求长度匹配且不声明 `90 Ω`；本轮也不据图片作阻抗结论。
- U7 的 `C12/C14/C13` 靠近芯片。USB Shield 当前策略已由用户结合 Altium 确认为 `SHIELD -> (R15 1MΩ || C18 1nF) -> GND`；R15 提供直流参考/泄放，C18 提供高频噪声回流，不替代专用 ESD 保护。
- USB-C 型号和 Shield 文档冲突已分别按 `PCB-002`、`PCB-004` 关闭；该关闭基于用户 Altium 确认、当前规格书及已有 PDF/BOM，不表示 AI/Codex 独立核对 `.PcbDoc`。

### 4.5 电源与 GND

- USB-C VBUS、F1、D5 和 SW3 位于同一底边区域；`+5V_SYS` 到 U8 的走线流向清楚。
- 主电源和负载走线视觉上明显宽于普通信号线。
- U8 的 C15 位于输入侧，C16/C17 位于输出侧并靠近 U8。
- 顶层和底层均有大面积铺铜，底层尤其连续；板边、MCU 和接口附近可见较多地过孔。
- 未见明显大面积孤立铜岛、极窄长铜颈或负载主走线穿越晶振、ADC 核心区。

### 4.6 ADC 模拟区域

- 两路 ADC 接口和前端器件分组清楚、布局相似，外部接口靠板边。
- `C10/C11`、`D3/D4` 和 TP_ADC1/2 位于靠近 MCU 的实际 ADC 节点一侧，测试点具备探测空间。
- ADC 走线未进入左侧 MOS_OUT/VLOAD、USB-C 或 SW3 入口区，未见负载主走线穿越前端。
- D3/D4 的 Pin/Pad mapping、TP_ADC1/2 网络对应关系仍需人工核对。

### 4.7 MOSFET 负载区域

- Q1/D1/H1 与 Q2/D2/H3 两路布局基本一致，MOSFET、续流二极管和负载接口形成紧凑局部区域。
- VLOAD_EXT、MOS_OUT 和 Q1/Q2 Drain 附近使用明显较宽走线，未见长距离绕行或反复换层。
- Gate 电阻、下拉电阻和 TP_GATE1/2 靠近 Q1/Q2；TP_OUT1/2 与 TP_GATE1/2 可直接探测。
- D1/D2 极性和 H1/H3 电压、共地边界仍需按 `PCB-003`、`PCB-008` 处理。

### 4.8 走线、过孔与铺铜

- 无铺铜视图未见明显飞线或视觉上明确的跨网短路；实际网络、间距仍以完整 DRC 为准。
- 大部分信号在顶层完成，底层仅见少量局部换层，未见明显不必要的往返换层。
- 走线以 45° 转角为主；LQFP48、USB-C 和 U6 周围虽较密集，但未见明显长细颈或走线穿越焊盘。
- 安装孔内未见铜或走线；孔到铜、孔到板边、环宽和孔径需由规则检查确认。

### 4.9 制造、装配、丝印与测试点

- 可见 SMD 器件主要位于顶层；底层未见 SMD 器件，可按单面 SMT 加通孔后焊方向评估。
- LQFP48、SOP-16、SOT-23、SOT-25 和 SMA 周围保留了基本返修空间；USB-C 细间距区和 U6 小封装更适合正规 SMT。
- 当前 BOM 缺少独立 PCB Footprint 列，不能据其完成封装和 SMT 物料映射。
- U1 Pin 1、D1/D2/D5 极性标记从图片中不够明确；SW3 高度和连接器机械空间仍待确认。
- SWD、SPI、UART2、I2C 和主要测试点总体可辨认、可访问；I2C `SDA` 疑似标成 `SCA`，UART2 未明确 MCU 视角。
- USB-C、ADC、MOSFET 和通信接口的安全边界未完整落实，详见 `PCB-003`。

## 5. 问题清单

### PCB-001：DRC 规则基线与项目规则不一致

- **模块**：全板规则 / 制造门禁
- **问题描述**：用户提供的摘要为 0 违规，但 Clearance 为 `6 mil`，低于项目基线 `0.20 mm（约 7.9 mil）`；默认信号 Width 和统一 `PWR` 规则也未体现负载、5V、3.3V、GND 的分级要求。摘要中的 `Direct Connect (All)` 与 GND Pad 默认 Relief Connect 的基线不明显一致。
- **风险等级**：高风险
- **证据**：用户提供的 DRC 摘要；[pcb_design_rules.md](pcb_design_rules.md) 第 3、4、11、13 节。
- **影响**：0 违规可能只代表当前规则集下无违规，不能证明项目批准的完整规则已满足。
- **建议修改**：核对实际规则的 Scope、优先级和数值，补齐必要检查；Repour 后运行完整 Batch DRC，并形成符合第 6.2 节要求的可追溯记录。
- **当前状态**：未关闭，阻断制造。

### PCB-002：USB-C 具体型号与设计文档冲突

- **模块**：USB-C / 机械封装
- **问题描述**：设计文档原记录 `TYPE-C 16PIN 2MD(073)`，当前 PDF/BOM 为 `TYPE-C-31-M-12`，存在型号冲突。
- **风险等级**：高风险
- **关闭依据**：用户在 Altium 中确认 Rev A 当前唯一 USB-C 为 `TYPE-C-31-M-12`、立创 `C165948`；当前规格书为 [C165948_USB连接器_TYPE-C-31-M-12_规格书_WJ310728.PDF](../references/datasheets/usb_c/C165948_USB连接器_TYPE-C-31-M-12_规格书_WJ310728.PDF)，且已有原理图 PDF/BOM 均记录 `TYPE-C-31-M-12`。设计文档已同步；旧 `TYPE-C 16PIN 2MD(073)` 因只适合约 `0.8mm` 板厚而标记为历史/已替代。
- **影响**：可能出现固定脚、焊盘、外壳尺寸或插口位置不匹配，导致无法装配。
- **结论限制**：关闭依据来自用户 Altium 确认、当前规格书及已有 PDF/BOM；AI/Codex 未解析或独立核对 `.PcbDoc`。
- **当前状态**：已关闭。

### PCB-003：关键接口安全边界未完整落实

- **模块**：USB、ADC、MOSFET、通信接口
- **问题描述**：当前图片未见完整的 USB-C `5V ONLY`、ADC `0-5V`、MOSFET `VLOAD 5-12V / COMMON GND` 和通信接口 `3.3V LOGIC` 提示；MOSFET 接口的 `512` 含义不清。
- **风险等级**：高风险
- **证据**：顶层和无铺铜图片；[接口、测试点与丝印](module_design/06_interfaces_testpoints.md) 第 9 节。
- **影响**：风险主要来自使用安全、接口误接和项目交付完整性，可能导致错误供电或接口损坏；不表示缺少某条丝印本身会造成 PCB 无法制造。
- **建议修改**：优先通过 PCB 丝印关闭；板上尽量保留关键电压和 GND。空间不足时，可用受版本控制、与硬件版本一致的接口图或使用说明补充，但不能省略安全边界。
- **当前状态**：未关闭，保持制造门禁。

### PCB-004：USB Shield 策略与当前实现证据冲突

- **模块**：USB Shield / ESD
- **问题描述**：设计文档原写 `SHIELD -> R15 0Ω -> GND`，与当前 PDF/BOM 的 `R15=1MΩ`、`C18=1nF` 冲突。
- **风险等级**：中风险
- **关闭依据**：用户结合 Altium 确认当前实现为 `SHIELD -> (R15 1MΩ || C18 1nF) -> GND`，并与已有原理图 PDF/BOM 一致；R15 提供直流参考/泄放，C18 提供高频噪声回流，该 RC 支路不替代专用 ESD 保护。相关设计文档已同步。
- **影响**：会造成 ESD/EMI 设计意图、装配值和维护文档不一致。
- **结论限制**：关闭依据来自用户 Altium 确认及已有 PDF/BOM；AI/Codex 未运行 Altium、未解析 `.PcbDoc`、未独立验证回流效果。
- **当前状态**：已关闭。

### PCB-005：板框尺寸、安装孔与机械间隙确认

- **模块**：板框 / 机械
- **问题描述**：首轮图片未带尺寸标注，板框尺寸、安装孔和关键器件机械间隙需要由 Altium 或机械尺寸证据确认。
- **风险等级**：中风险
- **尺寸子项依据**：用户在 Altium 中确认当前板框外接尺寸为 `59.563 mm × 60.000 mm`。
- **影响**：可能影响外壳、安装孔、拼板、装配报价和项目尺寸目标。
- **建议修改**：继续核对四个安装孔的孔位、孔径、禁布区、孔到板边/铜的间距，以及 SW3、USB-C 与安装孔的机械间隙；带尺寸机械图属于推荐证据。
- **当前状态**：尺寸子项已确认；安装孔和机械间隙子项未关闭，因此 `PCB-005` 整体未关闭。

### PCB-006：审查输入缺少完整同版追溯链

- **模块**：版本管理 / 审查证据
- **问题描述**：Git 可追溯五个输入文件，但缺少 `.PcbDoc` 版本、统一导出批次或修订号证明 PDF、BOM、PCB 图片和 DRC 来自完全相同保存状态。
- **风险等级**：中风险
- **证据**：本轮输入 Git blob 和用户提供的 DRC 摘要。
- **影响**：可能在错误版本上关闭问题，导致审查记录与制造源文件不一致。
- **建议修改**：后续记录对应 `.PcbDoc` 或 Git 版本、导出/运行日期和统一 Rev；DRC 按第 6.2 节记录。独立报告或截图推荐但不强制。
- **当前状态**：未关闭。

### PCB-007：BOM 缺少完整 PCB Footprint 和关键采购字段

- **模块**：BOM / 封装映射 / PCBA
- **问题描述**：当前 BOM 包含位号、数量和部分参数，但没有独立 PCB Footprint 列；多数制造商、制造商料号和供应商字段为空。
- **风险等级**：中风险
- **证据**：[STM32_DAQ_Control_Board.xlsx](../hardware/outputs/bom/STM32_DAQ_Control_Board.xlsx)。
- **影响**：无法仅凭 BOM 完成关键器件封装、焊盘映射、采购料号和 SMT 物料一致性核对。
- **建议修改**：制造前导出包含 Designator、Quantity、Comment/Value、Manufacturer Part Number、PCB Footprint 的 BOM；关键器件填写明确型号。
- **当前状态**：未关闭。

### PCB-008：关键极性和 Pin 1 标记不足以从图片确认

- **模块**：装配 / 丝印
- **问题描述**：U1 Pin 1、D1/D2 SS14 色带方向和 D5 TVS 极性标记在当前图片中不够明确。
- **风险等级**：中风险
- **证据**：顶层和无铺铜图片；BOM 和原理图中的器件类型。
- **影响**：增加贴装方向错误、返修和首板排查风险；二极管装反可能造成保护失效或负载短路。
- **建议修改**：核对 Top Overlay/Assembly 标记，确保 U1 Pin 1、二极管 K/色带端和连接器 Pin 1 可复核；装配图为推荐补充。
- **当前状态**：未关闭。

### PCB-009：I2C SDA 丝印疑似写成 SCA

- **模块**：I2C 接口
- **问题描述**：I2C 接口顶端信号丝印在图片中显示为 `SCA`，与 `SDA` 不一致。
- **风险等级**：低风险
- **证据**：顶层和无铺铜图片右下 I2C1 区。
- **影响**：降低接口可读性，可能造成接线困惑。
- **建议修改**：核对并改为 `SDA`，保留 `SCL / SDA / GND / 3V3`。
- **当前状态**：未关闭。

### PCB-010：UART2 TX/RX 未明确标注 MCU 视角

- **模块**：UART2 接口
- **问题描述**：H6 可见 `TX2 / RX2 / GND`，但板上未明确 TX/RX 从 MCU 视角命名。
- **风险等级**：低风险
- **证据**：顶层和无铺铜图片 H6 区；[接口、测试点与丝印](module_design/06_interfaces_testpoints.md) 第 5.4 节。
- **影响**：外接模块时可能把 TX 接 TX、RX 接 RX，增加调试时间。
- **建议修改**：空间允许时标为 `MCU_TX2 / MCU_RX2`，否则在受版本控制的接口说明中明确交叉连接关系。
- **当前状态**：未关闭。

## 6. DRC 与制造门禁

### 6.1 当前 DRC 记录

用户提供的摘要显示：

- Warnings：`0`
- Rule Violations Total：`0`
- Clearance、Short-Circuit、Un-Routed Net、Modified Polygon、Width、Power Plane Connect、Hole Size、Hole To Hole、Minimum Solder Mask Sliver、Silk To Solder Mask、Silk to Silk、Net Antennae、Height：均为 `0`

AI/Codex 未运行 Batch DRC。当前摘要可作为审查输入记录，但存在以下基线差异：

- Clearance 为 `6 mil`，项目基线为 `0.20 mm（约 7.9 mil）`。
- Width 摘要未体现 Load、5V、3.3V、GND 的分级 Scope。
- `Direct Connect (All)` 与 GND Pad 默认 Relief Connect 的 Polygon Connect 基线不明显一致。
- 摘要未体现 Routing Via Style、Minimum Annular Ring、Board Outline Clearance、Layer Pairs 等最终检查项。

因此当前 0 违规结果不能关闭制造门禁。

### 6.2 关闭 DRC 门禁所需记录

关闭门禁需要可追溯的完整 DRC 结果记录，至少包含：

- 对应 `.PcbDoc` 或 Git 版本；
- 运行日期；
- 使用的规则基线；
- Warnings 和 Rule Violations 总数；
- 关键检查类别；
- 用户确认完整 Batch DRC 已运行，所有问题已解决或有明确、合理的豁免。

记录可保存在对话、审查文档或独立输出中。导出 DRC 报告、规则截图或结果截图属于推荐做法，不是默认强制仓库输入。

### 6.3 门禁摘要

| 门禁类别      | 对应问题                            | 当前状态 |
| --------- | ------------------------------- | ---- |
| 必须关闭后才能制造 | PCB-001、PCB-003                 | 未关闭  |
| 制造前必须确认   | PCB-005、PCB-006、PCB-007、PCB-008 | 未关闭  |
| 建议同步修正    | PCB-009、PCB-010                 | 未关闭  |
| 已关闭        | PCB-002、PCB-004                 | 已关闭  |

当前没有批准的 DRC 规则豁免。Rev A 不建立 USB Differential Pair、不声明 `90 Ω`、不要求长度匹配，是设计基线，不是 Clearance、Width 或制造规则豁免。

**制造结论：否。当前不得描述为“PCB 已通过”或“可以投产”，也不得生成正式 Gerber、钻孔、贴片坐标或制造包。**

## 7. 下一步动作

1. 完善 USB、ADC、MOSFET 和通信接口安全边界；修正 `SCA`，明确 UART2 视角。
2. 在已确认 `59.563 mm × 60.000 mm` 板框外接尺寸的基础上，继续核对四个安装孔、SW3、USB-C 和板边的机械间隙。
3. 按 [pcb_design_rules.md](pcb_design_rules.md) 核对实际规则，Repour 后由用户运行完整 Batch DRC，并按第 6.2 节记录结果。
4. 导出包含 PCB Footprint 的 BOM，完成人工封装、Pin/Pad mapping、极性和方向核对。
5. 更新必要的 PCB 审查图和问题状态。制造门禁关闭前不生成 Gerber、钻孔、坐标或制造包，不推进到阶段 12。
