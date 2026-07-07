# 系统框图

```text
电脑 USB-C
   │
   │ 5V 输入
   ▼
USB-C 接口
   │
   ├─ D+ / D- ─────► USB 转 UART 芯片 ── TX/RX，3.3V UART ──► STM32F103C8T6 USART1
   │                                                        PA10/RX  PA9/TX
   │
   ▼
电源开关 / 保险丝或自恢复保险丝 / TVS-ESD / 输入滤波
   │
   ▼
3.3V 稳压
   │
   ├─► STM32F103C8T6
   │      ├─ 8MHz HSE 外部晶振
   │      ├─ NRST 复位
   │      ├─ BOOT 配置
   │      ├─ SWD 下载调试接口
   │      ├─ 用户 LED
   │      ├─ 用户按键
   │      ├─ UART 排针
   │      ├─ I2C 传感器接口排针
   │      ├─ SPI 扩展接口排针
   │      ├─ ADC1 输入  ◄── 分压 / 限流 / RC 滤波 / 保护 ◄── ADC IN1 0-5V + GND
   │      ├─ ADC2 输入  ◄── 分压 / 限流 / RC 滤波 / 保护 ◄── ADC IN2 0-5V + GND
   │      ├─ GPIO ─────► MOSFET 低边输出 CH1 ── OUT1 / VLOAD1 / GND
   │      └─ GPIO ─────► MOSFET 低边输出 CH2 ── OUT2 / VLOAD2 / GND
   │
   ├─► USB 转 UART 芯片逻辑侧
   ├─► 电源指示 LED
   └─► 接口上拉 / 低压外围电路

测试点：
5V / 3.3V / GND / NRST / SWDIO / SWCLK / USART TX-RX /
USB 转 UART 关键电源 / ADC 分压后节点 / MOSFET 栅极 / MOSFET 输出端

注意：
- USB-C D+ / D- 只接 USB 转 UART 芯片，不接 STM32 PA11 / PA12。
- ADC 外部接口可接 0-5V，但进入 STM32 ADC 引脚前必须限制在 0-3.3V。
- MOSFET 外部负载电源 VLOAD 必须与板子 GND 共地。
```
