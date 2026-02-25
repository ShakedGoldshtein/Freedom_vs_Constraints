```python
def game_winner(T, test_cases):
    results = []
    for i in range(T):
        N, M = test_cases[i]
        if N == 1 or M == 1 or (N == 2 and M == 2):
            results.append('Vanya')
        else:
            results.append('Tuzik')
    return results
```