```python
def nCr(n, r):
    if r > n:
        return 0
    r = min(r, n - r)
    num = den = 1
    for i in range(r):
        num *= (n - i)
        den *= (i + 1)
    return num // den

def solve_one_case(S, N, M, K):
    # Edge cases
    if K >= N:
        return 0.0
    if N > S or M > S:
        return 0.0
        
    # If all students go, probability is 1 if K <= M-1
    if N == S:
        return 1.0 if K <= M-1 else 0.0
        
    # K is number of friends needed in addition to Alice
    # So effective K is K+1 including Alice
    K = K + 1
    
    # If total spots less than required friends
    if N < K:
        return 0.0
    
    # Calculate probability assuming Alice goes
    total = 0
    # Try different numbers of friends (from K to min(M,N))
    for friends in range(K, min(M+1, N+1)):
        # Ways to choose 'friends-1' friends from M-1 friends
        # And N-friends students from S-M others
        ways = nCr(M-1, friends-1) * nCr(S-M, N-friends)
        total += ways
    
    # Total ways to choose N-1 others from S-1 students
    denominator = nCr(S-1, N-1)
    
    if denominator == 0:
        return 0.0
        
    return total / denominator

def solve(T, cases):
    """
    Solves multiple test cases
    T: Number of test cases
    cases: List of (S,N,M,K) tuples for each case
    Returns: List of probabilities for each case
    """
    result = []
    for S,N,M,K in cases:
        prob = solve_one_case(S, N, M, K)
        result.append(prob)
    return result
```