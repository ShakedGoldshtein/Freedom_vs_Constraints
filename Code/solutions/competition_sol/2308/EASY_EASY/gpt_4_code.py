```python
def max_column_sum(n, w, data):
    prefix_sum = [0]*(w+10)
    for array in data:
        l, *nums = array
        for j in range(l):
            prefix_sum[j] += nums[j]
            prefix_sum[j+1] -= nums[j]
        for j in range(l, w+1):
            prefix_sum[j] -= min(nums)
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] += prefix_sum[i-1]
    return prefix_sum[:w]
```