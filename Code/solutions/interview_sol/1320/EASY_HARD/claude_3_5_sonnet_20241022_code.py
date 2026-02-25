```python
def solve(T, N_list):
    result = []
    for N in N_list:
        # If N is even or N=1, A can win
        if N % 2 == 0 or N == 1:
            # B loses
            result.append('B')
        else:
            # For odd N>1, A loses since B can force odd number
            result.append('A')
    return result
```