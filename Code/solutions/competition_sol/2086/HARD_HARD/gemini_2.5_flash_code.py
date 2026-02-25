```python
import collections

def solve_deque_queries(n: int, q: int, initial_elements: list[int], queries: list[int]) -> list[tuple[int, int]]:
    """
    Simulates a deque operation process and answers queries about elements pulled out.

    The operation consists of taking the two leftmost elements (A and B).
    If A > B, A is put to the beginning and B to the end.
    Otherwise (A <= B), B is put to the beginning and A to the end.
    This process continues for a large number of operations.

    Args:
        n: The number of elements in the deque (2 <= n <= 10^5).
        q: The number of queries (0 <= q <= 3 * 10^5).
        initial_elements: A list of n integers representing the initial deque elements.
        queries: A list of q integers, where each integer m_j (1 <= m_j <= 10^18)
                 is a query for the m_j-th operation.

    Returns:
        A list of tuples, where each tuple (A, B) represents the two elements
        pulled out for the corresponding query m_j, in the order they were pulled.
    """
    if q == 0:
        return []
    
    # n is guaranteed to be >= 2 by constraints, so max(initial_elements) is safe.
    # A collections.deque is used for O(1) popleft, append, and appendleft operations.
    deque_simulation = collections.deque(initial_elements)
    max_val = max(initial_elements)

    # Stores (A, B) pairs for operations before the maximum element
    # settles permanently at the front of the deque.
    pre_cycle_history = []
    pre_cycle_ops_count = 0

    # Simulate operations until the maximum element is at the front of the deque.
    # Once the maximum element (max_val) is at the front, it will always be 'A'
    # in subsequent operations. Since 'A' (max_val) will always be greater than or
    # equal to 'B' (any other element), 'A' will be put back at the beginning.
    # This means max_val stays at the front, and the other n-1 elements cycle.
    # The loop ensures that the first operation where max_val is placed at the front
    # is also recorded in pre_cycle_history.
    while True:
        # Pull out the first two elements
        A = deque_simulation.popleft()
        B = deque_simulation.popleft()

        # Record this operation's pulled elements
        pre_cycle_history.append((A, B))
        pre_cycle_ops_count += 1

        # Apply the rule to put elements back
        if A > B:
            deque_simulation.appendleft(A)
            deque_simulation.append(B)
        else:  # A <= B
            deque_simulation.appendleft(B)
            deque_simulation.append(A)
        
        # If the maximum element is now at the front, the pre-cycle phase is complete.
        if deque_simulation[0] == max_val:
            break

    # After the loop, deque_simulation[0] is max_val.
    # The remaining n-1 elements are in a cyclic pattern.
    # Extract these (n-1) elements for constant-time lookup in the cyclic phase.
    # Since n >= 2, n-1 >= 1, so post_cycle_elements will always contain elements.
    post_cycle_elements = list(deque_simulation)[1:]

    results = []
    for m_j in queries:
        if m_j <= pre_cycle_ops_count:
            # If the query is within the initial, non-cyclic phase.
            # m_j is 1-indexed, pre_cycle_history is 0-indexed.
            results.append(pre_cycle_history[m_j - 1])
        else:
            # If the query is in the cyclic phase.
            # In this phase, A is always max_val. B is one of the cycling elements.
            # Calculate the effective operation number within the cycle (0-indexed).
            effective_op_in_cycle = (m_j - pre_cycle_ops_count - 1)
            
            # Use modulo to find the correct element in the cycle.
            # (n - 1) is the length of the cycle and is guaranteed to be >= 1.
            b_val = post_cycle_elements[effective_op_in_cycle % (n - 1)]
            results.append((max_val, b_val))
            
    return results
```