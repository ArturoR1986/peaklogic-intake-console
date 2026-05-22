# ARCHITECTURE_DECISION.md

## Decision

Rename and reframe the product from:

```text
PeakLogic Field Packet Builder
```

to:

```text
PeakLogic Roofing Field Intake Console
```

## Reason

The earlier name centered the output artifact: the field packet.

The corrected name centers the real operational pain: messy field intake.

## Product Boundary

The Intake Console receives messy field information and prepares it for review.

It does not produce final customer reports.

## Correct Product Logic

```text
messy foreman update
→ intake console
→ classification + structuring
→ missing information flags
→ reviewable field packet
→ office review
→ later report/customer update/job record
```

## Layer Separation

```text
Product:
Roofing Field Intake Console

Primary output:
Reviewable Field Packet

Future product/layer:
Report Generator

PeakLogic:
Problem-to-product machine that creates this painkiller
```

## Official Repo Name

```text
peaklogic-roofing-field-intake-console
```

## Official Main Handoff File

```text
ROOFING_FIELD_INTAKE_CONSOLE_CODEX_HANDOFF.md
```
