---
title: Document request chaser
parent: Accountant & bookkeeper
nav_order: 1
---

# Document request chaser

## What it does

Every client has a checklist of what you need — bank statements, invoices, receipts. The AI scans the list every morning and chases exactly what's missing, one friendly message at a time. No more 'just following up' emails.

## The loop

```mermaid
flowchart LR
  A[Checklist per client] --> B[Daily scan]
  B --> C{Anything missing?}
  C -->|Yes| D[Friendly chase to that client]
  C -->|No| E[Nothing to send]
  D --> F[Uploaded? Marked off]
```

## What a human still does

- Approves chase wording per client segment
- Handles clients the AI flags as stuck

## What it runs on

Watches your inbox + a simple checklist. Works with the tools you already use.

---

*Want this for your business? Free 15-min build review: [yodalai.xyz](https://yodalai.xyz)*
