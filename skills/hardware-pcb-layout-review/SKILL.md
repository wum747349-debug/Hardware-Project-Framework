---
name: hardware-pcb-layout-review
description: Review low-voltage embedded PCB readiness, layout, routing, copper, DRC evidence, and manufacturing release. Use for PCB Layout Preflight, placement or routing assistance, PCB visual review, Altium rule Scope/Priority review, DRC report analysis, rule exemptions, Gerber/drill/pick-place package checks, or deciding whether a board is ready for fabrication.
---

# Hardware PCB Layout and Release Review

## Purpose

Apply one of three modes:

1. **Layout Preflight**: confirm manufacturing, mechanical, footprint, rule, and schematic prerequisites before formal placement.
2. **Layout / Routing Review**: review placement, critical paths, routing, return paths, vias, and copper during PCB implementation.
3. **PCB Release Review**: review complete DRC evidence, assembly details, manufacturing outputs, exemptions, and fabrication release.

Keep the Skill focused on method and decision logic. Route item-by-item checks to:

- `checklists/pcb_layout_preflight_checklist.md`
- `checklists/pcb_layout_checklist.md`
- `checklists/pcb_release_checklist.md`

Record project values in `requirements.md` and `docs/pcb_design_rules.md`; record actual issues, evidence, DRC results, closure state, exemptions, and release conclusions in `docs/pcb_review.md`.

## Applicability

Use for low-voltage embedded, MCU control, sensor acquisition, power management, analog front-end, and communication interface boards.

For high voltage, RF, advanced high-speed digital, isolated power, automotive, medical, safety-certified, HDI, flex/rigid-flex, or other specialized construction, use this Skill only for the common baseline. Require a project-specific Skill, checklist, qualified reviewer, and applicable standards before release.

## Select the mode

Choose the narrowest mode that matches the request:

| Request | Mode | Required conclusion |
|---|---|---|
| “Can I start PCB layout?” or rule preparation | Layout Preflight | Approved / not approved for formal placement |
| Placement, routing, copper, return path, or PCB image review | Layout / Routing Review | Findings and required rework before release review |
| DRC, Gerber, drill, coordinates, manufacturing package, or release | PCB Release Review | Approved / not approved for fabrication |

If a request crosses modes, execute them in order and keep each gate separate. Do not let a later artifact compensate for a failed earlier gate.

## Read minimum context

Read:

1. `PROJECT_RULES.md`
2. `AGENTS.md`
3. `docs/AI_Context_Guide.md`
4. `skills/hardware-pcb-layout-review/SKILL.md`
5. Current project `requirements.md`
6. Current project `design_notes.md`
7. Current project `references.md`
8. Current project `docs/pcb_design_rules.md`
9. Current PCB review file, normally `docs/pcb_review.md`
10. Current PCB implementation evidence supplied for the request

Read conditionally:

- complete schematic PDF and current BOM when tracing connectivity, footprint, polarity, interface, or schematic-review issues;
- current module documents when a finding depends on module intent or special placement;
- key-device datasheets and application notes when checking layout, thermal, bypass, crystal, analog, USB, MOSFET, or protection requirements;
- target fabricator official capabilities when defining manufacturing or project design rules and checking order parameters;
- PCB top/bottom, copper, no-polygon, 3D, mechanical, or local screenshots when visual evidence is needed;
- DRC summary, report, messages, or screenshots when analyzing actual violations;
- Gerber, PTH/NPTH drill, pick-and-place, assembly drawing, BOM, stackup, and fabrication notes during release review.

Do not load other projects, all datasheets, all Skills, or all historical outputs by default. Do not load the reference implementation merely to obtain default values.

## Respect capability boundaries

