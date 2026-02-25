```python
def solve(n):
    if n % 2 != 0:
        return []
        
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
        
    result = []
    for i in range(2, n//2 + 1):
        if is_prime(i) and is_prime(n-i):
            if i <= n-i:
                result.append(f'{i}+{n-i}')
            
    return result
```