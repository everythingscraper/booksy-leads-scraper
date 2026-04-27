# Booksy Leads Scraper (Apify Actor)

Turn any **[Booksy](https://booksy.com)** search URL into a CSV of beauty- and wellness-business leads — names, addresses, **phone numbers**, **emails**, **websites**, **social handles**, ratings, review counts, and service categories. Built for B2B prospecting into barbers, salons, nail techs, spas, lash & brow studios, massage therapists, and the long tail of independent operators.

Apify Actor 👉 **https://apify.com/seo-scraper/booksy-leads-scraper**

This repo is a **Python lead-gen example**: one search URL → `leads.csv` ready to drop into Clay, Apollo, Lemlist, Instantly, HubSpot, or your CRM of choice.

## The lead-gen playbook

1. Pick a **service** on `booksy.com` (e.g. `haircut-beard`, `eyelash-extensions`, `manicure`).
2. Pick a **city** (e.g. Newport Beach, Miami, Austin).
3. Copy the search URL.
4. Run this scraper — get a CSV of every public business profile that matched.
5. Push the CSV into your outreach tool.

That's the whole workflow.

## What ships in each lead

| Column | Field |
|---|---|
| Business name | `name` |
| Address (street, city, ZIP) | `address` |
| Phone | `phone` |
| Email (if listed) | `email` |
| Website | `website` |
| Instagram / Facebook / TikTok | `socialMedia` |
| Star rating | `rating` |
| Review count | `reviewsCount` |
| Booksy category | `category` |
| Profile URL | `url` |

## Quick start

```bash
git clone https://github.com/everythingscraper/booksy-leads-scraper.git
cd booksy-leads-scraper
pip install -r requirements.txt
APIFY_TOKEN=your_token python main.py
```

`main.py` scrapes 10 barber leads from Newport Beach and writes them to `leads.csv` — drop into Clay or Lemlist as-is.

## Input options

- 🔗 `startUrls` — array of Booksy search URLs (`https://booksy.com/en-us/s/<service>/<city-id>_<city>`).
- 🔢 `resultsToScrape` — leads per URL (1–1,000, default 50).
- 🌐 `proxyConfiguration` — residential recommended.

Schema: **[Input tab](https://apify.com/seo-scraper/booksy-leads-scraper/input-schema)**.

## Sample row

```json
{
  "url": "https://booksy.com/en-us/129938_barber-lounge-co_barber-shop_102522_newport-beach",
  "name": "Barber Lounge & Co.",
  "address": "2507 W Coast Hwy, Newport Beach, 92663",
  "phone": "(323) 448-6931",
  "email": "info@barberlounge.example",
  "website": "https://barberlounge.example",
  "socialMedia": {"instagram": "@barberlounge"},
  "rating": 4.9,
  "reviewsCount": 312,
  "category": "Barber Shop",
  "scrapedAt": "2026-04-27T10:00:00Z"
}
```

Apify Storage exports as **JSON · CSV · Excel · HTML · XML** — pipe directly into your outreach stack.

## Pricing

**$2.00 per 1,000 leads.**

| Plan | ≈ Leads / month |
|---|---|
| Apify Free ($5 credit) | ~2,500 |
| Starter ($49/mo) | ~24,500 |
| Scale ($499/mo) | ~249,500 |

That's roughly **$0.002 per qualified, contactable lead** — orders of magnitude cheaper than typical lead-list vendors.

## Who uses this

- 📞 **Cold-call agencies** — daily lead drops by city + service
- 💸 **POS / SaaS sales teams** targeting independent salons & barbers
- 📧 **Cold-email infra** (Lemlist, Instantly, Smartlead) — pre-warmed CSV imports
- 🛒 **Beauty-supply distributors** — territory-by-territory prospecting
- 🤝 **Booking-platform competitors** — full-market mapping

## FAQ

**Is there a Booksy lead API?** No public one. Booksy is the merchant's primary marketing surface, so the contact info on their public profile is usually accurate and current.

**Which countries?** Booksy is strongest in the **US, UK, Poland, Brazil, and South Africa**. Any Booksy search URL works as a `startUrl`.

**How fresh is the data?** Live every run — phone numbers and emails are pulled at request time.

**Can I run multiple service types in one job?** Yes — pass multiple `startUrls` (e.g. one for haircut+beard, one for nails, one for massage).

**Does it dedupe across runs?** Within a run, yes (by Booksy profile URL). Across runs, dedupe in your CRM — Booksy URLs are stable IDs.

**Integrations?** Webhook on dataset-created, plus first-party Make / Zapier / n8n. CSV exports drop straight into Clay, Apollo, Lemlist, Instantly, Smartlead.

## Other Apify Actors

- 📊 [Moz Domain Authority Checker](https://github.com/everythingscraper/moz-domain-authority-checker)
- 🏢 [LoopNet Scraper](https://github.com/everythingscraper/loopnet-scraper)
- 🏠 [Airbnb Scraper](https://github.com/everythingscraper/airbnb-scraper)
- 🏨 [Trip.com Hotel Scraper](https://github.com/everythingscraper/trip-hotel-scraper)
- 🏖️ [Traveloka Hotel Scraper](https://github.com/everythingscraper/traveloka-hotel-scraper)

## Legality

This Actor extracts only publicly listed business information that operators themselves publish on Booksy as marketing. No customer accounts, bookings, or private user data are accessed. Personal data within scraped leads remains subject to GDPR (EU/UK) and similar laws — use leads only for legitimate B2B outreach and consult counsel where relevant.

## License

MIT — see [LICENSE](./LICENSE).
