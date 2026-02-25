```python
def solve_test_case(n):
    segment_costs = {
        '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
        '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
    }
    
    min_cost_digit = '1'
    min_cost = segment_costs[min_cost_digit]
    
    if n % 2 == 1:
        result = '7'
        remaining_segments = n - segment_costs['7']
    else:
        result = ''
        remaining_segments = n
    
    num_digits = remaining_segments // min_cost
    result += min_cost_digit * num_digits
    
    return result

def main():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(input_data[i])
        results.append(solve_test_case(n))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
```