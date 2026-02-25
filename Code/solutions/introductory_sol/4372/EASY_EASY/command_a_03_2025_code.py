```python
def lostSheep(friday: list[int], saturday: list[int], total: int) -> int:
    """
    Calculate the number of sheep lost after counting on Saturday.

    Args:
        friday (list[int]): List of sheep returned on Friday.
        saturday (list[int]): List of sheep returned on Saturday.
        total (int): Total number of sheep.

    Returns:
        int: Number of sheep lost.
    """
    # Sum the sheep returned on Friday and Saturday
    total_returned = sum(friday) + sum(saturday)
    
    # Calculate the number of sheep lost by subtracting the total returned from the total sheep
    lost = total - total_returned
    
    return lost
```