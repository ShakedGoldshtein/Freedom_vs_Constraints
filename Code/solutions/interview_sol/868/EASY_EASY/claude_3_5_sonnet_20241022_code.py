```python
def solve(n, k, arr):
    def get_kth_element(subarr):
        length = len(subarr)
        m = (k + length - 1) // length
        extended = subarr * m
        return sorted(extended)[k-1]
    
    def count_occurrences(value, arr):
        return sum(1 for x in arr if x == value)
    
    beautiful = 0
    
    for i in range(n):
        for j in range(i, n):
            subarr = arr[i:j+1]
            kth = get_kth_element(subarr)
            freq = count_occurrences(kth, subarr)
            if freq in subarr:
                beautiful += 1
                
    return beautiful

def solve_multiple_testcases(t, testcases):
    results = []
    for _ in range(t):
        n, k = testcases[_][0]
        arr = testcases[_][1]
        results.append(solve(n, k, arr))
    return results
```