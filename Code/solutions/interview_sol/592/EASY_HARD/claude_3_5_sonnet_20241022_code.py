```python
def solve(test_cases):
    def can_win(s, words, memo=None):
        if memo is None:
            memo = {}
            
        if s in memo:
            return memo[s]
            
        if not s:
            return False
            
        # Try each word in dictionary
        for word in words:
            # Try each possible position
            for i in range(len(s) - len(word) + 1):
                if s[i:i+len(word)] == word:
                    # Split string and recursively check remaining parts
                    left = s[:i]
                    right = s[i+len(word):]
                    
                    # If opponent can't win with either remaining part, this is a winning move
                    if not can_win(left + right, words, memo):
                        memo[s] = True
                        return True
                        
        memo[s] = False
        return False

    result = []
    for s, n, words in test_cases:
        if can_win(s, words):
            result.append("Teddy")
        else:
            result.append("Tracy") 
            
    return result

def parse_input(T, input_lines):
    test_cases = []
    i = 0
    for _ in range(T):
        s = input_lines[i]
        n = int(input_lines[i+1])
        words = input_lines[i+2:i+2+n]
        test_cases.append((s, n, words))
        i += n + 2
    return test_cases
```