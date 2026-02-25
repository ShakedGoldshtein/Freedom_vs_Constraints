```python
from math import comb

def hypergeometric_probability(total, draws, successes, required_successes):
    if required_successes > draws or required_successes > successes:
        return 0.0
    if required_successes < 0:
        return 0.0
    
    numerator = comb(successes, required_successes) * comb(total - successes, draws - required_successes)
    denominator = comb(total, draws)
    
    return numerator / denominator

def calculate_probability(S, N, M, K):
    if S < 1 or N < 1 or M < 1 or K < 0 or K >= M:
        return 0.0
    
    if N > S or M > S:
        return 0.0
    
    total_students = S - 1
    total_draws = N - 1
    total_friends = M - 1
    
    if total_draws > total_students:
        return 0.0
    
    probability = 0.0
    for i in range(K, min(total_friends, total_draws) + 1):
        if i <= total_friends and (total_draws - i) <= (total_students - total_friends):
            probability += hypergeometric_probability(total_students, total_draws, total_friends, i)
    
    return probability

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    
    for _ in range(t):
        S = int(input_data[index])
        N = int(input_data[index + 1])
        M = int(input_data[index + 2])
        K = int(input_data[index + 3])
        index += 4
        
        prob = calculate_probability(S, N, M, K)
        results.append(f"{prob:.6f}")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
```