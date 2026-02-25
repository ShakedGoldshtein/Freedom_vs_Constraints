```python
def solve(n, strings, m, operations):
    results = []
    all_strings = strings[:]
    
    for op in operations:
        a, b = op
        s1 = all_strings[a - 1]
        s2 = all_strings[b - 1]
        new_str = s1 + s2
        all_strings.append(new_str)
        
        max_k = 0
        for k in range(1, 15):
            if k > len(new_str):
                break
                
            found_all = True
            for num in range(1 << k):
                pattern = bin(num)[2:].zfill(k)
                if pattern not in new_str:
                    found_all = False
                    break
            
            if found_all:
                max_k = k
            else:
                break
        
        results.append(max_k)
    
    return results
```