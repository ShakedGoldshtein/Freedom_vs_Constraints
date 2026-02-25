```python
def solve(n, arr):
    used = [False] * n
    result = []
    while True:
        current_sequence = []
        prev = -float('inf')
        for i in range(n):
            if not used[i] and arr[i] > prev:
                current_sequence.append(arr[i])
                used[i] = True
                prev = arr[i]
        if not current_sequence:
            break
        result.append(' '.join(map(str, current_sequence)))
    return '\n'.join(result)
```