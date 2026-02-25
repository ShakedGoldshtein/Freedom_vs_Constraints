```python
def solve(n):
    result = []
    current = 2
    
    for level in range(1, n+1):
        # Find next perfect square that will be divisible by (level+1) after sqrt
        target = level + 1
        while target * target % (level + 1) != 0:
            target += level + 1
            
        # Calculate how many plus operations needed
        square = target * target
        plus_ops = (square - current) // level
        
        result.append(plus_ops)
        current = int((square) ** 0.5)
        
    return result
```