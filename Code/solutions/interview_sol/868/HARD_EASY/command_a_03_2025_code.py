```python
def solve(T: int, test_cases: list[tuple[int, int, list[int]]]) -> list[int]:
    """
    Solves the problem of finding the number of beautiful subarrays for each test case.

    Args:
        T (int): Number of test cases.
        test_cases (list): List of tuples, each containing (N, K, A), where:
            N (int): Length of the array A.
            K (int): The position of the K-th smallest element in the concatenated array B.
            A (list): The array of integers.

    Returns:
        list: A list of integers representing the number of beautiful subarrays for each test case.
    """
    results = []
    for case in test_cases:
        N, K, A = case
        count = 0
        for l in range(N):
            freq = {}
            for r in range(l, N):
                # Update frequency of the current element
                freq[A[r]] = freq.get(A[r], 0) + 1
                subarray = A[l : r + 1]
                subarray_len = r - l + 1
                m = (K + subarray_len - 1) // subarray_len  # Calculate m such that m * subarray_len >= K
                B = subarray * m  # Concatenate subarray m times to form B
                sorted_B = sorted(B)  # Sort B to find the K-th smallest element
                X = sorted_B[K - 1]  # The K-th smallest element in B
                F = freq.get(X, 0)  # Number of occurrences of X in the subarray
                # Check if F occurs in the subarray
                if F in freq.values():
                    count += 1
        results.append(count)
    return results


def main() -> None:
    """
    Main function to read input, process each test case, and print the results.
    """
    import sys

    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])  # Number of test cases
    idx += 1
    test_cases = []
    for _ in range(T):
        N = int(data[idx])  # Length of the array A
        K = int(data[idx + 1])  # Position of the K-th smallest element
        idx += 2
        A = list(map(int, data[idx : idx + N]))  # Array A
        idx += N
        test_cases.append((N, K, A))
    results = solve(T, test_cases)
    for res in results:
        print(res)


if __name__ == "__main__":
    main()
```