- Treat `.PcbDoc` as the authoritative PCB implementation source.
- Without a reliable Altium parser, script, or automation interface, do not claim to have read internal objects, nets, rules, layers, polygons, dimensions, or properties from `.PcbDoc`.
- Use PCB images only for visual findings such as placement, apparent routing, accessibility, labeling, polarity visibility, and obvious mechanical concerns.
- Do not use images to prove connectivity, exact clearance, trace width, hole diameter, annular ring, rule matching, polygon state, unrouted count, or DRC pass.
- Do not claim to run Altium Designer, configure rules, route traces, Repour polygons, run Batch DRC, or export manufacturing files.
- Require the user to perform actual rule configuration, placement, routing, copper work, Repour, DRC, and export.
- Mark unsupported implementation claims as `待 EDA 核对`.
- Distinguish “documented rule,” “user-confirmed AD rule,” and “DRC-verified rule.”

## Build the manufacturing baseline

1. Identify the target fabricator and obtain official capability information for the relevant service and date.
2. Record material, layer count, finished thickness, copper weight, assembly method, surface finish, solder-mask needs, panel or dimension constraints, and controlled-impedance declaration.
3. Separate three levels:

   - **Manufacturing capability**: the fabricator-supported range for a selected service.
   - **Project design default**: the normal value chosen with reliability, cost, assembly, and process margin.
   - **Manufacturing limit**: an edge condition that may require special pricing, process, approval, or reduced yield margin.

4. Do not copy a manufacturing limit into a default design rule without a documented reason and margin assessment.
5. Store the baseline summary in `requirements.md`; store executable project rules in `docs/pcb_design_rules.md`.
6. Recheck current official capability before ordering. Treat marketplace promotions, quotes, and free-service conditions as temporary order data, not repository defaults.

## Organize PCB rules

Cover only categories relevant to the project:

- Electrical Clearance
- Routing Width
- Routing Via Style
- Hole Size
- Minimum Annular Ring
- Solder Mask
- Paste Mask
- Silkscreen
- Board Outline / Board Clearance
- Polygon Connect
- differential, impedance, length, high-speed, analog, power, load, or other conditional rules when actually required

For each rule, record:

- source and rationale;
- units;
- preferred, minimum, and maximum values when meaningful;
- query Scope;
- Priority;
- relationship to default and other specialized rules;
- document-defined, AD-configured, Scope-checked, Priority-checked, and DRC-verified status.

Do not create complex classes, differential pairs, length matching, or impedance rules unless the project requires them.

## Choose Net Class or explicit Scope

Use a Net Class when several nets:

- share the same electrical and routing treatment;
- are stable enough to manage as a group;
- benefit from readable, auditable class membership.

Use an explicit network Scope when:

- only one or a few nets require a narrow exception;
- membership is unlikely to be reused;
- an explicit query is clearer and less error-prone.

Before choosing either:

1. list the target nets and required behavior;
2. confirm names against user-provided EDA evidence;
3. ensure the Scope matches only intended objects;
4. avoid broad wildcards unless their expansion is reviewed;
5. record the choice in `docs/pcb_design_rules.md`.

## Check Scope

For each rule:

1. Read the query as a set definition.
2. Identify intended object types, layers, nets, classes, components, regions, or pair relationships.
3. Ask the user to highlight or report matching objects in Altium when direct inspection is unavailable.
4. Test representative intended and unintended objects.
5. Check for empty Scope, overly broad matching, name mismatch, missing class membership, or layer mismatch.
6. Confirm that a specialized rule does not silently include unrelated objects.
7. Mark the rule `Scope 已核对` only with user confirmation or suitable EDA evidence.

## Check Priority and rule coverage

1. List rules from most specific to most general for each category.
2. Place intentional specialized rules above overlapping default rules.
3. Confirm that a default rule covers all objects not matched by a specialized rule.
4. Check for equal-category overlaps, gaps, disabled rules, conflicting constraints, and a broad rule shadowing a narrow rule.
5. Use Altium rule-priority or applicable-rule inspection supplied by the user as evidence.
6. Record the coverage relationship:

```text
specialized rule -> intended subset
default rule     -> remaining objects
```

7. Do not mark Priority verified from the document order alone.

