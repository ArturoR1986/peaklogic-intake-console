# TEST_CASES.md

## Test 1 — Intake Classification

Input contains words like leak, water, ceiling, or source.

Expected:

- intake type is Leak Investigation or Unknown / Needs Review
- no final leak cause is claimed

## Test 2 — Missing Job Name

Input contains work details but no job name.

Expected:

- job name is `Missing`
- missing information includes job name
- app still creates packet

## Test 3 — Unknown Leak Cause

Input says water is coming in but does not confirm cause.

Expected:

- leak cause stays `Unknown`
- no final cause claim appears
- human review required includes cause/technical conclusion

## Test 4 — Internal Notes Stay Internal

Input includes internal concern: "customer is upset" or "we forgot material."

Expected:

- internal concern appears in internal notes
- internal concern does not appear in customer-facing draft

## Test 5 — Customer-Facing Draft Warning

Any generated customer-facing notes must include:

`Draft only. Requires human review before sending.`

## Test 6 — JSON Export

Expected:

- export returns valid JSON
- required top-level keys exist

## Test 7 — Markdown Export

Expected:

- Markdown includes all required packet sections
