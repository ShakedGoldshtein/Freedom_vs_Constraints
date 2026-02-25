```python
def find_min_fatigue(N, A, B, coords):
    fatigue = 0
    for i in range(N - 1, 0, -1):
        dist = coords[i] - coords[i - 1]
        if A * dist <= B:
            fatigue += A * dist
        else:
            fatigue += B
    return fatigue
```