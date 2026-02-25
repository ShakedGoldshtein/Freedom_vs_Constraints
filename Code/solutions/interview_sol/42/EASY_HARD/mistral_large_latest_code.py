```python
def count_good_substrings(queries):
    results = []
    for s in queries:
        n = len(s)
        count = 0
        for i in range(n):
            current = 0
            for j in range(i, n):
                current = (current << 1) | (1 if s[j] == '1' else 0)
                if (j - i + 1) == current:
                    count += 1
        results.append(count)
    return results
```