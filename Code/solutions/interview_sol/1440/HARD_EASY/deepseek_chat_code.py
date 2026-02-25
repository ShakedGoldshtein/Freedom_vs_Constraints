```python
def solve_test_case(n, arr):
    if n == 1:
        return arr[0]
    
    arr.sort()
    
    if n == 2:
        return arr[0] % arr[1] if arr[0] < arr[1] else arr[1] % arr[0]
    
    max_val = arr[-1]
    second_max = arr[-2]
    
    if max_val == 1:
        return 0
    
    candidate1 = second_max % max_val
    
    for i in range(n - 3, -1, -1):
        if arr[i] > candidate1:
            candidate1 = arr[i] % max_val
            break
    
    return candidate1

def main():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        arr = list(map(int, input_data[idx:idx + n]))
        idx += n
        results.append(str(solve_test_case(n, arr)))
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
```