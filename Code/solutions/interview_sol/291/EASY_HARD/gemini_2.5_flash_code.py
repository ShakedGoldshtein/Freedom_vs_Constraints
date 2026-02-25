```python
def numOfSubarrays(arr: list[int]) -> int:
    MOD = 10**9 + 7
    
    # total_odd_subarrays stores the final count of subarrays with an odd sum.
    total_odd_subarrays = 0
    
    # current_prefix_sum_parity tracks the parity of the prefix sum ending at the current element.
    # 0 for even, 1 for odd.
    current_prefix_sum_parity = 0 
    
    # even_prefix_sum_parities_count stores the count of prefix sums encountered so far that are even.
    # We initialize it to 1 because an empty prefix sum (value 0) is considered even,
    # and it serves as a base for subarrays starting from index 0.
    even_prefix_sum_parities_count = 1 
    
    # odd_prefix_sum_parities_count stores the count of prefix sums encountered so far that are odd.
    odd_prefix_sum_parities_count = 0
    
    for num in arr:
        # Update the parity of the current prefix sum.
        # This gives the parity of (P_j) where P_j is the prefix sum up to the current element arr[j].
        current_prefix_sum_parity = (current_prefix_sum_parity + num) % 2
        
        if current_prefix_sum_parity == 1:  # If the current prefix sum (P_j) is odd
            # A subarray sum (P_j - P_i-1) is odd if P_j is odd AND P_i-1 is even.
            # Since P_j is currently odd, we need to count how many previous prefix sums (P_i-1) were even.
            # This count is stored in even_prefix_sum_parities_count.
            total_odd_subarrays = (total_odd_subarrays + even_prefix_sum_parities_count) % MOD
            
            # Increment the count of odd prefix sums because current_prefix_sum (P_j) is odd.
            odd_prefix_sum_parities_count += 1
        else:  # If the current prefix sum (P_j) is even
            # A subarray sum (P_j - P_i-1) is odd if P_j is even AND P_i-1 is odd.
            # Since P_j is currently even, we need to count how many previous prefix sums (P_i-1) were odd.
            # This count is stored in odd_prefix_sum_parities_count.
            total_odd_subarrays = (total_odd_subarrays + odd_prefix_sum_parities_count) % MOD
            
            # Increment the count of even prefix sums because current_prefix_sum (P_j) is even.
            even_prefix_sum_parities_count += 1
            
    return total_odd_subarrays

```