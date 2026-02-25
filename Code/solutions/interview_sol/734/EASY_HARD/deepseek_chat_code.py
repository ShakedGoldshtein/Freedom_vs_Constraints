```python
from collections import Counter

def solve_test_case(n, a):
    count = Counter(a)
    max_freq = max(count.values())
    
    if max_freq * 2 > n:
        return "No"
    
    sorted_a = sorted(a, key=lambda x: (count[x], x))
    result = [0] * n
    shift = max_freq
    for i in range(n):
        result[i] = sorted_a[(i + shift) % n]
    
    for i in range(n):
        if a[i] == result[i]:
            return "No"
    
    return ["Yes", " ".join(map(str, result))]

def main(T, test_cases):
    output = []
    for i in range(T):
        n = test_cases[i][0]
        a = test_cases[i][1]
        result = solve_test_case(n, a)
        if result == "No":
            output.append("No")
        else:
            output.extend(result)
    return output
```