```python
def min_operations_to_equalize(n: int) -> int:
    """
    Calculate the minimum number of operations required to make all elements of the array equal.

    The array is defined as arr[i] = (2 * i) + 1 for 0 <= i < n. Each operation allows transferring
    1 unit from any element to another. The solution leverages the mathematical property that the
    sum of the array remains constant, and the target value is the average of the array.

    Args:
        n: The length of the array (1 <= n <= 10^4).

    Returns:
        The minimum number of operations needed to make all elements equal.
    """
    if n == 1:
        return 0

    total_sum = n * n
    target = total_sum // n
    operations = 0

    for i in range(n):
        current = (2 * i) + 1
        if current > target:
            operations += (current - target)

    return operations
```