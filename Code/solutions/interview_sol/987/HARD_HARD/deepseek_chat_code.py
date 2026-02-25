```python
import math

def determine_winner(finish, distancetoBolt, tigerAccelaration, boltSpeed):
    time_bolt = finish / boltSpeed
    
    distance_tiger = finish + distancetoBolt
    
    if tigerAccelaration == 0:
        return "Tiger" if distancetoBolt == 0 else "Bolt"
    
    time_tiger = math.sqrt(2 * distance_tiger / tigerAccelaration)
    
    if time_bolt < time_tiger:
        return "Bolt"
    else:
        return "Tiger"

def solve(T, test_cases):
    results = []
    for i in range(T):
        finish, distancetoBolt, tigerAccelaration, boltSpeed = test_cases[i]
        results.append(determine_winner(finish, distancetoBolt, tigerAccelaration, boltSpeed))
    return results
```