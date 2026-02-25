```python
def solve(t, test_cases):
    results = []
    for i in range(t):
        n = test_cases[i][0]
        a = list(test_cases[i][1])
        b = list(test_cases[i][2])
        
        operations = []
        for j in range(n-1, -1, -1):
            if a[j] == b[j]:
                continue
            if a[0] != b[j]:
                operations.append(j+1)
                for k in range(0, (j+1)//2):
                    a[k], a[j-k] = a[j-k], a[k]
                for k in range(0, j+1):
                    a[k] = '1' if a[k] == '0' else '0'
            else:
                operations.append(1)
                a[0] = '1' if a[0] == '0' else '0'
                operations.append(j+1)
                for k in range(0, (j+1)//2):
                    a[k], a[j-k] = a[j-k], a[k]
                for k in range(0, j+1):
                    a[k] = '1' if a[k] == '0' else '0'
        
        results.append((len(operations), operations))
    
    return results
```