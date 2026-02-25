```python
def iq_test(numbers: str) -> int:
    """
    Finds the position of the number that differs in evenness from the others.

    Args:
        numbers (str): A string of space-separated integers.

    Returns:
        int: The 1-based index of the number that differs in evenness.
    """
    # Split the input string into a list of integers
    nums = list(map(int, numbers.split()))

    # Determine the evenness of the first number
    is_even = nums[0] % 2 == 0

    # Find the first number that differs in evenness
    for i, num in enumerate(nums):
        if (num % 2 == 0) != is_even:
            # Return the 1-based index
            return i + 1

    # If all numbers have the same evenness, return the index of the first number
    # This case should not occur based on the problem statement
    return 1
```