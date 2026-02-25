```python
def race_result(T, test_cases):
    results = []
    for case in test_cases:
        finish, distancetoBolt, tigerAccelaration, boltSpeed = case
        boltTime = finish / boltSpeed
        tigerTime = ((2*distancetoBolt/tigerAccelaration) ** 0.5)
        if boltTime < tigerTime:
            results.append("Bolt")
        else:
            results.append("Tiger")
    return results
```