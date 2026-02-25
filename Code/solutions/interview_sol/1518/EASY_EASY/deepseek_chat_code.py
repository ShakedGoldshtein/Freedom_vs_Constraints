```python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    max_n = 100000
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, max_n + 1) if is_prime[i]]
    results = []
    index = 0
    for _ in range(t):
        N = int(data[index + 1])
        K = int(data[index + 2])
        index += 2
        if K == 1:
            results.append('1' if is_prime[N] else '0')
        elif K == 2:
            if N % 2 == 0:
                results.append('1' if N >= 4 else '0')
            else:
                results.append('1' if is_prime[N - 2] and N - 2 >= 2 else '0')
        else:
            if N >= 2 * K:
                results.append('1')
            else:
                results.append('0')
    print("\n".join(results))

if __name__ == "__main__":
    solve()
```