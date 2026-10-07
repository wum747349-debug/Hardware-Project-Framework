# Bring-up 与硬件测试检查表

> 文档状态：当前有效
> 适用阶段：Stage 8 — Assembly, Bring-up and Hardware Test
> 适用对象：准备装配检查、首次上电、基础功能验证与调试记录的 Project / Hardware Revision

## 使用与证据边界

本表是 Stage 8 Core coverage guard。按 [AI Context Guide](../docs/AI_Context_Guide.md) 从当前需求、实际硬件 / Firmware、官方资料与已知风险形成项目测试范围；适用项与实际结果写入 `docs/bringup_log.md` / `docs/test_report.md`，不适用注明理由。用户负责实测，AI 只分析提供的 evidence。

- 任何可疑短路、极性错误、异常电流、异常温升或安全边界不明都应停止上电并先排查。

## 1. 上电前检查

- [ ] Project、Hardware Revision、装配版本和待测对象可追溯。
- [ ] 目视检查器件错装、漏装、连锡、虚焊、污染和机械损伤。
- [ ] IC、二极管、电解电容、电池、连接器及其他极性器件方向正确。
- [ ] 输入电源、主要电源轨与 GND 的阻值 / 二极管档表现已检查，未发现未解释的短路迹象。
- [ ] 电源输入范围、极性、连接顺序和保护边界明确。
- [ ] 测试点、调试口、复位方式和安全断电方式可用。
- [ ] 昂贵、敏感或可能放大故障后果的外设暂不接入，或已有隔离措施。

## 2. 首次限流上电

- [ ] 使用可限流电源或其他经风险评估的受控供电方式。
- [ ] 输入电压与限流值依据当前 Project 需求设置并记录，未照搬其他 Project 数值。
- [ ] 上电后先观察输入电流、异常气味、声音、烟雾和温升；异常时立即断电。
- [ ] 按电源树顺序测量输入、主要 rail、reference 与 reset / enable 等关键节点。
- [ ] 实测值、期望范围、测量工具、测量点和判定均已记录。
- [ ] 修改硬件或供电条件后重新执行受影响的安全检查。

## 3. 验证证据分层

Firmware 验证方法见 [Firmware Skill](../skills/hardware-firmware-development/SKILL.md)；本节只检查证据层级没有混用。

- [ ] 静态检查、compile、flash、实板功能与系统 / 性能验证分别记录；未执行层级保持 Pending / 未验证。
- [ ] 适用时关联 Hardware Revision、Firmware version / Commit、build configuration / binary identity 与测试条件。
- [ ] 编译成功未写成烧录、实板功能或性能 PASS；烧录成功未写成完整功能或系统验证 PASS。

## 4. 基础与功能验证

- [ ] 电源、复位、时钟和适用调试连接满足当前验证目标。
- [ ] Firmware / configuration 的版本和下载方式可追溯（如适用）。
- [ ] 仅按当前 Project 的接口、控制、采集、保护和负载边界选择测试项。
- [ ] 每项测试记录前置条件、步骤、输入、期望、实测、单位、容差和结论。
- [ ] 异常、未测项和受限结论没有被写成 PASS。
- [ ] Functional verification 与 `requirements.md` 的 Acceptance Criteria 或明确测试目标可追溯。

## 5. 调试记录覆盖

- [ ] 重要 session 的日期、人员、目标、装配状态与软硬件版本可追溯。
- [ ] 电源设置、实测电流、工具 / 探头 / 连接、负载、时长、环境与适用 host / peripheral 条件有记录。
- [ ] 测试步骤、期望、实测与电压 / 电流 / 波形 / 日志等证据对应。
- [ ] 异常复现条件、假设、排查依据、实际修改版本及修改后复测结果已记录。
- [ ] 当前结论、未关闭风险与下一步明确；系统 / 性能结论未超出实际测试覆盖。

## 6. 阶段结论

- [ ] 核心功能和验收边界已有用户提供的可追溯 Evidence，或明确标记未完成。
- [ ] 异常与未测项有 owner、风险、后续动作和所需复测。
- [ ] 任何改版影响已进入 `docs/revision_history.md`（实际触发时）。
- [ ] 当前结论没有把结构检查、文档计划或 AI 分析误写为实际硬件验证。
