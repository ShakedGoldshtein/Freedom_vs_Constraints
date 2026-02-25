```python
def assign_jobs(n, m, finished_jobs):
    """
    Assigns remaining jobs to Chef and assistant based on the given rules.

    Args:
        n: Total number of jobs (1 to n).
        m: Number of finished jobs.
        finished_jobs: List of already completed job indices (unsorted, 1-based).

    Returns:
        tuple: (chef_jobs, assistant_jobs) where each is a list of job indices in increasing order.
    """
    finished = set(finished_jobs)
    remaining = [job for job in range(1, n + 1) if job not in finished]
    chef_jobs = []
    assistant_jobs = []

    for i, job in enumerate(remaining):
        if i % 2 == 0:
            chef_jobs.append(job)
        else:
            assistant_jobs.append(job)

    return (chef_jobs, assistant_jobs)

def solve(test_cases):
    """
    Processes multiple test cases for job assignment.

    Args:
        test_cases: List of tuples where each tuple is (n, m, finished_jobs).

    Returns:
        list: List of tuples where each tuple is (chef_jobs, assistant_jobs) for a test case.
    """
    results = []
    for n, m, finished_jobs in test_cases:
        chef, assistant = assign_jobs(n, m, finished_jobs)
        results.append((chef, assistant))
    return results
```