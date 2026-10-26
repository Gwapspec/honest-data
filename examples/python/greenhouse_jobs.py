"""Open jobs from Greenhouse company boards, with a new-jobs-only mode for daily schedules.

pip install apify-client; export APIFY_TOKEN=...   ($0.001 per job)
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("honestdata/greenhouse-jobs-monitor").call(run_input={
    "boards": ["gitlab"],
    "titleKeywords": ["engineer"],
    "maxItems": 10,
})
for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row)
