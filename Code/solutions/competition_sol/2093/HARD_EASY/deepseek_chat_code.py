```python
def solve(n, arr):
    sequences = []
    used = [False] * n
    while any(not u for u in used):
        current_seq = []
        prev = -float('inf')
        for i in range(n):
            if not used[i] and arr[i] > prev:
                used[i] = True
                current_seq.append(arr[i])
                prev = arr[i]
        sequences.append(current_seq)
    return sequences

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    result = solve(n, arr)
    for seq in result:
        print(' '.join(map(str, seq)))

if __name__ == '__main__':
    main()
```