```python
MOD = 1000000007

def nCr(n, r, fact, inv_fact):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    
    max_n = 0
    test_cases = []
    for _ in range(t):
        N = int(data[idx]); idx += 1
        K = int(data[idx]); idx += 1
        M = int(data[idx]); idx += 1
        A = list(map(int, data[idx:idx+N])); idx += N
        test_cases.append((N, K, M, A))
        max_n = max(max_n, N)
    
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
    for i in range(max_n-1, -1, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
    
    for N, K, M, A in test_cases:
        buckets = [[] for _ in range(M)]
        for num in A:
            buckets[num % M].append(num)
        
        dp = [0] * (K + 1)
        dp[0] = 1
        
        for i in range(M):
            rem = (i + 1) % M
            count = len(buckets[rem])
            if count == 0:
                continue
            
            for j in range(min(K, count), 0, -1):
                combinations = nCr(count, j, fact, inv_fact)
                for k in range(K, j-1, -1):
                    dp[k] = (dp[k] + dp[k - j] * combinations) % MOD
        
        results.append(str(dp[K] % MOD))
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
```