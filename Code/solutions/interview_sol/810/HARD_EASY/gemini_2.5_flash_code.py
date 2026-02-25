```python
def solve_single_test_case(n: int, queries: list[tuple], initial_mountains: list[int]) -> list[int]:
    """
    Solves a single test case for the Chef's Mountain Travel problem.

    Args:
        n: The number of mountains.
        queries: A list of query tuples.
                 Type 0: (0, A, B) - update mountain A to height B.
                 Type 1: (1, A) - query for nearest valid mountain to A.
        initial_mountains: A list of N integers representing initial mountain heights.

    Returns:
        A list of integers, where each integer is the answer to a Type 1 query.
        -1 if no such mountain exists for a Type 1 query.
    """
    mountains = list(initial_mountains)  # Make a mutable copy of the mountain heights
    results = []

    for query in queries:
        query_type = query[0]

        if query_type == 0:
            # Type 0 query: 0 A B (update a_A = B)
            idx_A, new_height_B = query[1], query[2]
            # Validate index A based on constraints 0 <= A <= N-1
            if 0 <= idx_A < n:
                mountains[idx_A] = new_height_B
        elif query_type == 1:
            # Type 1 query: 1 A (find a_k)
            idx_A = query[1]

            # Validate index A based on constraints 0 <= A <= N-1
            if not (0 <= idx_A < n):
                results.append(-1)
                continue

            current_height_A = mountains[idx_A]

            # Calculate the set of distinct heights in the prefix a[0...A].
            # This is crucial for the "no other peak of same height till a_i" condition.
            distinct_prefix_elements = set()
            for i in range(idx_A + 1):  # Include a[A] itself
                distinct_prefix_elements.add(mountains[i])

            best_candidate_height = -1
            min_distance = float('inf')  # Initialize minimum distance to infinity

            # Search to the left of idx_A
            for k in range(idx_A - 1, -1, -1):
                dist = idx_A - k
                # Optimization: if current distance is already greater than or equal
                # to the best distance found so far, no need to search further in this direction.
                if dist >= min_distance:
                    break

                current_height_k = mountains[k]
                # Check the conditions for a valid candidate a[k]:
                # 1. a[k] must be greater than a[A]
                # 2. a[k] must not be present in the distinct prefix elements a[0...A]
                if current_height_k > current_height_A and current_height_k not in distinct_prefix_elements:
                    best_candidate_height = current_height_k
                    min_distance = dist
                    # Since we are searching outwards from A, the first valid element found
                    # will be the closest one in this direction.
                    break

            # Search to the right of idx_A
            for k in range(idx_A + 1, n):
                dist = k - idx_A
                # Optimization: if current distance is already greater than or equal
                # to the best distance found so far, no need to search further in this direction.
                if dist >= min_distance:
                    break

                current_height_k = mountains[k]
                # Check the conditions for a valid candidate a[k]:
                # 1. a[k] must be greater than a[A]
                # 2. a[k] must not be present in the distinct prefix elements a[0...A]
                if current_height_k > current_height_A and current_height_k not in distinct_prefix_elements:
                    # If this candidate is strictly closer than the current best candidate, update.
                    # If distances are equal, we prioritize the left-side candidate due to search order.
                    # This implies a preference for smaller index in case of distance ties.
                    if dist < min_distance:
                        best_candidate_height = current_height_k
                        min_distance = dist
                    # Since we are searching outwards from A, the first valid element found
                    # will be the closest one in this direction.
                    break

            results.append(best_candidate_height)

    return results


def solve(test_cases_data: list[tuple]) -> list[list[int]]:
    """
    Main function to process all test cases for the Chef's Mountain Travel problem.

    Args:
        test_cases_data: A list of tuples, each representing a test case.
                         Each tuple: (N, Q, mountains_list, queries_list)
                         N (int): Number of mountains.
                         Q (int): Number of queries.
                         mountains_list (list[int]): Initial mountain heights.
                         queries_list (list[tuple]): List of query tuples.

    Returns:
        A list of lists, where each inner list contains results for a single test case.
    """
    all_test_case_results = []
    for n, q, mountains, queries in test_cases_data:
        all_test_case_results.append(solve_single_test_case(n, queries, mountains))
    return all_test_case_results
```