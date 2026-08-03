# Ep 01 — Property Management: every renter answered

**Watch:** [Automating Property Management With AI Agents](https://www.loom.com/share/644d8bee2ead449c926b7745c3ebf478) (4 min)

A working system that handles the daily grind of leasing: posting listings, answering renter messages, booking inspections, and sending applications — with a human approving the replies.

## The workflow map

```
Facebook Marketplace ──► AI drafts reply from the property's
     renter DMs           own description + photos
                               │
                     Human approves on Telegram
                     (tone tweaked over a few iterations)
                               │
              ┌────────────────┼─────────────────┐
              ▼                ▼                 ▼
     Inspection booked   Application link    Move-in goal tracked
     (calendar, no       sent minutes after  (e.g. tenant in
     double-ups)         the inspection      within 4 days)
```

## The daily loops

1. **Listing poster** — posts each property to Facebook Marketplace and shares to local groups on a daily or every-two-days schedule.
2. **Enquiry responder** — people who see the listing message you. The AI reads the property's description and images from memory and drafts a reply. You review and approve on your phone (Telegram) before it sends.
3. **Inspection scheduler** — books inspections straight into Google Calendar or Cal.com and checks for clashes, so no double-bookings.
4. **Application chaser** — a few minutes after an inspection finishes, the applicant automatically gets the application link while the property is still front of mind.
5. **Move-in tracker** — works toward a stated goal (e.g. "tenant moved in within 4 days") and keeps the steps moving.

## What a human still does

- Approves every reply before it sends
- Sets the tone once (a few iterations at the start)
- Decides anything unusual — the AI escalates, it doesn't guess

*Generalised from a real working system. No tenant or property details included.*
