# 模拟前端条件参考片段

> 定位：optional domain reference；只选择当前项目实际具有的放大、滤波、采样和参考模块。
> 不预设运放型号、ADC 架构、电压或固定拓扑；不是完整模拟系统设计方法。

按 [AI Context Guide](../docs/AI_Context_Guide.md) 结合当前信号链、误差目标和官方资料补充项目检查范围。通用输入范围、保护、采样源阻抗与测试访问由 [Schematic Core](schematic_checklist.md) 覆盖；噪声隔离、参考回流和布局由 [PCB Core](pcb_layout_checklist.md) 覆盖。

## 放大与滤波 — 存在时

- [ ] 实际供电和负载下的输入共模范围、输出摆幅与级间范围匹配。
- [ ] 增益、带宽、压摆率、失调、偏置与噪声对当前精度 / 动态目标的影响有依据。
- [ ] RC / 有源滤波器的截止频率、容差和稳定性满足目标信号与采样要求。
- [ ] 实际负载、ADC 采样瞬态及保护外围未破坏驱动稳定性或建立时间。

## ADC / Reference — 存在时

- [ ] 当前 ADC 架构的 acquisition / settling、采样率与驱动要求已按实际源阻抗和时序核对。
- [ ] 参考源的驱动能力、负载瞬态、噪声、去耦和启动条件符合 ADC 与精度要求。
- [ ] 当前信号链的误差 / 噪声预算与校准假设可追溯；适用的采样噪声和性能测试已纳入项目测试范围。

具体参数和结论留在当前 owning design / review / test record；本片段不保存 Project Facts，也不要求为每个 ADC 或运放建立 Framework 清单。
