# FIELD_INTAKE_EXTRACTION_PROMPT.md

## Purpose

This prompt describes the future LLM-assisted extraction behavior.

For v0.1, Codex should implement deterministic/rule-based extraction and leave a clear extension point where this prompt could later be used.

## Extraction Behavior

Turn messy roofing field updates into a structured field packet.

Use only the provided notes and metadata.

Do not invent missing details.

Classify the intake type when possible:

- Daily Field Report
- Repair Update
- Leak Investigation
- Inspection Note
- Material / Follow-Up Note
- Unknown / Needs Review

Separate:

- job facts
- work completed
- issues found
- materials
- internal notes
- customer-facing draft notes
- missing information
- follow-up needs

Customer-facing draft notes must be safe, factual, and clearly labeled as requiring human review.
