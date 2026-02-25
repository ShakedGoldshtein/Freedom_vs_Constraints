```python
def solve(T, test_cases):
    results = []
    for case in test_cases:
        n, m = case[0]
        completed = set(case[1])
        unfinished = []
        for job in range(1, n + 1):
            if job not in completed:
                unfinished.append(job)
        unfinished.sort()
        chef = []
        assistant = []
        for idx, job in enumerate(unfinished):
            if idx % 2 == 0:
                chef.append(str(job))
            else:
                assistant.append(str(job))
        results.append((" ".join(chef), " ".join(assistant)))
    return results
```