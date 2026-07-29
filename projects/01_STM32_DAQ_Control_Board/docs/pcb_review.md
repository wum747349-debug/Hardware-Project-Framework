# PCB 辅助审查记录

> 文档状态：首轮正式辅助审查完成，存在未关闭问题，未批准制造输出
> 审查对象：STM32 DAQ Control Board Rev A
> 审查日期：2026-07-29
> 本地分支：`main`
> 审查时 HEAD：`49462616d00875fa011b27f3276eecddc76c6d80`

## 1. 文档定位和事实边界

本轮是基于完整原理图 PDF、当前 BOM、顶层/底层/无铺铜 PCB 图片及项目设计文档进行的 PCB 辅助审查。

- 未直接解析、打开或修改 `.PcbDoc`。
- 未运行或控制 Altium Designer。
- 未由 AI 运行 Batch DRC。
- 未生成 Gerber、钻孔、贴片坐标、装配图或正式制造包。
- 图片审查不能替代 Batch DRC、封装与焊盘映射核对、实际板框尺寸核对、3D 机械检查和制造文件检查。
- 本文只把图片中能够可靠辨认的内容写成事实；无法由图片证明的网络连接、间距、孔径、环宽和规则命中情况均保留为待 EDA 核对项。

用户在任务中补充了一份最新 DRC 文本摘要，其结果显示 `Warnings=0`、`Rule Violations=0`。该摘要不是 AI 运行所得，也不是仓库内可追溯的报告文件；其规则参数与当前 [PCB 设计规则](pcb_design_rules.md) 存在差异，因此不能单独作为按项目规则基线通过 Batch DRC 的证据。

## 2. 审查输入

### 2.1 硬件实现输入

| 输入 | 路径 | Git blob | 本轮用途 |
| --- | --- | --- | --- |
| 完整原理图 PDF | [STM32_DAQ_Control_Board_Schematic.pdf](../hardware/outputs/schematic_pdf/STM32_DAQ_Control_Board_Schematic.pdf) | `600b20539e8e5461e105329a2daa77df38323a13` | 核对模块、位号、接口、网络意图和关键器件 |
| BOM | [STM32_DAQ_Control_Board.xlsx](../hardware/outputs/bom/STM32_DAQ_Control_Board.xlsx) | `3eb4d0be6174fdbb1981c2f917ea44c8e2c6459d` | 核对器件集合、位号、数量和参数 |
| 顶层视图 | [顶层.png](../hardware/images/pcb/顶层.png) | `f5f4704908553e6b0eb1bd772a773b96269540b1` | 顶层器件、走线、铺铜、丝印和板框视觉检查 |
| 底层视图 | [底层.png](../hardware/images/pcb/底层.png) | `754d883c7296e6917b2364d24dad4a96678d7188` | 底层铺铜、换层、回流和底面装配视觉检查 |
| 无铺铜视图 | [无铺铜视图.png](../hardware/images/pcb/无铺铜视图.png) | `0146ceee386bc217830e386e9beb77742f1d32e3` | 走线、过孔、换层、细颈和密集区域重点检查 |

上述五个本地二进制文件已逐项核对，内容与审查时 `origin/main` 对应 blob 一致。三张图片分别为 `1277×1253`、`1259×1258` 和 `1247×1254` 像素。

### 2.2 设计意图和规则输入

- [项目 README](../README.md)
- [requirements.md](../requirements.md)
- [design_notes.md](../design_notes.md)
- [pcb_design_rules.md](pcb_design_rules.md)
- [MCU 最小系统](module_design/01_mcu_minimum_system.md)
- [USB-C 供电与 AP2112](module_design/02_usb_c_power_ap2112.md)
- [USB 转 UART / CH340C](module_design/03_usb_uart_ch340c.md)
- [ADC 输入保护](module_design/04_adc_input_protection.md)
- [MOSFET 低边输出](module_design/05_mosfet_low_side_output.md)
- [接口、测试点与丝印](module_design/06_interfaces_testpoints.md)

项目文档只用于确认设计意图和风险边界，不替代实际 PCB 实现证据。

