# BUILD_PACKET.md — Roofing Field Intake Console v0.1

## Build Target

Create a local Streamlit prototype for the PeakLogic Roofing Field Intake Console.

## Product Pain

Foremen do not always have time to write clear reports. Field updates arrive as rough notes, WhatsApp-style messages, voice transcripts, or photo comments. Office staff must reconstruct what happened before creating reports or customer updates.

## Product Boundary

Build an intake console, not a final report generator.

## Required Stack

- Python
- Streamlit
- pytest
- Standard library for JSON and Markdown export

## Required App Behavior

1. User opens Streamlit app.
2. User pastes messy field update.
3. User optionally enters job metadata.
4. App classifies the intake type.
5. App generates structured field packet.
6. App flags missing/unknown information.
7. App separates internal notes from customer-facing draft notes.
8. App exports packet as Markdown and JSON.

## Required Repo Structure

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

## Trust Rules

- Use provided information only.
- Mark absent information as Missing or Unknown.
- Do not infer final cause of leak.
- Do not make warranty, legal, price, safety, or liability claims.
- Keep internal notes separate.
- Customer-facing draft must include human review warning.

## Completion Criteria

- App runs locally with `streamlit run app.py`.
- Tests run with `pytest`.
- Markdown and JSON exports work.
- Required sections appear in packet output.
- README explains setup, run, and test commands.
