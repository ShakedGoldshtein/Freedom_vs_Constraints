```python
def check_dish_similarity(T, dish_pairs):
    results = []
    for _ in range(T):
        dish1, dish2 = dish_pairs[_]
        similars = set(dish1) & set(dish2)
        if len(similars) >= 2:
            results.append('similar')
        else:
            results.append('dissimilar')
    return results
```