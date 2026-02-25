```python
def solve(test_cases):
    results = []
    for case in test_cases:
        N, K, E, M = case['params']
        other_students = case['other_students']
        sergey_scores = case['sergey_scores']

        # Calculate total scores for other students
        other_totals = []
        for student in other_students:
            total = sum(student[:E-1]) + student[E-1]
            other_totals.append(total)

        # Calculate Sergey's current total without last exam
        sergey_current = sum(sergey_scores)

        # Determine the K-th smallest score (since top K are those > (N-K)th)
        # We need Sergey's total to be > (N-K)th smallest score
        # So we need to find the (N-K)th smallest score in other_totals
        # Then Sergey's total must be > that score
        # But if there are ties, we need to ensure Sergey is in top K

        # Sort other_totals to find the threshold
        other_totals_sorted = sorted(other_totals)
        threshold_index = N - K - 1
        if threshold_index < 0:
            # All students are enrolled, so Sergey is in
            min_score = 0
        else:
            threshold = other_totals_sorted[threshold_index] if threshold_index < len(other_totals) else -1
            # Sergey's total must be > threshold
            # So sergey_current + x > threshold => x > threshold - sergey_current
            min_x = max(0, threshold - sergey_current + 1)
            if min_x > M:
                results.append("Impossible")
                continue
            min_score = min_x

        results.append(min_score)

    return results

def parse_input(test_cases_data):
    T = test_cases_data[0][0]
    index = 1
    test_cases = []
    for _ in range(T):
        N, K, E, M = test_cases_data[index]
        index += 1
        other_students = []
        for _ in range(N-1):
            scores = test_cases_data[index]
            other_students.append(scores)
            index += 1
        sergey_scores = test_cases_data[index]
        index += 1
        test_cases.append({
            'params': (N, K, E, M),
            'other_students': other_students,
            'sergey_scores': sergey_scores
        })
    return test_cases

def famcs_enrollment(test_cases_data):
    test_cases = parse_input(test_cases_data)
    return solve(test_cases)
```