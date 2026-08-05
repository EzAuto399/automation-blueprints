---
title: After-hours question responder
parent: Allied health clinic
nav_order: 4
---

# After-hours question responder

## What it does

'Do you bulk bill? What do I bring to my first physio session?' The AI answers from the clinic's own policies at 9pm on a Sunday. The answer is right, and the patient feels looked after.

## The loop

```mermaid
flowchart LR
  A[Question at 9pm Sunday] --> B[AI drafts from clinic policies]
  B --> C{Clinical or sensitive?}
  C -->|No| D[Answered tonight]
  C -->|Yes| E[Queued for staff]
```

## What a human still does

- Approves the clinic policy answers once
- Reviews anything clinical the AI flags

## What it runs on

Same inbox watcher. Policies live in one document the AI quotes from.

---

*Want this for your business? Free 15-min build review: [yodalai.xyz](https://yodalai.xyz)*
