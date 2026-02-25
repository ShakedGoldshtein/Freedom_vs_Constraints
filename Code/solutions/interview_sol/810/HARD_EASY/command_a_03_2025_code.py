```python
from bisect import bisect_right
from collections import defaultdict


def solve(test_cases: list[tuple[int, int, list[int], list[tuple[int, int]]]]) -> list[int]:
    """
    Solves the mountain travel problem for multiple test cases.

    Args:
        test_cases (list): A list of tuples, where each tuple contains:
            - N (int): Number of mountains.
            - Q (int): Number of queries.
            - mountains (list): List of mountain heights.
            - queries (list): List of tuples representing queries.

    Returns:
        list: A list of results for Type 2 queries.
    """
    results = []
    for case in test_cases:
        N, Q, mountains, queries = case
        # Preprocess mountains to create a dictionary mapping heights to their indices
        height_to_indices = defaultdict(list)
        for idx, height in enumerate(mountains):
            height_to_indices[height].append(idx)

        # Process each query
        for query in queries:
            if query[0] == 0:
                # Type 1 query: Update mountain height
                A, B = query[1], query[2]
                old_height = mountains[A]
                mountains[A] = B
                # Update the height_to_indices dictionary
                height_to_indices[old_height].remove(A)
                height_to_indices[B].append(A)
            else:
                # Type 2 query: Find the next greater mountain
                A = query[1]
                current_height = mountains[A]
                # Find all heights greater than current_height
                greater_heights = [
                    h for h in height_to_indices.keys() if h > current_height
                ]
                greater_heights.sort()
                result = -1
                for height in greater_heights:
                    # Find the nearest mountain with this height that is not before A
                    indices = height_to_indices[height]
                    pos = bisect_right(indices, A)
                    if pos < len(indices):
                        result = height
                        break
                results.append(result)
    return results


# Example usage:
# test_cases = [
#     (10, 5, [1, 3, 5, 4, 5, 6, 7, 8, 4, 5], [
#         (1, 7), (1, 3), (1, 1), (0, 2, 7), (1, 3)
#     ])
# ]
# print(solve(test_cases))
```