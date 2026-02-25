```python
def solve(n, q, deque, queries):
    # Function to simulate one operation and return state after m operations
    def get_state_after_m_ops(arr, m):
        if m == 0:
            return arr
            
        cycle_len = 0
        seen = {}
        curr_state = tuple(arr)
        
        # Find cycle length
        while curr_state not in seen:
            seen[curr_state] = cycle_len
            A, B = curr_state[0], curr_state[1]
            next_state = list(curr_state[2:])
            if A > B:
                next_state = [A] + next_state + [B]
            else:
                next_state = [B] + next_state + [A]
            curr_state = tuple(next_state)
            cycle_len += 1
            
        # Get state after m operations using cycle detection
        cycle_start = seen[curr_state]
        cycle_length = cycle_len - cycle_start
        
        if m <= cycle_start:
            curr = list(arr)
            for _ in range(m):
                A, B = curr[0], curr[1]
                curr = curr[2:]
                if A > B:
                    curr = [A] + curr + [B] 
                else:
                    curr = [B] + curr + [A]
            return curr
            
        m = m - cycle_start
        m = m % cycle_length
        
        curr = list(arr)
        for _ in range(cycle_start + m):
            A, B = curr[0], curr[1]
            curr = curr[2:]
            if A > B:
                curr = [A] + curr + [B]
            else:
                curr = [B] + curr + [A]
        return curr

    result = []
    for m in queries:
        # Get state after m-1 operations to find A,B for m-th operation
        state = get_state_after_m_ops(deque, m-1)
        result.append((state[0], state[1]))
    
    return result
```