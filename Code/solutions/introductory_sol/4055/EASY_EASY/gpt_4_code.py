Here is the Python code for the problem:

```python
def solve(n):
    fib = ['0', '01']
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]
```