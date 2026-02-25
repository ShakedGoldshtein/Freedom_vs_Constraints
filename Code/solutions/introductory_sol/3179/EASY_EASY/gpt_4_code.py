```python
def integer_limits(l, d, x):
    is_digit_sum = lambda num, target: sum(int(digit) for digit in str(num)) == target

    n, m = l, d

    while not is_digit_sum(n, x):
        n += 1

    while not is_digit_sum(m, x):
        m -= 1

    return [n, m]
```