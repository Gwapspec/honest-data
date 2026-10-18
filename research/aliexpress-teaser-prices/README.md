# AliExpress teaser prices: what a search page really shows

On Oct 16, 2026 we pulled the first 120 AliExpress US search results for 10 common product searches:
wireless earbuds, dog toys, kitchen gadgets, car phone holder, makeup brush set, gaming mouse, water
bottle, sunglasses, desk organizer and bluetooth speaker. That's 1,196 results.

## Findings

1. **Most prices are first-order teasers.** 83% of organic listings showed a "New shoppers save $X"
   or Dollar Express price that only applies to a first order. A scraper always looks like a new
   shopper, so it only sees these. The median shown price was **$1.33**, and the median regular
   price was **$10.91**, about 8× higher. The shown price plus the "save $X" amount equalled the
   listed original price in every case we checked (574 of 574), so the regular price can be
   recovered.
2. **1 in 4 results is a paid ad.** In every one of the 10 searches, 2 to 3 of the top 10 results
   were ads.
3. **Ads sell less.** The median units sold was 107 for ads, against 358 for organic listings.
4. **Ratings barely tell products apart.** 81% of rated products were rated 4.5 or higher (median
   4.8). Units sold is the better signal, and "10,000+ sold" is a floor, not an exact number.
5. **1 in 9 results isn't a real listing.** These are "FREE with any purchase" gifts for new
   shoppers, with no price.
6. **Only 14% ship from a US warehouse.**
7. **Even outside the teasers, a discount is the default.** 98% of the remaining listings showed
   one, with a median of 56% off.

## What to do with it

- Price from regular prices, not shown prices.
- Drop ads and free-gift promos before comparing anything.
- Rank by units sold rather than by rating.

The [AliExpress tool](https://apify.com/honestdata/aliexpress-product-search) returns the regular
price next to the shown price, flags ads and promos, and outputs units sold as a number.

Findings: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), credit "Honest Data". The raw
rows aren't published.
