# PeakLogic Roofing Field Intake Console v0.1

## Product Identity

The **PeakLogic Roofing Field Intake Console** is the first product layer for solving messy roofing field reports.

It is not the report generator.

It is the intake console that receives messy field information, classifies it, structures it, flags missing details, and prepares a reviewable field packet for office review and later report creation.

## Product Sentence

PeakLogic Roofing Field Intake Console turns messy foreman updates into structured, reviewable field packets for office review and later report creation.

## Primary User

- Office admin
- Service manager
- PeakLogic operator

## Input Provider

- Foreman
- Field crew
- Service technician

## Input

Messy foreman updates such as:

- WhatsApp-style text
- pasted voice transcript
- rough job notes
- quick photo comments
- material notes
- follow-up comments

## Core Action

Capture, classify, structure, and flag missing field information.

## Primary Output

A reviewable field packet.

## Hard Boundary

This is not a final customer report generator.

Customer-facing output is draft-only and requires human review.

## Local MVP Run Command

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Test Command

```bash
pytest
```

## MVP Behavior

- Paste messy roofing field updates.
- Add optional metadata: job name, address, date, foreman, and crew.
- Classify the intake as daily report, repair update, leak investigation, inspection note, material/follow-up note, or unknown.
- Generate a structured reviewable field packet.
- Mark absent metadata as `Missing` and unclear captured details as `Unknown`.
- Keep internal notes separate from customer-facing draft notes.
- Include the human review warning in customer-facing draft notes.
- Export the field packet as Markdown or JSON from the Streamlit UI.

## Trust Boundary

The app uses deterministic, rule-based extraction only. It does not call an external LLM, require an API key, add authentication, or connect to cloud services. Customer-facing notes are draft-only and must be reviewed by a human before use.
