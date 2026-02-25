```python
def solve_game_winner(S, dictionary):
    from functools import lru_cache

    words = set(dictionary)
    n = len(S)

    @lru_cache(maxsize=None)
    def can_win(l, r):
        if l >= r:
            return False
        for i in range(l, r):
            for j in range(i + 1, r + 1):
                substring = S[i:j]
                if substring in words:
                    if not can_win(l, i) or not can_win(j, r):
                        return True
        return False

    return "Teddy" if can_win(0, n) else "Tracy"

def solve(test_cases):
    results = []
    for case in test_cases:
        S, dictionary = case
        results.append(solve_game_winner(S, dictionary))
    return results
```