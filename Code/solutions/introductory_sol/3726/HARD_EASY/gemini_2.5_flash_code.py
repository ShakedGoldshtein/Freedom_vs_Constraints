```python
def sort_array(arr: list[int]) -> list[int]:
    """
    Sorts odd numbers in ascending order while maintaining the positions of even numbers.
    Zero is treated as an even number and its position is not changed.

    Args:
        arr: A list of integers.

    Returns:
        A new list with odd numbers sorted in their original positions and
        even numbers remaining in their original places.
        Returns an empty list if the input list is empty.

    Time Complexity:
        O(N log K), where N is the total number of elements in the input array
        and K is the number of odd elements. This is due to one pass through
        the array (O(N)) to extract odd numbers and another pass to reconstruct
        the result, along with sorting the K odd numbers (O(K log K)).
        In the worst case (all elements are odd), this becomes O(N log N).

    Space Complexity:
        O(N), where N is the total number of elements in the input array.
        This is due to storing the extracted odd numbers (O(K)) and the
        resulting array (O(N)).
    """
    if not arr:
        return []

    # 1. Extract all odd numbers from the input array.
    # A number is odd if its remainder when divided by 2 is not 0.
    # This correctly handles both positive and negative integers.
    # Zero (0 % 2 == 0) is correctly identified as an even number.
    odd_numbers = [num for num in arr if num % 2 != 0]

    # 2. Sort the extracted odd numbers in ascending order.
    odd_numbers.sort()

    # 3. Reconstruct the array: Iterate through the original array.
    #    If an element is even, place it directly into the result.
    #    If an element is odd, take the next smallest number from the
    #    sorted_odd_numbers list and place it into the result.
    result_array = []
    odd_idx = 0  # Pointer to keep track of the next sorted odd number to use

    for num in arr:
        if num % 2 == 0:
            # If the current number is even, keep it in its original place.
            result_array.append(num)
        else:
            # If the current number is odd, replace it with the next
            # available sorted odd number.
            result_array.append(odd_numbers[odd_idx])
            odd_idx += 1

    return result_array
```