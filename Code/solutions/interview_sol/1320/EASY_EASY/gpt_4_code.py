```python
def find_game_winner(T, arr):
    result = []
    for i in range(T):
        N = arr[i]
        if N % 2 == 0:
            result.append("A")
        else:
            result.append("B")
    return result
```