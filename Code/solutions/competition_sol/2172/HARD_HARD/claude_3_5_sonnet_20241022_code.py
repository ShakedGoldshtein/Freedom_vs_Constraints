```python
def get_primes_up_to(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    return [i for i in range(len(is_prime)) if is_prime[i]]

def get_v_u(n, primes):
    v = 0
    u = 0
    
    for p in primes:
        if p <= n:
            v = p
        else:
            u = p
            break
            
    return v, u

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(n):
    primes = get_primes_up_to(n + 1000)  # Buffer for finding next prime
    
    num = 0
    den = 1
    
    for i in range(2, n + 1):
        v, u = get_v_u(i, primes)
        
        # Add fraction 1/(v*u)
        new_num = den
        new_den = v * u
        
        # Add to running sum using fraction arithmetic
        num = num * new_den + new_num * den
        den = den * new_den
        
        # Reduce fraction
        g = gcd(abs(num), den)
        num //= g
        den //= g
        
    return f"{num}/{den}"

def solve_multiple(test_cases):
    results = []
    for n in test_cases:
        results.append(solve(n))
    return results
```