```python
import math

def solve(N, A):
    """
    Calculates the optimal wire length and minimum cost to fulfill all connection requirements.

    The problem asks to choose a single integer length `L` for buying wire pieces.
    For each required connection length `A_i`, it must be possible to form `A_i` by connecting
    some number of pieces of length `L`. This implies that `A_i` must be a multiple of `L`.
    Therefore, the chosen length `L` must be a common divisor of all `A_i` in the sequence A.

    The cost is 1 per wire piece. If a connection requires length `A_i` and the chosen piece
    length is `L`, then `A_i / L` pieces are needed for that connection.
    The total cost is the sum of `(A_i / L)` for all `i`.
    To minimize this total cost, which is `(1/L) * sum(A_i)`, `L` must be maximized.

    Thus, the optimal length `L` is the greatest common divisor (GCD) of all elements in `A`.

    Args:
        N: The total number of connections (number of elements in A).
           While passed, N can also be derived from len(A).
        A: A list of integers representing the required wire lengths for each connection.

    Returns:
        A tuple (length, cost) where 'length' is the chosen integer length for buying wires
        and 'cost' is the corresponding minimum total expenditure.
    """
    if not A:
        # According to constraints (N >= 1), A will not be empty.
        # However, for robustness, if A were empty, 0 cost and length 1 (arbitrary) could be returned.
        return (1, 0)

    # Calculate the GCD of all elements in A.
    # This will be our optimal_length.
    optimal_length = A[0]
    for i in range(1, N):
        optimal_length = math.gcd(optimal_length, A[i])

    # Calculate the total cost.
    # For each required length A_i, we need A_i / optimal_length pieces.
    # Since optimal_length is the GCD, A_i is guaranteed to be perfectly divisible by optimal_length.
    total_cost = 0
    for length_req in A:
        total_cost += length_req // optimal_length

    return (optimal_length, total_cost)
```