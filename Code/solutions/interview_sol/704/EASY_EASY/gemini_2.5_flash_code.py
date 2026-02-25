```python
import math

def _geometric_sum(base, count, mod):
    if count == 0:
        return 0
    if count == 1:
        return 1
    
    if count % 2 == 0:
        half_count = count // 2
        sum_half_terms = _geometric_sum(base, half_count, mod)
        power_half_terms = pow(base, half_count, mod)
        return (sum_half_terms * (1 + power_half_terms)) % mod
    else:
        sum_k_minus_1_terms = _geometric_sum(base, count - 1, mod)
        power_k_minus_1_terms = pow(base, count - 1, mod)
        return (sum_k_minus_1_terms + power_k_minus_1_terms) % mod

def solve(A, N, M):
    if A == 0:
        return 0

    num_digits_A = int(math.log10(A)) + 1
    
    P_mod_M = pow(10, num_digits_A, M)

    sum_series_mod_M = _geometric_sum(P_mod_M, N, M)

    return (A % M * sum_series_mod_M) % M
```