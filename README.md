# Honest Data

Data tools that show what their data can't tell you: error bars, glitch flags, real prices, ads
labelled as ads. You only pay for real results.

All four tools run on [Apify](https://apify.com/honestdata). You can call them over HTTP, from
Python or JavaScript, or let an AI assistant use them through Apify's MCP server. Apify's free
plan includes $5 of usage credit every month.

| Tool | What you get | Price |
|---|---|---|
| [Google Trends Scraper: 200 Keywords on One Scale](https://apify.com/honestdata/google-trends-one-scale) | Up to 200 keywords on one consistent scale in one run, an error bar on every keyword, small terms that Google rounds to 0 as real numbers, and glitches in Google's data flagged | $0.005 per keyword |
| [AliExpress Scraper: Real Prices, Ads Flagged](https://apify.com/honestdata/aliexpress-product-search) | AliExpress US search results with the regular price next to the new-shopper teaser price, units sold as a number, and paid ads and free-gift promos flagged | $0.003 per product |
| [YouTube Transcript Scraper](https://apify.com/honestdata/youtube-transcript-scraper) | Transcripts in bulk, each labelled manual or auto-generated, with a flag when the language isn't the one you asked for and the share of the video covered | $0.002 per transcript |
| [Product Demand Radar](https://apify.com/honestdata/product-demand-radar) | Up to 50 product ideas ranked by Google search demand and AliExpress US supply in one run | $0.05 per idea |

Misses are free: keywords with no data, videos without a transcript and ads you filter out aren't billed.

## Research

- [**Google Trends, spring 2026: small US searches doubled, then snapped back**](research/google-trends-2026-glitch/).
  From late March to mid-June 2026, 20 unrelated everyday US searches ran 1.5 to 2.2 times their
  2025 level while big searches stayed flat. Weekly data, chart and method.
- [**AliExpress teaser prices**](research/aliexpress-teaser-prices/). In 1,196 search results, 83% of
  organic prices were first-order-only deals; the median shown price was $1.33 against a regular
  price of $10.91.

## Use the tools

- [40 ready-made examples](EXAMPLES.md): real inputs, real results, one click to run (also on the
  [website](https://gwapspec.github.io/honest-data/examples.html)).
- [Code examples](examples/) in Python and curl.
- From Claude, Cursor or any MCP client: add `https://mcp.apify.com?tools=honestdata/google-trends-one-scale`
  (or any of the four tool names) as a remote MCP server.

## License

Code examples: MIT. Research data and charts: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
credit "Honest Data".
