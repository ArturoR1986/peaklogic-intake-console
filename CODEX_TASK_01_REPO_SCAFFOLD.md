# CODEX_TASK_01_REPO_SCAFFOLD.md

## Task

Create the initial repository scaffold for **PeakLogic Intake Console v0.1**.

Product:

```text
PeakLogic Intake Console v0.1
```

This product is one output of the PeakLogic problem-to-product system.

It is not the whole PeakLogic system.

Read first:

```text
AGENTS.md
BUILD_PACKET.md
```

---

## Goal

Create the repo files, minimal working logic, sample input, and tests needed for the first runnable local prototype.

---

## Scope

Include:

```text
repository scaffold
basic rule-based extraction
human output layer
CLI runner
Streamlit review surface
SQLite storage layer
sample input
tests
README
```

Exclude:

```text
cloud deployment
authentication
mobile app
automatic customer sending
final report automation
pricing/estimating
warranty conclusions
full CRM/job-management replacement
```

---

## Required Files / Areas

Create:

```text
AGENTS.md
BUILD_PACKET.md
README.md
requirements.txt
cli.py
app.py
src/__init__.py
src/schemas.py
src/logic.py
src/human_output.py
src/database.py
src/export_utils.py
tests/test_intake_logic.py
tests/test_human_output.py
sample_inputs/field_note_001.txt
outputs/.gitkeep
data/.gitkeep
```

Do not overwrite existing `AGENTS.md` or `BUILD_PACKET.md` unless needed for consistency.

---

## Required Behavior

The scaffold should support:

```bash
python cli.py --input sample_inputs/field_note_001.txt --output outputs/field_packet_001.json
```

The command should:

```text
read the sample field note
generate a structured field packet
generate an internal summary
generate a customer-facing draft marked as draft
write JSON output
preserve human review warnings
```

---

## Implementation Guidance

Use engineering judgment.

Keep the implementation simple, testable, and aligned with the Build Packet.

Use rule-based extraction for v0.1.

Keep core logic out of `app.py`.

Use `src/human_output.py` for human-readable summaries and drafts.

Do not redesign the product unless an implementation blocker appears.

Preserve trust boundaries.

---

## Required Sample Input

Create `sample_inputs/field_note_001.txt`:

```text
Went to Conestoga today. R-36 had 3 punctures near drain. Patched with TPO. Water still ponding. Need to check next rain. Crew was Mike and Luis, 7 hours.
```

---

## Tests

Create tests that verify:

```text
sample note produces a valid packet
Conestoga, TPO, punctures, ponding water, and check next rain are detected
missing fields are marked
customer-facing output is marked as draft
internal notes do not leak into customer-facing text
review warning exists
```

---

## Commands to Run

Run:

```bash
pytest
```

Then run:

```bash
python cli.py --input sample_inputs/field_note_001.txt --output outputs/field_packet_001.json
```

Inspect the generated JSON.

Fix errors before reporting completion.

---

## Acceptance Criteria

This task is complete when:

```text
scaffold exists
tests pass
CLI sample runs
JSON output is created
human output layer exists
README includes setup/run instructions
trust boundaries remain visible
```

---

## Report Back

Report:

```text
Files changed:
Commands run:
Test result:
Run result:
Output files:
Notes / TODOs:
```
