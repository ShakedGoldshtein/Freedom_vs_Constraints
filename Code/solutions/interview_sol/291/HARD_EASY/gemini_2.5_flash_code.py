```python
def count_subarrays_with_odd_sum(arr: list[int]) -> int:
    """
    Calculates the number of subarrays with an odd sum in a given array.

    This solution uses an optimal O(N) time complexity and O(1) space complexity
    approach. It leverages the properties of prefix sums and their parities
    to efficiently count subarrays with an odd sum.
    The sum of a subarray arr[i...j] can be expressed as prefix_sum[j+1] - prefix_sum[i].
    For this difference to be odd, the parities of prefix_sum[j+1] and prefix_sum[i]
    must be different (one even, one odd).

    Args:
        arr: A list of integers. Constraints: 1 <= arr.length <= 10^5, 1 <= arr[i] <= 100.

    Returns:
        The total number of subarrays with an odd sum, computed modulo 10^9 + 7.
    """

    MOD = 10**9 + 7

    # Initialize the total count of subarrays with odd sum.
    total_odd_subarrays = 0

    # `current_prefix_sum_parity` tracks the parity of the cumulative sum
    # from the beginning of the array up to the current element.
    # It starts at 0 to represent the parity of an empty prefix sum (0, which is even).
    current_prefix_sum_parity = 0  # 0 for even, 1 for odd

    # `num_even_prefix_sums` counts how many times an even prefix sum parity
    # has been encountered so far. We initialize it to 1 to account for the
    # 'empty prefix sum' (0), which is always even.
    num_even_prefix_sums = 1

    # `num_odd_prefix_sums` counts how many times an odd prefix sum parity
    # has been encountered so far. Initially, no odd prefix sums have been seen.
    num_odd_prefix_sums = 0

    for num in arr:
        # Update the parity of the current cumulative sum.
        # We only need the parity of 'num' for this update.
        current_prefix_sum_parity = (current_prefix_sum_parity + num) % 2

        if current_prefix_sum_parity == 1:  # Current prefix sum (S_k) is odd
            # To get an odd subarray sum (S_k - S_i), S_i must be even.
            # All previously counted even prefix sums (S_i) will form an odd sum
            # when subtracted from the current odd prefix sum (S_k).
            total_odd_subarrays = (total_odd_subarrays + num_even_prefix_sums) % MOD
            # Since the current prefix sum S_k is odd, increment the count of odd prefix sums.
            num_odd_prefix_sums += 1
        else:  # Current prefix sum (S_k) is even
            # To get an odd subarray sum (S_k - S_i), S_i must be odd.
            # All previously counted odd prefix sums (S_i) will form an odd sum
            # when subtracted from the current even prefix sum (S_k).
            total_odd_subarrays = (total_odd_subarrays + num_odd_prefix_sums) % MOD
            # Since the current prefix sum S_k is even, increment the count of even prefix sums.
            num_even_prefix_sums += 1

    return total_odd_subarrays
```