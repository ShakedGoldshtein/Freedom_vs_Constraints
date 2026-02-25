```python
def solve(N, L, strings):
    def is_prefix(s1, s2):
        return s1.startswith(s2) or s2.startswith(s1)
    
    def can_add_string(curr_strings, length):
        if length > L:
            return False
            
        def check(curr, depth):
            if depth == length:
                new_str = curr
                # Check if new string would be prefix-free with all existing strings
                for s in curr_strings:
                    if is_prefix(new_str, s):
                        return False
                return True
            
            # Try adding 0 or 1
            return check(curr + "0", depth + 1) or check(curr + "1", depth + 1)
            
        return check("", 0)
    
    def can_win(curr_strings):
        # Try adding strings of each possible length
        for length in range(1, L+1):
            if can_add_string(curr_strings, length):
                return True
        return False
    
    # Game state is the current set of strings
    curr_strings = set(strings)
    
    # Alice's turn
    if can_win(curr_strings):
        return "Alice"
    return "Bob"
```