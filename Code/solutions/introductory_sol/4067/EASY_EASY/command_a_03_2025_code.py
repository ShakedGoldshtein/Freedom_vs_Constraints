```python
def iq_test(numbers: str) -> int:
    """
    Finds the position of the number that differs in evenness from the others.

    Args:
        numbers (str): A string of space-separated integers.

    Returns:
        int: The position (starting from 1) of the number that differs in evenness.
    """
    # Split the input string into a list of integers
    nums = list(map(int, numbers.split()))
    
    # Determine the evenness of the first number
    is_even = nums[0] % 2 == 0
    
    # Find the first number that differs in evenness
    for i, num in enumerate(nums):
        if (num % 2 == 0) != is_even:
            # Return the position (1-based index)
            return i + 1
    
    # If no differing number is found, return the position of the first number that is different
    is_even = not is_even
    for i, num in enumerate(nums):
        if (num % 2 == 0) == is_even:
            return i + 1
```