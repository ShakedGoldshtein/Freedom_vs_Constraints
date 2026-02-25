```python
def solve(queries):
    result = []
    
    for s in queries:
        n = len(s)
        good = 0
        
        for i in range(n):
            for j in range(i, min(i+20, n)):
                substr = s[i:j+1]
                length = j - i + 1
                val = int(substr, 2)
                if length == val:
                    good += 1
                    
        result.append(good)
        
    return result
```