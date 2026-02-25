```python
def is_monotonic(A):
    increasing = decreasing = True
    for i in range(len(A) - 1):
        if A[i] > A[i+1]:
            increasing = False
        if A[i] < A[i+1]:
            decreasing = False
        if not increasing and not decreasing:
            return False
    return True
```