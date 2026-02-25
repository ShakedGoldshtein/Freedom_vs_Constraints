```python
def can_convert(T, test_cases):
    results = []
    for case in test_cases:
        N, S, P = case

        count_s = S.count('1')
        count_p = P.count('1')

        if count_s < count_p:
            results.append("No")
            continue

        result = "Yes"
        for i in range(N - 1, -1, -1):
            if S[i] != P[i]:
                if P[i] == '1':
                    count_s -= 1
                else:
                    if S[:i + 1].count('1') <= count_p:
                        result = "No"
                        break
                    count_p -= 1
        results.append(result)
    return results
```
