```python
def maxProduct(arr, k):
    arr_sorted = sorted(arr, reverse=True)
    max_product = 1
    for num in arr_sorted[:k]:
        max_product *= num
    return max_product
```