```python
def get_winner(T, test_cases):
    result = []
    for _ in range(T):
        N, M = test_cases[_]
        if N == 1 or M == 1:
            result.append('Tuzik')
        elif N == 2 or M == 2:
            result.append('Vanya')
        else:
            result.append('Tuzik')

    return result

def solve():
    T = 2
    test_cases = [(4,4), (2,2)]
    result = get_winner(T, test_cases)

    for winner in result:
        print(winner)
        
solve()
```