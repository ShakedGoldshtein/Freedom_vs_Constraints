```python
def max_product(numbers, k):
    numbers.sort()
    n = len(numbers)
    max_product = float('-inf')
    
    for i in range(k + 1):
        left = numbers[:i]
        right = numbers[n - (k - i):]
        product = 1
        for num in left + right:
            product *= num
        if product > max_product:
            max_product = product
    
    return max_product
```