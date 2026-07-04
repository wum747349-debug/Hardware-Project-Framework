# 系统框图

```text
USB-C 5V
   ↓
输入保护 / 滤波
   ↓
3.3V LDO
   ↓
STM32 MCU
 ├─ SWD 调试接口
 ├─ UART 接口
 ├─ I2C 传感器接口
 ├─ SPI 扩展接口
 ├─ ADC 输入 × 2
 ├─ MOSFET 输出 × 2
 ├─ LED × 2
 └─ 按键 × 2
```
