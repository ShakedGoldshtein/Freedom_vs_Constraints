```python
def digit_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def find_min_max(l, d, x):
    min_num = None
    max_num = None
    
    for num in range(l, d + 1):
        if digit_sum(num) == x:
            if min_num is None:
                min_num = num
            max_num = num
    
    return [min_num, max_num]
```