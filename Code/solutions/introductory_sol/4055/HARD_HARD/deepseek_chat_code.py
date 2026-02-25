```python
def solve(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    
    if n == 0:
        return '0'
    if n == 1:
        return '01'
    
    fib_strings = ['0', '01']
    
    for i in range(2, n + 1):
        fib_strings.append(fib_strings[i - 1] + fib_strings[i - 2])
    
    return fib_strings[n]
```