## 3. 审查版本和一致性

### 3.1 Git 基线

- 本轮按用户后续指示，以当前本地工作树文件为事实源。
- 审查时本地 `HEAD` 与 `origin/main` 均指向 `49462616d00875fa011b27f3276eecddc76c6d80`。
- 本地工作树存在其他未提交修改；本轮只修改本文档，不把其他修改纳入本次提交。
- 本地 `pcb_design_rules.md` 相对 HEAD 的差异为表格排版变化，规则数值和含义未改变。

### 3.2 三张 PCB 图片

三张图片的板框形状、四角安装孔、器件坐标、接口位置和主要走线位置能够对应，未见明显属于不同 PCB 版本的证据，可判断为同一版布局的不同显示模式。

图片中可辨认的主要器件和接口包括 `U1`、`X1`、`U6`、`U7`、`U8`、`Q1/Q2`、`D1/D2`、`D3/D4`、`D5`、USB-C、SWD、SPI、I2C、UART2、两路 ADC 和两路 MOSFET 接口，与 PDF、BOM 和模块文档的总体功能结构一致。

### 3.3 版本追溯限制

Git 能证明五个审查输入同时存在于同一提交，但不能证明它们由完全相同的 `.PcbDoc` 保存状态一次性导出。图片本身没有 `.PcbDoc` 修订号、导出时间或源文件哈希；用户提供的 DRC 摘要也没有报告文件、运行时间、板文件路径或源文件哈希。因此：

- PDF、BOM、PCB 图片与 DRC 的完全同版关系尚未闭环。
- 不得自行假设图片就是最新 `.PcbDoc` 的完整、唯一实现状态。
- 该限制不妨碍本轮视觉辅助审查，但阻断正式制造批准。

## 4. 总体审查结论

三张 PCB 图片清晰且内容完整，足以完成首轮视觉辅助审查。布局总体按功能分区：左侧为 MOSFET 输出和 USB/CH340C，中央为 MCU、晶振和电源开关，顶部为 ADC/通信接口，右侧为 BOOT、SWD、I2C 和电源区。两层 GND 铺铜覆盖范围大，地过孔分布较多；关键器件位置总体符合信号流向。

视觉审查未发现明显短路、明显未布线飞线、晶振远离 MCU、ESD 远离接口、MOSFET 远离负载接口等高风险布局失控现象。无铺铜视图中未见明显不必要的反复换层或大电流网络长距离细线。

本轮共记录：

| 风险等级 | 数量 |
| --- | ---: |
| 高风险 | 3 |
| 中风险 | 5 |
| 低风险 | 2 |
| 合计 | 10 |

高风险项并非已确认的 PCB 短路，而是会阻断制造或可能导致接口误用的未闭环问题：DRC 规则基线不一致、USB-C 具体型号与设计文档冲突、关键安全丝印缺失或含义不清。

**结论：当前不允许生成正式制造文件。** 完成问题清单中的高风险项、按统一规则运行并保存可追溯 Batch DRC、完成封装/焊盘映射和机械尺寸人工核对后，才能进入制造输出。

## 5. 板框与机械检查

- 板框在三张图片中均表现为规则闭合的矩形，四角圆角一致，未见异常折线或明显断口。
- 四角各有一个安装孔，数量和分布对称；孔周围未见走线穿过孔体，铺铜在孔周围形成明显退让区域。
- USB-C 位于左侧板边，插拔方向朝向板外，具备正常接线条件。
- SPI、UART2、ADC、BOOT、SWD、I2C 和 MOSFET 排针均靠近板边，方向适合探测和接线。
- SW3 位于底边附近，顶面可操作；但开关实际高度、拨动空间、外壳开孔和与固定件的干涉无法由二维图片证明。
- 图片中的板框外观接近方形，与 `70 mm × 50 mm` 目标的 `1.4:1` 长宽比不明显一致。截图可能经过裁切，但常规等比例截图不会改变板框比例，因此 exact size 需在 Altium Board Information 或带尺寸机械图中人工确认。
- USB-C、安装孔、板边铜和丝印的精确板边间距无法由图片量化，待 Board Outline Clearance DRC 和机械尺寸核对。

