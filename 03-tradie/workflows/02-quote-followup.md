---
title: Quote follow-up chaser
parent: Tradie
nav_order: 2
---

# Quote follow-up chaser

## What it does

Jobs are won on the follow-up, not the first quote. The AI nudges the customer at 24, 48 and 72 hours with the same friendly line you'd use — so no quote ever goes quiet because you forgot.

## The loop

```mermaid
flowchart LR
  A[Quote sent] --> B[24h: still happy to help?]
  B --> C[48h: soft reminder]
  C --> D[72h: last line + alternative date]
  D --> E{Replied?}
  E -->|Yes| F[Booking or close]
  E -->|No| G[Marked cold · revisit in 3 months]
```

## How it runs, day to day

1. Every quote that goes out gets a follow-up schedule: 24 hours, 48 hours, then a last line at 72.
2. Each nudge is one short message — no pressure, just keeping the job on their mind.
3. When the customer replies, the AI sorts it: booking request, question, or 'going elsewhere'.
4. Big jobs or tricky conversations get escalated to you personally.

## What a reply looks like

"Just checking in on the quote I sent Tuesday — I can still get you in this week if that helps. No worries either way!"

## What a human still does

- Approves the follow-up lines once at the start
- Steps in personally when a big job replies
- Decides when to stop chasing

## What it runs on

Same always-on agent, same inbox. Follow-ups are scheduled, not remembered.

---

*Want this for your business? Free 15-min build review: [yodalai.xyz](https://yodalai.xyz)*
