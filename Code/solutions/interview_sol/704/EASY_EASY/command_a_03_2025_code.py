```python
def solve(T: int, test_cases: list[tuple[int, int, int]]) -> list[int]:
    """
    Solves the problem of finding the value of X modulo M, where X is formed by appending A to itself N times.

    Args:
        T (int): The number of test cases.
        test_cases (list of tuples): Each tuple contains three integers (A, N, M) representing the input for each test case.

    Returns:
        list of int: A list containing the result of X modulo M for each test case.
    """
    results = []
    for A, N, M in test_cases:
        # Handle the case where A is 0
        if A == 0:
            results.append(0)
            continue

        # Convert A to a string to easily compute its length
        A_str = str(A)
        length_A = len(A_str)

        # Calculate the modulo of 10^length_A with M
        # This is equivalent to the modulo of the number formed by length_A zeros (e.g., 1000 for length_A=3)
        mod = pow(10, length_A, M)

        # Calculate the geometric series sum: (mod^N - 1) / (mod - 1)
        # This sum represents the number of times A is appended in the sequence
        # We use modular arithmetic to handle large exponents
        numerator = pow(mod, N, M * (mod - 1)) - 1
        denominator = mod - 1
        sum_series = numerator // denominator

        # Calculate X modulo M by multiplying A with the sum_series and taking modulo M
        # Since A can be large, we convert it to a string and process it digit by digit
        X_mod_M = 0
        for digit in A_str:
            X_mod_M = (X_mod_M * 10 + int(digit)) % M
        X_mod_M = (X_mod_M * sum_series) % M

        results.append(X_mod_M)
    return results


def main() -> list[int]:
    """
    Reads input, processes each test case, and returns the results.

    Returns:
        list of int: A list containing the result of X modulo M for each test case.
    """
    import sys

    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    test_cases = []
    index = 1
    for _ in range(T):
        A = int(data[index])
        N = int(data[index + 1])
        M = int(data[index + 2])
        test_cases.append((A, N, M))
        index += 3
    return solve(T, test_cases)
```