## 6. 器件布局与分区

- MCU 最小系统集中在板中央，晶振、模拟电源去耦和数字去耦围绕 U1 放置，整体紧凑。
- USB-C、U6 ESD 和 U7 CH340C 位于左下角同一区域，USB 数据路径没有跨越整板。
- `VBUS_RAW -> F1 -> D5/SW3 -> +5V_SYS -> U8` 的器件位置从左下入口向底部中央、右下 LDO 区展开，电源流向清楚。
- 两路 ADC 位于上部 MCU 两侧，布局相似，外部接口靠板边，保护与滤波器件靠近 MCU。
- 两路 MOSFET 输出位于左侧板边，Q1/Q2、D1/D2、H1/H3 和测试点形成上下对称的局部区域。
- SWD、BOOT、按键、LED 和测试点大多位于边缘或器件间空白区，具备探测和操作空间。
- 未见器件压在安装孔禁布区内；USB-C 与左下安装孔较近，螺钉头、垫片和 USB 插头外壳的实际机械间隙仍需 3D 或实物尺寸核对。

## 7. MCU、晶振和去耦

- `X1` 位于 U1 上侧并紧靠 `OSC_IN/OSC_OUT` 侧，`C3/C4` 位于 X1 上方。
- 晶振两条走线短、局部近似对称，图片中未见晶振网络过孔。
- 晶振区远离左侧 MOSFET 输出、底部电源开关和 USB-C 入口，未见强干扰走线穿过晶振本体下方。
- `C2/C5/C9` 分布在 U1 对应边附近，`C1` 位于 U1 右下附近，符合就近去耦的总体意图。
- `R5/C7/C8` 集中在 U1 左上侧 VDDA/VSSA 附近，回路范围较小。
- 底层视图显示 MCU 和晶振区域下方以连续大面积铺铜为主，仅有少量换层走线，没有明显贯穿式地分割。
- 图片不能证明各电容焊盘实际网络、地回流长度或每个电源脚的连接顺序；这些内容仍需 `.PcbDoc` 网络高亮和人工核对。

## 8. USB-C、USB ESD 和 CH340C

- U6 紧邻 USB-C 数据引脚区域，位置符合 ESD 器件靠近接口的要求。
- USB_DP/USB_DM 主要限制在 USB-C、U6 和 U7 之间的小区域内；无铺铜图未见数据线长距离绕行或跨越 MCU/ADC/MOSFET 区域。
- 两条数据线在 U6 附近存在局部交叉/绕行关系，没有保持严格并行，但路径总体短，未见明显多次换层。
- 本项目未建立差分对、长度匹配或 `90 Ω` 声明，本轮也不据图片声称已经实现阻抗控制。
- 底层 USB 区域为大面积铺铜，视觉上未见明显地分割；U6 GND 实际是否使用最短路径和就近地过孔仍需网络高亮确认。
- U7 的 `C12/C14/C13` 位于芯片附近，局部去耦布局合理。
- USB-C 具体型号在设计文档与 PDF/BOM 中不一致，详见 `PCB-002`。
- Shield 连接设计文档与 PDF/BOM/PCB 器件集合不一致，详见 `PCB-004`。

## 9. 电源与 GND

- USB-C VBUS 到 F1 的入口段较短；F1、D5 和 SW3 位于同一底边区域。
- F1 到 SW3、SW3 到 `+5V_SYS`、`+5V_SYS` 到 U8 的主电源走线视觉上明显宽于普通信号线。
- D5 位于 F1/SW3 附近，保护支路没有跨越整板；D5 到 GND 的实际回路阻抗需结合铺铜网络和地过孔确认。
- U8 的 C15 位于输入侧，C16/C17 位于输出侧并靠近 U8，符合 AP2112 输入/输出电容就近放置要求。
- `3.3V` 主干使用较宽走线从 U8 向 MCU/接口区域分配；VDDA 区使用 R5 和局部 C7/C8。
- 顶层和底层均显示大面积铺铜，底层尤其连续；地过孔分布于板边、MCU 周围、接口和空白区域。
- 未见明显大面积孤立铜岛、极窄长铜颈或整板地分割。
- MOSFET 模块靠左边，USB/ADC/MCU 位于其他区域，视觉上没有负载主走线穿过晶振或 ADC 核心区。
- 图片颜色不能独立证明所有铺铜均为 GND，也不能证明不存在孤立铜岛；需在 Altium 中 Repour 后检查 Polygon、网络高亮和 DRC。

