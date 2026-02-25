```python
import math

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx+n]))
        idx += n
        
        max_val = max(arr)
        gcd_val = arr[0]
        for num in arr[1:]:
            gcd_val = math.gcd(gcd_val, num)
        
        total_cost = 0
        for length in arr:
            total_cost += length // gcd_val
        
        results.append(f"{gcd_val} {total_cost}")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
```