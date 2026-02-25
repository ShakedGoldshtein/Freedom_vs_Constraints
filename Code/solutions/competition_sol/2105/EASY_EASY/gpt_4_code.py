```python
def valentine_gift(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    result = [0] * n
    if n >= 2:
        result[0] = 1  #price=2
        result[1] = 1  #price=3
    if n > 2:
        for i in range(2, n):
            if is_prime(i + 2):
                result[i] = 1
            else:
                result[i] = 2
    return len(set(result)), result
```