## 10. ADC 模拟区域

- 两路 ADC 接口位于上边缘，通道结构左右相似。
- R8/R12/R10/C10/D3/TP_ADC1 与 R9/R13/R11/C11/D4/TP_ADC2 分组清楚。
- `C10/C11`、`D3/D4` 和测试点位于靠近 MCU 的实际 ADC 节点一侧，符合先分压、再限流/滤波/钳位的布局意图。
- TP_ADC1、TP_ADC2 周围有足够探针落点空间，标识可辨认。
- ADC 走线未进入左侧 MOS_OUT/VLOAD 区，也未进入 USB-C 和 SW3 入口区域。
- 两通道之间存在共用 VDDA/GND 回路，但未见数字总线或负载主走线直接穿越 ADC 前端。
- 图片不能证明 D3/D4 引脚映射、TP_ADC1/2 网络对应关系和回流网络，仍需 `.PcbDoc` 网络高亮或封装映射人工核对。

## 11. MOSFET 负载区域

- Q1/D1/H1 与 Q2/D2/H3 两路布局基本一致，器件和负载接口之间距离短。
- VLOAD_EXT、MOS_OUT 与 Q1/Q2 Drain 附近使用明显宽于普通信号的走线。
- D1/D2 紧邻对应 VLOAD/MOS_OUT，形成局部续流路径。
- Q1/Q2 靠近接口 GND PTH，Source 回流视觉上较短；PTH GND 也为上下层地连接提供路径。
- Gate 电阻、下拉电阻和 TP_GATE1/2 靠近 Q1/Q2，Gate 线未长距离平行贴靠 MOS_OUT/VLOAD。
- TP_OUT1/2 和 TP_GATE1/2 可直接探测。
- 未见负载线长距离绕行、反复换层或进入 MCU/ADC/USB 核心区。
- D1/D2 极性丝印和 H1/H3 电压边界不够明确，详见 `PCB-003`、`PCB-008`。

## 12. 过孔、走线和铺铜

- 无铺铜图未见明显未连接飞线；但图片不能代替 Un-Routed Net 检查。
- 未见视觉上明确的跨网短路；焊盘间距、线间距和实际网络必须由 DRC 证明。
- 大部分信号在顶层完成，底层只见少量局部换层，未出现明显多次往返换层。
- 电源、负载线宽与普通信号线之间存在清楚的视觉优先级。
- 走线以 45° 转角为主，未见明显锐角回折。
- LQFP48、USB-C 和 U6 周围走线密集，但未见明显焊盘出口被其他走线穿越或极窄长细颈。
- 安装孔孔体内未见铜或走线；孔到铜、孔到板边、环宽和孔径只能待 DRC/机械核对。
- 用户 DRC 摘要报告 `Un-Routed Net=0`、`Short-Circuit=0`，但由于规则和版本追溯问题，本轮不把图片或该摘要写成最终通过证据。

## 13. 可制造性检查

- U1 LQFP48 扇出有序，未见严重走线拥堵。
- USB-C 0.5 mm pitch 区域和 U6 小封装区域较密集，适合由正规 SMT 工艺装配，不适合作为优先手焊区域。
- U7 SOP-16、U8 SOT-25、Q1/Q2/D3/D4 SOT-23、D1/D2 SMA 周围均保留了基本返修空间。
- 所有可见 SMD 器件位于顶层；底层视图未见底面 SMD 器件，可按单面 SMT 加通孔后焊的方向评估。
- USB-C 固定焊脚、LQFP 阻焊桥、U6 焊盘、安装孔属性、板边间距、环宽和阻焊扩展不能由图片量化。
- 当前 BOM 不含明确 PCB Footprint 列，不能据其完成封装映射和 SMT 物料映射。
- 当前 DRC 摘要规则与项目规则基线不一致，不能作为制造规则通过证明。

