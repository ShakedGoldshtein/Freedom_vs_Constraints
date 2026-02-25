```python
import itertools

def solve(N, Q, P, B, queries):
    # CRITICAL REQUIREMENTS:
    # 1. Solution is a function: `solve`
    # 2. DO NOT use stdin/stdout, input(), print(), or sys.stdin/sys.stdout
    # 3. DO NOT use any I/O operations
    # 4. Function accepts all input as parameters and returns the result
    # 5. Example: def solve(n, m): return result

    # Preprocessing Step 1: Group prices by brand and sort them in descending order.
    # There are only 6 brands (1 to 6), so we use a dictionary for easy access.
    brand_prices = {i: [] for i in range(1, 7)}
    for price, brand in zip(P, B):
        brand_prices[brand].append(price)

    # Sort each brand's prices in descending order.
    # This prepares the lists for efficient merging and finding the K-th costliest.
    for brand_id in brand_prices:
        brand_prices[brand_id].sort(reverse=True)

    # Preprocessing Step 2: Precompute combined and sorted prices for all possible brand subsets.
    # Since there are only 6 brands, there are 2^6 - 1 = 63 non-empty subsets.
    # This precomputation significantly speeds up query processing.
    precomputed_combined_prices = {}
    
    all_brands = list(range(1, 7)) # Brands are 1 through 6
    
    # Iterate through all possible subset sizes from 1 to 6
    for r in range(1, 7):
        # Generate all combinations of brands for the current subset size 'r'
        for subset_tuple in itertools.combinations(all_brands, r):
            current_subset_frozenset = frozenset(subset_tuple)
            
            combined_prices = []
            for brand_id in current_subset_frozenset:
                combined_prices.extend(brand_prices[brand_id])
            
            # Sort the combined prices for this subset in descending order
            combined_prices.sort(reverse=True)
            
            precomputed_combined_prices[current_subset_frozenset] = combined_prices

    # List to store the results for each query
    results = []

    # Process each query
    # The queries input format is a list of tuples: (b_size, K, preference_list)
    for q_b_size, K, preference_list in queries:
        # Convert the preference_list to a frozenset.
        # frozenset is immutable and hashable, making it suitable as a dictionary key.
        query_preference_set = frozenset(preference_list)

        # Retrieve the precomputed sorted list of prices for this preference set.
        # Since `b` is guaranteed to be between 1 and 6, and we precomputed all such subsets,
        # the key will always exist.
        available_prices = precomputed_combined_prices[query_preference_set]

        # Check if there are enough phones to find the K-th costliest.
        # K is 1-indexed, so we compare with len(available_prices).
        if K > len(available_prices):
            # If K is out of bounds, no such phone is available.
            results.append(-1)
        else:
            # The K-th costliest phone is at index K-1 in the 0-indexed sorted list.
            results.append(available_prices[K - 1])
            
    return results
```