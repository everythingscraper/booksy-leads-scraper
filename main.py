"""Booksy Leads Scraper — Apify Actor client example.

Scrapes a Booksy search URL and exports the leads to leads.csv,
ready to import into Clay, Apollo, HubSpot, Lemlist, or Instantly.

Actor: https://apify.com/seo-scraper/booksy-leads-scraper
"""

import csv
import os
from pathlib import Path

from apify_client import ApifyClient

ACTOR_ID = "seo-scraper/booksy-leads-scraper"
CSV_PATH = Path("leads.csv")
CSV_FIELDS = ["name", "phone", "email", "website", "address", "rating", "reviewsCount", "category", "url"]


def export_csv(items: list[dict], path: Path) -> int:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for item in items:
            writer.writerow({k: item.get(k, "") for k in CSV_FIELDS})
    return len(items)


def main() -> None:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        raise SystemExit("Missing APIFY_TOKEN. Grab one: https://console.apify.com/settings/integrations")

    client = ApifyClient(token)

    run_input = {
        "startUrls": [{"url": "https://booksy.com/en-us/s/haircut-beard/102522_newport-beach"}],
        "resultsToScrape": 10,
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"]},
    }

    print(f"~ booksy » {ACTOR_ID}")
    run = client.actor(ACTOR_ID).call(run_input=run_input)
    print(f"~ run finished: {run['status']}")

    items = client.dataset(run["defaultDatasetId"]).list_items().items
    rows = export_csv(items, CSV_PATH)
    print(f"~ exported {rows} leads to {CSV_PATH.resolve()}\n")

    for item in items[:3]:
        print(f"   • {item.get('name', '—')} — {item.get('phone', 'no phone')} — ★{item.get('rating', '—')}")

    print(f"\n~ apify dataset: https://api.apify.com/v2/datasets/{run['defaultDatasetId']}/items?format=json")


if __name__ == "__main__":
    main()
