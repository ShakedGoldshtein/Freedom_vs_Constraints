```python
def count_beautiful_subarrays(n, k, arr):
    beautiful_count = 0
    
    # Check each possible subarray
    for l in range(n):
        for r in range(l, n):
            # Extract current subarray
            subarr = arr[l:r+1]
            subarr_len = r - l + 1
            
            # Calculate minimum m needed
            m = (k + subarr_len - 1) // subarr_len
            
            # Generate array B by repeating subarr m times
            b = []
            for _ in range(m):
                b.extend(subarr)
                
            # Sort B and get kth element
            b.sort()
            x = b[k-1]
            
            # Count frequency of x in original subarray
            f = sum(1 for num in subarr if num == x)
            
            # Check if f appears in subarray
            if f in subarr:
                beautiful_count += 1
                
    return beautiful_count

def solve(test_cases):
    result = []
    
    for _ in range(test_cases):
        n, k = test_cases[_][0]
        arr = test_cases[_][1]
        result.append(count_beautiful_subarrays(n, k, arr))
        
    return result
```