## Execute Layout Preflight

Use `checklists/pcb_layout_preflight_checklist.md`.

1. Confirm project/version and schematic-review gate.
2. Confirm fabricator, stackup baseline, assembly, board outline, mounting holes, mechanical boundaries, connector orientation, and accessibility.
3. Confirm critical footprints, Pin/Pad mapping, polarity, Pin 1, and mechanical models.
4. Extract critical-device mechanical and Layout requirements.
5. Define network classification, Net Classes or explicit Scopes.
6. Complete project rule categories, Scope, Priority, and coverage.
7. Require user confirmation that actual Altium rules are configured and checked.
8. Require an initial DRC run.
9. Record an explicit approval or refusal to start formal placement.

Do not approve formal placement while a required gate is unconfirmed or a high-risk schematic issue remains open.

## Review placement

Review in this order:

1. board outline, mounting holes, keepouts, dimensions, height, and enclosure constraints;
2. connector position, orientation, insertion path, cable clearance, and user access;
3. power entry, protection, switching, regulation, and main load-current flow;
4. functional partitioning and cross-domain boundaries;
5. MCU/core devices, clocks, reset, boot, debug, and local bypass;
6. analog input, reference, ADC, op-amp, and sensor regions;
7. USB, other high-speed interfaces, ESD, and return path;
8. MOSFET, flyback/protection, load connector, gate loop, and thermal copper;
9. test points, indicators, buttons, programming headers, rework, and probing space;
10. assembly side, component spacing, polarity, Pin 1, and silkscreen feasibility.

Separate visual findings from EDA-verifiable findings.

## Review routing and copper

Review in this order:

1. critical power and load-current loops;
2. sensitive analog and reference paths;
3. crystal and clock loops;
4. high-speed or edge-sensitive interfaces;
5. reset, boot, debug, and communication signals;
6. remaining low-speed signals;
7. return paths under each critical route;
8. via count, transitions, stubs, neck-downs, current bottlenecks, and layer changes;
9. plane continuity, splits, slots, copper islands, thermal connections, and stitching;
10. Repour status, unrouted count, and intermediate DRC.

Require the user to Repour after relevant changes. Do not infer current polygon results from an outdated screenshot.

## Apply specialty checks

### Power and load paths

- Trace source-to-load and return loops.
- Check bottlenecks at pads, vias, fuses, switches, connectors, pours, and neck-downs.
- Assess voltage drop, current density, thermal spreading, and fault-current consequences using project-specific data.

### Analog

- Protect high-impedance and low-level nodes from noisy current loops.
- Check reference, bias, filter, guard, grounding, and ADC source-impedance requirements against datasheets.
- Keep placement and return strategy consistent with the intended signal chain.

### High-speed and USB

- Confirm whether impedance, differential pair, length, or skew rules are actually declared.
- Check connector-to-protection-to-receiver order, pair continuity, return path, layer changes, and stubs.
- Do not impose impedance or length rules on a project that explicitly does not require them.

### Crystal

- Follow MCU/crystal vendor placement and routing guidance.
- Keep the loop compact, symmetric where required, isolated from aggressors, and free of unnecessary vias.
- Verify load components and ground treatment from current device evidence.

### MOSFET and switched loads

- Review gate drive loop, default-off state, switching node area, source return, flyback path, connector current path, and heat spreading.
- Confirm inductive-load protection direction and energy/current capability from datasheets.

## Analyze DRC evidence

1. Record the `.PcbDoc` or Git version, run date, rule baseline, and user confirmation that a complete Batch DRC was run.
2. Record total Warnings and Rule Violations.
3. Check that required categories were enabled; zero violations under an incomplete rule set is not a release pass.
4. Group findings by rule category and affected object.
5. For each finding, determine whether the cause is:

   - a real implementation violation;
   - incorrect Scope;
   - incorrect Priority or rule overlap;
   - stale polygon or missing Repour;
   - intentional exception requiring review;
   - incomplete or mismatched evidence.

