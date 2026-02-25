```python
def solve_game(S, words):
    n = len(S)
    word_set = set(words)
    dp = [0] * (n + 1)
    
    for i in range(n + 1):
        for j in range(i):
            if S[j:i] in word_set:
                dp[i] |= ~dp[j]
    
    return "Teddy" if dp[n] else "Tracy"

def main():
    import sys
    input_data = sys.stdin.read().splitlines()
    t = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        S = input_data[idx]; idx += 1
        n = int(input_data[idx]); idx += 1
        words = []
        for __ in range(n):
            words.append(input_data[idx]); idx += 1
        results.append(solve_game(S, words))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
```