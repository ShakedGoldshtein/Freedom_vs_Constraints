```python
def max_sum_divisible_by_three(nums):
    total_sum = sum(nums)
    remainder = total_sum % 3

    if remainder == 0:
        return total_sum

    # Group numbers by their remainder when divided by 3
    remainder_groups = [[], [], []]
    for num in nums:
        r = num % 3
        remainder_groups[r].append(num)

    # Sort each group in descending order for efficient removal of smallest elements
    for group in remainder_groups:
        group.sort(reverse=True)

    if remainder == 1:
        # Case 1: Remove one element with remainder 1
        if remainder_groups[1]:
            return total_sum - remainder_groups[1][-1]
        # Case 2: Remove two elements with remainder 2
        if len(remainder_groups[2]) >= 2:
            return total_sum - remainder_groups[2][-1] - remainder_groups[2][-2]
    elif remainder == 2:
        # Case 1: Remove one element with remainder 2
        if remainder_groups[2]:
            return total_sum - remainder_groups[2][-1]
        # Case 2: Remove two elements with remainder 1
        if len(remainder_groups[1]) >= 2:
            return total_sum - remainder_groups[1][-1] - remainder_groups[1][-2]

    return 0
```