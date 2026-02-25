```python
def construct_permutation(n, a):
    """
    Constructs a permutation b of array a such that for every non-empty proper subset S of indices,
    the sum of elements in S for a and b are different. Returns -1 if no such permutation exists.

    Args:
        n: int, size of the array (1 <= n <= 22)
        a: list[int], array of n distinct integers (0 <= a_i <= 1e9)

    Returns:
        list[int] or int: permutation b if exists, otherwise -1
    """
    if n == 1:
        return -1

    # Check if all elements are the same (though problem says distinct, so redundant)
    if len(set(a)) != n:
        return -1

    # For n=2, any swap works
    if n == 2:
        return [a[1], a[0]]

    # Try to find a permutation where the largest element is moved to a position
    # that breaks all subset sums. This works for most cases.
    max_val = max(a)
    max_idx = a.index(max_val)

    # Create a candidate permutation by swapping max element with the first element
    b = a.copy()
    b[0], b[max_idx] = b[max_idx], b[0]

    # Verify if this permutation works
    if _is_valid_permutation(a, b):
        return b

    # If the above fails, try a more systematic approach: pair elements to break sums
    # Sort the array and pair largest with smallest, second largest with second smallest, etc.
    sorted_a = sorted(a)
    b = []
    left, right = 0, n - 1
    while left <= right:
        if left == right:
            b.append(sorted_a[left])
        else:
            b.append(sorted_a[right])
            b.append(sorted_a[left])
        left += 1
        right -= 1

    # Verify this permutation
    if _is_valid_permutation(a, b):
        return b

    # If still not valid, try reversing the array
    b = a[::-1]
    if _is_valid_permutation(a, b):
        return b

    # For n=4, there's a special case where the above might fail (e.g., [1, 2, 3, 4])
    # Try a different permutation pattern
    if n == 4:
        for perm in _generate_permutations(a):
            if _is_valid_permutation(a, perm):
                return perm

    # If all else fails, return -1 (shouldn't happen for n <= 22 due to problem constraints)
    return -1

def _is_valid_permutation(a, b):
    """
    Checks if permutation b of a satisfies the condition that for every non-empty proper subset S,
    the sum of elements in S for a and b are different.

    Args:
        a: list[int], original array
        b: list[int], candidate permutation

    Returns:
        bool: True if b is valid, False otherwise
    """
    n = len(a)
    # Check all non-empty proper subsets (1 <= k < n)
    for mask in range(1, 1 << n):
        if mask == (1 << n) - 1:  # Skip full subset
            continue
        sum_a = 0
        sum_b = 0
        for i in range(n):
            if mask & (1 << i):
                sum_a += a[i]
                sum_b += b[i]
        if sum_a == sum_b:
            return False
    return True

def _generate_permutations(a):
    """
    Generates all possible permutations of a (for small n, e.g., n=4).
    Yields each permutation as a list.
    """
    from itertools import permutations
    for p in permutations(a):
        yield list(p)
```