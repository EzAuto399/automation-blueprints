---
title: Real estate sales agent
parent: Automating Real Businesses
has_children: true
nav_order: 3
---

# Real estate sales agent — the 5 loops

Appraisal requests, open-home follow-ups, vendor updates, buyer enquiries — none of it slips.

## The problem

A seller asks for an appraisal on Sunday. By Wednesday you've forgotten to reply and they've listed with someone else. After the open home, 14 people walked through and nobody was followed up. That's the listing you lose.

## The workflow map

```mermaid
flowchart LR
  A[Seller appraisal request Sunday] --> B[AI replies + books appraisal]
  B --> C[Open home runs]
  C --> D[Every attendee followed up same day]
  D --> E[Vendor gets a weekly update]
  E --> F[Buyer enquiries matched to listings]
  F --> G[Past clients nurtured]
```

## The 5 daily loops

1. **[Appraisal request responder](workflows/01-appraisal-responder)** — The enquiry that starts every listing — answered the same day, even on weekends.
2. **[Open-home follow-up (same day)](workflows/02-ofi-followup)** — Everyone who walks through gets a follow-up within hours, not days: a short, personal line about the property plus the next open-home time.
3. **[Vendor update loop](workflows/03-vendor-update)** — Sellers want to know what's happening.
4. **[Buyer enquiry matcher](workflows/04-buyer-match)** — A buyer asks about a suburb or price range.
5. **[Past-client nurture](workflows/05-past-client-nurture)** — The people who bought or sold with you are your next listing — in 2 or 5 years.

## What a human still does

- Approves every reply before it sends
- Sets the tone once (a few iterations at the start)
- Decides anything unusual — the AI escalates, it doesn't guess

*Generalised from real working patterns. No client details included. Plans shown are plans, not claims of deployed results.*

---

*Book a free 15-min build review: [yodalai.xyz](https://yodalai.xyz)*
