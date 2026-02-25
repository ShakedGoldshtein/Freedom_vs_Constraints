```python
def determine_winner(T, testCases):
    def play_game(S, N, dic):
        game = [0] * (len(S) + 1)
        for index in range(1, len(S) + 1):
            for st in range(0, index):
                if S[st:index] in dic:
                    game[index] = max(
                        game[index], game[st] + len(S[st:index]))

        result = game[len(S)]
        if result > 0 and result % 2 != 0 or result == 0 and N % 2 == 0:
            return "Teddy"
        else:
            return "Tracy"

    winners = []
    for i in range(T):
        testCase = testCases[i]
        S = testCase[0]
        N = testCase[1]
        dic = set(testCase[2])
        winners.append(play_game(S, N, dic))
    return winners
```
