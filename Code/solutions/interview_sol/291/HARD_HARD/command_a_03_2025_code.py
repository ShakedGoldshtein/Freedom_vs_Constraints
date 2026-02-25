```python
MOD = 10**9 + 7

def solve(arr: list[int]) -> int:
    """
    Returns the number of sub-arrays with odd sum in the given array.

    Args:
        arr (list[int]): A list of integers.

    Returns:
        int: The number of sub-arrays with odd sum, modulo 10^9 + 7.
    """
    n = len(arr)
    prefix_sum = 0
    odd_count = 0
    result = 0

    # Dictionary to store the frequency of prefix sums modulo 2
    prefix_mod_count = {0: 1}

    for num in arr:
        prefix_sum += num
        mod = prefix_sum % 2
        if mod in prefix_mod_count:
            result += prefix_mod_count[mod]
            result %= MOD
        prefix_mod_count[mod] = prefix_mod_count.get(mod, 0) + 1
        if mod == 1:
            odd_count += 1
        result += odd_count
        result %= MOD

    return result
```