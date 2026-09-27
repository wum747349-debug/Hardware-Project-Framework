# 原理图通用检查表

本 checklist 默认支持 Stage 4 Formal Schematic Review。Formal Review 使用适用的完整检查范围，并遵守完整 PDF / BOM 输入要求。用于 explicit scoped review / risk review 时，只应用与当前 scope 相关的 checklist items，证据要求与 scope 匹配；完整整板 PDF / BOM 和整板 Layout-entry decision 不因此成为 scoped review 的默认要求。

## 审查输入

- [ ] 默认必需审查输入已具备：可追溯到当前 `.SchDoc` 版本的完整原理图 PDF，以及当前版本 BOM；BOM 至少包含位号、数量、参数或型号、PCB 封装
- [ ] BOM 未为格式要求虚构器件料号；关键器件尽量包含明确型号或料号，通用阻容、LED、测试点、排针等可使用参数、额定值、精度和封装描述
- [ ] 不同源版本导出的审查证据没有混用；版本无法确认时已标记证据风险
- [ ] 网表、ERC 输出、元件报告、封装映射报告或截图仅在对应问题需要时按需提供，未把这些条件触发证据当作默认必需输入
- [ ] 完整原理图 PDF 和当前版本 BOM 无法确认的实际网络、引脚映射、封装映射或其他 EDA 实现事项，已标记为“待 EDA 核对”或说明结论限制
- [ ] 局部截图只用于补充局部证据，不代替完整原理图 PDF
- [ ] 设计意图文档与 EDA 实现证据分开记录，不把 `design_notes.md` 当作实现已经同步的证明

## 设计充分性与整板集成

- [ ] 当前 topology 与主要模块职责仍满足 requirements，没有依赖已经失效的 Stage 3 assumption
- [ ] 关键 operating range、gain / scaling、bandwidth / filtering、ADC acquisition / settling 与 timing 在当前 whole-design context 下成立
- [ ] 关键 voltage / current / thermal / headroom margin 已按项目风险评估
- [ ] startup / shutdown / reset / default / fault behavior 与必要 sequencing 已覆盖
- [ ] protection boundary、power integrity、analog / digital interaction 与跨模块接口不存在未处理的系统级冲突
- [ ] 适用的 hardware–firmware feasibility 没有被当前硬件资源、时序或接口实现阻断
- [ ] 对已有 Stage 3 engineering rationale 只在 assumption 变化、evidence 不足、可信矛盾或此前未覆盖的 mandatory scope 下重新深入评估；完整 coverage 不等于机械重新设计

## 总体结构

- [ ] 电源网络命名清楚
- [ ] 所有芯片电源脚已连接
- [ ] 所有芯片地脚已连接
- [ ] 去耦电容完整
- [ ] 复位、启动、调试接口完整
- [ ] 通信接口方向清楚
- [ ] 连接器引脚定义清楚
- [ ] 关键参数有 datasheet 依据
- [ ] 关键网络具有明确的测试 / 调试 access strategy；若访问需要 connector、jumper、0Ω / series break、debug interface 或其他会改变 schematic connectivity 的硬件，已在原理图中体现
- [ ] 如用户提供 ERC 报告、Messages 导出或相关截图并要求分析，相关 ERC 问题已记录为补充证据；未提供 ERC 输出时不声称已核对 ERC
- [ ] 模块划分清晰，电源路径和信号流向容易追踪
- [ ] 网络命名、接口命名和跨页网络标签一致
- [ ] 必要的功能框图或设计说明已补充

## 电源

- [ ] 输入电压范围符合需求
- [ ] USB-C 供电时 CC 电阻配置符合当前用途
- [ ] 输入端保险丝、TVS、ESD 或反接保护已按风险评估
- [ ] LDO / DC-DC 输入输出电容符合 datasheet
- [ ] EN / FB / PG / GND 等关键引脚连接正确
- [ ] 电源指示灯有限流电阻
- [ ] 关键电源轨已纳入可实现的测试 / 调试 access strategy；不因本项默认要求独立 test-point component
- [ ] 电源芯片功耗、温升和长期电流边界已评估
- [ ] 模拟电源和数字电源的滤波或隔离策略明确

## 通信接口

- [ ] UART / I2C / SPI 方向从 MCU 视角标注清楚
- [ ] I2C 上拉电阻、上拉电压或依赖外部上拉的说明明确
- [ ] 接口电平与外接设备匹配
- [ ] 外部接口的 ESD 保护需求已评估
- [ ] 接插件引脚顺序不易接反，GND 和电源脚位置合理
- [ ] 接口丝印能支持焊接和调试

## ADC / 模拟输入

- [ ] ADC 输入电压不超过 MCU、外置 ADC 或运放允许范围
- [ ] 输入限流、RC 滤波、钳位或 TVS 保护符合需求
- [ ] 分压电阻和信号源阻抗不破坏采样精度
- [ ] ADC 参考电压稳定，VDDA / VREF 去耦合理
- [ ] 模拟输入已纳入可实现的测试 / 调试 access strategy；不因本项默认要求独立 test-point component
- [ ] 模拟地和数字地处理不会引入明显回流风险

## MOSFET / 功率输出

- [ ] MOSFET 类型、Vds、Id、Rds(on)、Vgs 满足需求并有 datasheet 依据
- [ ] MCU GPIO 可在当前电压下可靠驱动 MOSFET
- [ ] 栅极串联电阻和默认下拉电阻合理
- [ ] 感性负载有续流路径或保护说明
- [ ] 负载接口极性、电压范围和共地要求明确
- [ ] 大电流回路不会明显干扰 MCU、ADC 或通信接口
- [ ] MOSFET 封装散热满足预期负载

## 封装、测试点和可制造性

- [ ] Formal Review 使用的 post-convergence current design 中，所有实际装配器件与当前 schematic / BOM / PCB footprint mapping 无歧义；不需要具体 MPN 的普通器件已有充分 specification、rating 与 footprint
- [ ] 极性器件方向、接插件脚位和丝印方向明确
- [ ] 电源、复位、调试、通信、ADC 和关键输出具备可实现的测试 / 调试访问方案；普通 PCB test pad 的最终尺寸、位置、探测空间与物理可达性留待 Stage 5 Layout 实现
- [ ] 器件封装适合当前焊接能力和 PCB 工艺
- [ ] 必要的跳帽、0Ω 电阻或调试焊盘已评估
- [ ] 丝印不与安全边界、接口定义或极性标识冲突
