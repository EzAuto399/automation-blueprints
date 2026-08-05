---
title: Buyer enquiry matcher
parent: Real estate sales agent
nav_order: 4
---

# Buyer enquiry matcher

## What it does

A buyer asks about a suburb or price range. The AI matches them to active listings and drafts a reply from the listing's own details. Enquiries become viewings instead of dead ends.

## The loop

```mermaid
flowchart LR
  A[Buyer enquiry] --> B[Matched to active listings]
  B --> C[Draft reply from listing details]
  C --> D[You approve]
  D --> E[Viewing booked]
```

## What a human still does

- Approves price-related replies
- Handles anything the AI flags as sensitive

## What it runs on

Reads the agency's active listings + enquiry inbox.

---

*Want this for your business? Free 15-min build review: [yodalai.xyz](https://yodalai.xyz)*
