# Hardware Firmware Development Skill

## 1. Purpose / Activation

本 Skill 提供跨项目的 MCU Firmware 开发方法，用于固件可行性原型、工程初始化、驱动与业务实现、构建、烧录、运行调试，以及 Hardware–Firmware 联调。它属于绑定 Framework 快照中的 Layer 3 method，由 **Task Intent** 按需启用，不建立新的 Firmware Framework、Runtime Contract、Stage / Gate 或 Authority。

Activation timing：

- Stage 1 只确认项目是否需要 Firmware、Firmware functional boundary、hardware interface requirements 与相关 acceptance criteria，不要求建立 Firmware 工程或目录；
- 实际开始持续性 Firmware 开发前，先确认或建立 Project `firmware/AGENTS.md` 等局部规则；
- 实际工程初始化由编译、可行性原型或开发需求触发，不由固定 Stage 强制触发；
- Stage 2–3 可在 MCU 资源、外设配置、时序或数据链路无法仅靠静态分析可靠关闭时建立最小 prototype；Stage 4–7 按实际任务继续 Firmware 工作；Stage 8 执行实际烧录、运行、接口联调、功能与性能测试；
- Firmware 工作不改变 Project 当前硬件 Stage；Stage transition 仍只遵循 `docs/08_Project_Workflow.md`。

## 2. Authority 与 Minimum Context

先完成 Project 根 `AGENTS.md` 的七步启动路由，再按以下顺序读取最小上下文：

1. Project `FRAMEWORK.md`、`PROJECT_RULES.md` 与绑定 Framework 的 `docs/AI_Context_Guide.md`；
2. 当前目录适用的 `firmware/AGENTS.md`（若存在）；
3. 绑定 Framework 快照中的本 Skill；
4. 当前任务真正需要的 Project hardware facts、requirements、module / interface owning records、official documentation 与 implementation evidence；
5. 当前 Firmware source、build configuration 与已有 validation evidence。

Project Repository 维护 Firmware local rules、hardware facts、toolchain / dependencies、source、build configuration 与 validation evidence。硬件器件、连接、pin / alternate function、clock、electrical limit、timing boundary 与 protocol definition 继续由相应 Project owning record 和 authoritative hardware source 负责；Firmware 实现引用这些事实，不建立竞争权威的第二份 pin table、clock baseline 或 interface contract。

其他 Project 的成熟实现只能作为 qualified reference input。复用不转移 qualification，也不能把其 MCU、外设映射、buffer size、时序参数、GPIO、故障状态机或工具版本提升为当前 Project 或 Framework 默认值。

## 3. Technology Route 与工程初始化

根据当前 Project requirements、目标器件、实时性、资源、团队能力、维护周期、认证 / license、debug 能力和官方支持，选择 HAL、LL、CMSIS / register-level、RTOS 或 bare-metal 等实际技术路线。Framework 不预设唯一组合，也不因某个参考项目采用某路线而要求其他 Project 跟随。

依赖与工具链遵循：

- MCU device support、startup、linker / scatter、SDK、HAL / LL、CMSIS、RTOS、middleware 与 programmer support 优先来自芯片或工具供应商的官方发布，并记录适用版本和来源；
- 明确 target device / core、memory layout、startup、compiler / linker options、optimization、warning policy、binary format 与下载方式；不得用相近器件工程替代而不核对差异；
- Project 保存自己的工程文件、构建配置、生成配置、依赖锁定方式和可复现构建入口；不依赖 Framework 当前工作树；
- Keil、CubeMX 或同类工具只是可选工程工具。使用代码生成时，Project 必须明确生成输入、可编辑区、再生成边界、手写模块归属与版本兼容性；不得让一次本机生成成为不可追溯的唯一事实；
- 工程初始化只创建当前技术路线和当前任务真正需要的内容，不为目录整齐预建 RTOS、Middleware、Protocol、USB、SYSTEM 或其他空模块。

## 4. Firmware Layering

Framework 统一职责原则，不统一强制目录树。Project 可以使用下列职责名称，也可以按既有工程约定映射到等价结构：

