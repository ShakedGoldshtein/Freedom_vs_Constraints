```python
def sale_hotdogs(n: int) -> int:
    """Calculate the total price for n hotdogs based on bulk pricing tiers.

    Args:
        n: Number of hotdogs to purchase (must be non-negative integer)

    Returns:
        Total price in cents (integer)

    Pricing tiers:
        - <5 hotdogs: 100 cents each
        - 5-9 hotdogs: 95 cents each
        - 10+ hotdogs: 90 cents each
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    return n * (90 if n >= 10 else 95 if n >= 5 else 100)
```