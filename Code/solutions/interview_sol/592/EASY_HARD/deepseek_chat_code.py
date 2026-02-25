```python
def solve_game():
    T = int(input().strip())
    results = []
    for _ in range(T):
        S = input().strip()
        N = int(input().strip())
        dictionary = [input().strip() for _ in range(N)]
        
        words_set = set(dictionary)
        n = len(S)
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and S[j:i] in words_set:
                    dp[i] = True
                    break
        
        grundy = [0] * (n + 1)
        for i in range(1, n + 1):
            moves = set()
            for j in range(i):
                if dp[j] and S[j:i] in words_set:
                    moves.add(grundy[j] ^ grundy[i])
            g = 0
            while g in moves:
                g += 1
            grundy[i] = g
        
        if grundy[n] != 0:
            results.append("Teddy")
        else:
            results.append("Tracy")
    
    for res in results:
        print(res)

if __name__ == "__main__":
    solve_game()
```