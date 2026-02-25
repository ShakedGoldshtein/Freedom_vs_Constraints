```python
def solve(test_cases):
    result = []
    
    for _ in range(test_cases):
        n, m = map(int, input().split())
        if m > 0:
            finished = list(map(int, input().split()))
        else:
            finished = []
            
        # Create list of unfinished jobs
        unfinished = []
        for i in range(1, n+1):
            if i not in finished:
                unfinished.append(i)
                
        chef = []
        assistant = []
        
        # Assign jobs alternately
        for i in range(len(unfinished)):
            if i % 2 == 0:
                chef.append(unfinished[i])
            else:
                assistant.append(unfinished[i])
                
        # Format output for each test case
        chef_str = ' '.join(map(str, chef)) if chef else ''
        assist_str = ' '.join(map(str, assistant)) if assistant else ''
        
        result.extend([chef_str, assist_str])
        
    return result

def solve_alt(T, cases):
    """
    Alternative implementation taking direct input parameters instead of using I/O
    
    Args:
        T: Number of test cases
        cases: List of tuples, each containing (n, m, finished_jobs)
            where n is total jobs, m is completed jobs, 
            finished_jobs is list of completed job indices
            
    Returns:
        List of strings representing chef and assistant assignments
    """
    result = []
    
    for n, m, finished in cases:
        # Create list of unfinished jobs
        unfinished = []
        for i in range(1, n+1):
            if i not in finished:
                unfinished.append(i)
                
        chef = []
        assistant = []
        
        # Assign jobs alternately
        for i in range(len(unfinished)):
            if i % 2 == 0:
                chef.append(unfinished[i])
            else:
                assistant.append(unfinished[i])
                
        # Format output for each test case
        chef_str = ' '.join(map(str, chef)) if chef else ''
        assist_str = ' '.join(map(str, assistant)) if assistant else ''
        
        result.extend([chef_str, assist_str])
        
    return result
```