## 14. 可装配性检查

- 排针、USB-C、SW3 和四个安装孔均位于板边或大空白区，未见器件本体明显互相遮挡。
- SW3 是较高的大型通孔器件，其高度、拨动范围和外壳干涉必须在 3D/实物尺寸阶段核对。
- USB-C 与左下安装孔的螺钉头/垫片间隙待机械核对。
- U1 Pin 1、D1/D2/D5 极性标记从当前图片中不够清楚，装配复核风险未关闭。
- 未提供贴片坐标和装配图，本轮不检查器件旋转角、贴片原点或机器可识别方向。

## 15. 丝印、接口与测试点

### 15.1 已确认较清楚的标识

- SWD 外侧可见 `GND / NRST / SWCLK / SWDIO / 3.3V` 顺序。
- SPI 可见 `MOSI / MISO / SCK / CS / GND`。
- UART2 可见 `TX2 / RX2 / GND`。
- I2C 可见 `3.3V / GND / SCL` 及疑似 `SCA`。
- H5 可见 `3.3`、GND、GPIO 名和 `5VOUT`；`5VOUT` 有助于表达输出属性。
- TP_VBUS1、5V_SYS、3V3、TP_GND1、TP_ADC1/2、TP_GATE1/2、TP_OUT1/2 标识大多可辨认且具备探针空间。

### 15.2 未闭环的安全边界

- USB-C 附近未见明确 `5V ONLY`。
- ADC 接口附近未见明确 `0-5V`。
- MOSFET 接口只见含义不完整的 `512`、`OUTx`、`GND`，未清楚表达 `VLOAD 5-12V` 和 `COMMON GND REQUIRED`。
- UART/I2C/SPI 附近未统一标明 `3.3V LOGIC`。
- TX2/RX2 未在板上明确标注“MCU 视角”。
- I2C `SDA` 位置的丝印疑似写成 `SCA`。
- `+5V_SYS` 在 H5 标为 `5VOUT`，方向基本清楚；仍建议在接口文档中继续明确禁止外部反灌。

## 16. 问题清单

### PCB-001：DRC 规则基线与项目规则不一致

- **模块**：全板规则 / 制造门禁
- **问题描述**：用户提供的 DRC 摘要显示 0 违规，但其中 Clearance 为 `6 mil`，而项目规则要求 `0.20 mm（约 7.9 mil）`；默认信号 Width 为 `Min 5 mil / Preferred 6 mil`，项目规则为 `0.15/0.20 mm`；摘要仅显示统一 `PWR` 规则，未体现负载、5V、3.3V、GND 分级规则。摘要也未显示 Routing Via Style、Minimum Annular Ring、Board Outline Clearance 和 Layer Pairs。
- **风险等级**：高风险
- **图片或文档证据**：用户提供的 DRC 文本；[pcb_design_rules.md](pcb_design_rules.md) 第 3-6、10、13 节。
- **影响**：即使当前报告为 0，也可能没有按项目批准的间距、线宽、环宽和板边规则检查，无法作为制造批准依据。
- **建议修改**：在 Altium 中核对规则 Scope、优先级和数值，补齐缺少的规则；Repour 后运行完整 Batch DRC，保存带运行时间、规则详情和源 `.PcbDoc` 版本的报告。
- **当前状态**：未关闭，阻断制造。

### PCB-002：USB-C 具体型号与设计文档冲突

