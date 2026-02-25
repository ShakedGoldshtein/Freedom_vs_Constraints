```python
def sale_hotdogs(n: int) -> int:
    """
    Calculate the total cost of hotdogs based on the number of customers.

    Args:
        n (int): The number of customers buying hotdogs.

    Returns:
        int: The total cost in cents.
    """
    # Use a ternary operator to determine the price per hotdog based on the number of customers
    price_per_hotdog = 90 if n >= 10 else 95 if n >= 5 else 100
    
    # Calculate the total cost by multiplying the number of customers by the price per hotdog
    return n * price_per_hotdog
```