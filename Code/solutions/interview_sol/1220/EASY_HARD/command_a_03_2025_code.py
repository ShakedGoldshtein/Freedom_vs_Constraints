```python
def solve(N: int, Q: int, P: list[int], B: list[int], queries: list[tuple[int, int, list[int]]]) -> list[int]:
    # Preprocess the data to create a dictionary mapping each brand to a list of prices
    brand_to_prices = {}
    for price, brand in zip(P, B):
        if brand not in brand_to_prices:
            brand_to_prices[brand] = []
        brand_to_prices[brand].append(price)
    
    # Sort the prices for each brand in descending order
    for brand in brand_to_prices:
        brand_to_prices[brand].sort(reverse=True)
    
    results = []
    for query in queries:
        b, K, preference = query
        # Collect all prices from the preferred brands
        preferred_prices = []
        for brand in preference:
            if brand in brand_to_prices:
                preferred_prices.extend(brand_to_prices[brand])
        
        # Sort the collected prices in descending order
        preferred_prices.sort(reverse=True)
        
        # Check if the K-th costliest phone exists
        if len(preferred_prices) >= K:
            results.append(preferred_prices[K-1])
        else:
            results.append(-1)
    
    return results
```