"""Run the Booksy Leads Scraper Apify Actor and print results.

Get your Apify API token: https://console.apify.com/settings/integrations
Actor page: https://apify.com/seo-scraper/booksy-leads-scraper

Install:
    pip install -r requirements.txt

Run:
    APIFY_TOKEN=your_token python main.py
"""

import os

from apify_client import ApifyClient

ACTOR_ID = "seo-scraper/booksy-leads-scraper"


def main() -> None:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        raise SystemExit("Set APIFY_TOKEN env var. Get one at https://console.apify.com/settings/integrations")

    client = ApifyClient(token)

    run_input = {
        "startUrls": [{"url": "https://booksy.com/en-us/s/haircut-beard/102522_newport-beach"}],
        "resultsToScrape": 10,
        "proxyConfiguration": {"useApifyProxy": True, "apifyProxyGroups": ["RESIDENTIAL"]},
    }

    print(f"Starting actor {ACTOR_ID} ...")
    run = client.actor(ACTOR_ID).call(run_input=run_input)

    print(f"Run finished: {run['status']}  (run id: {run['id']})")
    print(f"Console: https://console.apify.com/actors/runs/{run['id']}\n")

    dataset = client.dataset(run["defaultDatasetId"])
    items = dataset.list_items().items
    print(f"Got {len(items)} business leads.\n")

    for item in items[:5]:
        print(
            f"- {str(item.get('name', '?'))[:40]:40}  "
            f"{str(item.get('phone', '-'))[:18]:18}  "
            f"rating={item.get('rating', '-')}  "
            f"{str(item.get('address', ''))[:50]}"
        )

    print(f"\nFull dataset: https://api.apify.com/v2/datasets/{run['defaultDatasetId']}/items?format=json")


if __name__ == "__main__":
    main()
