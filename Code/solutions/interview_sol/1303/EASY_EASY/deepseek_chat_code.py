```python
MOD = 1000000007

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        N = int(data[idx]); idx += 1
        K = int(data[idx]); idx += 1
        M = int(data[idx]); idx += 1
        A = list(map(int, data[idx:idx+N])); idx += N
        
        req = [i % M for i in range(1, K+1)]
        freq = [0] * M
        for num in A:
            freq[num % M] += 1
        
        dp = [0] * (K + 1)
        dp[0] = 1
        for r in req:
            new_dp = [0] * (K + 1)
            for j in range(K + 1):
                if dp[j] == 0:
                    continue
                new_dp[j] = (new_dp[j] + dp[j]) % MOD
                if j + 1 <= K:
                    new_dp[j+1] = (new_dp[j+1] + dp[j] * freq[r]) % MOD
            dp = new_dp
        results.append(str(dp[K] % MOD))
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
```