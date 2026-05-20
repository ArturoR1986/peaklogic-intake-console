# CODEX_DELIVERY_CHECKLIST.md

## File Classification

Type:

```text
Product-specific implementation support file
```

Home:

```text
PeakLogic_Intake_Console_v0.1/
```

Purpose:

```text
Prepare the PeakLogic Intake Console v0.1 product packet for Codex delivery.
```

This file is not a PeakLogic system module.

It supports one product handoff.

---

## Goal

Deliver the correct product-specific files into Codex without confusing the PeakLogic system with the product being built.

PeakLogic stays in the ChatGPT Project library.

Codex receives only the product repo files needed to build this artifact.

---

## Clean Delivery Rule

```text
Do not send the whole Problem-to-Product system to Codex.

Send only the clean product repo packet.
```

For this test, Codex should receive:

```text
AGENTS.md
BUILD_PACKET.md
CODEX_TASK_01_REPO_SCAFFOLD.md
CODEX_HANDOFF_PROMPT.md
```

---

## Step 1 — Create a Clean Product Repo

Create a new folder outside the architecture library.

Suggested location:

```text
Documents/
└── PeakLogic/
    └── repos/
        └── peaklogic-intake-console/
```

This folder is the Codex build workspace.

---

## Step 2 — Copy the Four Active Files

From:

```text
Problem-to-Product/
└── PeakLogic_Intake_Console_v0.1/
```

Copy these files into:

```text
repos/
└── peaklogic-intake-console/
```

Files:

```text
AGENTS.md
BUILD_PACKET.md
CODEX_TASK_01_REPO_SCAFFOLD.md
CODEX_HANDOFF_PROMPT.md
```

Do not copy:

```text
00–14 system modules
System/
Templates/
Reviews/
Archive/
old v2 compact files
zip backup
```

---

## Step 3 — Optional Git Setup

Inside the clean product repo, initialize Git if needed:

```bash
git init
```

Optional first commit:

```bash
git add .
git commit -m "Add initial Codex product packet"
```

If you are using Codex without Git at first, this step can wait.

---

## Step 4 — Open the Repo in Codex

Open:

```text
repos/peaklogic-intake-console/
```

in the Codex environment.

Confirm Codex can see:

```text
AGENTS.md
BUILD_PACKET.md
CODEX_TASK_01_REPO_SCAFFOLD.md
CODEX_HANDOFF_PROMPT.md
```

---

## Step 5 — Start Codex

Open:

```text
CODEX_HANDOFF_PROMPT.md
```

Copy the full content.

Paste it into Codex as the first task.

Codex should then read:

```text
AGENTS.md
BUILD_PACKET.md
CODEX_TASK_01_REPO_SCAFFOLD.md
```

and complete the scaffold task.

---

## Step 6 — Required Codex Proof

Codex must run:

```bash
pytest
```

Then run:

```bash
python cli.py --input sample_inputs/field_note_001.txt --output outputs/field_packet_001.json
```

Codex should fix errors before reporting completion.

---

## Step 7 — Expected Codex Report

Codex should report back with:

```text
Files changed:
Commands run:
Test result:
Run result:
Output files:
Notes / TODOs:
```

---

## Step 8 — Bring Results Back to PeakLogic

After Codex finishes, bring this back into ChatGPT / PeakLogic:

```text
Codex final report
test result
CLI result
generated JSON output
repo file tree
any errors or TODOs
```

PeakLogic will then review using:

```text
QA / Trust Checker
Test Cases and Evaluation
Feedback Loop
System Maintenance if needed
```

---

## QA Review Questions

When the Codex result comes back, check:

```text
Did the repo scaffold correctly?
Did tests pass?
Did the CLI sample run?
Was JSON output created?
Did the output preserve missing-information flags?
Did it keep internal and customer-facing content separate?
Did customer-facing text stay draft-only?
Did it preserve human review warnings?
Did it stay inside v0.1 scope?
```

---

## Final Delivery Rule

```text
Codex builds the product artifact.

PeakLogic reviews the artifact.

The product repo is not the PeakLogic system.

The PeakLogic system remains the architecture and QA brain.
```
