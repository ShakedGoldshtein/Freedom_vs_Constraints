```python
def greatest_integer(t, ns):
    results = []
    for n in ns:
        if n % 2 == 0:
            results.append(int('1' * (n // 2)))
        else:
            results.append(int('7' + '1' * ((n - 3) // 2)))
    return results
```