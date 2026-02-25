```python
def sale_hotdogs(n: int) -> int:
    """
    Calculates the total cost for buying hotdogs based on the quantity.

    Prices are as follows:
    - n < 5: 100 cents per hotdog
    - 5 <= n < 10: 95 cents per hotdog
    - n >= 10: 90 cents per hotdog

    Args:
        n: The number of hotdogs to buy. Must be a non-negative integer.

    Returns:
        The total cost in cents.

    Raises:
        ValueError: If n is not an integer or is negative.
    """
    if not isinstance(n, int):
        raise ValueError("Number of hotdogs (n) must be an integer.")
    if n < 0:
        raise ValueError("Number of hotdogs (n) cannot be negative.")

    price_per_hotdog: int
    if n < 5:
        price_per_hotdog = 100
    elif n < 10:  # This condition implicitly covers 5 <= n < 10
        price_per_hotdog = 95
    else:  # This condition implicitly covers n >= 10
        price_per_hotdog = 90

    return n * price_per_hotdog
```