- **Core**：系统入口、初始化组织、调度入口和主循环；不堆积外设底层配置或复杂业务状态机；
- **BSP**：板级 GPIO、clock、timer、ADC、通信外设及硬件安全控制；回答“如何操作本板硬件”，不承担产品业务决策；
- **App**：业务逻辑、状态机、数据管理、通信语义和故障策略；通过明确接口使用下层能力；
- **SYSTEM / Platform / Middleware（可选）**：仅在实际需要时提供时基、调度、队列、日志、协议基础设施或平台适配。

依赖方向、跨层访问、公共接口、内部状态和共享对象所有权必须清楚。头文件只暴露必要接口，模块内部符号保持局部；不得为了符合名称而强制所有 Project 创建全部层级，也不得把某一项目的目录布局变成通用 Contract。

## 5. Hardware Safety 与初始化顺序

- 从 Project hardware facts 确认 reset state、active level、pull、drive mode、power domain、boot / debug pin、外部上拉下拉和危险组合，不猜测连接或默认态；
- 在可能产生能量、运动、通信驱动或敏感模拟时序的外设启动前，先建立安全 GPIO / output state，再按依赖关系确认 power、clock、reset、memory、peripheral 与 application state；
- 明确 startup、first cycle、steady state、controlled stop、reset、watchdog / brownout 与 fault recovery 的行为；
- 对互斥输出、功率器件、motor / heater / relay、converter enable 等安全相关控制，定义硬件默认保护与 Firmware 接管边界；Firmware 不替代必要硬件保护；
- Hardware configuration 或启动顺序变化时，回查 owning Project record 与相关 firmware configuration，避免单边更新。

## 6. ISR、实时性与主循环

ISR 应短小、确定且有明确 worst-case responsibility：确认和清除事件 / error、搬运最小必要数据、更新原子状态、转移 ownership、投递事件，或执行不能延后的即时硬件安全动作。不要机械要求全部 ISR 位于 BSP，也不要机械要求所有事件都延后到主循环；ISR 位置与职责由 hardware ownership、latency 和 safety requirement 决定。

ISR 中避免无界循环、阻塞资源、格式化输出、不可控延时、复杂协议解析和完整业务状态机。共享状态必须按 MCU / compiler / RTOS memory model 处理 `volatile`、原子访问、临界区、优先级反转和嵌套风险。

主循环或任务原则上非阻塞。必要的有界等待必须有工程依据、明确最大时间、timeout / abort path 与对采样、通信、安全和其他任务的实时性影响评估。对周期、deadline、latency、jitter、interrupt priority 和 CPU budget，只验证当前功能真正需要的边界。

## 7. DMA、Buffer 与并发

仅在项目实际使用 DMA、异步队列或共享 buffer 时应用本节：

- 核对 request / channel / trigger mapping、方向、数据宽度、地址、长度、alignment、priority、completion / error event 与 restart sequence；固定映射和 errata 必须回到适用官方资料；
- 明确 producer、consumer、DMA / peripheral 对每个 buffer 状态的 ownership，以及 ownership publish / return 的时点；禁止在消费完成前静默覆盖；
- 定义 full / overflow / underrun / overrun、丢弃、backpressure、stop 或 degrade 策略，并保留足以诊断的计数或 fault reason；
- 处理 ISR、主循环、RTOS task、DMA 与 cache / memory ordering 的适用并发问题；不因简单项目不存在这些风险而强制引入 queue、DMA 或动态内存禁令；
- 用数据率、burst、处理时间和 memory budget 证明容量选择；不复制参考项目的固定 sample count 或 buffer size。

## 8. Communication 与数据完整性

通信实现根据实际协议明确 framing、length、byte order、version / compatibility、integrity check、timeout、retry、duplicate / sequence handling、flow control 与 malformed input policy。区分 transport、protocol parsing 与 business action，避免 ISR 或底层 driver 直接承担复杂业务。

