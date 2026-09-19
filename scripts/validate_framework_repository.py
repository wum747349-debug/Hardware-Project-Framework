#!/usr/bin/env python3
"""Run the canonical full validation for the Hardware Project Framework."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "templates/hardware_project_template"
FINAL_REFERENCE_ROOT = ROOT / "examples/reference_project_v1"
FINAL_LEGACY_PROJECT_DIRS = (
    "projects/01_STM32_DAQ_Control_Board",
    "projects/02_LiIon_Charger_Protection_Board",
    "projects/03_STM32_OpAmp_ADC_Acquisition_Board",
)

REQUIRED_FRAMEWORK_FILES = (
    "PROJECT_RULES.md",
    "AGENTS.md",
    "README.md",
    "CHANGELOG.md",
    "docs/Project_Structure_Standard.md",
    "docs/08_Project_Workflow.md",
    "docs/AI_Context_Guide.md",
    "docs/Project_Template_Guide.md",
    "docs/Project_Initialization_Guide.md",
    "docs/Framework_Maintenance_and_Release_Guide.md",
    "docs/Framework_Migration_Guide.md",
    "skills/hardware-project-initialization/SKILL.md",
    "skills/hardware-firmware-development/SKILL.md",
    "checklists/project_initialization_checklist.md",
    "scripts/validate_project_repository.py",
    "scripts/validate_framework_repository.py",
    "templates/hardware_project_template/scripts/validate_project_repository.py",
    "templates/optional_firmware/AGENTS.md",
    ".github/workflows/repository-framework-check.yml",
)

REQUIRED_TEMPLATE_FILES = {
    "AGENTS.md",
    "FRAMEWORK.md",
    "PROJECT_RULES.md",
    "README.md",
    "requirements.md",
    "block_diagram.md",
    "design_notes.md",
    "references.md",
    "docs/README.md",
    "hardware/README.md",
    "references/README.md",
    "scripts/validate_project_repository.py",
}

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ABSOLUTE_LOCAL_PATH = re.compile(
    r"(?i)(?<![A-Za-z0-9])(?:[A-Z]:[\\/]|/Users/|/home/|/mnt/[a-z]/)"
)

LEGACY_PROJECT_RESIDUE = (
    "projects/01_STM32_DAQ_Control_Board",
    "projects/02_LiIon_Charger_Protection_Board",
    "projects/03_STM32_OpAmp_ADC_Acquisition_Board",
    "01_STM32_DAQ_Control_Board",
    "02_LiIon_Charger_Protection_Board",
    "03_STM32_OpAmp_ADC_Acquisition_Board",
    "STM32 DAQ Control Board",
    "Li-Ion Charger Protection Board",
    "STM32 OpAmp ADC Acquisition Board",
    "Hardware-Practice-Projects/projects",
)

SMOKE_STAGE_PATHS = (
    "docs/component_selection_plan.md",
    "docs/module_design",
    "docs/schematic_review.md",
    "docs/pcb_design_rules.md",
    "docs/pcb_review.md",
    "docs/bringup_log.md",
    "docs/test_report.md",
    "docs/revision_history.md",
)

RUNTIME_RULE_SEMANTIC_GUARDS = {
    1: (
        ("current Project facts", r"(?:Project facts|项目事实|fixture facts)"),
        ("current repository authority", r"(?:only\s+from|只(?:能)?来自)"),
    ),
    2: (
        ("FRAMEWORK.md binding", r"`?FRAMEWORK\.md`?"),
        ("Framework version identity", r"Framework\s+(?:version|版本)"),
        ("binding authority", r"(?:Release\s*\+\s*Commit|以.*为准|recorded in)"),
    ),
    3: (
        ("automatic-adoption prohibition", r"(?:不自动|do not (?:automatically|default))"),
        ("Framework main", r"Framework\s+`main`"),
    ),
    4: (
        ("explicit user request", r"(?:用户明确要求|explicit(?:ly)? request(?:ed)?)"),
        ("Pinned Framework Evaluation", r"Pinned Framework Evaluation"),
        ("Compatible Framework Sync", r"Compatible Framework Sync"),
        ("Framework Contract Migration", r"Framework Contract Migration"),
        ("applicable validation", r"validation"),
    ),
    5: (
        ("official documentation", r"(?:官方|official)"),
        ("datasheet", r"datasheet"),
        ("reference manual", r"reference manual"),
        ("application note", r"application note"),
    ),
    6: (
        ("SchDoc authority", r"\.SchDoc"),
        ("PcbDoc authority", r"\.PcbDoc"),
        ("EDA implementation authority", r"(?:authoritative|权威)"),
    ),
    7: (
        ("fabricated-result prohibition", r"(?:不得伪造|must not (?:fabricate|falsify))"),
        ("EDA result", r"EDA"),
        ("ERC result", r"ERC"),
        ("DRC result", r"DRC"),
        ("manufacturing result", r"Manufacturing"),
        ("test result", r"Test"),
    ),
    8: (
        ("Project Stage", r"(?:Project\s+stage|项目阶段)"),
        ("root README authority", r"README\.md"),
        ("single Stage authority", r"(?:only|只)"),
    ),
    9: (
        ("other Project boundary", r"(?:其他|another|other)\s+Project"),
        ("fact-source prohibition", r"(?:fact source|事实源)"),
    ),
    10: (
        ("current-task scope", r"(?:current task|当前任务)"),
        ("Stage Skill", r"Stage Skill"),
        ("minimum-read boundary", r"(?:Read only|只读取|所需|必要)"),
    ),
}


class Validator:
    def __init__(self, mode: str) -> None:
        self.mode = mode
        self.errors: list[str] = []
        self.check_count = 0

    def check(self, condition: bool, path: str, reason: str) -> None:
        self.check_count += 1
        if not condition:
            self.errors.append(f"{path}: {reason}")

    def read(self, relative_path: str) -> str:
        return (ROOT / relative_path).read_text(encoding="utf-8")


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]
    return unquote(target.split("#", 1)[0])


def framework_markdown_files() -> list[Path]:
    files = [ROOT / name for name in ("PROJECT_RULES.md", "AGENTS.md", "README.md", "CHANGELOG.md")]
    for directory in ("docs", "skills", "checklists", "templates"):
        files.extend((ROOT / directory).rglob("*.md"))
    return sorted(set(files))


def check_required_files(validator: Validator) -> None:
    for relative_path in REQUIRED_FRAMEWORK_FILES:
        validator.check((ROOT / relative_path).is_file(), relative_path, "missing required Framework file")

    actual_template_files = {
        path.relative_to(TEMPLATE_ROOT).as_posix()
        for path in TEMPLATE_ROOT.rglob("*")
        if path.is_file()
    }
    validator.check(actual_template_files == REQUIRED_TEMPLATE_FILES, "templates/hardware_project_template", "Template must contain exactly the Contract Required files")


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
                    validator.check(False, f"{markdown_file.relative_to(ROOT)}:{line_number}", f"relative link escapes Framework root: {match.group(1)}")
                    continue
                validator.check(target_path.exists(), f"{markdown_file.relative_to(ROOT)}:{line_number}", f"relative link target does not exist: {match.group(1)}")


def check_contract_authorities(validator: Validator) -> None:
    rules = validator.read("PROJECT_RULES.md")
    structure = validator.read("docs/Project_Structure_Standard.md")
    workflow = validator.read("docs/08_Project_Workflow.md")
    context = validator.read("docs/AI_Context_Guide.md")
    template_guide = validator.read("docs/Project_Template_Guide.md")
    init_guide = validator.read("docs/Project_Initialization_Guide.md")
    migration_guide = validator.read("docs/Framework_Migration_Guide.md")
    changelog = validator.read("CHANGELOG.md")
    init_skill = validator.read("skills/hardware-project-initialization/SKILL.md")
    init_checklist = validator.read("checklists/project_initialization_checklist.md")
    readme = validator.read("README.md")

    for phrase in (
        "Framework 定义硬件项目的方法和契约，不作为真实 Project 的活动事实源",
        "一个正式 Project 只能有一个活动权威仓库",
        "framework-pre-v1-migration",
        "禁止长期双写",
    ):
        validator.check(phrase in rules, "PROJECT_RULES.md", f"missing stable authority Contract: {phrase}")

    for field in (
        "Framework Repository:",
        "Framework Release:",
        "Framework Commit:",
        "Project Structure Version:",
        "Repository Model:",
        "Initialization Framework Release:",
        "Initialization Status:",
    ):
        validator.check(field in structure, "docs/Project_Structure_Standard.md", f"FRAMEWORK.md schema drift: {field}")

    for phrase in (
        "Required / Conditional / Stage-enabled",
        "`firmware/` 不再是所有项目 Required",
        "Project Structure Version: 1",
        "不默认跟随 Framework `main`",
        "Template 是实现",
    ):
        validator.check(phrase in structure, "docs/Project_Structure_Standard.md", f"structure Contract drift: {phrase}")

    validator.check("Gate 1.5 — Project Initialization & Requirements Baseline" in workflow, "docs/08_Project_Workflow.md", "Gate 1.5 canonical name missing")
    validator.check("Bootstrap 位于八阶段之前，不是 Stage 0" in workflow, "docs/08_Project_Workflow.md", "Bootstrap boundary drift")
    validator.check("migration provenance 可以保留" in workflow, "docs/08_Project_Workflow.md", "Gate 1.5 migration provenance boundary missing")
    for number, name in {
        1: "Requirements Definition",
        2: "Critical Component Selection",
        3: "Schematic Module Design and Capture",
        4: "Schematic Review",
        5: "PCB Layout",
        6: "Routing and Copper",
        7: "PCB Release Review",
        8: "Assembly, Bring-up and Hardware Test",
    }.items():
        validator.check(f"Stage {number} — {name}" in workflow, "docs/08_Project_Workflow.md", f"canonical Stage {number} missing")

    for layer in (
        "Layer 0 — Framework Binding",
        "Layer 1 — Runtime Rules",
        "Layer 2 — Project Facts",
        "Layer 3 — Stage Method",
    ):
        validator.check(layer in context, "docs/AI_Context_Guide.md", f"four-layer context drift: {layer}")
    validator.check("Project 不默认读取 Framework `main`" in context, "docs/AI_Context_Guide.md", "context routing allows Framework main")

    for phrase, path, text in (
        ("唯一开发源", "docs/Project_Template_Guide.md", template_guide),
        ("固定 Framework Release", "docs/Project_Initialization_Guide.md", init_guide),
        ("不自动升级", "docs/Framework_Migration_Guide.md", migration_guide),
        ("Framework v0.9 Executable Candidate", "CHANGELOG.md", changelog),
        ("Gate 1.5", "skills/hardware-project-initialization/SKILL.md", init_skill),
        ("No Premature Conclusions", "checklists/project_initialization_checklist.md", init_checklist),
        ("Framework v0.9", "README.md", readme),
    ):
        validator.check(phrase in text, path, f"Framework v0.9 alignment missing: {phrase}")


def check_firmware_capability(validator: Validator) -> None:
    skill_path = "skills/hardware-firmware-development/SKILL.md"
    template_path = "templates/optional_firmware/AGENTS.md"
    skill = validator.read(skill_path)
    optional_template = validator.read(template_path)
    agents = validator.read("AGENTS.md")
    context = validator.read("docs/AI_Context_Guide.md")
    template_guide = validator.read("docs/Project_Template_Guide.md")
    readme = validator.read("README.md")
    project_validator = validator.read("scripts/validate_project_repository.py")

    for phrase in (
        "Task Intent",
        "Stage 1 只确认项目是否需要 Firmware",
        "Framework 统一职责原则，不统一强制目录树",
        "不要机械要求全部 ISR 位于 BSP",
        "必要的有界等待必须有工程依据",
        "Build PASS 不能替代 Flash、Runtime、Logic Analyzer 或 Hardware Validation",
        "不建立新的 Firmware Gate",
    ):
        validator.check(phrase in skill, skill_path, f"Firmware method coverage missing: {phrase}")

    for phrase in (
        "Project 根 `AGENTS.md` 仍是启动入口",
        "绑定的 immutable Framework snapshot",
        "不要读取或依赖 Framework `main`",
        "不要求创建全部目录",
        "Build PASS 不等于 Flash、Runtime 或 Hardware Validation",
    ):
        validator.check(phrase in optional_template, template_path, f"Optional Firmware template boundary missing: {phrase}")

    for path, text in ((skill_path, skill), (template_path, optional_template)):
        validator.check(ABSOLUTE_LOCAL_PATH.search(text) is None, path, "Firmware capability contains a local absolute path")
        for forbidden in ("STM32F103", "TIM1", "SPI1", "DMA1", "512-sample", "CCR1", "CCR2", "CCR3", "CCR4"):
            validator.check(forbidden not in text, path, f"Firmware capability contains project-specific default: {forbidden}")

    validator.check("skills/hardware-firmware-development/SKILL.md" in agents, "AGENTS.md", "Firmware Skill routing missing")
    validator.check("hardware-firmware-development" in context, "docs/AI_Context_Guide.md", "Firmware task-intent routing missing")
    validator.check("templates/optional_firmware/AGENTS.md" in template_guide, "docs/Project_Template_Guide.md", "Optional Firmware template guidance missing")
    validator.check("templates/optional_firmware/AGENTS.md" in readme, "README.md", "Optional Firmware template navigation missing")
    validator.check("firmware/AGENTS.md" not in REQUIRED_TEMPLATE_FILES, "templates/hardware_project_template", "Optional Firmware local rules became a Required Template file")
    validator.check('"firmware/AGENTS.md"' not in project_validator, "scripts/validate_project_repository.py", "Project Validator requires the optional Firmware local rules")


def check_template_contract(validator: Validator) -> None:
    agents = (TEMPLATE_ROOT / "AGENTS.md").read_text(encoding="utf-8")
    rules = (TEMPLATE_ROOT / "PROJECT_RULES.md").read_text(encoding="utf-8")
    binding = (TEMPLATE_ROOT / "FRAMEWORK.md").read_text(encoding="utf-8")
    readme = (TEMPLATE_ROOT / "README.md").read_text(encoding="utf-8")

    for phrase in ("Read `FRAMEWORK.md` first", "bound Framework Release", "Do not default to Framework `main`", "Do not read another Project"):
        validator.check(phrase in agents, "templates/hardware_project_template/AGENTS.md", f"Project AGENTS contract drift: {phrase}")
    validator.check(len(re.findall(r"^\d+\. ", rules, flags=re.MULTILINE)) == 10, "templates/hardware_project_template/PROJECT_RULES.md", "Project Runtime Rules must contain ten rules")
    validator.check("Current Project Stage: Bootstrap" in readme, "templates/hardware_project_template/README.md", "Template must start at Bootstrap")
    validator.check("Repository Model: Standalone Project" in binding, "templates/hardware_project_template/FRAMEWORK.md", "Template binding model drift")

    for path in TEMPLATE_ROOT.rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        relative_path = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() == ".md":
            validator.check(ABSOLUTE_LOCAL_PATH.search(text) is None, relative_path, "Template contains a local absolute path")
        for token in LEGACY_PROJECT_RESIDUE:
            if path.suffix.lower() == ".md":
                validator.check(token not in text, relative_path, f"Template contains legacy Project residue: {token}")

    snapshot_text = (TEMPLATE_ROOT / "scripts/validate_project_repository.py").read_text(encoding="utf-8")
    validator.check("D:\\Hardware-Practice-Projects" not in snapshot_text, "templates/hardware_project_template/scripts/validate_project_repository.py", "Project Validator depends on the current local Framework path")


def check_project_runtime_rule_alignment(validator: Validator) -> None:
    structure_path = "docs/Project_Structure_Standard.md"
    structure = validator.read(structure_path)
    section_match = re.search(
        r"^## 5\.[^\n]*PROJECT_RULES\.md[^\n]*Contract\s*$\n(?P<body>.*?)(?=^##\s)",
        structure,
        flags=re.MULTILINE | re.DOTALL,
    )
    validator.check(section_match is not None, structure_path, "Project Runtime Rules Section 5 missing")

    sources = []
    if section_match is not None:
        sources.append((f"{structure_path} Section 5", section_match.group("body")))
    sources.extend(
        (
            ("templates/hardware_project_template/PROJECT_RULES.md", validator.read("templates/hardware_project_template/PROJECT_RULES.md")),
            ("examples/reference_project_v1/PROJECT_RULES.md", validator.read("examples/reference_project_v1/PROJECT_RULES.md")),
        )
    )

    expected_rule_numbers = set(RUNTIME_RULE_SEMANTIC_GUARDS)
    for path, text in sources:
        rules = {
            int(match.group("number")): match.group("body").strip()
            for match in re.finditer(
                r"^(?P<number>\d+)\.\s+(?P<body>.*?)(?=^\d+\.\s+|\Z)",
                text,
                flags=re.MULTILINE | re.DOTALL,
            )
        }
        validator.check(set(rules) == expected_rule_numbers, path, "Project Runtime Rules must preserve Rule #1-#10 identities")
        for number, semantic_guards in RUNTIME_RULE_SEMANTIC_GUARDS.items():
            rule = rules.get(number, "")
            for identity, pattern in semantic_guards:
                validator.check(
                    re.search(pattern, rule, flags=re.IGNORECASE) is not None,
                    path,
                    f"Runtime Rule #{number} semantic drift: missing {identity}",
                )

        if path != f"{structure_path} Section 5":
            validator.check(
                re.search(r"\bEvidence\b", rules.get(10, ""), flags=re.IGNORECASE) is not None,
                path,
                "Runtime Rule #10 semantic drift: missing task-required Evidence boundary",
            )


def check_validator_snapshot(validator: Validator) -> None:
    source = ROOT / "scripts/validate_project_repository.py"
    snapshot = TEMPLATE_ROOT / "scripts/validate_project_repository.py"
    if source.is_file() and snapshot.is_file():
        validator.check(source.read_bytes() == snapshot.read_bytes(), str(snapshot.relative_to(ROOT)), "Template Project Validator snapshot differs from the Framework development source")


def run_template_validator(validator: Validator) -> None:
    source = ROOT / "scripts/validate_project_repository.py"
    if not source.is_file():
        return
    result = subprocess.run(
        [sys.executable, str(source), str(TEMPLATE_ROOT), "--template"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    details = (result.stdout + result.stderr).strip()
    validator.check(result.returncode == 0, "scripts/validate_project_repository.py", f"Template fixture validation failed: {details}")


def run_fixture_validator(project_root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(project_root / "scripts/validate_project_repository.py"), *arguments],
        cwd=project_root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def prepare_stage_1_fixture(target: Path, framework_commit: str) -> None:
    shutil.copytree(TEMPLATE_ROOT, target)
    replacements = {
        "<PROJECT_NAME>": "Framework Validator Fixture",
        "<HARDWARE_REVISION>": "TEST-REV-A",
        "<FRAMEWORK_REPOSITORY>": "wum747349-debug/Hardware-Project-Framework",
        "<FRAMEWORK_RELEASE>": "development-v0.9",
        "<FRAMEWORK_COMMIT>": framework_commit,
        "<PROJECT_STRUCTURE_VERSION>": "1",
        "<INITIALIZATION_FRAMEWORK_RELEASE>": "development-v0.9",
        "<INITIALIZATION_STATUS>": "Gate 1.5 Pending",
    }
    for markdown_file in target.rglob("*.md"):
        text = markdown_file.read_text(encoding="utf-8")
        for placeholder, value in replacements.items():
            text = text.replace(placeholder, value)
        markdown_file.write_text(text, encoding="utf-8")

    readme = target / "README.md"
    readme.write_text(
        readme.read_text(encoding="utf-8").replace(
            "Current Project Stage: Bootstrap",
            "Current Project Stage: Stage 1 — Requirements Definition",
        ),
        encoding="utf-8",
    )


def initialize_fixture(target: Path) -> None:
    binding = target / "FRAMEWORK.md"
    binding.write_text(
        binding.read_text(encoding="utf-8").replace(
            "Initialization Status: Gate 1.5 Pending",
            "Initialization Status: Initialized",
        ),
        encoding="utf-8",
    )


def set_fixture_stage(target: Path, stage_number: int, stage_name: str) -> None:
    readme = target / "README.md"
    readme.write_text(
        re.sub(
            r"^Current Project Stage: .*?$",
            f"Current Project Stage: Stage {stage_number} — {stage_name}",
            readme.read_text(encoding="utf-8"),
            flags=re.MULTILINE,
        ),
        encoding="utf-8",
    )


def set_fixture_binding(target: Path, release: str, commit: str) -> None:
    binding = target / "FRAMEWORK.md"
    text = binding.read_text(encoding="utf-8")
    text = re.sub(r"^Framework Release: .*?$", f"Framework Release: {release}", text, flags=re.MULTILINE)
    text = re.sub(r"^Framework Commit: .*?$", f"Framework Commit: {commit}", text, flags=re.MULTILINE)
    text = re.sub(r"^Initialization Framework Release: .*?$", f"Initialization Framework Release: {release}", text, flags=re.MULTILINE)
    binding.write_text(text, encoding="utf-8")


def check_project_smoke_tests(validator: Validator) -> None:
    commit_result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    framework_commit = commit_result.stdout.strip()
    validator.check(
        commit_result.returncode == 0 and re.fullmatch(r"[0-9a-f]{40}", framework_commit) is not None,
        "git rev-parse HEAD",
        "Smoke fixtures require the current immutable Framework commit",
    )
    if commit_result.returncode != 0 or re.fullmatch(r"[0-9a-f]{40}", framework_commit) is None:
        return

    temporary_path: Path | None = None
    with tempfile.TemporaryDirectory(prefix="framework-validator-", dir=ROOT) as temporary_directory:
        temporary_path = Path(temporary_directory)

        clean_project = temporary_path / "clean-bootstrap"
        prepare_stage_1_fixture(clean_project, framework_commit)
        validator.check(not (clean_project / "firmware").exists(), "Clean Bootstrap Smoke", "Conditional firmware directory was pre-created")
        validator.check(
            not any((clean_project / path).exists() for path in SMOKE_STAGE_PATHS),
            "Clean Bootstrap Smoke",
            "Stage-enabled content was pre-created",
        )
        gate_result = run_fixture_validator(clean_project, "--gate-1-5")
        gate_details = (gate_result.stdout + gate_result.stderr).strip()
        validator.check(gate_result.returncode == 0, "Clean Bootstrap Smoke", f"Gate 1.5 Pending validation failed: {gate_details}")

        initialize_fixture(clean_project)
        initialized_gate_result = run_fixture_validator(clean_project, "--gate-1-5")
        initialized_gate_details = (initialized_gate_result.stdout + initialized_gate_result.stderr).strip()
        validator.check(
            initialized_gate_result.returncode != 0 and "Gate 1.5 Pending" in initialized_gate_details,
            "Clean Bootstrap Smoke",
            f"Gate mode accepted a pre-Initialized fixture: {initialized_gate_details}",
        )
        normal_result = run_fixture_validator(clean_project)
        normal_details = (normal_result.stdout + normal_result.stderr).strip()
        validator.check(normal_result.returncode == 0, "Clean Bootstrap Smoke", f"Initialized normal validation failed: {normal_details}")

        valid_bindings = (
            "development-v0.9",
            "development-v1.1.0",
            "development-v1.2.0",
            "development-v2.0.0",
            "hardware-project-framework-v1.1.0",
            "hardware-project-framework-v1.1.0-rc1",
        )
        for release in valid_bindings:
            binding_project = temporary_path / f"binding-valid-{release}"
            shutil.copytree(clean_project, binding_project)
            set_fixture_binding(binding_project, release, framework_commit)
            result = run_fixture_validator(binding_project)
            details = (result.stdout + result.stderr).strip()
            validator.check(result.returncode == 0, "Framework Binding Regression", f"valid binding rejected: {release}: {details}")

        invalid_bindings = (
            ("main", framework_commit),
            ("HEAD", framework_commit),
            ("latest", framework_commit),
            ("development-v1.1", framework_commit),
            ("development-v1.1.0", framework_commit[:12]),
        )
        for index, (release, commit) in enumerate(invalid_bindings):
            binding_project = temporary_path / f"binding-invalid-{index}"
            shutil.copytree(clean_project, binding_project)
            set_fixture_binding(binding_project, release, commit)
            result = run_fixture_validator(binding_project)
            validator.check(result.returncode != 0, "Framework Binding Regression", f"invalid binding accepted: {release} @ {commit}")

        stage_enabled_project = temporary_path / "stage-enabled-semantics"
        prepare_stage_1_fixture(stage_enabled_project, framework_commit)
        initialize_fixture(stage_enabled_project)
        stage_documents = {
            "docs/component_selection_plan.md": (
                "# Component Selection Plan Fixture\n\n"
                "Status: Pending current component-selection work.\n\n"
                "## Record Responsibility\n\n"
                "Own the fixture's current critical-component candidates, sources, decisions, and open questions.\n"
            ),
            "docs/module_design/fixture.md": (
                "# Owning Module Design Fixture\n\n"
                "Status: Pending current detailed design work.\n\n"
                "## Record Responsibility\n\n"
                "Own the fixture's current module design basis, open calculations, interfaces, and verification needs.\n"
            ),
        }
        for relative_path, content in stage_documents.items():
            document = stage_enabled_project / relative_path
            document.parent.mkdir(parents=True, exist_ok=True)
            document.write_text(content, encoding="utf-8")

        set_fixture_stage(stage_enabled_project, 3, "Schematic Module Design and Capture")
        stage_3_result = run_fixture_validator(stage_enabled_project)
        stage_3_details = (stage_3_result.stdout + stage_3_result.stderr).strip()
        validator.check(stage_3_result.returncode == 0, "Stage Transition Regression", f"valid Stage 3 fixture failed: {stage_3_details}")

        set_fixture_stage(stage_enabled_project, 4, "Schematic Review")
        stage_4_missing_result = run_fixture_validator(stage_enabled_project)
        stage_4_missing_details = (stage_4_missing_result.stdout + stage_4_missing_result.stderr).strip()
        validator.check(
            stage_4_missing_result.returncode != 0 and "docs/schematic_review.md" in stage_4_missing_details,
            "Stage Transition Regression",
            f"Stage 4 accepted missing schematic_review.md: {stage_4_missing_details}",
        )
        (stage_enabled_project / "docs/schematic_review.md").write_text(
            "# Schematic Review Fixture\n\n"
            "Status: Pending Formal Schematic Review.\n\n"
            "## Record Responsibility\n\n"
            "Record the review scope, evidence, findings, limitations, and eventual Stage exit conclusion.\n",
            encoding="utf-8",
        )
        stage_4_result = run_fixture_validator(stage_enabled_project)
        stage_4_details = (stage_4_result.stdout + stage_4_result.stderr).strip()
        validator.check(stage_4_result.returncode == 0, "Stage Transition Regression", f"initialized Stage 4 fixture failed: {stage_4_details}")

        set_fixture_stage(stage_enabled_project, 5, "PCB Layout")
        stage_5_missing_result = run_fixture_validator(stage_enabled_project)
        stage_5_missing_details = (stage_5_missing_result.stdout + stage_5_missing_result.stderr).strip()
        validator.check(
            stage_5_missing_result.returncode != 0 and "docs/pcb_design_rules.md" in stage_5_missing_details,
            "Stage Transition Regression",
            f"Stage 5 accepted missing pcb_design_rules.md: {stage_5_missing_details}",
        )
        (stage_enabled_project / "docs/pcb_design_rules.md").write_text(
            "# PCB Design Rules Fixture\n\n"
            "Status: Pending Layout Preflight.\n\n"
            "## Record Responsibility\n\n"
            "Own the verified manufacturing, mechanical, placement, routing, and rule baseline.\n\n"
            "## Current Rule Values\n\n"
            "TBD — Pending Layout Preflight; no engineering values are asserted by this fixture.\n",
            encoding="utf-8",
        )
        stage_5_result = run_fixture_validator(stage_enabled_project)
        stage_5_details = (stage_5_result.stdout + stage_5_result.stderr).strip()
        validator.check(
            stage_5_result.returncode == 0 and not (stage_enabled_project / "docs/pcb_review.md").exists(),
            "Stage-enabled Semantics Smoke",
            f"Stage 5 incorrectly required pcb_review.md before review activity: {stage_5_details}",
        )

        reusable_review_project = temporary_path / "stage-5-existing-pcb-review"
        shutil.copytree(stage_enabled_project, reusable_review_project)
        reusable_review = reusable_review_project / "docs/pcb_review.md"
        reusable_review.write_text(
            "# PCB Review Fixture\n\n"
            "Status: Pending Layout Preflight review.\n\n"
            "## Record Responsibility\n\n"
            "Maintain the durable Stage 5-7 review record without asserting an engineering result.\n",
            encoding="utf-8",
        )
        reusable_content = reusable_review.read_bytes()
        reusable_stage_5_result = run_fixture_validator(reusable_review_project)
        reusable_stage_5_details = (reusable_stage_5_result.stdout + reusable_stage_5_result.stderr).strip()
        validator.check(
            reusable_stage_5_result.returncode == 0,
            "Stage Transition Regression",
            f"Stage 5 rejected an existing Preflight review record: {reusable_stage_5_details}",
        )
        set_fixture_stage(reusable_review_project, 6, "Routing and Copper")
        reusable_stage_6_result = run_fixture_validator(reusable_review_project)
        reusable_stage_6_details = (reusable_stage_6_result.stdout + reusable_stage_6_result.stderr).strip()
        validator.check(
            reusable_stage_6_result.returncode == 0
            and reusable_review.read_bytes() == reusable_content
            and len(list((reusable_review_project / "docs").glob("pcb_review*.md"))) == 1,
            "Stage Transition Regression",
            f"Stage 6 failed to reuse the existing pcb_review.md: {reusable_stage_6_details}",
        )

        set_fixture_stage(stage_enabled_project, 6, "Routing and Copper")
        stage_6_missing_result = run_fixture_validator(stage_enabled_project)
        stage_6_missing_details = (stage_6_missing_result.stdout + stage_6_missing_result.stderr).strip()
        validator.check(
            stage_6_missing_result.returncode != 0 and "docs/pcb_review.md" in stage_6_missing_details,
            "Stage Transition Regression",
            f"Stage 6 accepted missing pcb_review.md: {stage_6_missing_details}",
        )
        (stage_enabled_project / "docs/pcb_review.md").write_text(
            "# PCB Review Fixture\n\n"
            "Status: Pending Routing and Copper review.\n\n"
            "## Record Responsibility\n\n"
            "Maintain the durable Stage 6-7 review scope, evidence, findings, limitations, and decisions.\n",
            encoding="utf-8",
        )
        stage_6_result = run_fixture_validator(stage_enabled_project)
        stage_6_details = (stage_6_result.stdout + stage_6_result.stderr).strip()
        validator.check(
            stage_6_result.returncode == 0,
            "Stage Transition Regression",
            f"initialized Stage 6 fixture failed: {stage_6_details}",
        )

        set_fixture_stage(stage_enabled_project, 8, "Assembly, Bring-up and Hardware Test")
        stage_8_result = run_fixture_validator(stage_enabled_project)
        stage_8_details = (stage_8_result.stdout + stage_8_result.stderr).strip()
        validator.check(
            stage_8_result.returncode == 0
            and not (stage_enabled_project / "docs/bringup_log.md").exists()
            and not (stage_enabled_project / "docs/test_report.md").exists(),
            "Stage-enabled Semantics Smoke",
            f"Stage 8 incorrectly required bring-up/test records before those activities: {stage_8_details}",
        )

        migration_project = temporary_path / "migration-provenance"
        prepare_stage_1_fixture(migration_project, framework_commit)
        migration_readme = migration_project / "README.md"
        migration_readme.write_text(
            migration_readme.read_text(encoding="utf-8")
            + "\n## Migration Provenance\n\n"
            + "Source Repository: wum747349-debug/Hardware-Practice-Projects\n\n"
            + "Legacy Project Path: projects/02_LiIon_Charger_Protection_Board\n\n"
            + "Git History Strategy: Clean Import\n",
            encoding="utf-8",
        )
        migration_gate_result = run_fixture_validator(migration_project, "--gate-1-5")
        migration_gate_details = (migration_gate_result.stdout + migration_gate_result.stderr).strip()
        validator.check(
            migration_gate_result.returncode == 0,
            "Migration Provenance Smoke",
            f"Legal migration provenance was rejected: {migration_gate_details}",
        )

        initialize_fixture(migration_project)
        migration_normal_result = run_fixture_validator(migration_project)
        migration_normal_details = (migration_normal_result.stdout + migration_normal_result.stderr).strip()
        validator.check(
            migration_normal_result.returncode == 0,
            "Migration Provenance Smoke",
            f"Initialized migration fixture failed: {migration_normal_details}",
        )

        migration_readme.write_text(
            migration_readme.read_text(encoding="utf-8")
            + "\nFramework Runtime Path: ../Hardware-Practice-Projects/projects/02_LiIon_Charger_Protection_Board\n",
            encoding="utf-8",
        )
        illegal_result = run_fixture_validator(migration_project)
        illegal_details = (illegal_result.stdout + illegal_result.stderr).strip()
        validator.check(
            illegal_result.returncode != 0 and "runtime path/dependency" in illegal_details,
            "Illegal Runtime Dependency Negative Test",
            f"Illegal runtime dependency was not rejected by the expected check: {illegal_details}",
        )

    if temporary_path is not None:
        validator.check(not temporary_path.exists(), "Temporary Project Fixtures", "Smoke-test temporary directory was not removed")


def check_full_mode(validator: Validator) -> None:
    if validator.mode not in {"full", "final"}:
        return
    reference_path = FINAL_REFERENCE_ROOT.relative_to(ROOT).as_posix()
    validator.check(FINAL_REFERENCE_ROOT.is_dir(), reference_path, "Full validation requires the Reference Project")
    if FINAL_REFERENCE_ROOT.is_dir():
        actual_reference_files = {
            path.relative_to(FINAL_REFERENCE_ROOT).as_posix()
            for path in FINAL_REFERENCE_ROOT.rglob("*")
            if path.is_file()
        }
        validator.check(
            actual_reference_files == REQUIRED_TEMPLATE_FILES,
            reference_path,
            "Full validation Reference Project must remain a lightweight Required-files-only fixture",
        )
        reference_readme = (FINAL_REFERENCE_ROOT / "README.md").read_text(encoding="utf-8")
        for phrase in (
            "Fixture Type: Synthetic Framework documentation and regression fixture",
            "Authority Status: Not an Active Project Authority",
            "Current Project Stage: Bootstrap",
        ):
            validator.check(phrase in reference_readme, f"{reference_path}/README.md", f"Final Reference Project boundary missing: {phrase}")

        source = ROOT / "scripts/validate_project_repository.py"
        reference_snapshot = FINAL_REFERENCE_ROOT / "scripts/validate_project_repository.py"
        validator.check(
            reference_snapshot.is_file() and source.read_bytes() == reference_snapshot.read_bytes(),
            f"{reference_path}/scripts/validate_project_repository.py",
            "Final Reference Project validator snapshot differs from the Framework development source",
        )
        result = subprocess.run(
            [sys.executable, str(source), str(FINAL_REFERENCE_ROOT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        details = (result.stdout + result.stderr).strip()
        validator.check(result.returncode == 0, reference_path, f"Final Reference Project validation failed: {details}")

    tracked_result = subprocess.run(
        ["git", "ls-files", "--cached", "--", "projects"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    tracked_projects = set(tracked_result.stdout.splitlines())
    validator.check(tracked_result.returncode == 0, "projects", "Full validation could not inspect tracked current-tree content")
    validator.check("projects/README.md" in tracked_projects, "projects/README.md", "Full validation requires the lightweight Legacy history marker")
    for legacy_directory in FINAL_LEGACY_PROJECT_DIRS:
        validator.check(
            not any(path == legacy_directory or path.startswith(f"{legacy_directory}/") for path in tracked_projects),
            legacy_directory,
            "Full validation forbids tracked Legacy real-project copies",
        )


def validate(mode: str) -> Validator:
    validator = Validator(mode)
    check_required_files(validator)
    check_markdown_links(validator)
    check_contract_authorities(validator)
    check_firmware_capability(validator)
    check_template_contract(validator)
    check_project_runtime_rule_alignment(validator)
    check_validator_snapshot(validator)
    run_template_validator(validator)
    check_project_smoke_tests(validator)
    check_full_mode(validator)
    return validator


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("full", "final", "v0.9"),
        default="full",
        help="full is canonical; final is a compatibility alias; v0.9 retains the legacy reduced check set",
    )
    args = parser.parse_args(argv)
    validator = validate(args.mode)
    if validator.errors:
        print(f"Framework repository validation failed: {len(validator.errors)} error(s)")
        for error in validator.errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Framework repository validation passed ({validator.check_count} checks, mode={args.mode}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
