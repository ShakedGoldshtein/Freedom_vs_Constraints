```python
from functools import lru_cache

def determine_winner(test_cases):
    results = []
    for case in test_cases:
        S, dictionary = case
        winner = _determine_winner(S, set(dictionary))
        results.append("Teddy" if winner else "Tracy")
    return results

def _determine_winner(S, dictionary):
    n = len(S)
    memo = {}

    def can_win(l, r):
        if (l, r) in memo:
            return memo[(l, r)]
        if l >= r:
            return False

        current_str = S[l:r]
        for word in dictionary:
            word_len = len(word)
            if word_len > (r - l):
                continue
            for i in range(l, r - word_len + 1):
                if S[i:i+word_len] == word:
                    left_possible = can_win(l, i)
                    right_possible = can_win(i + word_len, r)
                    if not left_possible or not right_possible:
                        memo[(l, r)] = True
                        return True
        memo[(l, r)] = False
        return False

    return can_win(0, n)
```