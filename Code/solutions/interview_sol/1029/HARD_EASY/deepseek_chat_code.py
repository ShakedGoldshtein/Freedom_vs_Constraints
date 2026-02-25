```python
def solve_test_case(n, m, completed_jobs):
    completed_set = set(completed_jobs)
    remaining_jobs = []
    
    for job in range(1, n + 1):
        if job not in completed_set:
            remaining_jobs.append(job)
    
    remaining_jobs.sort()
    
    chef_jobs = []
    assistant_jobs = []
    
    for idx, job in enumerate(remaining_jobs):
        if idx % 2 == 0:
            chef_jobs.append(job)
        else:
            assistant_jobs.append(job)
    
    return chef_jobs, assistant_jobs

def main(T, test_cases):
    results = []
    for i in range(T):
        n, m = test_cases[i][0]
        completed_jobs = test_cases[i][1]
        chef_jobs, assistant_jobs = solve_test_case(n, m, completed_jobs)
        results.append((chef_jobs, assistant_jobs))
    return results
```