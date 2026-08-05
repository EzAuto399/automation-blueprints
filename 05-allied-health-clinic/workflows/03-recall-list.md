---
title: Recall list runner
parent: Allied health clinic
nav_order: 3
---

# Recall list runner

## What it does

Patients who should come back at 6 or 12 months get a short, friendly nudge at the right time. The list builds itself from past visits — nobody has to remember who's due.

## The loop

```mermaid
flowchart LR
  A[Visit completed] --> B[Recall date saved]
  B --> C[Due soon]
  C --> D[Nudge sent]
  D --> E{Rebook?}
  E -->|Yes| F[Appointment booked]
  E -->|No| G[Back on the list]
```

## What a human still does

- Decides which visit types get recall nudges

## What it runs on

A list maintained from the booking calendar.

---

*Want this for your business? Free 15-min build review: [yodalai.xyz](https://yodalai.xyz)*
