```python
def nim(x):
    while x & (x + 1):
        x &= x + 1
    return x

def solve(N, L, S):
    S = sorted(S, key=lambda x: -len(x))
    dp = [0] * (L + 1)
    base = 0

    for s in S:
        x = dp[len(s) + 1]
        while x in dp[:len(s) + 1]:
            x += 1
        dp[len(s)] = x
        base ^= x
        
    return "Alice" if base else "Bob"

N = 2
L = 2
S = ["00", "01"]
print(solve(N, L, S))
```
