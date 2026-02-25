```python
def disariumNumber(number: int) -> str:
    """
    Determines if a given positive integer is a Disarium number.

    A Disarium number is a number where the sum of its digits, each raised
    to the power of its respective 1-indexed position, equals the number itself.

    Args:
        number: A positive integer to be checked.

    Returns:
        "Disarium !!" if the number is a Disarium number, otherwise "Not !!".
    """
    # Convert the number to a string to easily access individual digits
    # and their positions.
    num_str = str(number)

    # Initialize a variable to store the sum of digits powered by their positions.
    sum_of_powered_digits = 0

    # Iterate through the digits of the number along with their 1-indexed positions.
    # enumerate provides 0-indexed 'i', so position is 'i + 1'.
    for i, digit_char in enumerate(num_str):
        # Convert the character digit back to an integer.
        digit = int(digit_char)
        
        # Calculate the 1-indexed position.
        position = i + 1
        
        # Add the digit raised to its position to the running sum.
        sum_of_powered_digits += digit ** position

    # Compare the calculated sum with the original number.
    if sum_of_powered_digits == number:
        return "Disarium !!"
    else:
        return "Not !!"

```