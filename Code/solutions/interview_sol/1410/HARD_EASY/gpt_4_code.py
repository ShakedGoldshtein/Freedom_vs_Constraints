```python
from math import comb

def probability_students(T, cases):
    EPS = 1e-7
    results = []
    for _ in range(T):
        S, N, M, K = cases[_]
        if M < K or N < K or N > S or M > S or S < 1 or M < 1 or N < 1 or K < 0:
            results.append("0.000000")
            continue
        chance = 0
        if M != S or K == 0:
            for j in range(K, min(N, M)):
                if (N - 1 - j) <= (S - M):
                    chance += comb(M - 1, j) * comb(S - M, N - 1 - j)
            chance /= comb(S - 1, N - 1)
        results.append("{:0.6f}".format(chance if abs(chance) > EPS else 0))
    return results

T = 3
cases = [(10,10,5,3),(10,4,6,4),(3,2,2,1)]
print(probability_students(T, cases))
```