```python
def solve(n, q, a, queries):
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + (1 if a[i - 1] <= i else 0)
    
    res = []
    for x, y in queries:
        left = x
        right = n - y - 1
        ans = prefix[right + 1] - prefix[left]
        res.append(ans)
    return res

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    q = int(data[1])
    a = list(map(int, data[2:2+n]))
    queries = []
    idx = 2 + n
    for _ in range(q):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        queries.append((x, y))
    
    results = solve(n, q, a, queries)
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
```