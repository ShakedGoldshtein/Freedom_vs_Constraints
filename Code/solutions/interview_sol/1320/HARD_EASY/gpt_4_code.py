```python
def game_winner(T, N):
    
    names = {0: 'A', 1: 'B'}
    winners = []
    
    for t in range(T):
        n = N[t]
        if n % 2 == 0:
            # If the number of marbles is even, the first player will always take 1 marble
            # which forces the second player into the position of the first player but with
            # an odd number of marbles remaining, thus the first player will always win.
            winners.append('B')
        else:
            # If the number of marbles is odd, the first player can take one marble and
            # then mimic the second player's moves for the rest of the game, thus ensuring
            # their win unless the second player makes a mistake.
            winners.append('A')

    return winners
```