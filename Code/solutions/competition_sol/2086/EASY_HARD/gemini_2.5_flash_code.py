```python
import collections

def solve(n, q, a, queries):
    d = collections.deque(a)
    
    # Find the maximum value in the initial deque.
    # Once this value reaches the front, it will stay there permanently.
    max_val = max(a)
    
    # Store the (A, B) pairs pulled during the initial phase.
    # This phase continues until max_val is at the front of the deque.
    initial_operations_results = []
    
    # Simulate operations until the maximum value is at the front.
    # This loop runs at most n-1 times.
    while d[0] != max_val:
        A = d.popleft()
        B = d.popleft()
        initial_operations_results.append((A, B))
        
        if A > B:
            d.appendleft(A)
            d.append(B)
        else: # B >= A
            d.appendleft(B)
            d.append(A)
            
    # k is the number of operations that occurred in the initial phase.
    k = len(initial_operations_results)
    
    # After the initial phase, d[0] is max_val.
    # The remaining n-1 elements will cycle through the second position.
    # We extract these elements to efficiently determine future pairs.
    # Since n >= 2, n-1 is always at least 1.
    cyclic_elements = list(d)[1:] 
    
    # Prepare a list to store results for all queries.
    results = []
    
    # Process each query.
    for m_j in queries:
        if m_j <= k:
            # If the query operation m_j falls within the initial phase,
            # we can retrieve the result directly from our stored history.
            results.append(initial_operations_results[m_j - 1])
        else:
            # If the query operation m_j falls into the stable phase (after max_val is at front).
            # The first element pulled (A) will always be max_val.
            # The second element pulled (B) will be one of the cyclic_elements.
            
            # Calculate the 0-based index of the operation within the stable phase.
            # (m_j - k) is the 1-based index of the operation in the stable phase.
            # Subtract 1 to get a 0-based index, then use modulo (n-1) for cycling.
            idx = (m_j - k - 1) % (n - 1)
            
            B_pulled = cyclic_elements[idx]
            results.append((max_val, B_pulled))
            
    return results
```