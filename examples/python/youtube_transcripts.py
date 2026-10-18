"""YouTube transcripts in bulk, each labelled manual or auto-generated.

pip install apify-client; export APIFY_TOKEN=...   ($0.002 per transcript; videos without one are free)
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("honestdata/youtube-transcript-scraper").call(run_input={
    "videos": [
        "https://www.youtube.com/watch?v=jNQXAC9IVRw",
        "https://www.youtube.com/watch?v=2JK7NMfvZTY",
    ],
    "language": "en",
})
for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row)
