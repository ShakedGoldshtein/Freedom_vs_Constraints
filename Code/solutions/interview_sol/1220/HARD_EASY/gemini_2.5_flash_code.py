```python
import bisect

def solve(N: int, Q: int, P: list[int], B: list[int], queries: list[tuple[int, list[int]]]) -> list[int]:
    """
    Finds the K-th costliest phone price for given brand preferences.

    This solution pre-processes the smartphone data by organizing prices for each brand
    into sorted lists. For each query, it uses binary search over the possible price range
    to find the K-th costliest price, leveraging the sorted brand-specific price lists
    for efficient counting.

    Time Complexity:
    - Preprocessing: O(N log N) for sorting all prices across all brands.
      Specifically, sum(N_j log N_j) where N_j is the number of phones of brand j,
      which is at most O(N log N) in the worst case (all N phones of one brand).
    - Per Query: O(b * log N * log(max_price)), where b is the number of preferred brands (max 6),
      log N is for binary search within each brand's price list, and log(max_price) is for
      the overall binary search for the K-th price (max price is 10^5, so log(10^5) is ~17).
      Since b and log(max_price) are small constants, this is effectively O(log N) per query.
    - Total: O(N log N + Q * b * log N * log(max_price)).
      Given N, Q <= 10^5, b <= 6, max_price <= 10^5, this is approx
      10^5 * log(10^5) + 10^5 * 6 * log(10^5) * log(10^5)
      ~ 1.7 * 10^6 + 10^5 * 6 * 17 * 17 ~ 1.7 * 10^8 operations, which is acceptable.

    Space Complexity:
    - O(N) to store all prices in brand-specific lists.

    Args:
        N: Total number of smartphones.
        Q: Total number of queries.
        P: List of N smartphone prices.
        B: List of N smartphone brands (1 to 6).
        queries: A list of queries. Each query is a tuple (K, preference_subset),
                 where K is the desired rank (1-indexed for costliest) and
                 preference_subset is a list of preferred brand IDs (e.g., [1, 2, 3]).

    Returns:
        A list of integers, where each element is the price for the corresponding
        query, or -1 if no such phone is available.
    """

    # Preprocessing: Organize prices by brand and sort them.
    # We use a list of lists (indexed 0-6).
    # sorted_brand_prices[brand_id] will store prices for brand_id.
    # Index 0 is unused for convenience to map brand IDs 1-6 directly.
    # Prices are sorted in ascending order to use bisect_left efficiently.
    sorted_brand_prices = [[] for _ in range(7)] 

    for price, brand_id in zip(P, B):
        # Constraints ensure brand_id is between 1 and 6.
        sorted_brand_prices[brand_id].append(price)
    
    # Sort each brand's price list in ascending order.
    for brand_id in range(1, 7):
        sorted_brand_prices[brand_id].sort()

    results = []

    for K_val, preference_subset in queries:
        # Helper function to count phones with price >= target_price
        # among the preferred brands.
        def count_ge(target_price: int) -> int:
            total_count = 0
            for brand_id in preference_subset:
                # Retrieve the sorted prices for the current brand.
                prices_for_brand = sorted_brand_prices[brand_id]
                
                # bisect_left returns an insertion point which comes before (to the left of)
                # any existing entries of target_price in the list.
                # All elements from this index to the end are >= target_price.
                idx = bisect.bisect_left(prices_for_brand, target_price)
                total_count += (len(prices_for_brand) - idx)
            return total_count

        # Binary search for the K-th costliest price.
        # The search space for price is from 1 to 10^5 (inclusive, as per constraints).
        low_price = 1       
        high_price = 100000 
        current_ans = -1    # Initialize result for current query to -1 (no phone found).

        while low_price <= high_price:
            mid_price = low_price + (high_price - low_price) // 2
            
            # Count how many phones across all preferred brands are at least as expensive as mid_price.
            count = count_ge(mid_price)

            if count >= K_val:
                # If there are K_val or more phones with price >= mid_price,
                # then mid_price is a possible K-th costliest price.
                # We save this as a potential answer and try to find an even higher price
                # that still satisfies the condition.
                current_ans = mid_price
                low_price = mid_price + 1
            else:
                # If there are fewer than K_val phones with price >= mid_price,
                # then mid_price is too high; we need to look for a lower price.
                high_price = mid_price - 1
        
        results.append(current_ans)

    return results

```