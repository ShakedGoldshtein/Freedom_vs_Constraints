```python
def solve(T, cases):
    results = []
    for i in range(T):
        n, m = cases[i][0]
        completed_jobs = cases[i][1]
        remaining_jobs = sorted(list(set(range(1, n+1)) - set(completed_jobs)))
        chef_jobs = ' '.join(map(str,remaining_jobs[::2]))
        assistant_jobs = ' '.join(map(str,remaining_jobs[1::2]))
        results.append((chef_jobs, assistant_jobs))
    return results
```