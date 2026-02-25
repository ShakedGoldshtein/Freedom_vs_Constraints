```python
def solve(test_cases: list[tuple[int, int, list[tuple[int, int, int]]]]) -> list[str]:
    """
    Determines if a partially filled matrix B can be completed to be a "good" matrix.

    A matrix B is "good" if there exists an array A such that B[i][j] = |A[i] - A[j]|.

    Args:
        test_cases (list): A list of tuples, where each tuple contains:
            - N (int): Dimension of the matrix.
            - Q (int): Number of filled entries in the matrix.
            - entries (list): List of tuples (i, j, val) representing filled entries.

    Returns:
        list: A list of strings ("yes" or "no") indicating whether each test case can be completed to a good matrix.
    """
    results = []
    for case in test_cases:
        N, Q, entries = case
        parent = list(range(N + 1))  # Union-Find data structure for connected components
        zero_rows = [False] * (N + 1)  # Tracks if a row has a zero entry

        def find(u: int) -> int:
            """
            Finds the root of the set containing element u with path compression.

            Args:
                u (int): The element to find the root for.

            Returns:
                int: The root of the set containing u.
            """
            while parent[u] != u:
                parent[u] = parent[parent[u]]  # Path compression
                u = parent[u]
            return u

        for i, j, val in entries:
            if i == j and val == 1:  # Diagonal entry cannot be 1
                results.append("no")
                break
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j:
                if (zero_rows[i] and val == 1) or (zero_rows[j] and val == 1):
                    results.append("no")
                    break
            else:
                if (zero_rows[i] and zero_rows[j] and val == 1) or (
                    zero_rows[i] and val == 0
                ):
                    results.append("no")
                    break
                parent[root_j] = root_i
                zero_rows[root_i] = zero_rows[root_i] or zero_rows[root_j] or (val == 0)
        else:
            results.append("yes")
    return results


# Example usage:
# test_cases = [
#     (2, 2, [(1, 1, 0), (1, 2, 1)]),
#     (2, 3, [(1, 1, 0), (1, 2, 1), (2, 1, 0)]),
#     (3, 2, [(2, 2, 0), (2, 3, 1)]),
#     (3, 3, [(1, 2, 1), (2, 3, 1), (1, 3, 1)])
# ]
# print(solve(test_cases))
```