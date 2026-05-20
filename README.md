# PeakLogic Intake Console v0.1

Turn messy roofing field notes into structured, reviewable field packets.

## Setup

```bash
pip install -r requirements.txt
```

## Run tests

```bash
pytest
```

## Run CLI sample

```bash
python cli.py --input sample_inputs/field_note_001.txt --output outputs/field_packet_001.json
```

## Run Streamlit review UI

```bash
streamlit run app.py
```

## Trust boundaries

- Uses provided input only.
- Flags missing information.
- Keeps internal and customer-facing output separate.
- Marks customer-facing text as draft.
- Requires human review before customer use.
