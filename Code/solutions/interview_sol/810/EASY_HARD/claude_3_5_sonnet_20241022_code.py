```python
def solve(T, test_cases):
    results = []
    
    for _ in range(T):
        N, Q = test_cases[_][0]
        A = test_cases[_][1]
        queries = test_cases[_][2]
        
        for query in queries:
            if query[0] == 0:
                # Update query
                A[query[1]] = query[2]
            else:
                # Find next greater unique height
                pos = query[1]
                curr_height = A[pos]
                next_greater = float('inf')
                result = -1
                
                # Check heights between current position and end
                seen_heights = set()
                for i in range(pos+1, N):
                    if A[i] > curr_height and A[i] not in seen_heights:
                        if A[i] < next_greater:
                            next_greater = A[i]
                            result = A[i]
                    seen_heights.add(A[i])
                
                results.append(result)
                
    return results
```