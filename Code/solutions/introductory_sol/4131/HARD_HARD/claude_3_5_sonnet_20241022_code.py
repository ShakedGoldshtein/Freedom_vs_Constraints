```python
def how_much_water(water, load, clothes):
    if clothes > 2 * load:
        return 'Too much clothes'
    if clothes < load:
        return 'Not enough clothes'
    extra_items = clothes - load
    if extra_items == 0:
        return float(water)
    water_needed = water * (1.1 ** extra_items)
    return round(water_needed, 2)
```