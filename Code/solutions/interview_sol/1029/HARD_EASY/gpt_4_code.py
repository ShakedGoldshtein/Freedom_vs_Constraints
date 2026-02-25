```python
def job_assignments(T, test_cases):
    output = []
    for i in range(T):
        n, m, completed = test_cases[i]
        all_jobs = set(range(1, n+1))
        remaining_jobs = sorted(list(all_jobs - set(completed)))
        chef_jobs = remaining_jobs[::2]
        assistant_jobs = remaining_jobs[1::2]
        output.append((chef_jobs, assistant_jobs))
    return output

# Example usage:
T = 3
test_cases = [
    (6, 3, [2, 4, 1]),
    (3, 2, [3, 2]),
    (8, 2, [3, 8]),
]
print(job_assignments(T, test_cases))
```