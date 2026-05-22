# CODEX_TASK.md — Build Streamlit MVP

## Task

Implement the PeakLogic Roofing Field Intake Console v0.1 as a local Streamlit prototype.

## Implementation Notes

Use deterministic/rule-based extraction and classification for v0.1.

Do not require an external LLM, API key, database, or paid service.

Build readable, well-commented Python files with clear section headers.

## Files to Create

- `app.py`
- `requirements.txt`
- `src/__init__.py`
- `src/models.py`
- `src/intake_classifier.py`
- `src/packet_builder.py`
- `src/exporters.py`
- `src/sample_loader.py`
- `tests/test_intake_classifier.py`
- `tests/test_packet_builder.py`
- `tests/test_exporters.py`
- `outputs/.gitkeep`

## Functional Tasks

1. Define field intake and field packet data models.
2. Build a simple rule-based intake classifier.
3. Build a packet builder that accepts metadata and messy text.
4. Extract obvious known items when possible.
5. Mark missing items as Missing or Unknown.
6. Separate likely internal notes from customer-facing draft notes.
7. Add human review warnings.
8. Export packet to Markdown and JSON.
9. Create tests for classifier, packet builder, and exporters.
10. Update README with exact commands.

## Run Commands

```bash
pip install -r requirements.txt
streamlit run app.py
pytest
```

## Delivery Requirement

Return a summary listing files created, commands run, test results, limitations, and recommended next improvement.
