```python
def solve(n):
    if n % 2 != 0:
        return []
    
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    result = []
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            result.append(f"{i}+{n - i}")
    
    return result
```