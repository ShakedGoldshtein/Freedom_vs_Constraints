```python
def count_good_substrings(s):
    n = len(s)
    count = 0
    
    for i in range(n):
        if s[i] == '0':
            continue
            
        num = 0
        for j in range(i, min(n, i + 20)):
            num = (num << 1) | (1 if s[j] == '1' else 0)
            length = j - i + 1
            if num == length:
                count += 1
            elif num > length:
                break
    
    return count

def solve(t, queries):
    results = []
    for s in queries:
        results.append(count_good_substrings(s))
    return results
```