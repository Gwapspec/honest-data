"""Rank product ideas by Google search demand and AliExpress US supply in one run.

pip install apify-client; export APIFY_TOKEN=...   ($0.03 per idea)
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("honestdata/product-demand-radar").call(run_input={
    "products": ["laptop stand", "magnetic phone mount", "led strip lights"],
    "geo": "US",
})
for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row)