- **模块**：USB-C / 机械封装
- **问题描述**：[design_notes.md](../design_notes.md) 和 [USB-C 电源模块文档](module_design/02_usb_c_power_ap2112.md) 记录 `TYPE-C 16PIN 2MD(073)`，当前 PDF 和 BOM 则为 `TYPE-C-31-M-12`。图片只能看到 USBC1 封装，不能证明它对应哪一个实际采购型号。
- **风险等级**：高风险
- **图片或文档证据**：原理图 PDF 的 USBC1 型号、BOM 第 45 行、USB 区 PCB 图片及上述设计文档。
- **影响**：若采购型号与 PCB 封装不一致，可能出现固定脚、0.5 mm 焊盘、外壳尺寸或插口位置不匹配，导致无法装配。
- **建议修改**：确定唯一采购型号，按 datasheet 人工核对原理图库引脚、PCB 焊盘、固定脚、插口伸出量和封装方向；随后同步 BOM 和设计文档。
- **当前状态**：未关闭，阻断制造。

### PCB-003：关键接口安全丝印缺失或含义不清

- **模块**：USB、ADC、MOSFET、通信接口
- **问题描述**：当前图片未见 USB-C `5V ONLY`、ADC `0-5V`、MOSFET `VLOAD 5-12V / COMMON GND REQUIRED`、通信接口 `3.3V LOGIC` 等完整边界；MOSFET 接口的 `512` 表达不清。
- **风险等级**：高风险
- **图片或文档证据**：顶层和无铺铜图片；[接口、测试点与丝印](module_design/06_interfaces_testpoints.md) 第 9 节。
- **影响**：可能导致 USB 高压误接、ADC 过压、MOSFET 负载接错或 5V 逻辑直连，存在接口损坏和错误供电风险。
- **建议修改**：在接口旁增加简短、不会被器件遮挡的边界丝印；空间不足时至少保留电压和 GND，并在装配/使用说明中重复。
- **当前状态**：未关闭，阻断制造。

### PCB-004：USB Shield 连接设计意图与当前实现证据冲突

- **模块**：USB Shield / ESD
- **问题描述**：设计文档写 `SHIELD -> R15 0Ω -> GND`，而当前 PDF/BOM 显示 `R15=1MΩ`、`C18=1nF`，PCB 图片也同时存在 R15/C18。
- **风险等级**：中风险
- **图片或文档证据**：原理图 PDF USB-C 区、BOM R15/C18、USB PCB 局部、[USB-C 电源模块文档](module_design/02_usb_c_power_ap2112.md) 第 3 节。
- **影响**：版本意图不清会影响 ESD 回流、EMI 调试和后续维护，且可能导致文档与装配值不一致。
- **建议修改**：确认实际采用的 Shield 接地策略和器件值，回到相应器件资料及板级 EMI/ESD 目标核对，并统一原理图、BOM 和设计说明。
- **当前状态**：未关闭。

### PCB-005：板框比例与约 70 mm × 50 mm 目标不明显一致

- **模块**：板框 / 机械
- **问题描述**：三张截图中的板框均接近方形，视觉比例与 `70×50 mm` 的 1.4:1 目标不明显一致；图片没有尺寸标注。
- **风险等级**：中风险
- **图片或文档证据**：三张 PCB 图片；[requirements.md](../requirements.md) PCB 尺寸要求；[pcb_design_rules.md](pcb_design_rules.md) 单位约定。
- **影响**：可能影响外壳、安装孔、拼板、装配报价和项目尺寸目标。
- **建议修改**：在 Altium Board Information 或机械层尺寸中确认实际 X/Y 尺寸、圆角、孔位和孔径，导出带尺寸机械图并记录最终尺寸决定。
- **当前状态**：未关闭。

### PCB-006：PDF、BOM、PCB 图片和 DRC 缺少同版追溯链

- **模块**：版本管理 / 审查证据
- **问题描述**：五个文件在同一 Git 提交内，但没有 `.PcbDoc` 源文件哈希、导出批次或修订号证明它们来自完全相同保存状态；DRC 摘要也不可追溯。
- **风险等级**：中风险
- **图片或文档证据**：本轮输入文件元数据与 Git blob；用户提供的纯文本 DRC 摘要。
- **影响**：可能出现审查图片与实际制造源文件不同版，导致问题在错误版本上被关闭。
- **建议修改**：下轮导出时记录 `.PcbDoc` 文件哈希/提交 SHA、导出日期和统一 Rev；将 DRC 报告与图片、PDF、BOM放入同一审查批次。
- **当前状态**：未关闭。

