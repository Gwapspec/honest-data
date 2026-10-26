"""Autocomplete keyword ideas from Google, YouTube, Amazon, Bing and DuckDuckGo, merged and deduplicated.

pip install apify-client; export APIFY_TOKEN=...   ($0.001 per suggestion; autocomplete shows what people type, not search volume)
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("honestdata/autocomplete-keywords").call(run_input={
    "queries": ["standing desk"],
    "engines": ["google", "bing"],
    "maxItems": 10,
})
for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row)
