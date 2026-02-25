```python
def check_dish_similarity(test_cases):
    results = []
    for case in test_cases:
        dish1, dish2 = case
        set1 = set(dish1)
        set2 = set(dish2)
        common = set1 & set2
        results.append("similar" if len(common) >= 2 else "dissimilar")
    return results
```