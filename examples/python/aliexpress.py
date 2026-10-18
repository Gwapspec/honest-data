"""AliExpress US search results with the regular price next to the teaser price, ads left out.

pip install apify-client; export APIFY_TOKEN=...   ($0.003 per product)
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("honestdata/aliexpress-product-search").call(run_input={
    "keywords": ["laptop stand"],
    "maxItemsPerKeyword": 60,
    "organicOnly": True,
})
for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row)
