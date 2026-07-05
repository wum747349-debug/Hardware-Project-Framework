# 参考资料

## 官方资料

> 后续补充充电 IC、保护 IC、MOSFET、稳压芯片、接口器件和电池规格等官方资料。

- 单节锂电池充电 IC datasheet
- 电池保护 IC datasheet
- MOSFET datasheet
- LDO / DCDC datasheet
- USB-C 取电相关规范和应用笔记
- 目标电池规格书

## 开源硬件参考项目

> 开源项目只作为结构、设计思路、文档组织和输出文件组织参考，不直接复制原理图、PCB、BOM、Gerber 或源文件。

更多开源参考项目统一记录在：`references/open_source_hardware_projects.md`

| 仓库名称 | GitHub 地址 | 参考用途 | 注意事项 |
| --- | --- | --- | --- |
| `SolderedElectronics/Li-ion-charger-with-protection-hardware-design` | <https://github.com/SolderedElectronics/Li-ion-charger-with-protection-hardware-design> | 参考 USB-C 输入、单节锂电池充电、保护电路、状态 LED 和制造输出文件组织。 | 充电电流、热设计、保护阈值、接口极性必须按目标芯片和实际电池重新计算，不能照抄电源路径和保护参数。 |
| `SolderedElectronics/1S-Li-Ion-battery-protection-hardware-design` | <https://github.com/SolderedElectronics/1S-Li-Ion-battery-protection-hardware-design> | 参考 1S 电池保护电路和 CAD/OUTPUTS、BOM、iBOM、PDF、STEP、Gerber 等输出物管理。 | 保护芯片、MOSFET、过充、过放、过流、短路保护参数必须重新核对，只记录学习点。 |
| `sparkfun/Lipo_Charger_Basic-microUSB` | <https://github.com/sparkfun/Lipo_Charger_Basic-microUSB> | 参考简单单节 LiPo/Li-Ion 充电板、充电 IC、状态 LED、电池接口和最小实现。 | 该项目是 micro-USB，本项目计划 USB-C 输入；CC 电阻、充电电流、热设计和电池接口极性必须重新设计。 |

## 需要提取的学习点

- 充电、保护、稳压输出、电池接口和状态指示需要明确功能边界。
- USB-C 只取电场景需要核对 CC 电阻连接、输入保护和接口耐压。
- 充电电流应结合 USB 输入能力、芯片热阻、PCB 铜皮散热和电池规格计算。
- 保护电路需要核对过充、过放、过流、短路保护阈值和 MOSFET 安全工作区。
- 制造输出应单独管理 Gerber、钻孔、BOM、PDF 原理图、装配图和测试记录。

## 不可直接照抄的内容

- 第三方原理图、PCB、BOM、Gerber、生产文件和源工程文件。
- 充电电流设定、电源路径、保护阈值、MOSFET 型号和封装选择。
- USB-C 接口、电池座极性、热设计、铜皮面积和安全间距。
