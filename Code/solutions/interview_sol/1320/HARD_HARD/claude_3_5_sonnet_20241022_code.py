```python
def solve_game(n):
    """
    Solve single test case for marble game.
    Returns 'A' if player A loses, 'B' if player B loses.
    """
    # For n=1, A takes 1 marble and B has no valid move
    if n == 1:
        return 'B'
    
    # For n=2, A takes 2 marbles and B has no valid move
    if n == 2:
        return 'B'
        
    # For n=3, A must take 1 or 2 marbles
    # If A takes 1, B has 2 marbles left and wins
    # If A takes 2, B has 1 marble left and wins
    if n == 3:
        return 'A'
    
    # For n>=4, we can find pattern:
    # - If n is even, A can take all marbles in one move
    # - If n is odd, A must leave odd number for B:
    #   - If A takes 1, B gets even n-1
    #   - If A takes even k, B gets odd n-k
    # So A wins for all n except n=3
    return 'B' if n != 3 else 'A'

def solve(t, test_cases):
    """
    Solve multiple test cases for marble game.
    Returns list of results ('A' or 'B') for each test case.
    """
    results = []
    for n in test_cases:
        results.append(solve_game(n))
    return results
```