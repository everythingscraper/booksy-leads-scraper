# Booksy Leads Scraper — Beauty & Wellness Business Contact Data (Apify Actor)

Scrape **[Booksy](https://booksy.com)** business profiles at scale: business names, addresses, **phone numbers**, **emails**, **social media** links, ratings, review counts, and service categories. Built for B2B lead generation across barbers, hair salons, nail technicians, spas, beauty professionals, and wellness businesses.

> 👉 Run it on Apify (no install): **[apify.com/seo-scraper/booksy-leads-scraper](https://apify.com/seo-scraper/booksy-leads-scraper)**

This repository contains a minimal **Python example** showing how to call the deployed Actor through the Apify API and pull lead records.

## What this Booksy scraper extracts

| Field | Description |
|---|---|
| `url` | Direct Booksy profile URL |
| `name` | Official business name |
| `address` | Full address (street, city, ZIP) |
| `phone` | Primary contact phone number |
| `email` | Public business email when listed |
| `website` | Business website link |
| `socialMedia` | Instagram / Facebook / TikTok handles |
| `rating` | Average star rating |
| `reviewsCount` | Total reviews on Booksy |
| `category` | Booksy service category (barber, salon, spa, etc.) |

## Quick start — Python example

```bash
git clone https://github.com/everythingscraper/booksy-leads-scraper.git
cd booksy-leads-scraper
pip install -r requirements.txt
export APIFY_TOKEN=your_apify_token   # https://console.apify.com/settings/integrations
python main.py
```

`main.py` scrapes 10 barber leads from Newport Beach and prints name, phone, rating, address per result.

## How to scrape Booksy — input options

- **`startUrls`** — array of Booksy search-results URLs. Visit booksy.com, run a search by service + location, copy the URL. Example: `https://booksy.com/en-us/s/haircut-beard/102522_newport-beach`.
- **`resultsToScrape`** — leads per URL (1–1000, default 50).
- **`proxyConfiguration`** — residential proxies recommended for reliability.

Full input schema: **[Input tab on Apify](https://apify.com/seo-scraper/booksy-leads-scraper/input-schema)**.

## Sample output

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

Datasets export as **JSON, CSV, Excel, HTML, or XML** — push directly into your CRM or cold-email tool.

## How much does it cost to scrape Booksy?

Pay-per-result: **$2.00 per 1,000 leads**. The Apify Free plan ($5 platform credit) covers ≈ 2,500 Booksy leads. The Starter plan ($49/mo) covers ≈ 24,500 leads. Costs scale linearly.

## FAQ

**Does Booksy have an official API?**
No public B2C lead API. This Actor is the practical route for prospecting beauty / wellness businesses listed on Booksy.

**Which countries does Booksy cover?**
Booksy operates strongest in the US, UK, Poland, Brazil, and South Africa. Any Booksy search URL works as a start URL.

**How fresh are phone numbers and emails?**
Pulled live each run. Booksy is the merchant's primary booking surface, so contact info is usually accurate and current.

**Can I scrape multiple service types in one run?**
Yes — pass multiple search URLs in `startUrls` (e.g. one for haircut+beard, one for nail-tech, one for massage).

**Can I integrate the leads into HubSpot / Pipedrive / Lemlist / Instantly / Clay?**
Yes — pipe results via Apify's **[webhooks](https://docs.apify.com/platform/integrations/webhooks)** or **[Make](https://apify.com/integrations/make)** / **[Zapier](https://apify.com/integrations/zapier)** integrations. CSV export drops straight into Clay / Apollo / Lemlist.

**Need a custom field, a different geo, or a dedicated lead-gen pipeline?**
Open an issue or contact us via the [Apify Actor page](https://apify.com/seo-scraper/booksy-leads-scraper).

## Other Apify Actors by everythingscraper

- 📊 **[Moz Domain Authority Checker](https://github.com/everythingscraper/moz-domain-authority-checker)** — DA / PA / backlinks for SEO audits
- 🏠 **[Airbnb Scraper](https://github.com/everythingscraper/airbnb-scraper)** — STR metrics, ADR, RevPAR
- 🏨 **[Trip.com Hotel Scraper](https://github.com/everythingscraper/trip-hotel-scraper)** — hotel pricing across 51 countries

## Is it legal to scrape Booksy?

This Actor extracts only publicly listed business information — names, addresses, phone numbers, websites, and social handles that businesses themselves have published on Booksy as a marketing surface. It does not access user accounts, bookings, or private customer data. Personal data may still be subject to the GDPR (EU) and similar laws — use leads only for legitimate B2B outreach and consult your lawyers if unsure.

## License

MIT — see [LICENSE](./LICENSE).
