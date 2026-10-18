# Examples

You need an Apify account (the free plan includes $5 of monthly credit) and an API token from
[Console → Settings → API & Integrations](https://console.apify.com/settings/integrations).

```bash
pip install apify-client
export APIFY_TOKEN=your_token
python python/google_trends.py
```

| Script | Tool | Cost of the example |
|---|---|---|
| [python/google_trends.py](python/google_trends.py) | Google Trends, many keywords on one scale | 5 keywords ≈ $0.025 |
| [python/aliexpress.py](python/aliexpress.py) | AliExpress US search with real prices | 60 products ≈ $0.18 |
| [python/youtube_transcripts.py](python/youtube_transcripts.py) | YouTube transcripts in bulk | 2 videos ≈ $0.004 |
| [python/product_demand_radar.py](python/product_demand_radar.py) | Demand and supply per product idea | 3 ideas ≈ $0.15 |

## Without Python

Every tool can run in one HTTP call that waits for the results:

```bash
curl -X POST "https://api.apify.com/v2/acts/honestdata~youtube-transcript-scraper/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" -H "Content-Type: application/json" \
  -d '{"videos": ["https://www.youtube.com/watch?v=jNQXAC9IVRw"], "language": "en"}'
```

Swap in `google-trends-one-scale`, `aliexpress-product-search` or `product-demand-radar` with the
inputs from the Python examples.

## From an AI assistant

Add Apify's MCP server with the tools you want, for example in Claude Code:

```bash
claude mcp add --transport http honestdata "https://mcp.apify.com?tools=honestdata/youtube-transcript-scraper,honestdata/google-trends-one-scale"
```
