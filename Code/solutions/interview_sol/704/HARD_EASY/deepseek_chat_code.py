```python
def mod_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def solve_test_case(A, N, M):
    if N == 0:
        return 0
    
    if A == 0:
        return 0
    
    len_A = len(str(A))
    pow_10_len = mod_pow(10, len_A, M)
    
    numerator = (mod_pow(pow_10_len, N, M) - 1 + M) % M
    denominator = (pow_10_len - 1 + M) % M
    
    if denominator == 0:
        return (A % M * N) % M
    
    inv_denominator = pow(denominator, M - 2, M)
    geometric_sum = (numerator * inv_denominator) % M
    
    return (A % M * geometric_sum) % M

def main(T, test_cases):
    results = []
    for i in range(T):
        A, N, M = test_cases[i]
        results.append(solve_test_case(A, N, M))
    return results
```