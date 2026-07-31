#!/usr/bin/env python3
"""Validate the repository's shared hardware-project framework."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]

CANONICAL_STAGE_MAP = {
    1: "需求确认阶段",
    2: "关键器件选型阶段",
    3: "原理图模块设计和绘制阶段",
    4: "原理图审查阶段",
    5: "PCB 布局阶段",
    6: "布线和铺铜阶段",
    7: "PCB 审查阶段",
    8: "焊接和硬件调试阶段",
}

CANONICAL_STAGES = tuple(CANONICAL_STAGE_MAP.values())

REQUIRED_COMMON_FILES = (
    "PROJECT_RULES.md",
    "AGENTS.md",
    "README.md",
    "docs/Project_Structure_Standard.md",
    "docs/08_Project_Workflow.md",
    "docs/AI_Context_Guide.md",
    "docs/Project_Template_Guide.md",
    "skills/hardware-pcb-layout-review/SKILL.md",
    "skills/hardware-pcb-layout-review/agents/openai.yaml",
    "checklists/pcb_layout_preflight_checklist.md",
    "checklists/pcb_layout_checklist.md",
    "checklists/pcb_release_checklist.md",
)

REQUIRED_TEMPLATE_FILES = (
    "README.md",
    "requirements.md",
    "block_diagram.md",
    "design_notes.md",
    "references.md",
    "docs/README.md",
    "docs/component_selection_plan.md",
    "docs/module_design/README.md",
    "docs/schematic_review.md",
    "docs/pcb_design_rules.md",
    "docs/pcb_review.md",
    "docs/bringup_log.md",
    "docs/test_report.md",
    "docs/revision_history.md",
    "docs/user/README.md",
    "hardware/README.md",
    "hardware/altium_project/README.md",
    "hardware/outputs/README.md",
    "hardware/images/README.md",
    "firmware/README.md",
    "references/datasheets/README.md",
    "references/lcsc_parts/README.md",
)

TEMPLATE_STANDARD_HEADER_FILES = (
    "requirements.md",
    "block_diagram.md",
    "design_notes.md",
    "references.md",
    "docs/README.md",
    "docs/component_selection_plan.md",
    "docs/module_design/README.md",
    "docs/schematic_review.md",
    "docs/pcb_design_rules.md",
    "docs/pcb_review.md",
    "docs/bringup_log.md",
    "docs/test_report.md",
    "docs/revision_history.md",
    "docs/user/README.md",
    "hardware/README.md",
    "firmware/README.md",
)

TEMPLATE_HEADER_EXEMPT_FILES = (
    "hardware/altium_project/README.md",
    "hardware/outputs/README.md",
    "hardware/images/README.md",
    "references/datasheets/README.md",
    "references/lcsc_parts/README.md",
)

PROJECT_ONE_ROOT = "projects/01_STM32_DAQ_Control_Board"
PROJECT_ONE_ROOT_README = f"{PROJECT_ONE_ROOT}/README.md"

PROJECT_ONE_LEGACY_STAGE_EXEMPT_FILES = (
    f"{PROJECT_ONE_ROOT}/docs/revision_history.md",
    f"{PROJECT_ONE_ROOT}/references/lcsc_parts/lcsc_search_notes.md",
)

PROJECT_ONE_REMOVED_FILES = (
    f"{PROJECT_ONE_ROOT}/docs/component_selection.md",
    f"{PROJECT_ONE_ROOT}/docs/user/learning_record.md",
)

PROJECT_ONE_REQUIRED_SUPPORTING_FILES = (
    f"{PROJECT_ONE_ROOT}/docs/component_selection_plan.md",
    f"{PROJECT_ONE_ROOT}/docs/user/project_overview.md",
)

STANDARD_STATUS_FIELDS = (
    "文档状态",
    "适用阶段",
    "适用对象",
    "最后核对依据",
)

ROOT_README_STATUS_FIELDS = (
    "文档状态",
    "当前项目阶段",
    "当前硬件版本",
    "最后核对依据",
)

PROJECT_ONE_TOKENS = (
    "STM32F103C8T6",
    "AP2112K",
    "CH340C",
    "AO3400A",
    "VLOAD_EXT",
    "MOS_OUT",
    "59.563",
)

OPTIONAL_READMES_REMOVED_FROM_TEMPLATE = (
    "hardware/outputs/schematic_pdf/README.md",
    "hardware/outputs/bom/README.md",
    "hardware/outputs/netlist/README.md",
    "hardware/outputs/erc/README.md",
    "hardware/outputs/component_reports/README.md",
    "hardware/outputs/footprint_reports/README.md",
    "hardware/outputs/gerber/README.md",
    "hardware/outputs/drill/README.md",
    "hardware/outputs/pick_place/README.md",
    "hardware/outputs/fabrication_package/README.md",
    "hardware/images/pcb/README.md",
)

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ABSOLUTE_LOCAL_PATH = re.compile(
    r"(?i)(?<![A-Za-z0-9])(?:[A-Z]:[\\/]|/Users/|/home/|/mnt/[a-z]/)"
)
LEGACY_STAGE_MODEL = re.compile(r"(?:17\s*个?阶段|十七\s*个?阶段|阶段\s*17)")


class Validator:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.check_count = 0

    def check(self, condition: bool, path: str, reason: str) -> None:
        self.check_count += 1
        if not condition:
            self.errors.append(f"{path}: {reason}")

    def read(self, relative_path: str) -> str:
        return (ROOT / relative_path).read_text(encoding="utf-8")


def framework_markdown_files() -> list[Path]:
    files = [ROOT / name for name in ("PROJECT_RULES.md", "AGENTS.md", "README.md")]
    for directory in ("docs", "skills", "checklists", "templates"):
        files.extend((ROOT / directory).rglob("*.md"))
    files.extend((ROOT / PROJECT_ONE_ROOT).rglob("*.md"))
    return sorted(set(files))


def has_status_field(text: str, field: str) -> bool:
    return (
        re.search(
            rf"^>\s*{re.escape(field)}：",
            text,
            flags=re.MULTILINE,
        )
        is not None
    )


def check_required_files(validator: Validator) -> None:
    for relative_path in REQUIRED_COMMON_FILES:
        validator.check(
            (ROOT / relative_path).is_file(),
            relative_path,
            "缺少必需通用文件",
        )

    template_root = ROOT / "templates/hardware_project_template"
    for relative_path in REQUIRED_TEMPLATE_FILES:
        validator.check(
            (template_root / relative_path).is_file(),
            f"templates/hardware_project_template/{relative_path}",
            "缺少模板必需文件",
        )


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]
    return unquote(target.split("#", 1)[0])


def check_markdown_links(validator: Validator) -> None:
    for markdown_file in framework_markdown_files():
        text = markdown_file.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in MARKDOWN_LINK.finditer(line):
                target = normalize_link_target(match.group(1))
                if not target or target.startswith("#"):
                    continue
                if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
                    continue
                target_path = (markdown_file.parent / target).resolve()
                try:
                    target_path.relative_to(ROOT.resolve())
                except ValueError:
                    validator.check(
                        False,
                        f"{markdown_file.relative_to(ROOT)}:{line_number}",
                        f"相对链接越出仓库：{match.group(1)}",
                    )
                    continue
                validator.check(
                    target_path.exists(),
                    f"{markdown_file.relative_to(ROOT)}:{line_number}",
                    f"相对链接目标不存在：{match.group(1)}",
                )


def check_template_content(validator: Validator) -> None:
    template_root = ROOT / "templates/hardware_project_template"
    template_files = [path for path in template_root.rglob("*") if path.is_file()]

    for path in template_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        relative_path = str(path.relative_to(ROOT))
        for token in PROJECT_ONE_TOKENS:
            validator.check(
                token not in text,
                relative_path,
                f"模板包含项目 1 专属关键词：{token}",
            )
        validator.check(
            ABSOLUTE_LOCAL_PATH.search(text) is None,
            relative_path,
            "模板包含本地绝对路径",
        )

        if path.suffix.lower() == ".md" and path.resolve() != (
            template_root / "README.md"
        ).resolve():
            validator.check(
                not has_status_field(text, "当前阶段")
                and not has_status_field(text, "当前项目阶段"),
                relative_path,
                "模板根 README 以外的 Markdown 错误维护当前阶段状态头字段",
            )

        validator.check(
            re.search(
                r"^>\s*最近更新：\s*<YYYY-MM-DD>\s*$",
                text,
                flags=re.MULTILINE,
            )
            is None,
            relative_path,
            "模板仍强制维护“最近更新”日期占位",
        )

    root_readme = template_root / "README.md"
    root_text = root_readme.read_text(encoding="utf-8")
    for field in ROOT_README_STATUS_FIELDS:
        validator.check(
            has_status_field(root_text, field),
            str(root_readme.relative_to(ROOT)),
            f"项目根 README 缺少状态头字段：{field}",
        )
    validator.check(
        len(
            re.findall(
                r"^>\s*当前项目阶段：",
                root_text,
                flags=re.MULTILINE,
            )
        )
        == 1,
        str(root_readme.relative_to(ROOT)),
        "项目根 README 必须且只能维护一个“当前项目阶段”状态头字段",
    )
    validator.check(
        not has_status_field(root_text, "当前阶段"),
        str(root_readme.relative_to(ROOT)),
        "项目根 README 不得使用旧“当前阶段”状态头字段",
    )

    for relative_path in TEMPLATE_STANDARD_HEADER_FILES:
        path = template_root / relative_path
        text = path.read_text(encoding="utf-8")
        for field in STANDARD_STATUS_FIELDS:
            validator.check(
                has_status_field(text, field),
                str(path.relative_to(ROOT)),
                f"缺少标准状态头字段：{field}",
            )

    classified_template_files = {
        "README.md",
        *TEMPLATE_STANDARD_HEADER_FILES,
        *TEMPLATE_HEADER_EXEMPT_FILES,
    }
    actual_template_markdown = {
        path.relative_to(template_root).as_posix()
        for path in template_root.rglob("*.md")
    }
    validator.check(
        actual_template_markdown == classified_template_files,
        "templates/hardware_project_template",
        "模板 Markdown 未全部归入根 README、标准状态头列表或底层 README 豁免白名单",
    )

    for relative_path in OPTIONAL_READMES_REMOVED_FROM_TEMPLATE:
        validator.check(
            not (template_root / relative_path).exists(),
            f"templates/hardware_project_template/{relative_path}",
            "低信息量按需子目录 README 不应预建",
        )


def check_stage_model(validator: Validator) -> None:
    common_files = [
        ROOT / "PROJECT_RULES.md",
        ROOT / "AGENTS.md",
        ROOT / "README.md",
        *sorted((ROOT / "docs").rglob("*.md")),
        *sorted((ROOT / "skills").rglob("*.md")),
        *sorted((ROOT / "checklists").rglob("*.md")),
        *sorted((ROOT / "templates").rglob("*.md")),
    ]
    for path in common_files:
        text = path.read_text(encoding="utf-8")
        validator.check(
            LEGACY_STAGE_MODEL.search(text) is None,
            str(path.relative_to(ROOT)),
            "通用框架仍把旧 17 阶段作为当前模型",
        )

    workflow = validator.read("docs/08_Project_Workflow.md")
    readme = validator.read("README.md")
    for stage_number, stage_name in enumerate(CANONICAL_STAGES, start=1):
        validator.check(
            re.search(
                rf"^##\s+\d+\.\s+阶段\s*{stage_number}：{re.escape(stage_name)}\s*$",
                workflow,
                flags=re.MULTILINE,
            )
            is not None,
            "docs/08_Project_Workflow.md",
            f"八阶段名称缺失或不一致：阶段 {stage_number} {stage_name}",
        )
        validator.check(
            re.search(
                rf"^{stage_number}\.\s+{re.escape(stage_name)}\s*$",
                readme,
                flags=re.MULTILINE,
            )
            is not None,
            "README.md",
            f"仓库入口的八阶段名称不一致：阶段 {stage_number} {stage_name}",
        )


def check_skill_references(validator: Validator) -> None:
    skill_path = ROOT / "skills/hardware-pcb-layout-review/SKILL.md"
    skill_text = skill_path.read_text(encoding="utf-8")
    for checklist_name in (
        "pcb_layout_preflight_checklist.md",
        "pcb_layout_checklist.md",
        "pcb_release_checklist.md",
    ):
        validator.check(
            checklist_name in skill_text,
            str(skill_path.relative_to(ROOT)),
            f"PCB Skill 未引用 checklist：{checklist_name}",
        )
        validator.check(
            (ROOT / "checklists" / checklist_name).is_file(),
            f"checklists/{checklist_name}",
            "PCB Skill 引用的 checklist 不存在",
        )


def check_project_one_document_contract(validator: Validator) -> None:
    project_root = ROOT / PROJECT_ONE_ROOT
    project_markdown = sorted(project_root.rglob("*.md"))
    exempt_paths = set(PROJECT_ONE_LEGACY_STAGE_EXEMPT_FILES)
    legacy_stage = re.compile(r"阶段\s*(?:11|12)")
    dated_history_line = re.compile(r"^\|\s*\d{4}-\d{2}-\d{2}\s*\|")

    for path in project_markdown:
        relative_path = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")

        validator.check(
            not has_status_field(text, "当前阶段"),
            relative_path,
            "项目 1 Markdown 不得使用旧“当前阶段”状态头字段",
        )

        if relative_path != PROJECT_ONE_ROOT_README:
            validator.check(
                not has_status_field(text, "当前项目阶段"),
                relative_path,
                "项目 1 非根 README 不得维护“当前项目阶段”状态头字段",
            )

        legacy_lines = [
            line for line in text.splitlines() if legacy_stage.search(line)
        ]
        if relative_path in exempt_paths:
            for line in legacy_lines:
                validator.check(
                    dated_history_line.search(line) is not None,
                    relative_path,
                    "阶段 11 / 12 仅允许出现在明确日期化的历史记录行中",
                )
        else:
            validator.check(
                not legacy_lines,
                relative_path,
                "项目 1 非历史豁免文件仍使用阶段 11 / 12",
            )

    root_text = validator.read(PROJECT_ONE_ROOT_README)
    stage_field_count = len(
        re.findall(
            r"^>\s*当前项目阶段：",
            root_text,
            flags=re.MULTILINE,
        )
    )
    validator.check(
        stage_field_count == 1,
        PROJECT_ONE_ROOT_README,
        "项目根 README 必须且只能维护一个“当前项目阶段”状态头字段",
    )
    stage_fields = re.findall(
        r"^>\s*当前项目阶段：\s*阶段\s*(\d+)：([^\r\n]+?)\s*$",
        root_text,
        flags=re.MULTILINE,
    )
    validator.check(
        len(stage_fields) == 1,
        PROJECT_ONE_ROOT_README,
        "项目根 README 的“当前项目阶段”字段格式不正确",
    )
    if len(stage_fields) == 1:
        stage_number_text, stage_name = stage_fields[0]
        stage_number = int(stage_number_text)
        validator.check(
            stage_number in CANONICAL_STAGE_MAP,
            PROJECT_ONE_ROOT_README,
            "当前项目阶段编号必须为 1～8",
        )
        validator.check(
            CANONICAL_STAGE_MAP.get(stage_number) == stage_name,
            PROJECT_ONE_ROOT_README,
            "当前项目阶段编号和名称必须与八阶段标准完全对应",
        )

    for relative_path in PROJECT_ONE_REMOVED_FILES:
        validator.check(
            not (ROOT / relative_path).exists(),
            relative_path,
            "已合并或删除的项目 1 文档不应继续存在",
        )

    for relative_path in PROJECT_ONE_REQUIRED_SUPPORTING_FILES:
        validator.check(
            (ROOT / relative_path).is_file(),
            relative_path,
            "项目 1 必需保留的辅助文档不存在",
        )


def check_layout_checklist(validator: Validator) -> None:
    relative_path = "checklists/pcb_layout_checklist.md"
    text = validator.read(relative_path)
    required_keywords = (
        "审查对象与版本",
        "板框",
        "机械",
        "电源",
        "去耦",
        "回流",
        "换层",
        "过孔",
        "铺铜",
        "Repour",
        "丝印",
        "测试点",
        "可进入 PCB Release Review",
    )
    for keyword in required_keywords:
        validator.check(
            keyword in text,
            relative_path,
            f"Layout / Routing Checklist 缺少关键覆盖：{keyword}",
        )


def check_drc_policy(validator: Validator) -> None:
    preflight_path = ROOT / "checklists/pcb_layout_preflight_checklist.md"
    preflight = preflight_path.read_text(encoding="utf-8")
    forbidden_preflight_phrases = (
        "用户已运行初始 DRC",
        "初始 DRC 已运行",
        "通过 DRC 后才能布局",
        "用户运行初始 DRC",
        "记录初始 Warnings",
        "记录初始 Rule Violations",
    )
    for phrase in forbidden_preflight_phrases:
        validator.check(
            phrase not in preflight,
            str(preflight_path.relative_to(ROOT)),
            f"Layout Preflight 重新出现强制 DRC 项：{phrase}",
        )

    general_paths = (
        "PROJECT_RULES.md",
        "AGENTS.md",
        "README.md",
        "docs/Project_Structure_Standard.md",
        "docs/08_Project_Workflow.md",
        "docs/AI_Context_Guide.md",
        "docs/Project_Template_Guide.md",
        "skills/hardware-pcb-layout-review/SKILL.md",
        "checklists/pcb_layout_preflight_checklist.md",
    )
    mandatory_pre_layout_drc = re.compile(
        r"(?:正式布局|Layout)前(?:必须|要求)?[^。\n]*(?:运行|完成)初始?\s*DRC"
        r"|必须运行初始\s*DRC"
    )
    for relative_path in general_paths:
        text = validator.read(relative_path)
        validator.check(
            mandatory_pre_layout_drc.search(text) is None,
            relative_path,
            "通用规则重新要求正式布局前运行初始 DRC",
        )

    project_rules = validator.read("PROJECT_RULES.md")
    workflow = validator.read("docs/08_Project_Workflow.md")
    template_guide = validator.read("docs/Project_Template_Guide.md")
    template_rules = validator.read(
        "templates/hardware_project_template/docs/pcb_design_rules.md"
    )
    validator.check(
        "完整 Batch DRC 只在阶段 7" in project_rules,
        "PROJECT_RULES.md",
        "缺少完整 Batch DRC 仅在阶段 7 正式要求的规则",
    )
    validator.check(
        "阶段 6 不要求保存、导出或归档中间 DRC 记录" in workflow,
        "docs/08_Project_Workflow.md",
        "阶段 6 的中间 DRC 简化规则缺失",
    )
    validator.check(
        "中间 DRC 记录" not in template_guide,
        "docs/Project_Template_Guide.md",
        "模板指南仍把中间 DRC 记录列为阶段 6 输出",
    )
    validator.check(
        "| DRC 已验证 |" not in template_rules,
        "templates/hardware_project_template/docs/pcb_design_rules.md",
        "规则模板仍长期维护“DRC 已验证”列",
    )


def main() -> int:
    validator = Validator()
    check_required_files(validator)
    check_markdown_links(validator)
    check_template_content(validator)
    check_stage_model(validator)
    check_skill_references(validator)
    check_project_one_document_contract(validator)
    check_layout_checklist(validator)
    check_drc_policy(validator)

    if validator.errors:
        print(f"Repository framework validation failed: {len(validator.errors)} error(s)")
        for error in validator.errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Repository framework validation passed ({validator.check_count} checks).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
