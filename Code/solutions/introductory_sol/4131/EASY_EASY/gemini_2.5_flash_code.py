```python
def how_much_water(water, load, clothes):
    if clothes < load:
        return 'Not enough clothes'
    
    if clothes > 2 * load:
        return 'Too much clothes'
        
    if clothes == load:
        return round(float(water), 2)
    
    # clothes > load and clothes <= 2 * load
    extra_items = clothes - load
    calculated_water = water * (1.1 ** extra_items)
    
    return round(calculated_water, 2)
```