```python
def solve(N: int, Q: int, prices: list[int], brands: list[int], queries: list[tuple[int, int, list[int]]]) -> list[int]:
    """
    Solves the problem of finding the K-th costliest phone among preferred brands.

    Args:
        N (int): Total number of smartphones.
        Q (int): Number of queries.
        prices (list[int]): List of prices for each smartphone.
        brands (list[int]): List of brands for each smartphone.
        queries (list[tuple[int, int, list[int]]]): List of queries, each containing:
            - b (int): Size of the preference subset.
            - K (int): The K-th costliest phone to find.
            - subset (list[int]): List of preferred brands.

    Returns:
        list[int]: List of results for each query, where each result is the price of the K-th costliest phone or -1 if not found.
    """
    # Preprocess: Create a dictionary to map each brand to its list of prices
    brand_to_prices = {}
    for price, brand in zip(prices, brands):
        if brand not in brand_to_prices:
            brand_to_prices[brand] = []
        brand_to_prices[brand].append(price)

    # Preprocess: Sort the prices for each brand in descending order
    for brand in brand_to_prices:
        brand_to_prices[brand].sort(reverse=True)

    results = []
    for query in queries:
        b, K, subset = query
        # Collect all prices from the preferred brands
        preferred_prices = []
        for brand in subset:
            if brand in brand_to_prices:
                preferred_prices.extend(brand_to_prices[brand])

        # Sort the collected prices in descending order
        preferred_prices.sort(reverse=True)

        # Check if the K-th costliest phone exists
        if len(preferred_prices) >= K:
            results.append(preferred_prices[K - 1])
        else:
            results.append(-1)

    return results


# Example usage:
# N, Q = 4, 2
# prices = [4, 5, 6, 7]
# brands = [1, 2, 3, 4]
# queries = [(3, 3, [1, 2, 3]), (3, 4, [4, 5, 6])]
# print(solve(N, Q, prices, brands, queries))  # Output: [4, -1]
```