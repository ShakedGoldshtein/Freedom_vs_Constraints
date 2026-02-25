```python
def find_increasing_sequences(n, arr):
    if n == 0:
        return []

    used = [False] * n
    sequences = []

    while True:
        current_sequence = []
        prev = None

        for i in range(n):
            if not used[i]:
                if prev is None or arr[i] > prev:
                    used[i] = True
                    current_sequence.append(arr[i])
                    prev = arr[i]

        if not current_sequence:
            break
        sequences.append(current_sequence)

    return [' '.join(map(str, seq)) for seq in sequences]
```