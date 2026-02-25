```python
def how_much_water(water, load, clothes):
    if clothes < load:
        return 'Not enough clothes'
    if clothes > 2 * load:
        return 'Too much clothes'
    
    multiplier = 1.1 ** (clothes - load)
    result = water * multiplier
    return round(result, 2)
```