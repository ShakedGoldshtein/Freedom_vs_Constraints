```python
def sieve_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i*i:limit+1:i] = [False] * ((limit - i*i) // i + 1)
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

def is_prime(x, primes):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    limit = int(x**0.5) + 1
    for p in primes:
        if p > limit:
            break
        if x % p == 0:
            return False
    return True

def find_primes_around(n, primes):
    if n <= 2:
        return (2, 3)
    
    if n in primes_set:
        v = n
        u_candidate = n + 1
        while True:
            if is_prime(u_candidate, primes):
                u = u_candidate
                break
            u_candidate += 1
    else:
        idx = bisect.bisect_right(primes, n) - 1
        v = primes[idx]
        u_candidate = n + 1
        while True:
            if is_prime(u_candidate, primes):
                u = u_candidate
                break
            u_candidate += 1
    return (v, u)

def compute_sum(n, primes):
    if n == 2:
        return (1, 6)
    
    total_num = 0
    total_den = 1
    
    i = 2
    while i <= n:
        v_i, u_i = find_primes_around(i, primes)
        j = min(n, u_i - 1)
        
        term_num = j - i + 1
        term_den = v_i * u_i
        
        g1 = math.gcd(term_num, term_den)
        term_num //= g1
        term_den //= g1
        
        if total_num == 0:
            total_num = term_num
            total_den = term_den
        else:
            lcm_den = total_den * term_den // math.gcd(total_den, term_den)
            total_num = total_num * (lcm_den // total_den) + term_num * (lcm_den // term_den)
            total_den = lcm_den
            g = math.gcd(total_num, total_den)
            total_num //= g
            total_den //= g
        
        i = j + 1
    
    return (total_num, total_den)

def solve(t, test_cases):
    max_n = max(test_cases)
    sieve_limit = min(int(max_n**0.5) + 1000, 10**6)
    primes = sieve_eratosthenes(sieve_limit)
    global primes_set
    primes_set = set(primes)
    
    results = []
    for n in test_cases:
        num, den = compute_sum(n, primes)
        results.append(f"{num}/{den}")
    
    return results

import math
import bisect

primes_set = set()
```