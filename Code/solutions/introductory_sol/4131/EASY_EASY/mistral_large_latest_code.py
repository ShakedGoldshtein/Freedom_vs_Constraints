```python
def how_much_water(water, load, clothes):
    if clothes > 2 * load:
        return "Too much clothes"
    if clothes < load:
        return "Not enough clothes"
    excess = clothes - load
    if excess <= 0:
        return round(water, 2)
    multiplier = 1.1 ** excess
    result = water * multiplier
    return round(result, 2)
```