```python
def solve(test_cases: list[tuple[int, list[int]]]) -> list[int]:
    """
    Solves the problem of finding the maximum cost for each test case.

    Args:
        test_cases (list of tuples): Each tuple contains (N, A), where N is the number of elements,
                                     and A is the list of integers.

    Returns:
        list of int: A list containing the maximum cost for each test case.
    """
    results = []
    for case in test_cases:
        N, A = case
        # Sort the array in descending order to maximize the cost
        A_sorted = sorted(A, reverse=True)
        # Initialize the result with the first element
        result = A_sorted[0]
        # Iterate through the sorted array starting from the second element
        for num in A_sorted[1:]:
            # Update the result by taking the modulus with the current number
            result = result % num
        results.append(result)
    return results


def main() -> list[int]:
    """
    Reads input, processes each test case, and returns the results.

    Returns:
        list of int: A list containing the maximum cost for each test case.
    """
    import sys

    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])  # Number of test cases
    idx += 1
    test_cases = []
    for _ in range(T):
        N = int(data[idx])  # Number of elements in the current test case
        idx += 1
        A = list(map(int, data[idx : idx + N]))  # List of integers for the current test case
        idx += N
        test_cases.append((N, A))
    return solve(test_cases)


# Example usage:
# results = main()
# for result in results:
#     print(result)
```