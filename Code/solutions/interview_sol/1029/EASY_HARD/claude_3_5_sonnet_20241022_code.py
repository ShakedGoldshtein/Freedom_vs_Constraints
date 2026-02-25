```python
def solve(n, m, completed):
    # Create set of completed jobs
    completed = set(completed)
    
    # Get list of remaining jobs
    remaining = [x for x in range(1, n+1) if x not in completed]
    
    chef = []
    assistant = []
    
    # Assign remaining jobs alternately
    for i in range(len(remaining)):
        if i % 2 == 0:
            chef.append(remaining[i])
        else:
            assistant.append(remaining[i])
    
    return chef, assistant
```