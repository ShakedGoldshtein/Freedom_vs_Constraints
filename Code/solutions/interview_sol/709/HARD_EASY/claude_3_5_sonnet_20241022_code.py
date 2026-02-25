```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def array_gcd(arr):
    if not arr:
        return 0
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result

def get_max_gcd(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
        
    # Try removing each possible subarray and compute GCD
    max_gcd = 0
    
    # Normal array
    for i in range(n):
        for j in range(i, n):
            # Remove subarray from i to j
            remaining = arr[:i] + arr[j+1:]
            if remaining:  # Check if array is non-empty
                curr_gcd = array_gcd(remaining)
                max_gcd = max(max_gcd, curr_gcd)
    
    # Reversed array
    arr = arr[::-1]
    for i in range(n):
        for j in range(i, n):
            # Remove subarray from i to j
            remaining = arr[:i] + arr[j+1:]
            if remaining:  # Check if array is non-empty
                curr_gcd = array_gcd(remaining)
                max_gcd = max(max_gcd, curr_gcd)
                
    return max_gcd

def solve(T, test_cases):
    result = []
    for _ in range(T):
        N, arr = test_cases[_]
        result.append(get_max_gcd(arr))
    return result
```