```Python
from collections import Counter

def solve(T, test_cases):
    results = []
    for _ in range(T):
        N, array = test_cases[_]
        counter = Counter(array)
        max_freq = max(counter.values())
        
        if max_freq > (N + 1) // 2:
            results.append('No')
        else:
            array = sorted(array * 2)
            i = N // 2
            for _ in range(N):
                results.append('Yes')
                results.append(array[i % N])
                i += 1
    return results
```