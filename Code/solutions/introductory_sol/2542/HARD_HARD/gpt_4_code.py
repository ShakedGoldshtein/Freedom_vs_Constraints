```python
def is_monotonic(A):

    if len(A) == 1:
        return True

    direction = A[1] - A[0]
    
    for i in range(2, len(A)):
        if direction == 0:
            direction = A[i] - A[i-1]
            continue
        if breaks_direction(A[i-1], A[i], direction):
            return False

    return True

def breaks_direction(prev, curr, direction):
    difference = curr - prev
    if direction > 0:
        return difference < 0   
    return difference > 0              
```