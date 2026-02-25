```python
def padovan(n):
    """ Function to calculate the i-th Padovan number """
    if n < 3:
        # base case, P(0)=P(1)=P(2)=1
        if n < 0:
            raise Exception("Invalid input, n must be a non-negative integer.")
        else:
            return 1
    else:
        # store the first three numbers
        p = [1,1,1]
        for i in range(3, n+1):
            # P(n)=P(n-2)+P(n-3)
            p.append(p[i-2] + p[i-3])
        return p[n]
```