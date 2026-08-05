---
title: Tradie
parent: Automating Real Businesses
has_children: true
nav_order: 3
---

# Tradie — the 5 loops

Plumber, sparky, builder — quotes answered, followed up, jobs booked, reviews collected.

## The problem

Job enquiries land at 8pm. You're on the roof. The quote goes out next week — if it goes out at all. And the job goes to whoever called back first.

## The workflow map

```mermaid
flowchart LR
  A[Job enquiry at 8pm<br/>SMS or Messenger] --> B[AI drafts a quote reply<br/>from your price list]
  B --> C{You approve<br/>on your phone}
  C -->|Yes| D[Reply sent in minutes]
  C -->|Edit| E[You tweak the price]
  E --> D
  D --> F[Follow-up at 24/48/72h]
  F --> G[Job booked + reminder]
  G --> H[Review request 2h after done]
  H --> I[Service reminder in 6 months]
```

## The 5 daily loops

1. **[After-hours quote responder](workflows/01-quote-responder)** — A customer sends a photo of the job at 8pm.
2. **[Quote follow-up chaser](workflows/02-quote-followup)** — Jobs are won on the follow-up, not the first quote.
3. **[Job booking + reminders](workflows/03-job-booking)** — Once the job is accepted, the AI books it into your calendar, sends the customer a confirmation with a window, reminds them the day before, and gives them a one-tap 'I'm running late' path if anything changes.
4. **[Review requester](workflows/04-review-requester)** — Two hours after the job, while the customer is still happy, the AI sends a short message with the Google review link.
5. **[Seasonal service reminders](workflows/05-service-reminder)** — Past customers come back on schedule: filter checks before winter, hot water service checks, roof inspections before storm season.

## What a human still does

- Approves every reply before it sends
- Sets the tone once (a few iterations at the start)
- Decides anything unusual — the AI escalates, it doesn't guess

*Generalised from real working patterns. No client details included. Plans shown are plans, not claims of deployed results.*

---

*Book a free 15-min build review: [yodalai.xyz](https://yodalai.xyz)*
