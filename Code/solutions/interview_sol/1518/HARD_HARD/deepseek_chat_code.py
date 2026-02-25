```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return is_prime, primes

def can_be_sum_of_k_primes(N, K, is_prime, primes_set):
    if K == 1:
        return is_prime[N]
    if K == 2:
        if N % 2 == 0:
            return N >= 4
        else:
            return N >= 5 and is_prime[N - 2]
    if K == 3:
        if N < 6:
            return False
        if N % 2 == 0:
            return True
        else:
            return is_prime[N - 2] or N >= 9
    return N >= 2 * K

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    max_n = 10**5
    is_prime, primes = sieve(max_n)
    primes_set = set(primes)
    
    results = []
    index = 1
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        if N < 2 * K:
            results.append(0)
        else:
            results.append(1 if can_be_sum_of_k_primes(N, K, is_prime, primes_set) else 0)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    solve()
```