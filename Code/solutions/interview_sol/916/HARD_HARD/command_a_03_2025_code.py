```python
import math


def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The LCM of a and b.
    """
    return abs(a * b) // math.gcd(a, b)


def solve(T: int, test_cases: list[tuple[int, int]]) -> list[int]:
    """
    Solve the problem for multiple test cases.

    Args:
        T (int): The number of test cases.
        test_cases (list of tuples): A list of tuples, where each tuple contains two integers (N, M).

    Returns:
        list of int: A list of results, where each result is the minimum amount to be spent for each test case.
    """
    results = []
    for N, M in test_cases:
        # Calculate the minimum amount to be spent using LCM
        min_amount = lcm(N, M)
        results.append(min_amount)
    return results


def main(T: int, test_cases: list[tuple[int, int]]) -> list[int]:
    """
    Main function to handle input and output.

    Args:
        T (int): The number of test cases.
        test_cases (list of tuples): A list of tuples, where each tuple contains two integers (N, M).

    Returns:
        list of int: A list of results, where each result is the minimum amount to be spent for each test case.
    """
    return solve(T, test_cases)
```