6. Fix the design or rule definition at its source; rerun Repour and complete Batch DRC as applicable.
7. Preserve unresolved items and rerun evidence. Do not accept cropped “0 violations” evidence without version and rule context for release.

## Record rule exemptions

Use a table with:

| ID | Rule | Object | Reason | Risk | Verification | Approver / evidence | Status |
|---|---|---|---|---|---|---|---|

Require every exemption to be:

- narrow and object-specific;
- technically justified rather than used to hide errors;
- assessed for manufacturing, electrical, mechanical, and assembly risk;
- verified by an appropriate method;
- approved by the user;
- recorded in `docs/pcb_design_rules.md` and referenced from `docs/pcb_review.md`.

Do not convert a project design choice, such as intentionally not declaring impedance, into a false “rule exemption.”

## Check manufacturing outputs

During PCB Release Review:

1. confirm all outputs come from the same approved PCB version;
2. inspect the output manifest and naming;
3. verify expected Gerber layers, outline handling, solder mask, paste, and silkscreen;
4. verify separate and complete PTH/NPTH drill outputs where applicable;
5. verify coordinate units, origin, side, rotation convention, and component population;
6. cross-check BOM designators, quantities, values/models, manufacturer part numbers where required, and PCB Footprints;
7. confirm assembly drawing, polarity, Pin 1, connector direction, special process, stackup, surface finish, solder-mask color, assembly side, panelization, and dimensions;
8. inspect the fabrication package for missing, duplicate, stale, temporary, or cross-version files;
9. require explicit user confirmation of order parameters and fabrication approval.

Do not treat file presence as proof that the output is current, correct, or released.

## Classify risk

- **High**: may damage hardware, create unsafe use, reverse polarity, short power, invalidate key connectivity, make the board unmanufacturable, or leave critical DRC/rule evidence unreliable. Block the current gate.
- **Medium**: may impair function, signal/power integrity, thermal performance, assembly, reliability, mechanical fit, or require costly rework. Resolve before release unless a justified exemption is approved.
- **Low**: mainly affects readability, documentation, silkscreen, probing convenience, or maintainability. Record and schedule deliberately.

Evidence insufficiency does not automatically define electrical severity, but it prevents unsupported closure or release.

## Produce the output

Use this structure:

### Current conclusion

Choose one conclusion matching the mode:

- Layout Preflight: `批准开始正式布局` / `不批准开始正式布局`
- Layout / Routing Review: `可进入 PCB Release Review` / `修改后复审` / `存在高风险，停止推进`
- PCB Release Review: `批准制造` / `不批准制造`

State evidence scope and limitations immediately after the conclusion.

### Inputs and version

| Input | Version / date | Purpose | Traceability risk |
|---|---|---|---|

### Findings

| ID | Area | Finding | Risk | Evidence | Required action | Owner | Status |
|---|---|---|---|---|---|---|---|

Use status values: `待决策`, `待修改`, `待核对`, `待 EDA 核对`, `待用户确认`, `已修改 / 待复核`, `已关闭`, `已豁免`.

### Rule and DRC status

| Rule / category | Documented | AD configured | Scope checked | Priority checked | DRC verified | Evidence |
|---|---|---|---|---|---|---|

### Exemptions

Include the exemption table or state `无已批准豁免`.

### Gate decision and next actions

List blockers first, then user EDA actions, evidence to re-export, and the next permitted stage.

## Prohibitions

- Do not copy values, net names, footprints, dimensions, order parameters, findings, or exemptions from another project.
- Do not use a reference project as a default rule set.
- Do not invent fabricator capabilities, rule configuration, DRC results, manufacturing outputs, or verification.
- Do not weaken or disable rules merely to reach zero violations.
- Do not equate visual cleanliness with electrical or manufacturing correctness.
- Do not approve fabrication without a complete user-run Batch DRC and explicit user confirmation.
- Do not describe a board as manufactured, assembled, powered, or tested without actual user evidence.
