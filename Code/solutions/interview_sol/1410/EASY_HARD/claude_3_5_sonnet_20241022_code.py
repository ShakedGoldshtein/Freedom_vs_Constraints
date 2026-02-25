```python
def solve(S, N, M, K):
    if N < K + 1:  # impossible if selected students less than required friends + Alice
        return 0.0
    
    if N >= M:  # if all friends can be selected
        return 1.0
        
    # Calculate combination C(n,r)
    def comb(n, r):
        if r > n - r:
            r = n - r
        num = den = 1
        for i in range(r):
            num *= (n - i)
            den *= (i + 1)
        return num // den
    
    # Probability calculation
    # First assume Alice is already selected
    # Then calculate probability of selecting K or more friends from remaining M-1 friends
    # from remaining N-1 slots out of remaining S-1 total students
    total = 0
    M = M - 1  # excluding Alice
    S = S - 1  # excluding Alice
    N = N - 1  # one slot taken by Alice
    
    for i in range(K, min(M + 1, N + 1)):
        # selecting i friends from M friends * selecting (N-i) non-friends from (S-M) non-friends
        ways = comb(M, i) * comb(S - M, N - i)
        total += ways
    
    # Total possible ways of selecting N students from S students
    total_ways = comb(S, N)
    
    if total_ways == 0:
        return 0.0
        
    return total / total_ways
```