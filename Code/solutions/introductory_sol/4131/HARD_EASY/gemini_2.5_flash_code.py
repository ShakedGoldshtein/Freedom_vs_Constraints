```python
def how_much_water(water: float, load: int, clothes: int) -> float | str:
    """
    Calculates the amount of water needed for washing clothes, considering
    the standard load, extra items, and machine capacity limits.

    The machine uses `water` amount of water for `load` amount of clothes.
    For each single item of load above the standard amount, the machine
    will use 10% more water (multiplicatively).

    The machine has capacity limits:
    - It cannot handle any amount of clothes less than the standard `load`.
    - It cannot handle clothes more than 2 times the standard `load`.

    Args:
        water: The standard amount of water (float) used for `load` clothes.
               Expected to be non-negative.
        load: The standard amount of clothes (integer) the machine handles
              with `water` amount of water. Expected to be non-negative.
        clothes: The actual amount of clothes (integer) to wash.
                 Expected to be non-negative.

    Returns:
        The calculated water amount (float) rounded to 2 decimal places,
        or a string error message ('Not enough clothes', 'Too much clothes')
        if capacity limits are exceeded.
    """
    # Handle the "not enough clothes" edge case.
    if clothes < load:
        return 'Not enough clothes'
    
    # Handle the "too much clothes" edge case.
    # This check needs to be `elif` because if `clothes < load` is true,
    # we've already returned. If `load` is 0, and `clothes` is > 0,
    # then `clothes > 2 * 0` (i.e., `clothes > 0`) correctly triggers this.
    elif clothes > 2 * load:
        return 'Too much clothes'
    
    # If clothes are within the acceptable range (load <= clothes <= 2 * load),
    # calculate the water needed.
    else:
        # Determine the number of extra items beyond the standard load.
        # If clothes == load, extra_items will be 0.
        extra_items = clothes - load

        # Calculate the total water needed.
        # The base water amount is multiplied by 1.1 for each extra item.
        # If extra_items is 0, (1.1 ** 0) is 1, so water remains unchanged.
        calculated_water = water * (1.1 ** extra_items)

        # Round the final result to the nearest 2 decimal places.
        return round(calculated_water, 2)
```