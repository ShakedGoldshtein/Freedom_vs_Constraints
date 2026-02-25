```python
def solve(t, strings):
    results = []
    for s in strings:
        n = len(s)
        count = 0
        prev = [0] * n
        for i in range(n):
            if s[i] == '0':
                prev[i] = prev[i-1] + 1 if i > 0 else 1
            else:
                prev[i] = 0
        
        for i in range(n):
            num = 0
            for j in range(i, max(i - 20, -1), -1):
                if s[j] == '1':
                    num += 1 << (i - j)
                    if num == i - j + 1:
                        count += 1
                    elif num > i - j + 1:
                        if num <= i - j + 1 + prev[j-1] if j > 0 else 0:
                            count += 1
                        break
                elif num == 0:
                    continue
        results.append(count)
    return results
```