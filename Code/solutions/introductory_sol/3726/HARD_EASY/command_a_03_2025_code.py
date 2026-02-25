```python
def sort_array(arr: list[int]) -> list[int]:
    """
    Sorts the odd numbers in the array in ascending order while keeping even numbers in place.

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        list[int]: The modified array with odd numbers sorted in ascending order.
    """
    # Separate odd numbers from the array while keeping track of their original indices
    odd_numbers = [x for x in arr if x % 2 != 0]
    odd_numbers.sort()  # Sort the odd numbers in ascending order

    # Create a result array to store the final sorted array
    result = arr.copy()

    # Replace the odd numbers in the result array with the sorted odd numbers
    odd_index = 0
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            result[i] = odd_numbers[odd_index]
            odd_index += 1

    return result
```