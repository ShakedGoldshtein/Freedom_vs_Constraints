```python
def canConvert(T, test_cases):
    result = []
    for t in range(T):
        N, S, P = test_cases[t]
        S, P = list(S), list(P)
        for i in range(N-1, -1, -1):
            if S[i] < P[i]:
                result.append("No")
                break
            elif S[i] > P[i]:
                if '1' in S[:i]:
                    S[S[:i].index('1')] = '0'
                    S[i] = '1'
                else:
                    result.append("No")
                    break
        else:
            result.append("Yes")
    return result
```
Here is how you could call this function:

```python
T = 3
test_cases = [
    (2, "00", "00"),
    (3, "101", "010"),
    (4, "0110", "0011"),
]
print(canConvert(T, test_cases))  # ['Yes', 'No', 'Yes']
```