跨 MCU、host、FPGA 或其他端点修改协议时，核对所有参与端和 owning protocol / interface record；只改单端不能宣告兼容。对外部输入执行长度和范围检查，诊断输出不得破坏实时数据通道或泄露不应暴露的信息。

## 9. Error Handling 与恢复

- 为 initialization failure、peripheral error、timeout、buffer fault、communication fault、clock / power anomaly 与 invalid state 定义可观察结果；
- 区分 root fault、secondary recovery failure 与 historical diagnostics，避免成功 restart 后静默抹除根因；
- 恢复顺序先停止 trigger / producer，处理在途 transaction，再清除明确 flag / state、恢复安全硬件态、重新初始化依赖并受控重启；
- retry 必须有次数、时间或上层 policy 边界；无法安全恢复时进入已定义的 safe / degraded state；
- fault injection、watchdog、brownout、断线重连或长期运行验证只在 requirements / risk 实际需要时执行，不虚构已经完成。

## 10. Hardware–Firmware Feedback Loop

Firmware prototype、linker map、build warning、runtime trace、logic analyzer 或实板测试若发现 pin / peripheral conflict、clock / timing 不足、memory / throughput 不足、electrical default 不安全或 recovery 不成立，应：

1. 保存与当前 Hardware / Firmware identity 对应的最小 evidence；
2. 判断问题是 implementation bug、Project-specific constraint 还是 hardware design assumption 失效；
3. 更新实际 owning Project record，而不是在 Firmware 内建立第二硬件事实源；
4. 按影响范围重新评估相关 schematic / PCB / requirement，不自动改变 Project Stage；
5. 重新验证受影响的 Firmware 和 hardware conclusion。

Firmware prototype 可以为硬件设计提供辅助 evidence，但只证明实际覆盖的器件、配置、输入、时间和测试条件。

## 11. Validation Evidence Boundary

分别记录下列 evidence，不能相互替代：

| Evidence | 可以证明 | 不能单独证明 |
| --- | --- | --- |
| Source / static review | 可读代码范围内的逻辑、配置一致性或已检查风险 | 编译、烧录、真实时序与板级功能 |
| Build / linker / map | 选定工具链能构建、链接并满足已检查的 memory / warning 条件 | binary 可烧录、能运行或 hardware interface 正确 |
| Flash / verify | 指定 binary 已写入并通过适用校验 | application 正确运行 |
| Runtime / debugger / trace | 指定环境和路径中的实际运行行为 | 未覆盖路径、长期稳定性或外部电气性能 |
| Hardware measurement / interface test | 指定板卡、版本、仪器和条件下的真实信号 / 功能 / 性能 | 其他版本、其他条件或未测边界 |

每项结果关联 source commit / binary identity、Hardware Revision、toolchain / configuration、test condition 与已知 limitation。未执行项保持 `Pending`。**Build PASS 不能替代 Flash、Runtime、Logic Analyzer 或 Hardware Validation**；Framework 文档检查也不证明任何 Product Project Firmware 已完成实板验收。

## 12. Output / Prohibited Actions

Firmware 任务输出应按范围给出：适用 Authority、技术路线与依赖、模块职责、实现 / diff、构建或测试入口、实际执行的 evidence、限制、hardware feedback 与下一步。

禁止：

- 建立第二套 Framework binding、Runtime Contract、Stage / Gate、Release / Migration 或 Validator required structure；
- 把 Firmware 工程、`firmware/AGENTS.md` 或固定目录变成所有 Project 的 Required 内容；
- 强制所有项目使用 HAL、LL、register-level、RTOS、DMA、queue、动态内存禁令、Keil 或 CubeMX；
- 猜测 pin、clock、DMA mapping、electrical limit、protocol 或 safety behavior；
- 复制参考项目源码、工程文件或具体 MCU / peripheral / timing / buffer 参数作为 Framework 默认实现；
- 将 Build、static review 或文档 validation 冒充 Flash、Runtime、logic-analyzer 或 Hardware Validation 结果；
- 不建立新的 Firmware Gate，也不因 Firmware 工作自动推进或回退硬件 Stage。
