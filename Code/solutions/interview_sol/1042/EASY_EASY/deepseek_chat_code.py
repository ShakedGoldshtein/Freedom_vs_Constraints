```python
import math

def solve(N, P):
    primes = []
    temp = P
    for i in range(2, int(math.isqrt(P)) + 1):
        if temp % i == 0:
            primes.append(i)
            while temp % i == 0:
                temp //= i
    if temp > 1:
        primes.append(temp)
    
    def count_coprime(x):
        total = 0
        k = len(primes)
        for mask in range(1, 1 << k):
            prod = 1
            bits = 0
            for j in range(k):
                if mask & (1 << j):
                    prod *= primes[j]
                    bits += 1
            cnt = x // prod
            if bits % 2 == 1:
                total += cnt
            else:
                total -= cnt
        return x - total
    
    res = 0
    for a in range(1, N + 1):
        if math.gcd(a, P) != 1:
            continue
        max_b = N // a
        res += count_coprime(max_b)
    
    return res

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    idx = 1
    results = []
    for _ in range(t):
        N = int(input_data[idx])
        P = int(input_data[idx + 1])
        idx += 2
        results.append(str(solve(N, P)))
    print("\n".join(results))

if __name__ == "__main__":
    main()
```