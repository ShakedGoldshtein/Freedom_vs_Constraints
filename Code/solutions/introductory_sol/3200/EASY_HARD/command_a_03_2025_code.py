```python
def thirt(n: int) -> int:
    """
    Calculate the stationary number using the thirt sequence.

    Args:
        n (int): The input number to process.

    Returns:
        int: The stationary number after applying the thirt sequence.
    """
    remainders: list[int] = [1, 10, 9, 12, 3, 4]  # The repeating sequence of remainders
    while True:
        total: int = 0
        digits: list[int] = [
            int(d) for d in str(n)
        ]  # Convert the number to a list of digits
        if len(digits) > len(remainders):
            # If the number has more digits than the sequence, repeat the sequence
            multiplied_remainders: list[int] = remainders * (
                len(digits) // len(remainders) + 1
            )
        else:
            multiplied_remainders: list[int] = remainders[
                : len(digits)
            ]  # Use the sequence up to the number of digits
        for i, digit in enumerate(reversed(digits)):
            total += digit * multiplied_remainders[i]  # Sum the products
        if total == n:
            return n  # If the total is the same as the input, return it
        n = total  # Update n to the new total for the next iteration
```