```python
def solve(n, q, arr, queries):
    def max_removable(modified_arr):
        removed = 0
        positions = list(range(1, len(modified_arr) + 1))
        
        while True:
            found = False
            for i in range(len(modified_arr)):
                if modified_arr[i] == positions[i]:
                    found = True
                    modified_arr.pop(i)
                    positions.pop(i)
                    removed += 1
                    break
            if not found:
                break
                
        return removed
    
    result = []
    for x, y in queries:
        # Make copy of original array
        curr_arr = arr.copy()
        
        # Replace first x elements with n+1
        for i in range(x):
            curr_arr[i] = n + 1
            
        # Replace last y elements with n+1 
        for i in range(y):
            curr_arr[n-1-i] = n + 1
            
        result.append(max_removable(curr_arr))
        
    return result
```