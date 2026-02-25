```python
def maxSumDivThree(nums):
    remainder = sum(nums) % 3
    nums.sort()
    if remainder != 0:
        r1, r2, = float('inf'), float('inf')
        for n in nums:
            if n % 3 == remainder:
                return sum(nums) - n
            elif n % 3 == 3 - remainder:
                r2 = min(r2, r1 + n)
                r1 = min(r1, n)
        return sum(nums) - r2
    else:
        return sum(nums)
```