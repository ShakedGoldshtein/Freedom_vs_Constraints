```python
def max_sum_divisible_by_three(nums: list[int]) -> int:
    # dp[i] stores the maximum sum found so far that has a remainder of i when divided by 3.
    # Initialize dp[0] to 0, representing the sum of an empty set, which is divisible by 3.
    # Initialize dp[1] and dp[2] to float('-inf') to signify that no sums with these
    # remainders have been found yet. Using -infinity ensures that any valid sum
    # (even a small one) will be chosen over it.
    dp = [0, float('-inf'), float('-inf')]

    for num in nums:
        # Create a temporary list to store the updated dp values for the current 'num'.
        # This is crucial to avoid using partially updated dp values within the same iteration.
        # For example, if we update dp[0] based on dp[0] and then dp[1] based on the NEW dp[0],
        # it would be incorrect. 'new_dp' ensures all updates for 'num' are based on the 'dp'
        # values from the *previous* iteration (before considering 'num').
        new_dp = list(dp)

        # Iterate through all possible previous remainders (0, 1, 2)
        for i in range(3):
            # If dp[i] is float('-inf'), it means no valid sum with remainder i was found yet,
            # so we cannot build upon it.
            if dp[i] != float('-inf'):
                # Calculate the potential new sum by adding the current number.
                current_sum = dp[i] + num
                # Determine the remainder of this new sum.
                new_remainder = current_sum % 3
                # Update the new_dp state. We want to store the maximum sum for each remainder.
                # So, we take the maximum between the existing value in new_dp[new_remainder]
                # and the 'current_sum' derived from dp[i].
                new_dp[new_remainder] = max(new_dp[new_remainder], current_sum)
        
        # After processing the current 'num' with all previous dp states,
        # update the main dp array for the next iteration.
        dp = new_dp
    
    # The maximum sum divisible by 3 will be stored in dp[0].
    # Since all numbers in `nums` are positive (1 <= nums[i] <= 10^4),
    # dp[0] will never be negative. If no numbers can form a sum divisible by 3
    # (other than 0), dp[0] will remain 0.
    return dp[0]

```