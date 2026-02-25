```python
from bisect import bisect_left
from collections import defaultdict

def solve(N, Q, prices, brands, queries):
    # Preprocess: map each brand to a sorted list of prices
    brand_to_prices = defaultdict(list)
    for price, brand in zip(prices, brands):
        brand_to_prices[brand].append(price)

    # Sort each brand's prices in descending order for efficient K-th max lookup
    for brand in brand_to_prices:
        brand_to_prices[brand].sort(reverse=True)

    results = []
    for query in queries:
        b, K, preference = query
        # Collect all relevant prices from preferred brands
        all_prices = []
        for brand in preference:
            if brand in brand_to_prices:
                all_prices.extend(brand_to_prices[brand])

        # Sort all collected prices in descending order
        all_prices.sort(reverse=True)

        # Determine the K-th costliest price (1-based index)
        if K <= len(all_prices):
            results.append(all_prices[K-1])
        else:
            results.append(-1)

    return results

def parse_input(N, Q, prices, brands, query_data):
    queries = []
    idx = 0
    for _ in range(Q):
        b, K = query_data[idx]
        preference = query_data[idx + 1]
        queries.append((b, K, preference))
        idx += 2
    return solve(N, Q, prices, brands, queries)
```