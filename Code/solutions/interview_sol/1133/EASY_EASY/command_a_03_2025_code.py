```python
import math
from collections import defaultdict


def solve(test_cases: list[tuple[int, list[int]]]) -> list[tuple[int, int]]:
    """
    Solves the problem of determining the optimal wire length and minimum cost for each test case.

    Args:
        test_cases (list of tuples): Each tuple contains (N, A), where N is the number of connections,
                                     and A is a list of required wire lengths for each connection.

    Returns:
        list of tuples: Each tuple contains (length, cost), where length is the optimal wire length,
                        and cost is the minimum total cost for the corresponding test case.
    """
    results = []
    for case in test_cases:
        N, A = case
        # Find the greatest common divisor (GCD) of all wire lengths in A
        # This will be the optimal wire length to minimize waste and cost
        wire_length = A[0]
        for num in A[1:]:
            wire_length = math.gcd(wire_length, num)

        # Calculate the total cost by summing the required number of wires
        # The number of wires needed for each connection is the ceiling of the connection length divided by the wire length
        total_cost = sum((a + wire_length - 1) // wire_length for a in A)

        results.append((wire_length, total_cost))
    return results


def main() -> None:
    """
    Reads input, processes each test case, and prints the results.
    """
    import sys

    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])  # Number of test cases
    idx += 1
    test_cases = []
    for _ in range(T):
        N = int(data[idx])  # Number of connections for the current test case
        idx += 1
        A = list(map(int, data[idx : idx + N]))  # List of required wire lengths
        idx += N
        test_cases.append((N, A))
    results = solve(test_cases)
    for res in results:
        print(res[0], res[1])


if __name__ == "__main__":
    main()
```