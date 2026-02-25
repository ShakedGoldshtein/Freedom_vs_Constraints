```python
from collections import Counter

def rearrange_caps(n, arr):
    freq = Counter(arr)
    max_freq = max(freq.values()) if freq else 0
    
    if max_freq * 2 > n:
        return None
    
    sorted_indices = sorted(range(n), key=lambda i: (arr[i], i))
    result = [0] * n
    
    for i in range(n):
        result[sorted_indices[(i + max_freq) % n]] = arr[sorted_indices[i]]
    
    return result

def solve_test_cases(T, test_cases):
    results = []
    for i in range(T):
        n = test_cases[i][0]
        arr = test_cases[i][1]
        
        rearrangement = rearrange_caps(n, arr)
        if rearrangement is None:
            results.append(["No"])
        else:
            results.append(["Yes", rearrangement])
    
    return results

def main(T, N_list, A_list):
    test_cases = []
    for i in range(T):
        test_cases.append((N_list[i], A_list[i]))
    return solve_test_cases(T, test_cases)
```