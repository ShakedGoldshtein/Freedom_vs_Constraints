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
        
        if n == 1:
            results.append(str(arr[0]))
            continue
            
        prefix = [0] * (n + 2)
        suffix = [0] * (n + 2)
        
        for i in range(1, n + 1):
            prefix[i] = math.gcd(prefix[i-1], arr[i-1])
        
        for i in range(n, 0, -1):
            suffix[i] = math.gcd(suffix[i+1], arr[i-1])
        
        ans = 0
        for i in range(1, n + 1):
            current = math.gcd(prefix[i-1], suffix[i+1])
            if current > ans:
                ans = current
        
        reversed_gcd = arr[0]
        for i in range(1, n):
            reversed_gcd = math.gcd(reversed_gcd, arr[i])
            if reversed_gcd > ans:
                ans = reversed_gcd
        
        reversed_gcd = arr[-1]
        for i in range(n-2, -1, -1):
            reversed_gcd = math.gcd(reversed_gcd, arr[i])
            if reversed_gcd > ans:
                ans = reversed_gcd
        
        results.append(str(ans))
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
```