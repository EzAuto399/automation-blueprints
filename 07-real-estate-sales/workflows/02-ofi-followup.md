---
title: Open-home follow-up (same day)
parent: Real estate sales agent
nav_order: 2
---

# Open-home follow-up (same day)

## What it does

Everyone who walks through gets a follow-up within hours, not days: a short, personal line about the property plus the next open-home time. Speed is the whole game — the AI never sleeps after an inspection.

## The loop

```mermaid
flowchart LR
  A[Open home ends] --> B[Attendee list saved]
  B --> C[Same-day follow-up to each]
  C --> D{Replied?}
  D -->|Interested| E[Booked private viewing]
  D -->|Not yet| F[Next open-home reminder]
```

## What a human still does

- Approves the follow-up lines once
- Takes over the hot leads personally

## What it runs on

Reads the sign-in sheet / enquiry list. Messages go out by SMS or email.

---

*Want this for your business? Free 15-min build review: [yodalai.xyz](https://yodalai.xyz)*
