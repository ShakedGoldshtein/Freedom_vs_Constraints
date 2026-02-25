```python
def solve(test_cases: list[tuple[int, list[int]]]) -> list[int]:
    """
    Solves the problem of maximizing the sum of absolute differences between pairs of elements in an array.

    Args:
        test_cases (list of tuples): Each tuple contains (N, A), where N is the number of elements in the array,
                                     and A is the list of integers.

    Returns:
        list of int: A list containing the maximum sum achievable for each test case.
    """
    results = []
    for case in test_cases:
        N, A = case
        # Sort the array to easily pair the smallest with the largest elements
        A_sorted = sorted(A)
        total = 0
        # Iterate over the sorted array in steps of 2, pairing adjacent elements
        for i in range(0, N, 2):
            # Add the absolute difference between the current pair to the total
            total += abs(A_sorted[i] - A_sorted[i + 1])
        results.append(total)
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
        N = int(data[idx])  # Number of elements in the current test case
        idx += 1
        A = list(map(int, data[idx : idx + N]))  # Array of integers for the current test case
        idx += N
        test_cases.append((N, A))
    results = solve(test_cases)
    for res in results:
        print(res)


if __name__ == "__main__":
    main()
```