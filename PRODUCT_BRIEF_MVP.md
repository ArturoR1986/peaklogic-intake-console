# PRODUCT_BRIEF_MVP.md

## Product Name

PeakLogic Roofing Field Intake Console

## Version

v0.1 Local Streamlit Prototype

## Pain Being Solved

Roofing foremen and field crews do not always have time to write clear reports. They send quick, rough, incomplete field updates. Office staff must reconstruct what happened before preparing reports, customer updates, internal records, or follow-up actions.

## Primary User

Office admin, service manager, or PeakLogic operator.

## Input Provider

Foreman or field crew.

## Product Job

This product helps office/service staff turn messy roofing field intake into structured, reviewable field packets so they can create reports, customer updates, and internal records faster with fewer missing details.

## Smallest Useful Version

A local Streamlit intake console where the user pastes messy field updates, optionally enters job metadata, and receives a structured field packet with missing information, internal notes, customer-facing draft notes, and follow-up needs.

## Must-Have Features

- Paste messy field update.
- Optional metadata fields: job name, address, date, foreman, crew.
- Intake classification: daily report, repair update, leak investigation, inspection note, material/follow-up note, unknown.
- Structured field packet output.
- Missing information checklist.
- Internal vs customer-facing separation.
- Human review warnings.
- Markdown export.
- JSON export.
- Local pytest test suite.

## Excluded From v0.1

- External LLM/API requirement.
- Photo upload processing.
- Full CRM/job management.
- Final customer report automation.
- Legal/warranty/pricing/cause conclusions.
- User accounts and permissions.
- Cloud deployment.

## Success Signals

- Office can understand messy field updates faster.
- Missing information is easier to identify.
- Internal comments stay internal.
- Customer-facing draft notes are safer and easier to review.
- The prototype can be tested on real foreman updates.
