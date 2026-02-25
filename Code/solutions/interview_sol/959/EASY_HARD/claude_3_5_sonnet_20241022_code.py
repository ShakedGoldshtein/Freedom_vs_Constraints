```python
def solve(test_cases):
    results = []
    for _ in range(test_cases):
        n = int(input())
        arr = sorted(list(map(int, input().split())))
        
        max_sum = 0
        for i in range(0, n-1, 2):
            max_sum += abs(arr[n-1-i] - arr[i])
            
        results.append(max_sum)
        
    return results

def solve_single(n, arr):
    arr.sort()
    max_sum = 0
    for i in range(0, n-1, 2):
        max_sum += abs(arr[n-1-i] - arr[i])
    return max_sum
```