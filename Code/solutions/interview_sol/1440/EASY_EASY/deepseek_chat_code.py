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
        if n == 2:
            a, b = arr
            results.append(str(max(a % b, b % a)))
        else:
            results.append(str(max(arr)))
    return "\n".join(results)

if __name__ == "__main__":
    print(solve())
```