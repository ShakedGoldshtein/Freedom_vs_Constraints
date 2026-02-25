```python
import math
from math import gcd
from functools import lru_cache

def solve(N, P):
    if P == 1:
        return N * (N - 1) // 2

    prime_factors = set()
    temp = P
    for i in range(2, int(math.isqrt(temp)) + 1):
        if temp % i == 0:
            prime_factors.add(i)
            while temp % i == 0:
                temp //= i
    if temp > 1:
        prime_factors.add(temp)
    prime_factors = sorted(prime_factors)

    def count_coprime_up_to(x):
        if x == 0:
            return 0
        res = x
        for p in prime_factors:
            res -= x // p
        return res

    total_pairs = 0
    for b in range(2, N + 1):
        a_max = b - 1
        if a_max < 1:
            continue
        product = b
        if gcd(product, P) != 1:
            continue
        cnt = count_coprime_up_to(a_max)
        total_pairs += cnt
    return total_pairs

def solve_optimized(N, P):
    if P == 1:
        return N * (N - 1) // 2

    prime_factors = set()
    temp = P
    for i in range(2, int(math.isqrt(temp)) + 1):
        if temp % i == 0:
            prime_factors.add(i)
            while temp % i == 0:
                temp //= i
    if temp > 1:
        prime_factors.add(temp)
    prime_factors = sorted(prime_factors)

    @lru_cache(maxsize=None)
    def count_coprime_up_to(x):
        if x == 0:
            return 0
        res = x
        for p in prime_factors:
            res -= x // p
        return res

    total = 0
    for b in range(2, N + 1):
        a_max = b - 1
        if a_max < 1:
            continue
        if gcd(b, P) == 1:
            cnt = count_coprime_up_to(a_max)
            total += cnt
    return total

def solve_final(N, P):
    if P == 1:
        return N * (N - 1) // 2

    def get_prime_factors(x):
        factors = set()
        if x == 1:
            return factors
        while x % 2 == 0:
            factors.add(2)
            x //= 2
        i = 3
        while i * i <= x:
            while x % i == 0:
                factors.add(i)
                x //= i
            i += 2
        if x > 1:
            factors.add(x)
        return factors

    prime_factors = get_prime_factors(P)
    if not prime_factors:
        return N * (N - 1) // 2

    def count_coprime_up_to(x):
        if x == 0:
            return 0
        res = x
        for p in prime_factors:
            res -= x // p
        return res

    total = 0
    for b in range(2, N + 1):
        a_max = b - 1
        if a_max < 1:
            continue
        if gcd(b, P) == 1:
            total += count_coprime_up_to(a_max)
    return total
```