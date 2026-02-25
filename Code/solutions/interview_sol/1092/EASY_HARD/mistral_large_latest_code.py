```python
def solve(test_cases):
    results = []
    for case in test_cases:
        N, K, E, M = case['params']
        other_students = case['other_students']
        sergey_scores = case['sergey_scores']

        total_scores = []
        for student in other_students:
            total = sum(student)
            total_scores.append(total)

        min_sergey = 0
        left = 0
        right = M
        best = -1

        while left <= right:
            mid = (left + right) // 2
            sergey_total = sum(sergey_scores) + mid
            temp_scores = total_scores.copy()
            temp_scores.append(sergey_total)
            temp_scores.sort(reverse=True)

            if temp_scores[K-1] == sergey_total:
                count = temp_scores.count(sergey_total)
                if K - (temp_scores.index(sergey_total)) < count:
                    pass
                else:
                    left = mid + 1
                    continue

            if sergey_total > temp_scores[K-1]:
                best = mid
                right = mid - 1
            else:
                left = mid + 1

        if best != -1:
            results.append(best)
        else:
            results.append("Impossible")

    return results
```