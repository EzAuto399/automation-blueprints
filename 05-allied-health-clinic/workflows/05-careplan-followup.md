---
title: Care-plan follow-up
parent: Allied health clinic
nav_order: 5
---

# Care-plan follow-up

## What it does

After the first visit, the patient gets the exercise sheet or care plan link, and a check-in a few days later: 'how are the exercises going?' If they're due for the next visit, the AI offers the booking.

## The loop

```mermaid
flowchart LR
  A[First visit done] --> B[Care plan + exercise link sent]
  B --> C[Check-in a few days later]
  C --> D{Doing well?}
  D -->|Yes| E[Next visit offered]
  D -->|Struggling| F[Flagged to the clinician]
```

## What a human still does

- Writes the care plan the AI delivers
- Handles any flagged struggles personally

## What it runs on

The practice's existing care-plan documents.

---

*Want this for your business? Free 15-min build review: [yodalai.xyz](https://yodalai.xyz)*
