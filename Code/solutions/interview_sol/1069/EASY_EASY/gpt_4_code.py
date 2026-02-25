```python
def sum_numbers(T, test_cases):
    result = []
    for i in range(T):
        result.append(sum(test_cases[i]))
    return result
```