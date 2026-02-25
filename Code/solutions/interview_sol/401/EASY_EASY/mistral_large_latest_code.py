```python
def max_sum_divisible_by_three(nums):
    total_sum = sum(nums)
    remainder = total_sum % 3

    if remainder == 0:
        return total_sum

    nums_sorted = sorted(nums)
    n = len(nums_sorted)

    if remainder == 1:
        # Try to remove one element with remainder 1
        for num in nums_sorted:
            if num % 3 == 1:
                return total_sum - num
        # If not found, remove two elements with remainder 2
        count = 0
        sum_to_remove = 0
        for num in nums_sorted:
            if num % 3 == 2:
                sum_to_remove += num
                count += 1
                if count == 2:
                    return total_sum - sum_to_remove
    else:  # remainder == 2
        # Try to remove one element with remainder 2
        for num in nums_sorted:
            if num % 3 == 2:
                return total_sum - num
        # If not found, remove two elements with remainder 1
        count = 0
        sum_to_remove = 0
        for num in nums_sorted:
            if num % 3 == 1:
                sum_to_remove += num
                count += 1
                if count == 2:
                    return total_sum - sum_to_remove

    return 0
```