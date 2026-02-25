```python
def solve(n, q, prices, brands, queries):
    results = []
    
    for query in queries:
        b, k = query[0]
        pref_brands = set(query[1])
        
        # Get prices of phones matching preferred brands
        matching_prices = []
        for i in range(n):
            if brands[i] in pref_brands:
                matching_prices.append(prices[i])
                
        # Sort in descending order
        matching_prices.sort(reverse=True)
        
        # Get kth costliest if available
        if k <= len(matching_prices):
            results.append(matching_prices[k-1])
        else:
            results.append(-1)
            
    return results
```