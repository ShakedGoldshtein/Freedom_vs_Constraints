```python
def solve(T, cases):
    results = []
    for N, P in cases:
        results.append(count_good_pairs(N, P))
    return results

def count_good_pairs(N, P):
    if P == 1:
        return N * (N - 1) // 2
    
    prime_factors = get_prime_factors(P)
    
    mobius = compute_mobius(N, prime_factors)
    
    total_pairs = 0
    for d in range(1, N + 1):
        if mobius[d] == 0:
            continue
        count = 0
        for k in range(d, N + 1, d):
            count += 1
        pairs_with_d = count * (count - 1) // 2
        total_pairs += mobius[d] * pairs_with_d
    
    return total_pairs

def get_prime_factors(n):
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors

def compute_mobius(N, prime_factors):
    mobius = [1] * (N + 1)
    mobius[0] = 0
    
    for p in prime_factors:
        if p > N:
            continue
        for j in range(p, N + 1, p):
            mobius[j] = 0
    
    for p in prime_factors:
        if p > N:
            continue
        p2 = p * p
        for j in range(p2, N + 1, p2):
            mobius[j] = 0
    
    for p in prime_factors:
        if p > N:
            continue
        for j in range(p, N + 1, p):
            mobius[j] *= -1
    
    return mobius
```