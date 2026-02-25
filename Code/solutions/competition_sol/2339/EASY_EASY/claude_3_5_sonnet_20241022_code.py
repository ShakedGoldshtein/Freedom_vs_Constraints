```python
def solve(n, a, b):
    steps = []
    a = list(map(int, a))
    b = list(map(int, b))
    
    for i in range(n-1, -1, -1):
        if a[i] != b[i]:
            # First make a[0] match target
            if a[0] != (b[i] if i == 0 else 1):
                steps.append(1)
                a[0] = 1 - a[0]
            
            # Then flip prefix up to i+1
            if i > 0:
                steps.append(i+1)
                temp = a[:i+1]
                temp.reverse()
                for j in range(i+1):
                    temp[j] = 1 - temp[j]
                a[:i+1] = temp
            
            # Then flip prefix length 1 if needed
            if i > 0:
                steps.append(1) 
                a[0] = 1 - a[0]
    
    return [len(steps)] + steps
```