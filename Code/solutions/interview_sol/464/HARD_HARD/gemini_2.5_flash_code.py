```python
def min_operations_to_equalize_array(n: int) -> int:
    """
    Calculates the minimum number of operations to make all elements of an array equal.

    The array `arr` is initialized such that `arr[i] = (2 * i) + 1` for `0 <= i < n`.
    In one operation, 1 is subtracted from `arr[x]` and 1 is added to `arr[y]`.
    The goal is to make all elements equal. The problem guarantees this is possible.

    The sum of the initial array is `sum((2*i) + 1 for i in range(n)) = n*n`.
    Since operations preserve the sum, the target value for each element will be `n*n / n = n`.

    The minimum number of operations is the total sum of units that need to be moved
    from elements `arr[i]` where `arr[i] > n`. Each operation moves 1 unit.

    If 'n' is odd (e.g., n=3):
        The array elements are [1, 3, ..., n, ..., 2n-1].
        The elements greater than 'n' are `n+2, n+4, ..., 2n-1`.
        The differences from 'n' are `2, 4, ..., n-1`.
        This is an arithmetic progression. The number of terms is `(n-1)/2`.
        The sum is `((n-1)//2) * (2 + (n-1)) // 2 = ((n-1)//2) * ((n+1)//2)`.
        This simplifies to `(n*n - 1) // 4`.

    If 'n' is even (e.g., n=6):
        The array elements are [1, 3, ..., n-1, n+1, ..., 2n-1].
        There is no element exactly equal to 'n'.
        The elements greater than 'n' are `n+1, n+3, ..., 2n-1`.
        The differences from 'n' are `1, 3, ..., n-1`.
        This is an arithmetic progression. The number of terms is `n/2`.
        The sum is `(n//2) * (1 + (n-1)) // 2 = (n//2) * (n//2)`.
        This simplifies to `(n*n) // 4`.

    Both formulas provide an optimal time complexity of O(1) and space complexity of O(1).

    Args:
        n: The length of the array (1 <= n <= 10^4).

    Returns:
        The minimum number of operations needed to make all elements equal.
    """
    if n % 2 == 1:
        # n is odd, e.g., n=3 -> arr=[1,3,5], target=3. Operations needed: (5-3) = 2.
        # Formula: (3*3 - 1) // 4 = 8 // 4 = 2.
        operations = (n * n - 1) // 4
    else:
        # n is even, e.g., n=6 -> arr=[1,3,5,7,9,11], target=6. Operations needed: (7-6)+(9-6)+(11-6) = 1+3+5 = 9.
        # Formula: (6*6) // 4 = 36 // 4 = 9.
        operations = (n * n) // 4

    return operations
```