```python
def solve(n, arr):
    sequences = []
    last = []
    for num in arr:
        placed = False
        for seq in sequences:
            if num > seq[-1]:
                seq.append(num)
                placed = True
                break
        if not placed:
            sequences.append([num])
    
    result = []
    for seq in sequences:
        result.append(" ".join(map(str, seq)))
    return "\n".join(result)

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    print(solve(n, arr))
```