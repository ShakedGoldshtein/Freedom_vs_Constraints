```python
def solve_test_case(n, arr):
    arr.sort()
    mid = n // 2
    left_sum = 0
    right_sum = 0
    
    for i in range(mid):
        left_sum += abs(arr[i] - arr[n - i - 1])
    
    for i in range(0, n - 1, 2):
        right_sum += abs(arr[i + 1] - arr[i])
    
    return max(left_sum, right_sum)

def main(T, test_cases):
    results = []
    for i in range(T):
        n = test_cases[i][0]
        arr = test_cases[i][1]
        results.append(solve_test_case(n, arr))
    return results
```