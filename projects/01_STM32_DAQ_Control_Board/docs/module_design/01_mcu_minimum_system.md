# MCU 最小系统设计说明

> 文档状态：当前有效，模块详细依据
> 适用版本：Rev A

## 1. 模块定位

本模块记录 `STM32F103C8T6` 最小系统原理图设计说明，包括供电、去耦、VDDA/VSSA、VBAT、NRST、BOOT0、HSE 8MHz 晶振、SWD 下载调试接口和基础测试点。

当前内容作为阶段 7 / 制造放行前复核的模块设计依据，不是最终 BOM。

## 2. MCU 选择说明

MCU 确定为 `STM32F103C8T6`，封装方向按常见 `LQFP48`。

选择原因：

- 器件常见，资料丰富。
- 适合 STM32 入门、最小系统和基础外设训练。
- LQFP48 方向适合手焊练习和 2 层板布局训练。
- Keil、STM32CubeMX、ST-Link/SWD 调试链路成熟。

阶段 7 / 制造放行前仍需根据 STM32F103C8T6 datasheet / reference manual 核对封装、引脚、电源脚、去耦、BOOT、NRST、SWD、HSE 和 ADC 等细节。

## 3. 数字电源与去耦

- `VDD_1`、`VDD_2`、`VDD_3` 全部接 `3.3V`。
- `VSS_1`、`VSS_2`、`VSS_3` 全部接 `GND`。
- 每个 VDD 附近放置 `100nF` 去耦电容。
- MCU 附近额外放置 `4.7uF` 总去耦电容，Layout 时尽量靠近 `VDD_3`。
- `VBAT` 不使用备用电池时接 `3.3V`，避免悬空；可根据需要预留 `100nF` 去耦。

## 4. VDDA / VSSA 模拟电源

- `STM32F103C8T6 LQFP48` 中 pin8 为 `VSSA`，pin9 为 `VDDA`。
- `VSSA` 接 `GND`，`VDDA` 接独立网络 `VDDA_3V3`。
- `VDDA_3V3` 由 `3.3V` 通过 `0Ω` 电阻 `R5` 接入，`R5` 作为磁珠/小电阻替换预留。
- `VDDA_3V3` 对 `GND` 放置 `C7=100nF` 和 `C8=1uF` 去耦电容，靠近 VDDA/VSSA 引脚。
- 第一版建议 `R5` 先使用 `0Ω`、`0603` 普通贴片电阻，不直接使用磁珠。
- 原因：本项目 ADC 只是低速采集和功能验证，不追求高精度模拟测量；`0Ω` 更简单、可靠、方便调试，也便于后续发现 ADC 抖动时替换为磁珠。
- `VDDA` 不能悬空，也不能与 `VSSA` 接反。`VDDA` 主要给 ADC、模拟相关模块、复位/内部 RC/PLL 等部分供电，并影响 ADC 采集稳定性。

## 5. NRST 复位电路

- `NRST` 接复位按键 `SW2` 到 `GND`。
- `NRST` 对 `GND` 放置 `C6=100nF` 电容。
- `NRST` 同时引出到 SWD 接口。
- STM32 NRST 内部已有弱上拉，因此外部 `10k` 上拉可不放或预留 DNP；当前模块设计说明以按键 + `100nF` 为主。
- 阶段 7 / 制造放行前复核 `NRST` 网络标签必须接到 pin7 `NRST`，不能误接到 HSE 晶振脚。

## 6. BOOT0 启动配置

- `BOOT0` 通过 `R2=10kΩ` 下拉到 `GND`，默认从用户 Flash 启动。
- 预留 3Pin 跳帽 `H2`：`H2-1` 接 `3.3V`，`H2-2` 接 `BOOT0`，`H2-3` 接 `GND`。
- 不插跳帽时 `BOOT0` 由 `10k` 下拉，默认运行用户程序。
- 跳帽接 `1-2` 时 `BOOT0` 拉高，可进入系统 Bootloader。
- 跳帽接 `2-3` 时 `BOOT0` 强制拉低，仍从 Flash 启动。
- `PB2/BOOT1` 通过 `R21=10kΩ` 下拉到 `GND`，确保 `BOOT0` 拉高时 `BOOT1` 仍保持低电平，便于进入系统 Bootloader。
- 注意不要画成会导致 `3.3V` 和 `GND` 被跳帽短接的结构。

## 7. HSE 8MHz 晶振

- HSE 使用 `X1 XC53G2-8.000-F12NJHP`，为 `8MHz` 基频无源晶振。
- `STM32F103C8T6 LQFP48` 中 pin5 = `PD0 / OSC_IN`，pin6 = `PD1 / OSC_OUT`。
- 8MHz 晶振 `X1` 接在 `OSC_IN` 与 `OSC_OUT` 之间。
- `OSC_IN` 对 `GND` 放置负载电容 `C3=5.1pF`，`OSC_OUT` 对 `GND` 放置负载电容 `C4=5.1pF`。
- X1 标称负载电容 `CL=12pF`；`C3/C4` 采购时选用 C0G/NP0 材质。
- `PC14/PC15` 是 LSE 32.768kHz 低速晶振脚，不是本项目 8MHz HSE 晶振脚。本项目暂不使用 LSE，`PC14/PC15` 可先悬空。
- Layout 时晶振和负载电容尽量靠近 `OSC_IN/OSC_OUT`，走线短且对称、无过孔，远离高速/大电流信号。
- 可选预留 `OSC_OUT` 串联电阻焊盘作为低风险优化，但这不是必须修改项，也不表示当前已实现。

当前资料显示 `XC53G2-8.000-F12NJHP` 系列为 5.0mm x 3.2mm x 1.3mm 两焊盘贴片无源晶振，8MHz 属于基频范围，8MHz-12MHz 对应 ESR 约 80Ω。

## 8. SWD 调试接口

- 保留 `1x5` SWD 接口 `H4`：`3.3V`、`SWDIO`、`SWCLK`、`NRST`、`GND`。
- `SWDIO` 使用 `PA13`，`SWCLK` 使用 `PA14`。
- 网络名统一使用 `SWDIO`、`SWCLK`、`NRST`，不建议使用容易混淆的 `CLK`。
- 后续建议预留测试点：`3.3V`、`GND`、`NRST`、`SWDIO`、`SWCLK`。

## 9. 阶段 7 / 制造放行前检查项

MCU 最小系统模块设计说明已完成。已记录内容包括：VDD/VSS 连接、基础去耦、VBAT 接 3.3V、VDDA/VSSA 简单模拟电源、NRST 复位、BOOT0 跳帽、HSE 8MHz、SWD 接口。

阶段 7 / 制造放行前重点复核：

1. `VDDA/VSSA` 是否接反。
2. `NRST` 是否误接到 `OSC_OUT`。
3. `BOOT0` 跳帽是否会造成 `3.3V` 与 `GND` 短接。
4. HSE 晶振、`C3/C4=5.1pF` 和布局约束是否与当前设计一致。
5. `4.7uF` 总去耦电容是否靠近 `VDD_3`。
6. 晶振和 VDDA 去耦在 PCB 上是否靠近 MCU。
