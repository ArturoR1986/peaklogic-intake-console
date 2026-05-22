# QA_TRUST_CHECKLIST.md

## Purpose

Review the PeakLogic Roofing Field Intake Console before using with real client material.

## Function Check

- App accepts pasted field updates.
- App accepts optional metadata.
- App classifies intake type or marks it Unknown.
- App creates structured field packet.
- App exports Markdown and JSON.
- Tests pass.

## Accuracy Check

- Uses only provided input.
- Missing fields are marked Missing.
- Unclear conclusions are marked Unknown.
- No invented job facts appear.

## Privacy / Trust Check

- Internal notes stay separate.
- Customer-facing draft does not include internal-only concerns.
- Customer-facing section includes human review warning.

## Claim Safety Check

The tool must not make final claims about:

- leak cause
- warranty
- legal responsibility
- pricing
- safety
- liability
- final completion status when unclear

## Release Recommendation

This MVP is only ready for internal testing after tests pass and a human reviews sample outputs.
