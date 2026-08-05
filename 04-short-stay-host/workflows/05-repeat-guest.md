---
title: Quiet-night + repeat-guest offer
parent: Short-stay host
nav_order: 5
---

# Quiet-night + repeat-guest offer

## What it does

When a night is sitting empty, past guests who loved the stay get a short note: 'this weekend is free at yours again.' Past guests rebook cheaper than new ones — and the AI keeps the list.

## The loop

```mermaid
flowchart LR
  A[Stay completed] --> B[Guest saved as repeat]
  B --> C[Quiet night detected]
  C --> D[Short offer to past guests]
  D --> E[Rebook into calendar]
```

## What a human still does

- Approves the offer and the discount level
- Chooses who gets the note

## What it runs on

A guest list the AI builds from completed stays.

---

*Want this for your business? Free 15-min build review: [yodalai.xyz](https://yodalai.xyz)*
