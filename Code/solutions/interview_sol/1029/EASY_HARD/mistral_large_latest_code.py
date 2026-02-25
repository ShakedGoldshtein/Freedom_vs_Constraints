```python
def solve(test_cases):
    results = []
    for case in test_cases:
        n, m, finished = case
        finished_set = set(finished)
        remaining = [i for i in range(1, n + 1) if i not in finished_set]
        chef = []
        assistant = []
        for i, job in enumerate(remaining, 1):
            if i % 2 == 1:
                chef.append(str(job))
            else:
                assistant.append(str(job))
        results.append((' '.join(chef), ' '.join(assistant)))
    return results
```