```python
from collections import deque
from math import ceil, log2

def solve(n: int, q: int, a: list[int], queries: list[int]) -> list[tuple[int, int]]:
    """
    Solves the problem of determining the two elements pulled out of a deque after m_j operations.

    Args:
        n (int): Number of elements in the deque.
        q (int): Number of queries.
        a (list[int]): List of integers representing the deque elements.
        queries (list[int]): List of integers representing the queries.

    Returns:
        list[tuple[int, int]]: List of tuples, each containing the two elements pulled out for each query.
    """
    # Initialize the deque with the given elements
    dq = deque(a)
    
    # Precompute the sequence of operations until a cycle is detected
    sequence = []
    seen = {}
    max_operations = 2 * n  # To prevent infinite loops
    operation_count = 0
    
    while operation_count < max_operations:
        a = dq.popleft()
        b = dq.popleft()
        sequence.append((a, b))
        if (a, b) in seen:
            # Cycle detected, break the loop
            break
        seen[(a, b)] = operation_count
        if a > b:
            dq.appendleft(a)
            dq.append(b)
        else:
            dq.appendleft(b)
            dq.append(a)
        operation_count += 1
    
    # If no cycle, assume the sequence repeats after max_operations
    if operation_count == max_operations:
        cycle_length = operation_count
    else:
        cycle_length = operation_count - seen[(a, b)]
    
    # Process each query
    result = []
    for m in queries:
        if m <= len(sequence):
            result.append(sequence[m - 1])
        else:
            # Find the position in the cycle
            pos = (m - 1) % cycle_length
            result.append(sequence[pos])
    
    return result

# Example usage:
# n, q = 5, 3
# a = [1, 2, 3, 4, 5]
# queries = [1, 2, 10]
# print(solve(n, q, a, queries))
```