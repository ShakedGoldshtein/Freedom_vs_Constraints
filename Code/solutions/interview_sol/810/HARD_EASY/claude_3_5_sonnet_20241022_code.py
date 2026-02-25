```python
def solve_mountain_queries(T, test_cases):
    results = []
    
    for _ in range(T):
        N, Q = test_cases[_][0]
        mountains = test_cases[_][1]
        queries = test_cases[_][2]
        
        case_results = []
        for query in queries:
            if query[0] == 0:  # Type 1 - Update height
                A, B = query[1], query[2]
                mountains[A] = B
            else:  # Type 2 - Find next greater height
                A = query[1]
                current_height = mountains[A]
                
                # Find next greater height
                result = -1
                min_greater = float('inf')
                found_heights = set()
                
                for i in range(A+1, N):
                    if mountains[i] > current_height:
                        if mountains[i] not in found_heights:
                            if mountains[i] < min_greater:
                                min_greater = mountains[i]
                                result = mountains[i]
                    if mountains[i] == current_height:
                        break
                    found_heights.add(mountains[i])
                
                case_results.append(result)
                
        results.extend(case_results)
        
    return results

def solve(test_input):
    # Parse input
    T = test_input[0]
    current_line = 1
    test_cases = []
    
    for _ in range(T):
        N, Q = test_input[current_line]
        current_line += 1
        
        mountains = test_input[current_line]
        current_line += 1
        
        queries = []
        for i in range(Q):
            queries.append(test_input[current_line+i])
        current_line += Q
        
        test_cases.append(((N,Q), mountains, queries))
    
    return solve_mountain_queries(T, test_cases)
```