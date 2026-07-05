# 参考资料

## 官方资料

> 后续补充 MCU datasheet、reference manual、application note、芯片数据手册等。

- STM32 目标型号 datasheet
- STM32 reference manual
- 运放 datasheet
- ADC datasheet
- 参考电压芯片 datasheet
- 模拟 PCB Layout application note
- ADC 输入保护、采样保持、源阻抗和参考电压相关资料

## 开源硬件参考项目

> 开源项目只作为结构、设计思路、文档组织和输出文件组织参考，不直接复制原理图、PCB、BOM、Gerber 或源文件。

更多开源参考项目统一记录在：`references/open_source_hardware_projects.md`

| 仓库名称 | GitHub 地址 | 参考用途 | 注意事项 |
| --- | --- | --- | --- |
| `JacobParent7/Mixed-Signal-STM32-Dev-Board` | <https://github.com/JacobParent7/Mixed-Signal-STM32-Dev-Board> | 参考 STM32 混合信号硬件、USB-C 供电、模拟电源、ADC/DAC、偏置、滤波、混合信号 PCB 分区、回流路径控制和 README 的系统级记录方式。 | 该项目是 4 层混合信号 PCB，本项目可参考思路但不追求同等复杂度；运放、ADC、参考电压和滤波参数必须重新计算验证。 |

## 需要提取的学习点

- 模拟前端、参考电压、ADC 输入、数字控制和供电模块需要清晰分区。
- 模拟/数字回流路径、敏感节点、参考电压走线和输入滤波位置应在 PCB 阶段重点检查。
- 运放供电范围、输入共模范围、输出摆幅、带宽、压摆率和稳定性需要和目标信号匹配。
- ADC 输入阻抗、采样时间、保护电阻、RC 滤波截止频率和参考电压噪声必须成组验证。
- README、框图、Layout 截图和测试记录可作为项目展示方式参考。

## 不可直接照抄的内容

- 第三方原理图、PCB、BOM、Gerber、生产文件和源工程文件。
- 运放型号、ADC 型号、参考电压、滤波参数、偏置参数和供电拓扑。
- 4 层板布局细节、模拟/数字分区边界、过孔/铺铜/回流路径等具体实现。
