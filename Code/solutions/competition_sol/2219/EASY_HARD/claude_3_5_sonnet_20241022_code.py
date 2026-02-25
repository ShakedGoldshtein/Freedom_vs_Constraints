```python
def check_subsequence(s, pattern):
    j = 0
    for i in range(len(s)):
        if j < len(pattern) and s[i] == pattern[j]:
            j += 1
    return j == len(pattern)

def can_coexist(s, words):
    n = len(s)
    used = [0] * n
    
    def find_subsequence(word, start_pos):
        if not word:
            return True
            
        pos = 0
        for i in range(start_pos, n):
            if used[i]:
                continue
            if s[i] == word[pos]:
                used[i] = 1
                pos += 1
                if pos == len(word):
                    return True
        
        # Backtrack - remove marked positions
        pos = 0
        for i in range(start_pos, n):
            if not used[i]:
                continue
            if s[i] == word[pos]:
                used[i] = 0
                pos += 1
        return False
                
    if not find_subsequence(words[0], 0):
        return False
        
    if not find_subsequence(words[1], 0):
        # Backtrack first word
        for i in range(n):
            used[i] = 0
        return False
        
    if not find_subsequence(words[2], 0):
        return False
        
    return True

def solve(n, q, s, queries):
    words = ["", "", ""]
    result = []
    
    for query in queries:
        if query[0] == "+":
            rel_id = int(query[2]) - 1
            char = query[4]
            words[rel_id] += char
        else:
            rel_id = int(query[2]) - 1 
            words[rel_id] = words[rel_id][:-1]
            
        result.append("YES" if can_coexist(s, words) else "NO")
            
    return result
```