```python
def solve(n, strings, m, operations):
    results = []
    all_strings = strings[:]
    
    for a, b in operations:
        new_str = all_strings[a-1] + all_strings[b-1]
        all_strings.append(new_str)
        
        max_k = 0
        for k in range(1, 15):
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