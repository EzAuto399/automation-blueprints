---
title: After-hours quote responder
parent: Tradie
nav_order: 1
---

# After-hours quote responder

## What it does

A customer sends a photo of the job at 8pm. The AI reads your price list and past jobs, drafts a quote reply, and sends it after you tap approve on your phone — while you're still on the couch.

## The loop

```mermaid
flowchart LR
  A[Job enquiry with photo] --> B[AI drafts reply<br/>from your price list]
  B --> C{You approve}
  C -->|Yes| D[Quote reply sent tonight]
  C -->|Edit| E[You adjust price]
  E --> D
```

## What a human still does

- Approves the price before anything is promised
- Decides anything unusual (hard job, access issues)
- Sets the tone once — a few iterations at the start

## What it runs on

A small always-on computer (a Mac mini is plenty) watching your SMS and Messenger. No website rebuild, no CRM migration needed.

---

*Want this for your business? Free 15-min build review: [yodalai.xyz](https://yodalai.xyz)*
