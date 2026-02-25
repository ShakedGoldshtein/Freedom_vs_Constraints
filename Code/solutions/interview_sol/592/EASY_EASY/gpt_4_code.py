```python
def find_winner(T, test_cases):
    result = []
    for t in range(T):
        S, N, words = test_cases[t]
        is_containing_substring = any(word in S for word in words)
        if is_containing_substring:
            result.append("Teddy" if (S.count(word) % 2 == 1) else "Tracy")
        else:
            result.append("Tracy")
    return result
```