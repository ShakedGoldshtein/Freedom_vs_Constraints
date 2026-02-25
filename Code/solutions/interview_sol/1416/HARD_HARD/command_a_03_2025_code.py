```python
def divide_stones(n: int, values: list[int]) -> tuple[list[int], list[int]]:
    """
    Divide the stones into two halves with minimal value difference.

    Args:
        n (int): Number of stones.
        values (list[int]): List of stone values.

    Returns:
        tuple[list[int], list[int]]: Two lists representing the stones assigned to Han Solo and Chewbacca.
    """
    # Determine the sizes of the two halves
    if n % 2 == 0:
        half_size = n // 2
    else:
        half_size = (n - 1) // 2

    # Initialize the two halves with the first value assigned to Han Solo
    han_solo = [values[0]]
    chewbacca = []

    # Initialize the sum of values for both halves
    sum_han = values[0]
    sum_chew = 0

    # Iterate through the remaining values to balance the sums
    for value in values[1:]:
        if len(han_solo) < half_size or (
            len(han_solo) == half_size and len(chewbacca) < half_size + 1
        ):
            if abs(sum_han + value - sum_chew) <= abs(sum_han - (sum_chew + value)):
                han_solo.append(value)
                sum_han += value
            else:
                chewbacca.append(value)
                sum_chew += value
        else:
            break

    # If n is odd, ensure the sizes are (n-1)/2 and (n+1)/2
    if n % 2 != 0:
        if len(han_solo) > len(chewbacca):
            chewbacca.append(han_solo.pop())
        else:
            han_solo.append(chewbacca.pop())

    return han_solo, chewbacca
```