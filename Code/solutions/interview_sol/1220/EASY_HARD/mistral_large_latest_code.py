```python
def solve(N, Q, prices, brands, queries):
    brand_to_prices = {}
    for brand in range(1, 7):
        brand_to_prices[brand] = []

    for price, brand in zip(prices, brands):
        brand_to_prices[brand].append(price)

    for brand in brand_to_prices:
        brand_to_prices[brand].sort(reverse=True)

    results = []
    for query in queries:
        b, K, preference = query
        selected_prices = []
        for brand in preference:
            selected_prices.extend(brand_to_prices[brand])

        selected_prices.sort(reverse=True)
        if K <= len(selected_prices):
            results.append(selected_prices[K-1])
        else:
            results.append(-1)

    return results
```