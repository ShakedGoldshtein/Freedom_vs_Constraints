```python
def solve_query(arr, n, x, y):
    # Create copy of array and mark invalid positions with n+1
    modified = arr.copy()
    for i in range(x):
        modified[i] = n + 1
    for i in range(y):
        modified[n-1-i] = n + 1
        
    # Greedy approach - count valid positions where value matches index+1
    weight = 0
    current_len = n
    
    # Keep trying to remove elements until no more can be removed
    while True:
        found = False
        # For each index, check if element matches position
        for i in range(current_len):
            if modified[i] == i + 1:
                # Can remove this element
                found = True
                weight += 1
                # Shift remaining elements left
                modified[i:current_len-1] = modified[i+1:current_len]
                current_len -= 1
                break
                
        if not found:
            break
            
    return weight

def solve(n, q, arr, queries):
    results = []
    for x, y in queries:
        results.append(solve_query(arr, n, x, y))
    return results
```