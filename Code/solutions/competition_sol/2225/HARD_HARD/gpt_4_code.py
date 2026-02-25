```python
def determine_winner(N, L, good_set):
    max_len = max(map(len, good_set))
    lengths = [0] * (max_len + 1)
    for s in good_set:
        lengths[len(s)] += 1
    lengths.reverse()
    ans = 0
    for i in range(1, len(lengths)):
        if lengths[i] % 2 == 1:
            lengths[i - 1] += len(lengths) // 2
            ans ^= i
    return "Alice" if ans > 0 else "Bob"
```