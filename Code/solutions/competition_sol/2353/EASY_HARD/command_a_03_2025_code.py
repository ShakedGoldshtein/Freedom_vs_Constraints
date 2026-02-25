```python
from itertools import permutations


def solve(n: int, a: list[int]) -> list[int] | int:
    """
    Constructs an array b by permuting array a such that for every non-empty subset of indices,
    the sums of elements at those positions in a and b are different.

    Args:
        n (int): The size of the array.
        a (list[int]): A list of n distinct integers.

    Returns:
        list[int] | int: A permutation of a that satisfies the condition, or -1 if no such permutation exists.
    """
    # Generate all possible permutations of the array a
    perms = permutations(a)

    # Iterate through each permutation
    for perm in perms:
        # Assume the current permutation is valid
        valid = True

        # Generate all possible non-empty subsets of indices
        for r in range(1, n):
            # Generate all combinations of indices of size r
            from itertools import combinations

            # Iterate through each combination of indices
            for indices in combinations(range(n), r):
                # Calculate the sum of elements in a and b for the current subset
                sum_a = sum(a[i] for i in indices)
                sum_b = sum(perm[i] for i in indices)

                # If the sums are equal, the permutation is not valid
                if sum_a == sum_b:
                    valid = False
                    break
            # If the permutation is not valid, move to the next permutation
            if not valid:
                break

        # If the permutation is valid, return it
        if valid:
            return list(perm)

    # If no valid permutation is found, return -1
    return -1
```