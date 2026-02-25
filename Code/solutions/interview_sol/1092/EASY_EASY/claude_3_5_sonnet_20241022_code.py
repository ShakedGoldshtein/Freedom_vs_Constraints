```python
def solve(T, test_cases):
    results = []
    
    for _ in range(T):
        N, K, E, M = test_cases[0]
        curr_pos = 1
        
        other_scores = test_cases[1:N]
        sergey_scores = test_cases[N]
        
        test_cases = test_cases[N+1:]
        
        total_scores = []
        sergey_total = sum(sergey_scores)
        
        for scores in other_scores:
            total_scores.append(sum(scores))
            
        total_scores.sort(reverse=True)
        
        min_rank = N - K + 1
        if min_rank == 1:
            min_score_needed = total_scores[0] - sergey_total + 1
        else:
            min_score_needed = total_scores[min_rank-2] - sergey_total + 1
            
        if min_score_needed > M:
            results.append("Impossible")
        elif min_score_needed < 0:
            results.append(0) 
        else:
            results.append(min_score_needed)
            
    return results
```