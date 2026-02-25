```python
def solve(t, inputs):
    results = []
    
    for _ in range(t):
        # Parse input for this test case
        a1, a2, a3, a4, a5, p = inputs[_]
        
        # Calculate total hours needed when working from home
        total_hours = 0
        for hours in [a1, a2, a3, a4, a5]:
            total_hours += hours * p
            
        # Check if work can be completed in 5 weekdays
        # 5 days * 24 hours = 120 total available hours
        if total_hours <= 120:
            results.append("No") 
        else:
            results.append("Yes")
            
    return results

def parse_input(raw_input):
    lines = raw_input.strip().split('\n')
    t = int(lines[0])
    inputs = []
    for i in range(t):
        nums = list(map(int, lines[i+1].split()))
        inputs.append(nums)
    return t, inputs
```