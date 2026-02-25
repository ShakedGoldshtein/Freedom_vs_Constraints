```python
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
        arr.sort()
        total = 0
        for i in range(n//2):
            total += abs(arr[i] - arr[n-1-i])
        results.append(str(total))
    return "\n".join(results)
```