# AGENTS.md

## Project

Build **PeakLogic Intake Console v0.1**.

This product is one output of the PeakLogic problem-to-product system.

It is not the whole PeakLogic system.

Product purpose:

```text
Turn messy roofing field notes into structured, reviewable field packets.
```

Current stage:

```text
Local prototype
```

---

## Engineering Principle

Build the smallest working version that proves the workflow.

Use engineering judgment to keep the implementation simple, testable, and easy to extend.

Stay inside the approved v0.1 scope unless an implementation blocker requires a small adjustment.

---

## Architecture

Use the approved Build Packet as the product source of truth.

Use an agent-runnable core with a human review surface:

```text
Python core logic
CLI runner
JSON output
SQLite storage
tests
Streamlit review UI
human output layer
```

Separate responsibilities clearly:

```text
src/logic.py = mechanical extraction and structured packet generation
src/human_output.py = natural summaries and customer-facing draft language
src/database.py = SQLite storage
src/schemas.py = field contracts and defaults
src/export_utils.py = JSON/export helpers
cli.py = command-line execution
app.py = Streamlit display and review surface
tests/ = behavior proof
```

Streamlit is the review interface, not the business logic layer.

---

## Human Output Rule

Human-facing language belongs in:

```text
src/human_output.py
```

Human-facing language should:

```text
use only known facts
sound natural and professional
preserve uncertainty
stay reviewable
avoid unsupported claims
```

Customer-facing output is draft-only unless a human approves it.

---

## Trust Rules

The product must:

```text
use provided input only
flag missing information
avoid invented facts
separate internal and external content
mark customer-facing text as draft
preserve human review before customer use
avoid unsupported legal, pricing, warranty, liability, or final technical claims
```

Domain-specific rule:

```text
Do not make final claims about leak cause, roof condition, warranty status, completion status, pricing, or liability unless a responsible human confirms them.
```

---

## Commands

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Run the CLI sample:

```bash
python cli.py --input sample_inputs/field_note_001.txt --output outputs/field_packet_001.json
```

Run the Streamlit review UI:

```bash
streamlit run app.py
```

---

## Completion Criteria

A task is complete only when:

```text
requested files/code are created or updated
tests pass
the relevant run command succeeds
outputs remain structured and reviewable
trust boundaries are preserved
README or run instructions are updated when needed
```

---

## Final Rule

Build the product artifact.

Do not redesign the PeakLogic system unless the user explicitly asks for system-level work.
