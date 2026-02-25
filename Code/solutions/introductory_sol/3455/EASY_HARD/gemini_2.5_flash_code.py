```python
def disariumNumber(number):
    """
    Checks if a given number is a Disarium number.

    A Disarium number is a number that the sum of its digits powered with
    their respective positions is equal to the number itself.

    Args:
        number (int): A positive integer.

    Returns:
        str: "Disarium !!" if the number is Disarium, "Not !!" otherwise.
    """
    num_str = str(number)
    sum_of_powers = 0
    for i, digit_char in enumerate(num_str):
        digit = int(digit_char)
        position = i + 1  # Positions are 1-indexed
        sum_of_powers += digit ** position

    if sum_of_powers == number:
        return "Disarium !!"
    else:
        return "Not !!"

```