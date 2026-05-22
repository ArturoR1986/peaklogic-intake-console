# Roofing Field Intake Console — Codex Handoff

Paste this prompt into Codex from the target GitHub repository or local Codex environment.

---

You are Codex working inside a product-specific PeakLogic repository.

Build the first MVP of the **PeakLogic Roofing Field Intake Console**.

## Product Context

This product solves a roofing operations pain:

Foremen and field crews do not always have time to write clear reports. They often send rough notes, WhatsApp-style updates, voice transcripts, material comments, or quick photo notes. The office must reconstruct what happened before creating reports, customer updates, job records, or follow-up actions.

This MVP is **not** a final customer report generator.

It is the intake and structuring layer:

```text
messy field input
→ intake console
→ classification + structuring
→ missing information flags
→ reviewable field packet
→ office review
→ later report-ready material
```

## Product Identity Rule

The product is the **Roofing Field Intake Console**.

The field packet is the primary output.

Do not rename the product back to Field Packet Builder.

## Build Target

Build a simple local Streamlit prototype that converts messy pasted field updates into structured, reviewable field packets.

For v0.1, use deterministic/rule-based extraction. Do not require an external LLM, API key, or paid service.

Leave clear extension points for future LLM-assisted extraction.

## Source of Truth Files

Use the files in this build package as source of truth:

- `AGENTS.md`
- `ARCHITECTURE_DECISION.md`
- `BUILD_PACKET.md`
- `CODEX_TASK.md`
- `PRODUCT_BRIEF_MVP.md`
- `DATA_SCHEMA.md`
- `QA_TRUST_CHECKLIST.md`
- `TEST_CASES.md`
- `prompts/FIELD_INTAKE_EXTRACTION_PROMPT.md`
- `sample_data/messy_foreman_updates.md`

## Create This Repo Structure

```text
README.md
requirements.txt
app.py
src/__init__.py
src/models.py
src/intake_classifier.py
src/packet_builder.py
src/exporters.py
src/sample_loader.py
tests/test_intake_classifier.py
tests/test_packet_builder.py
tests/test_exporters.py
sample_data/messy_foreman_updates.md
outputs/.gitkeep
```

## Functional Requirements

- User can paste messy field updates.
- User can optionally enter metadata: job name, address, date, foreman, crew.
- App classifies intake type when possible.
- App returns a structured field packet.
- Missing information is clearly flagged.
- Internal notes stay separate from customer-facing draft notes.
- Customer-facing notes are clearly labeled as draft and require human review.
- Customer-facing notes only use facts present in the field input or metadata.
- App can export Markdown and JSON.
- Tests pass with `pytest`.

## Intake Classification Types

Use simple rule-based classification for v0.1:

- Daily Field Report
- Repair Update
- Leak Investigation
- Inspection Note
- Material / Follow-Up Note
- Unknown / Needs Review

## Trust Requirements

- Do not invent facts.
- Use `Missing` or `Unknown` when information is absent.
- Do not make final cause, warranty, legal, pricing, safety, or liability claims.
- Preserve human review warnings.
- Keep internal notes out of customer-facing draft notes unless explicitly approved by a human.
- Keep the MVP narrow, readable, and easy to test.

## Minimum Test Requirements

Tests must verify:

- messy input is accepted
- intake type can be classified or marked Unknown
- missing fields are flagged
- unknown leak cause stays unknown
- internal notes stay separate from customer-facing notes
- customer-facing draft includes review warning
- JSON export is valid
- Markdown export includes required sections
- app logic works with sample messy foreman updates

## Delivery Summary Required

After implementation, provide a delivery summary with:

- files created
- run command
- test command
- test results
- known limitations
- recommended next improvement
