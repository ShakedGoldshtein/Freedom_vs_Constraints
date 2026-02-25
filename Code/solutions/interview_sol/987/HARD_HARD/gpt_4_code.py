```python
from math import sqrt

def race_winner(t, cases):
    results = []
    for i in range(t):
        finish, distancetoBolt, tigerAccelaration, boltSpeed = cases[i]
        tigerTime = sqrt((2 * (finish + distancetoBolt)) / tigerAccelaration)
        boltTime = finish / boltSpeed
        if boltTime < tigerTime:
            results.append("Bolt")
        else:
            results.append("Tiger")
    return results

# Usage
print(race_winner(2, [(10, 100, 10, 10), (100, 10, 5, 10)]))
```