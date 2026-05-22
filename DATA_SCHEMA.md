# DATA_SCHEMA.md — Roofing Field Intake Console Schema

## Field Intake Object

```json
{
  "raw_input": "string",
  "metadata": {
    "job_name": "string | Missing",
    "address": "string | Missing",
    "date": "string | Missing",
    "foreman": "string | Missing",
    "crew": ["string"]
  },
  "intake_type": "Daily Field Report | Repair Update | Leak Investigation | Inspection Note | Material / Follow-Up Note | Unknown / Needs Review"
}
```

## Field Packet Object

```json
{
  "job_information": {
    "job_name": "string | Missing",
    "address": "string | Missing",
    "date": "string | Missing",
    "foreman": "string | Missing",
    "crew": ["string"]
  },
  "intake_classification": "string",
  "field_summary": "string",
  "work_completed": ["string"],
  "issues_found": ["string"],
  "materials_mentioned": ["string"],
  "photos_or_visual_references": ["string"],
  "internal_notes": ["string"],
  "customer_facing_draft": {
    "warning": "Draft only. Requires human review before sending.",
    "notes": ["string"]
  },
  "missing_information": ["string"],
  "follow_up_needs": ["string"],
  "human_review_required": ["string"]
}
```

## Required Packet Sections

1. Job Information
2. Intake Classification
3. Field Summary
4. Work Completed
5. Issues Found
6. Materials Mentioned
7. Photos / Visual References
8. Internal Notes
9. Customer-Facing Draft Notes
10. Missing Information
11. Follow-Up Needs
12. Human Review Required

## Missing Information Rules

Use `Missing` for absent metadata.

Use `Unknown` when a concept is mentioned but unclear.

Example:

- Leak cause mentioned but not confirmed → `Unknown`
- Job name not provided → `Missing`
