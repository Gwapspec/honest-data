"""Compare Google Trends keywords on one scale, with an error bar on each.

pip install apify-client; export APIFY_TOKEN=...   ($0.005 per keyword)
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("honestdata/google-trends-one-scale").call(run_input={
    "keywords": ["coffee", "tea", "matcha", "yerba mate", "chicory coffee"],
    "geo": "US",
    "timeRange": "today 12-m",
})
for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row)
