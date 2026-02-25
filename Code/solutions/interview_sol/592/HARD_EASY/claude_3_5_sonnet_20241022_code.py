```python
def check_win(s, words, memo):
    if not s:
        return False
    
    if s in memo:
        return memo[s]
    
    # Try all words in dictionary
    for word in words:
        # Try all possible positions to erase the word
        for i in range(len(s) - len(word) + 1):
            if s[i:i+len(word)] == word:
                # Split string into left and right parts
                left = s[:i]
                right = s[i+len(word):]
                
                # Check if next player loses with these parts
                next_player_loses = True
                
                if left and right:
                    next_player_loses = not check_win(left, words, memo) or not check_win(right, words, memo)
                elif left:
                    next_player_loses = not check_win(left, words, memo)
                elif right:
                    next_player_loses = not check_win(right, words, memo)
                    
                if next_player_loses:
                    memo[s] = True
                    return True
                    
    memo[s] = False
    return False

def solve(test_cases):
    results = []
    
    for s, words in test_cases:
        # Memoization dict to store computed results
        memo = {}
        
        # Check if first player (Teddy) wins
        teddy_wins = check_win(s, words, memo)
        
        results.append("Teddy" if teddy_wins else "Tracy")
        
    return results

def process_input(raw_input):
    # Convert raw input format to list of (string, words) tuples
    test_cases = []
    i = 1  # Skip first line with T
    
    while i < len(raw_input):
        s = raw_input[i]
        n = int(raw_input[i+1])
        words = raw_input[i+2:i+2+n]
        test_cases.append((s, words))
        i += n + 2
        
    return test_cases
```