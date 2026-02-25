```python
def solve(n: int, a: list[int]) -> list[int] | int:
    """
    Constructs an array b by permuting array a such that for every non-empty subset of indices,
    the sums of elements at those positions in a and b are different.

    Args:
        n (int): The size of the array.
        a (list[int]): The array of distinct integers.

    Returns:
        list[int] | int: A permutation of array a that satisfies the condition, or -1 if no such permutation exists.
    """
    if n <= 1:
        return -1

    # Sort the array in ascending order to facilitate permutation
    a_sorted = sorted(a)

    # Create a permutation by alternating between the smallest and largest remaining elements
    b = []
    left, right = 0, n - 1
    for i in range(n):
        if i % 2 == 0:
            b.append(a_sorted[right])
            right -= 1
        else:
            b.append(a_sorted[left])
            left += 1

    return b
```