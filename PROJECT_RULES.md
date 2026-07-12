# PROJECT_RULES

## 1. 仓库定位

本仓库是低压嵌入式硬件实战项目工作区，用于训练和沉淀从需求定义、模块拆分、器件选型、原理图设计、PCB Layout、打样、焊接、上电调试、测试验证到简历整理的完整硬件设计流程。

当前仓库采用“渐进式硬件设计流程”：先明确需求和模块边界，再围绕当前设计决策分批选择关键器件、阅读关键资料、反推外围参数和完善 BOM 草稿。

## 2. 当前项目

当前核心项目优先级：

1. `projects/01_STM32_DAQ_Control_Board`
2. `projects/02_LiIon_Charger_Protection_Board`
3. `projects/03_STM32_OpAmp_ADC_Acquisition_Board`

## 3. 工具链

- EDA 软件：Altium Designer
- STM32 配置工具：STM32CubeMX
- 固件开发：Keil MDK
- 文档格式：Markdown
- 版本管理：Git / GitHub

## 4. 渐进式硬件设计原则

- 不要求在项目一开始一次性收集所有元器件 datasheet。
- 第一轮优先完成需求整理、模块拆分和关键器件候选选型。
- 关键器件优先，普通电阻、电容、LED、按键、排针、测试点、跳帽等外围器件后置。
- 资料收集按模块、按当前设计决策需要分批进行。
- 先根据需求和模块边界选择关键器件候选，再根据关键 datasheet、reference manual 或 application note 反推外围阻容、保护、接口和封装要求。
- BOM 草稿只能在关键器件和模块电路依据基本明确后生成；最终 BOM 必须经过 datasheet、封装和采购可得性核对。

## 5. 资料依据规则

- 官方 datasheet、reference manual、application note 是关键参数的主要依据。
- 立创商城 / 嘉立创生态用于用户手动搜索器件、检查库存/价格/封装/基础库或扩展库状态、获取 C 编号和下载 datasheet。
- AI/Codex 不默认自动访问、爬取或批量下载立创商城资料。
- 立创商城商品页只能作为库存、价格、封装、C 编号和资料入口参考，不能替代 datasheet。
- 不允许把立创商城商品页、教程、博客、论坛、视频或开源项目作为唯一设计依据。
- 关键参数必须回到官方 datasheet、reference manual 或 application note 核对；如果资料来源不清楚，应标记“来源待确认”。

## 6. 开源项目参考规则

- 开源项目只能用于学习功能结构、模块划分、接口组织、PCB 布局思路、文档组织和制造输出组织方式。
- 禁止直接复制开源项目的原理图、PCB、BOM、Gerber、生产文件、源工程文件或文字说明作为本项目成果。
- 引用开源项目时必须记录来源仓库地址、参考用途、学习点和不可照抄内容。
- 如果未来确实需要复用开源项目中的某个具体电路片段，必须先检查 license，并在文档中记录来源、修改点、datasheet 核对结果和验证结果。

## 7. 文件管理规则

- 每个项目必须包含 `README.md`、`requirements.md`、`block_diagram.md`、`design_notes.md` 和 `references.md`。
- 项目资料统一放在 `references/` 下，datasheet 按模块放入 `references/datasheets/` 的子目录。
- 立创商城搜索过程记录在项目 `references/lcsc_parts/lcsc_search_notes.md`。
- 阶段文档统一放在项目 `docs/` 下。
- Altium 工程文件统一放在 `hardware/altium_project/`。
- Gerber、BOM、PDF、贴片坐标等输出文件统一放在 `hardware/outputs/`。
- 固件工程统一放在 `firmware/`。
- 项目截图、装配照片和测试照片统一放在 `hardware/images/`。

## 8. AI 协作规则

AI 在协助本仓库时，应先识别当前任务所属项目和阶段，再按 `docs/AI_Context_Guide.md` 读取最小必要上下文。

具体 AI 行为、能力边界、Skill 路由和输出要求以 `AGENTS.md` 为准；具体读取范围以 `docs/AI_Context_Guide.md` 为准。

## 9. 安全规则

- 电源、电池、MOSFET、ADC 输入保护、运放供电范围、参考电压等风险模块必须回到 datasheet / application note 核对。
- 锂电池项目首次上电必须使用限流电源，禁止无人看管充电测试。
- MOSFET 驱动感性负载时必须考虑续流路径和保护。
- 模拟输入接口必须考虑输入电压范围、限流、钳位和保护。
- 每个关键电源、复位、调试、通信、ADC 信号必须预留必要测试点。
