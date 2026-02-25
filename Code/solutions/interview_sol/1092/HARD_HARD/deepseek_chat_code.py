```python
def solve_test_case(N, K, E, M, others_scores, sergey_scores):
    total_others = []
    for scores in others_scores:
        total = sum(scores[:E-1]) + scores[E-1]
        total_others.append(total)
    
    sergey_current = sum(sergey_scores)
    
    total_others.sort(reverse=True)
    
    if K == N:
        required_total = 0
    else:
        required_total = total_others[K-1] + 1
    
    needed_score = required_total - sergey_current
    
    if needed_score > M:
        return "Impossible"
    if needed_score < 0:
        return 0
    return needed_score

def main(T, test_cases):
    results = []
    for i in range(T):
        N, K, E, M = test_cases[i][0]
        others_scores = test_cases[i][1]
        sergey_scores = test_cases[i][2]
        result = solve_test_case(N, K, E, M, others_scores, sergey_scores)
        results.append(result)
    return results
```