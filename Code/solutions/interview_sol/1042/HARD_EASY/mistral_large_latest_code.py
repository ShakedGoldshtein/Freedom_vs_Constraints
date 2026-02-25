```python
import math
from math import gcd
from functools import lru_cache

def compute_good_pairs(N, P):
    if P == 1:
        return N * (N - 1) // 2

    prime_factors = get_prime_factors(P)
    if not prime_factors:
        return N * (N - 1) // 2

    total_pairs = N * (N - 1) // 2
    non_coprime_pairs = count_non_coprime_pairs(N, prime_factors)
    return total_pairs - non_coprime_pairs

def get_prime_factors(x):
    factors = set()
    if x == 1:
        return factors
    while x % 2 == 0:
        factors.add(2)
        x = x // 2
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        while x % i == 0:
            factors.add(i)
            x = x // i
    if x > 2:
        factors.add(x)
    return factors

@lru_cache(maxsize=None)
def count_multiples_up_to(n, d):
    return n // d

def count_non_coprime_pairs(N, prime_factors):
    total = 0
    for p in prime_factors:
        multiples_p = count_multiples_up_to(N, p)
        total += multiples_p * (multiples_p - 1) // 2
    for i, p1 in enumerate(prime_factors):
        for p2 in list(prime_factors)[i+1:]:
            lcm_p1_p2 = (p1 * p2) // gcd(p1, p2)
            if lcm_p1_p2 > N:
                continue
            multiples_lcm = count_multiples_up_to(N, lcm_p1_p2)
            total -= multiples_lcm * (multiples_lcm - 1) // 2
    for i, p1 in enumerate(prime_factors):
        for j, p2 in enumerate(prime_factors):
            if i >= j:
                continue
            for p3 in list(prime_factors)[j+1:]:
                lcm_p1_p2 = (p1 * p2) // gcd(p1, p2)
                lcm_p1_p2_p3 = (lcm_p1_p2 * p3) // gcd(lcm_p1_p2, p3)
                if lcm_p1_p2_p3 > N:
                    continue
                multiples_lcm = count_multiples_up_to(N, lcm_p1_p2_p3)
                total += multiples_lcm * (multiples_lcm - 1) // 2
    return total

def solve(T, test_cases):
    results = []
    for N, P in test_cases:
        results.append(compute_good_pairs(N, P))
    return results
```