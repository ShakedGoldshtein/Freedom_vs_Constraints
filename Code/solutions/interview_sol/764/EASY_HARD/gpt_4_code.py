```python
def solve(T, dishes):
    output = []
    for i in range(T):
        first_dish, second_dish = dishes[i]
        same_ingredients = set(first_dish.split()) & set(second_dish.split())
        output.append('similar' if len(same_ingredients) >= 2 else 'dissimilar')
    return output
```