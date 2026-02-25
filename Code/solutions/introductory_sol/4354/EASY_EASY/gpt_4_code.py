```python
def padovan(n):
    sequence = [1, 1, 1]

    for i in range(3, n + 1):
        sequence.append(sequence[i-2] + sequence[i-3])
    
    return sequence[n]
```