```python
def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i in range(n+1) if primes[i]]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_prime_factors(n):
    if n <= 10**6:
        primes = sieve(n+100)
        v_prime = primes[-1]
        for p in primes:
            if p > n:
                u_prime = p
                break
        return v_prime, u_prime
    
    # For large n, use trial division
    v_prime = n
    while not is_prime(v_prime):
        v_prime -= 1
    u_prime = n + 1
    while not is_prime(u_prime):
        u_prime += 1
    return v_prime, u_prime

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve(test_cases):
    result = []
    for n in test_cases:
        num = 0
        den = 1
        for i in range(2, n+1):
            v, u = get_prime_factors(i)
            cur_num = 1
            cur_den = v * u
            # num/den + 1/(v*u) = (num*v*u + den)/(den*v*u)
            num = num * cur_den + den * cur_num
            den = den * cur_den
            g = gcd(abs(num), abs(den))
            num //= g
            den //= g
        result.append(f"{num}/{den}")
    return result
```