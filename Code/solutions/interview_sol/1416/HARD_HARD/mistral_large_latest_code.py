```python
def divide_stones(n, stones):
    """
    Divides the stones between Han Solo and Chewbacca such that the difference in total value
    between the two halves is minimized, while respecting the size constraints (n/2 for even n,
    (n-1)/2 and (n+1)/2 for odd n). The first stone in the input is always assigned to Han Solo,
    and the original order is preserved in the output.

    Args:
        n (int): Number of stones (2 <= n <= 99).
        stones (list[int]): List of stone values (1 <= value <= 10^4).

    Returns:
        tuple[list[int], list[int]]: Two lists representing stones assigned to Han Solo and Chewbacca.
    """
    def backtrack(start, han_count, chew_count, han_sum, chew_sum, path, best_diff, best_han, best_chew):
        nonlocal min_diff, result_han, result_chew
        if start == n:
            if han_count == target_han and chew_count == target_chew:
                current_diff = abs(han_sum - chew_sum)
                if current_diff < min_diff:
                    min_diff = current_diff
                    result_han = path[:]
                    result_chew = [stones[i] for i in range(n) if i not in path]
                elif current_diff == min_diff:
                    if han_sum > chew_sum:
                        result_han = path[:]
                        result_chew = [stones[i] for i in range(n) if i not in path]
            return

        if han_count < target_han:
            path.append(start)
            backtrack(start + 1, han_count + 1, chew_count, han_sum + stones[start], chew_sum, path, best_diff, best_han, best_chew)
            path.pop()

        if chew_count < target_chew:
            backtrack(start + 1, han_count, chew_count + 1, han_sum, chew_sum + stones[start], path, best_diff, best_han, best_chew)

    if n % 2 == 0:
        target_han = n // 2
        target_chew = n // 2
    else:
        target_han = (n + 1) // 2
        target_chew = (n - 1) // 2

    min_diff = float('inf')
    result_han = []
    result_chew = []

    # Ensure the first stone is always in Han's set
    initial_path = [0]
    backtrack(1, 1, 0, stones[0], 0, initial_path, min_diff, result_han, result_chew)

    # Reconstruct the result in original order
    han_set = [stones[i] for i in result_han]
    chew_set = [stones[i] for i in range(n) if i not in result_han]

    return han_set, chew_set
```