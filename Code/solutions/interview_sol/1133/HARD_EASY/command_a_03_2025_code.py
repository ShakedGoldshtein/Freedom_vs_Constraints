```python
from math import gcd
from functools import reduce

def compute_gcd_of_list(numbers: list[int]) -> int:
    """
    Compute the greatest common divisor (GCD) of a list of integers.

    Args:
        numbers (list[int]): List of integers.

    Returns:
        int: The GCD of all integers in the list.
    """
    return reduce(gcd, numbers)

def calculate_total_cost(wire_length: int, connections: list[int]) -> int:
    """
    Calculate the total cost of wires needed for all connections.

    Args:
        wire_length (int): The length of each wire piece.
        connections (list[int]): List of required wire lengths for each connection.

    Returns:
        int: The total cost of wires needed.
    """
    return sum(connection // wire_length for connection in connections)

def solve(test_cases: list[tuple[int, list[int]]]) -> list[tuple[int, int]]:
    """
    Solve the wire connection problem for multiple test cases.

    Args:
        test_cases (list[tuple[int, list[int]]]): List of tuples, where each tuple contains:
            - n (int): Number of connections.
            - connections (list[int]): List of required wire lengths for each connection.

    Returns:
        list[tuple[int, int]]: List of tuples, where each tuple contains:
            - wire_length (int): The optimal length of each wire piece.
            - total_cost (int): The corresponding minimum cost.
    """
    results = []
    for case in test_cases:
        n, connections = case
        wire_length = compute_gcd_of_list(connections)
        total_cost = calculate_total_cost(wire_length, connections)
        results.append((wire_length, total_cost))
    return results

# Example usage:
# test_cases = [(3, [2, 4, 8])]
# print(solve(test_cases))  # Output: [(2, 7)]
```