### PCB-007：BOM 缺少完整 PCB Footprint 和关键采购字段

- **模块**：BOM / 封装映射 / PCBA
- **问题描述**：当前 BOM 为 A1:L46，包含位号、数量和部分参数，但没有独立 PCB Footprint 列；大多数 Manufacturer、Manufacturer Part Number 和 Supplier 字段为空。
- **风险等级**：中风险
- **图片或文档证据**：[STM32_DAQ_Control_Board.xlsx](../hardware/outputs/bom/STM32_DAQ_Control_Board.xlsx)。
- **影响**：无法仅凭 BOM 完成关键器件封装、焊盘映射、采购料号和 SMT 物料一致性核对。
- **建议修改**：制造前导出包含 Designator、Quantity、Comment/Value、Manufacturer Part Number、PCB Footprint 的当前 BOM；关键器件填入明确型号，通用阻容可保持参数化描述。
- **当前状态**：未关闭。

### PCB-008：关键极性和 Pin 1 丝印不足以从图片确认

- **模块**：装配 / 丝印
- **问题描述**：U1 Pin 1、D1/D2 SS14 色带方向和 D5 TVS 极性标记在当前图片中不够明确；无法据图确认装配人员能快速复核方向。
- **风险等级**：中风险
- **图片或文档证据**：顶层和无铺铜图片；BOM 和原理图中的器件类型。
- **影响**：可能增加贴装方向错误、返修和首板排查成本；二极管装反可能造成保护失效或负载短路风险。
- **建议修改**：检查 Top Overlay/Assembly 标记，确保 U1 Pin 1 点、二极管 K/色带端和连接器 Pin 1 在装配后仍可见；在装配图中明确方向。
- **当前状态**：未关闭。

### PCB-009：I2C SDA 丝印疑似写成 SCA

- **模块**：I2C 接口
- **问题描述**：I2C 接口顶端信号丝印在图片中显示为 `SCA`，与应有的 `SDA` 不一致。
- **风险等级**：低风险
- **图片或文档证据**：顶层和无铺铜图片右下 I2C1 区。
- **影响**：降低接口可读性，可能造成接线困惑。
- **建议修改**：核对并改为 `SDA`，同时保留 `SCL / SDA / GND / 3V3`。
- **当前状态**：未关闭。

### PCB-010：UART2 TX/RX 未明确标注 MCU 视角

- **模块**：UART2 接口
- **问题描述**：H6 可见 `TX2 / RX2 / GND`，但板上未明确说明 TX/RX 从 MCU 视角命名。
- **风险等级**：低风险
- **图片或文档证据**：顶层和无铺铜图片 H6 区；[接口、测试点与丝印](module_design/06_interfaces_testpoints.md) 第 5.4 节。
- **影响**：外接模块时可能把 TX 接 TX、RX 接 RX，增加调试时间。
- **建议修改**：空间允许时标为 `MCU_TX2 / MCU_RX2`，否则在接口说明中明确“TX2 接外部 RX，RX2 接外部 TX”。
- **当前状态**：未关闭。

## 17. DRC 状态

### 17.1 用户提供的最新摘要

用户提供的文本显示：

- Warnings：`0`
- Clearance、Short-Circuit、Un-Routed Net、Modified Polygon、Width、Power Plane Connect、Hole Size、Hole To Hole、Minimum Solder Mask Sliver、Silk To Solder Mask、Silk to Silk、Net Antennae、Height 等项目：均为 `0`
- Rule Violations Total：`0`

### 17.2 本轮结论

- 本轮 AI **未运行 Batch DRC**。
- 该摘要可以记录为“用户提供的当前 DRC 结果为 0”，但不能写成 AI 已验证 DRC 通过。
- Clearance `6 mil` 低于项目规则 `0.20 mm（约 7.9 mil）`。
- Width 摘要未体现项目规则中 Load、5V、3.3V、GND 的分级 Scope。
- Power Plane Connect 摘要显示 `Direct Connect (All)`，与项目 GND Pad 默认 Relief Connect 的设计意图不明显一致。
- 摘要未显示 Routing Via Style、Minimum Annular Ring、Board Outline Clearance、Layer Pairs。
- 摘要没有报告文件、运行时间、`.PcbDoc` 版本或规则导出，因此版本追溯未闭环。

