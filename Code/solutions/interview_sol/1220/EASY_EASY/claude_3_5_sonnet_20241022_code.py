```python
def solve(N, Q, prices, brands, queries):
    result = []
    
    for query in queries:
        b, k = query[0]
        prefs = query[1]
        
        # Get prices of phones matching preferred brands
        valid_prices = []
        for i in range(N):
            if brands[i] in prefs:
                valid_prices.append(prices[i])
                
        # Sort in descending order
        valid_prices.sort(reverse=True)
        
        # Get kth costliest if exists
        if k <= len(valid_prices):
            result.append(valid_prices[k-1])
        else:
            result.append(-1)
            
    return result
```