```python
def solve(n):
    if n < 0:
        raise ValueError("Invalid input. 'n' should be a non-negative integer.") 

    fibonacci_strings = ['0', '01']
    
    while len(fibonacci_strings) <= n:
        fibonacci_strings.append(fibonacci_strings[-1] + fibonacci_strings[-2])
    
    return fibonacci_strings[n]
```