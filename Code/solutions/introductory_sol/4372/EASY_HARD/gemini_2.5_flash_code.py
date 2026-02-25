```python
def calculate_lost_sheep(friday_sheep, saturday_sheep, total_sheep_on_farm):
    """
    Calculates the amount of sheep lost after final counting on Saturday.

    Args:
        friday_sheep (list): A list of integers representing groups of sheep
                             returned on Friday.
        saturday_sheep (list): A list of integers representing groups of sheep
                              returned on Saturday.
        total_sheep_on_farm (int): The total amount of sheep the farmer originally has.

    Returns:
        int: The amount of sheep lost (not returned to the farm).
    """
    total_returned_on_friday = sum(friday_sheep)
    total_returned_on_saturday = sum(saturday_sheep)

    total_returned = total_returned_on_friday + total_returned_on_saturday
    lost_sheep = total_sheep_on_farm - total_returned

    return lost_sheep
```