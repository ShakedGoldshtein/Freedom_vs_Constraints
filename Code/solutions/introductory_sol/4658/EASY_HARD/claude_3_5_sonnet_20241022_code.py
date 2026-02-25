```python
def max_product(lst, k):
    sorted_lst = sorted(lst, reverse=True)
    product = 1
    for i in range(k):
        product *= sorted_lst[i]
    return product
```