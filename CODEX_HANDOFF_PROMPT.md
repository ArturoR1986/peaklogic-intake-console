# CODEX_HANDOFF_PROMPT.md

Use this prompt to start Codex.

---

You are working inside the **PeakLogic Intake Console v0.1** repository.

This product is one output of the PeakLogic problem-to-product system.

It is not the whole PeakLogic system.

Read these files first:

```text
AGENTS.md
BUILD_PACKET.md
CODEX_TASK_01_REPO_SCAFFOLD.md
```

Complete the task in:

```text
CODEX_TASK_01_REPO_SCAFFOLD.md
```

Follow:

```text
AGENTS.md = engineering rules and trust boundaries
BUILD_PACKET.md = product requirements
CODEX_TASK_01_REPO_SCAFFOLD.md = current implementation task
```

Use engineering judgment.

Keep the work inside the approved v0.1 scope.

---

## Key Architecture Rule

Separate mechanical processing from human expression:

```text
src/logic.py = mechanical extraction and structured packet generation
src/human_output.py = natural summaries and customer-facing draft language
src/database.py = SQLite storage
src/schemas.py = field contracts and defaults
cli.py = command-line execution
app.py = Streamlit review surface
tests/ = behavior proof
```

Streamlit is the display/review layer, not the business logic layer.

---

## Required Proof

Run:

```bash
pytest
```

Then run:

```bash
python cli.py --input sample_inputs/field_note_001.txt --output outputs/field_packet_001.json
```

Fix errors before reporting completion.

---

## Completion Report

When finished, report:

```text
Files changed:
Commands run:
Test result:
Run result:
Output files:
Notes / TODOs:
```
