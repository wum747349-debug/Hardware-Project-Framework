# STM32 条件参考片段

> 定位：optional domain reference；仅在当前项目实际使用 STM32 时选用。
> 保留原路径以兼容引用；不是所有 MCU 的检查表，也不是某个 STM32 型号的完整清单。

按 [AI Context Guide](../docs/AI_Context_Guide.md) 形成项目检查范围，将适用项与当前型号、封装和官方资料关联后记入当前 owning review / validation 文档。通用供电、接口、保护、测试访问由 [Schematic Core](schematic_checklist.md) 覆盖；晶振放置、去耦回路和载流路径由 [PCB Core](pcb_layout_checklist.md) 覆盖，不在此重复。

## 型号相关补充

- [ ] 当前型号 / 封装实际具有的 VDDA、VREF、备用供电、内部稳压器相关引脚及未用脚，已按官方资料核对连接和外围；不预设固定供电或电容值。
- [ ] 当前器件的 reset、boot selection、option bytes 与默认启动路径相符；不把 BOOT0 下拉视为所有型号的统一要求。
- [ ] 使用外部晶体 / 时钟时，实际振荡器模式、晶体参数、负载电容计算与启动条件有依据。
- [ ] 实际使用的 SWD / JTAG 或其他下载路径具备所需信号、地、目标参考电压与恢复访问；按当前器件和调试器要求判断 reset access。
- [ ] 外设复用、调试脚占用、boot function 与项目 pin map 无冲突；多个设备共用接口时，驱动冲突、上电状态和隔离方式已有依据，不一概禁止复用。
- [ ] 各引脚在实际供电、模拟 / 数字模式下的输入容限、注入电流与掉电反灌风险已按官方资料核对。

其他 MCU 直接从其官方资料推导对应检查，不套用 STM32 引脚名，也不要求新增每芯片一份的 Framework Checklist。