因此当前状态为：**已有用户提供的 0 违规摘要，但尚未获得按本项目完整规则基线、可追溯到当前 `.PcbDoc` 的 Batch DRC 通过证据。**

## 18. 未关闭问题

| 编号 | 风险 | 当前门禁 |
| --- | --- | --- |
| PCB-001 | 高 | 必须关闭后才能制造 |
| PCB-002 | 高 | 必须关闭后才能制造 |
| PCB-003 | 高 | 必须关闭后才能制造 |
| PCB-004 | 中 | 应在设计文档同步和 ESD 策略确认后关闭 |
| PCB-005 | 中 | 必须在制造尺寸确认前关闭 |
| PCB-006 | 中 | 必须建立制造批次追溯 |
| PCB-007 | 中 | 必须在 PCBA/BOM 输出前关闭 |
| PCB-008 | 中 | 必须在装配文件审核前关闭 |
| PCB-009 | 低 | 建议下版丝印修正 |
| PCB-010 | 低 | 建议下版丝印或使用说明修正 |

## 19. 规则豁免

- 当前没有批准的 DRC 规则豁免。
- Rev A 不建立 USB Differential Pair、不声明 `90 Ω`、不要求长度匹配，是当前设计基线，不是对 Clearance、Width 或制造规则的豁免。
- USB-C 结构件靠板边属于预期机械位置，但不得据此全局取消 Board Outline Clearance；如确需局部例外，应记录具体对象、理由和人工核对结果。
- 在完整 Batch DRC 结果出来前，不创建“视觉看起来没问题”的临时豁免。

## 20. 是否允许生成制造文件

**否。**

当前不得把项目描述为“PCB 已通过”或“可以投产”，也不得基于本文生成正式 Gerber、钻孔、贴片坐标或制造包。

进入制造输出前至少需要：

1. 关闭 PCB-001、PCB-002、PCB-003。
2. 确认实际板框尺寸、安装孔和 USB-C 机械位置。
3. 完成关键器件封装、Pin/Pad mapping、极性和旋转角人工核对。
4. 按统一规则 Repour 并运行完整 Batch DRC，保存可追溯报告。
5. 输出包含 PCB Footprint 和关键采购型号的当前 BOM。
6. 修正关键接口和装配方向丝印。
7. 对实际 Gerber、钻孔、阻焊、钢网和装配层进行独立制造文件检查。

## 21. 下一步动作

建议按以下顺序推进：

1. 在 Altium 中确认 USBC1 唯一采购型号和封装，核对固定脚、焊盘、方向和板边伸出量。
2. 确认 Shield 实际策略：`0Ω` 直连，或 `1MΩ // 1nF`，并同步设计文档、原理图和 BOM。
3. 补齐 USB、ADC、MOSFET 和通信接口安全丝印，修正 `SCA`，明确 UART2 视角。
4. 核对板框实际尺寸、四个安装孔孔径/坐标/禁布区及 SW3、USB-C 的机械空间。
5. 按 [pcb_design_rules.md](pcb_design_rules.md) 配置和核对 Clearance、分级 Width、Via Style、Hole、Annular Ring、Board Outline、Polygon Connect 和 Layer Pairs。
6. Repour 后完整运行 Batch DRC；导出报告并记录 `.PcbDoc` 哈希或对应 Git 提交。
7. 导出包含 PCB Footprint 的 BOM，并人工完成 U1、USBC1、U6、U7、U8、Q1/Q2、D1-D5、连接器和开关的封装/焊盘映射核对。
8. 更新三张 PCB 审查图和本文问题状态；所有制造门禁关闭后，再单独执行制造输出审查。
9. 项目 README、requirements、design_notes 的阶段状态存在滞后时，在后续统一状态同步任务中处理，本轮不扩展修改范围。
