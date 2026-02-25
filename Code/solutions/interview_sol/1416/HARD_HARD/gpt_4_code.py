```python
def divide_stones(n, values):
    def split_sequence(n, seq):
        mid = n // 2
        return seq[:mid], seq[mid:]

    def subset_sum_closest_to_half(total, half_values):
        dp = [0] * (total + 1)
        dp[0] = 1
        closest = 0
        for i in half_values:
            for sum_ in range(total, i - 1, -1):
                dp[sum_] |= dp[sum_ - i] << 1
            closest = max(closest, dp[total // 2] >> 1)
        for sum_ in range(total // 2, -1, -1):
            if closest & 1:
                return sum_, total - sum_
            closest >>= 1

    total_value = sum(values)
    half_1_values, half_2_values = split_sequence(n, values)
    half_1_value, half_2_value = subset_sum_closest_to_half(total_value, half_1_values + half_2_values)
    half_1 = []
    half_2 = []

    for value in values:
        if value <= half_1_value and (value not in half_2_values or half_2_values.count(value) < half_1_values.count(value)):
            half_1_value -= value
            half_1.append(value)
        else:
            half_2_value -= value
            half_2.append(value)
    return half_1, half_2
```
