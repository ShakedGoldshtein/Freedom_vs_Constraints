```python
from collections import defaultdict
from bisect import bisect_left
def solve(N, Q, prices, brands, queries):
    brand_price = defaultdict(list)
    for i in range(N):
        brand_price[brands[i]].append(prices[i])
    for _, prices in brand_price.items():
        prices.sort(reverse=True)
    result = []
    for b, K, preference in queries:
        available_prices = []
        for p in preference:
            available_prices.extend(brand_price[p])
        available_prices.sort(reverse=True)
        if K > len(available_prices):
            result.append(-1)
        else:
            result.append(available_prices[K-1])
    return result
```