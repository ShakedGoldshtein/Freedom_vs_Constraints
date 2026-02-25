```python
def solve_test_case(rows):
    total_chef = 0
    middle_values = []
    
    for row in rows:
        n = len(row)
        if n % 2 == 1:
            mid = n // 2
            middle_values.append(row[mid])
        
        chef_sum = 0
        ramsay_sum = 0
        
        for i in range(n):
            if i < (n + 1) // 2:
                chef_sum += row[i]
            if i >= n // 2:
                ramsay_sum += row[i]
        
        total_chef += chef_sum
    
    middle_values.sort(reverse=True)
    
    for i in range(len(middle_values)):
        if i % 2 == 0:
            total_chef += middle_values[i]
        else:
            total_chef -= middle_values[i]
    
    return total_chef

def main(T, test_cases):
    results = []
    for i in range(T):
        N = test_cases[i][0]
        rows = test_cases[i][1]
        results.append(solve_test_case(rows))
    return results
```