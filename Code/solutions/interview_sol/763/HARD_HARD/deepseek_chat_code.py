```python
def can_convert(S, P):
    if S == P:
        return True
    
    count_S1 = S.count('1')
    count_P1 = P.count('1')
    if count_S1 != count_P1:
        return False
    
    n = len(S)
    balance = 0
    for i in range(n):
        if S[i] != P[i]:
            if S[i] == '1':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
    
    return True

def main(T, test_cases):
    results = []
    for i in range(T):
        N, S, P = test_cases[i]
        if can_convert(S, P):
            results.append("Yes")
        else:
            results.append("No")
    return results
```