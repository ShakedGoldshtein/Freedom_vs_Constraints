```python
def x_shape(n):
    if n < 3 or n % 2 == 0:
        return ""
        
    result = []
    for i in range(n):
        row = ['□'] * n
        row[i] = '■'
        row[n-1-i] = '■'
        result.append(''.join(row))
    
    return '\n'.join(result)
```