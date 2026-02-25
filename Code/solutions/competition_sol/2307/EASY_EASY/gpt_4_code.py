```python
def minimum_fatigue(N, A, B, X):
    total_fatigue = 0
    for i in range(N-1):
        total_fatigue += min((X[i+1]-X[i])*A, B)
    return total_fatigue
```