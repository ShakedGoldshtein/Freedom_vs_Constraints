```python
def how_much_water(water: float, load: int, clothes: int) -> float | str:
    """
    Calculate the water needed to wash a given load of clothes, accounting for
    increased water usage for loads above the standard capacity. Handles edge cases
    where the load is too small or too large for the machine.

    Args:
        water: Base water amount required for the standard load.
        load: Standard capacity of clothes the machine can handle.
        clothes: Actual amount of clothes to be washed.

    Returns:
        Water needed (rounded to 2 decimal places) or an error message if the load
        is invalid ('Too much clothes' or 'Not enough clothes').
    """
    if clothes > 2 * load:
        return "Too much clothes"
    if clothes < load:
        return "Not enough clothes"

    excess = clothes - load
    multiplier = 1.1 ** excess if excess > 0 else 1.0
    total_water = water * multiplier

    return round(total_water, 2)
```