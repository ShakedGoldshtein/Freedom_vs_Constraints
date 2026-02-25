```python
def sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i*i:limit+1:i] = [False] * len(sieve[i*i:limit+1:i])
    return [i for i in range(2, limit + 1) if sieve[i]]

def solve_test(n):
    if n < 2:
        return "0/1"
    
    primes = sieve(int(n**0.5) + 1500)
    
    def is_prime(x):
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
    
    def v(x):
        if x == 2:
            return 2
        if x % 2 == 0:
            x -= 1
        while x >= 2:
            if is_prime(x):
                return x
            x -= 2
        return 2
    
    def u(x):
        if x < 2:
            return 2
        x += 1
        if x % 2 == 0 and x != 2:
            x += 1
        while True:
            if is_prime(x):
                return x
            x += 2
    
    if n == 2:
        return "1/6"
    
    total_num = 0
    total_den = 1
    
    primes_list = []
    current = 2
    while current <= n:
        primes_list.append(current)
        next_prime = u(current)
        if next_prime > n:
            break
        current = next_prime
    
    for i in range(len(primes_list) - 1):
        p1 = primes_list[i]
        p2 = primes_list[i + 1]
        count = p2 - p1
        term_num = count
        term_den = p1 * p2
        
        total_num = total_num * term_den + term_num * total_den
        total_den *= term_den
        
        g = gcd(total_num, total_den)
        total_num //= g
        total_den //= g
    
    return f"{total_num}/{total_den}"

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    results = []
    for i in range(1, t + 1):
        n = int(input_data[i])
        results.append(solve_test(n))
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```