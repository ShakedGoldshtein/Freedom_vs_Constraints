```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def array_gcd(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result

def solve(T, test_cases):
    result = []
    
    for _ in range(T):
        N = test_cases[_][0] 
        arr = test_cases[_][1]
        
        if N == 1:
            result.append(arr[0])
            continue
            
        max_gcd = 0
        
        # Try removing subarrays
        for i in range(N):
            for j in range(i, N):
                # Remove subarray from i to j
                new_arr = arr[:i] + arr[j+1:]
                if len(new_arr) > 0:
                    max_gcd = max(max_gcd, array_gcd(new_arr))
                    
        # Try reversing array
        reversed_arr = arr[::-1]
        max_gcd = max(max_gcd, array_gcd(reversed_arr))
        
        # Try removing subarrays after reversing
        for i in range(N):
            for j in range(i, N):
                new_arr = reversed_arr[:i] + reversed_arr[j+1:]
                if len(new_arr) > 0:
                    max_gcd = max(max_gcd, array_gcd(new_arr))
                    
        result.append(max_gcd)
        
    return result
```