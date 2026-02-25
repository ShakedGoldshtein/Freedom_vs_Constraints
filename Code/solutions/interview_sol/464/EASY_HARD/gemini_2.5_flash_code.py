```python
def minOperations(n: int) -> int:
    """
    Calculates the minimum number of operations to make all elements of the array equal.
    The array is arr[i] = (2 * i) + 1 for 0 <= i < n.
    An operation involves subtracting 1 from arr[x] and adding 1 to arr[y].

    The target value for all elements in the array is the average of its initial elements.
    The sum of the array elements is sum(2*i + 1 for i in range(n)).
    This sum is 2 * sum(i for i in range(n)) + sum(1 for i in range(n)).
    sum(i for i in range(n)) = n * (n-1) / 2.
    sum(1 for i in range(n)) = n.
    So, total_sum = 2 * (n * (n-1) / 2) + n = n * (n-1) + n = n^2 - n + n = n^2.
    The average value for each element is total_sum / n = n^2 / n = n.

    The minimum number of operations is the sum of units that need to be added to elements
    that are initially less than the target value `n`.
    These are the elements arr[i] = 2*i + 1 where 2*i + 1 < n.
    This means 2*i < n - 1, or i < (n-1)/2.
    The indices i for elements less than n are 0, 1, ..., floor((n-1)/2 - 1).
    Let's analyze based on whether n is odd or even.

    Case 1: n is odd. Let n = 2k + 1.
    The elements are 1, 3, ..., n-2, n, n+2, ..., 2n-1.
    The target value is n.
    The elements less than n are 1, 3, ..., n-2.
    The differences (n - arr[i]) are:
    (n - 1), (n - 3), ..., (n - (n-2)) = 2.
    This is an arithmetic progression: 2, 4, ..., (n-1).
    The number of terms is (n-1)/2.
    The sum of this series is (number of terms / 2) * (first term + last term)
    = ((n-1)/2 / 2) * (2 + (n-1))
    = ((n-1)/4) * (n+1)
    = (n^2 - 1) / 4.

    Case 2: n is even. Let n = 2k.
    The elements are 1, 3, ..., n-1, n+1, ..., 2n-1.
    The target value is n.
    The elements less than n are 1, 3, ..., n-1.
    The differences (n - arr[i]) are:
    (n - 1), (n - 3), ..., (n - (n-1)) = 1.
    This is an arithmetic progression: 1, 3, ..., (n-1).
    This is the sum of the first n/2 odd numbers.
    The sum of the first 'm' odd numbers is m^2. Here m = n/2.
    So, the sum is (n/2)^2 = n^2 / 4.

    Both cases can be covered by these formulas.
    Python's integer division `//` will handle the results correctly.
    """
    if n % 2 == 1:
        # n is odd, e.g., n=3 -> (3*3 - 1) // 4 = 8 // 4 = 2
        return (n * n - 1) // 4
    else:
        # n is even, e.g., n=6 -> (6*6) // 4 = 36 // 4 = 9
        return (n * n) // 4

```