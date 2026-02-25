```python
def solve():
    t = int(input().strip())
    results = []
    for _ in range(t):
        x = int(input().strip())
        count = 0
        n = 1
        while True:
            needed = (n * (n + 1)) // 2
            if x >= needed:
                count += 1
                x -= needed
            else:
                break
            n = 2 * n + 1
        results.append(count)
    return results

if __name__ == "__main__":
    for res in solve():
        print(res)
```