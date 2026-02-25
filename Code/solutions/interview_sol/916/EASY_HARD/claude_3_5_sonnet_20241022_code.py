```python
def solve(N, M):
    # Find LCM of N and M since both need to pay equal amount
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
        
    lcm = (N * M) // gcd(N, M)
    return lcm
```