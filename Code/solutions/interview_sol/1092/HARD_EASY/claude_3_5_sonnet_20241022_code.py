```python
def solve_testcase(N, K, E, M, others_scores, sergey_scores):
    # Calculate total scores for all other students
    total_scores = []
    for scores in others_scores:
        total_scores.append(sum(scores))
    
    # Sort scores in ascending order
    total_scores.sort()
    
    # Calculate Sergey's current score from first E-1 exams
    sergey_current = sum(sergey_scores)
    
    # Calculate minimum score needed to be better than N-K students
    if N-K >= len(total_scores):
        # Need to be better than everyone
        min_score_needed = max(total_scores) - sergey_current + 1
    else:
        # Need to be better than N-K students
        min_score_needed = total_scores[N-K-1] - sergey_current + 1
    
    # Check if score is achievable within M points
    if min_score_needed > M:
        return "Impossible"
    
    # Check if already qualified
    if min_score_needed <= 0:
        return 0
        
    return min_score_needed

def solve(T, cases):
    results = []
    case_idx = 0
    
    for _ in range(T):
        # Parse each test case
        N, K, E, M = cases[case_idx]
        case_idx += 1
        
        others_scores = []
        for _ in range(N-1):
            scores = cases[case_idx]
            others_scores.append(scores)
            case_idx += 1
            
        sergey_scores = cases[case_idx]
        case_idx += 1
        
        # Solve test case
        result = solve_testcase(N, K, E, M, others_scores, sergey_scores)
        results.append(result)
        
    return results
```