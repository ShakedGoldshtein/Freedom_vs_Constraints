```python
import bisect

def solve(T, test_cases):
    results = []
    for case in test_cases:
        N, Q, a, queries = case
        res = []
        for query in queries:
            if query[0] == 0:
                _, A, B = query
                a[A] = B
            else:
                _, A = query
                current = a[A]
                found = -1
                for i in range(A + 1, N):
                    if a[i] > current:
                        valid = True
                        for j in range(A + 1, i):
                            if a[j] == a[i]:
                                valid = False
                                break
                        if valid:
                            found = a[i]
                            break
                res.append(found)
        results.append(res)
    return results

def solve_optimized(T, test_cases):
    results = []
    for case in test_cases:
        N, Q, a, queries = case
        res = []
        for query in queries:
            if query[0] == 0:
                _, A, B = query
                a[A] = B
            else:
                _, A = query
                current = a[A]
                found = -1
                seen = set()
                for i in range(A + 1, N):
                    if a[i] > current and a[i] not in seen:
                        found = a[i]
                        break
                    seen.add(a[i])
                res.append(found)
        results.append(res)
    return results

def solve_efficient(T, test_cases):
    results = []
    for case in test_cases:
        N, Q, a, queries = case
        res = []
        for query in queries:
            if query[0] == 0:
                _, A, B = query
                a[A] = B
            else:
                _, A = query
                current = a[A]
                found = -1
                seen = {}
                for i in range(A + 1, N):
                    if a[i] > current:
                        if a[i] not in seen:
                            found = a[i]
                            break
                        elif seen[a[i]] < A:
                            found = a[i]
                            break
                    seen[a[i]] = i
                res.append(found)
        results.append(res)
    return results

def solve_final(T, test_cases):
    results = []
    for case in test_cases:
        N, Q, a, queries = case
        res = []
        for query in queries:
            if query[0] == 0:
                _, A, B = query
                a[A] = B
            else:
                _, A = query
                current = a[A]
                found = -1
                last_occurrence = {}
                for i in range(A + 1, N):
                    if a[i] > current:
                        if a[i] not in last_occurrence or last_occurrence[a[i]] <= A:
                            found = a[i]
                            break
                    last_occurrence[a[i]] = i
                res.append(found)
        results.append(res)
    return results
```