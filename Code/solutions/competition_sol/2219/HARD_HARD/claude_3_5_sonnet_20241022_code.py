```python
def can_religions_coexist(universe, r1, r2, r3):
    def is_subsequence(s, t):
        if not s:
            return True, list(range(len(t)))
        i = j = 0
        indices = []
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                indices.append(j)
                i += 1
            j += 1
        return i == len(s), indices
    
    def can_coexist_helper(p1, p2, p3, used):
        if p1 >= len(r1):
            return can_coexist_helper(len(r1), p2, p3, used) if p2 < len(r2) or p3 < len(r3) else True
            
        start = max(used[-1] + 1 if used else 0, p1)
        for i in range(start, len(universe)):
            if i not in used and universe[i] == r1[p1]:
                used.add(i)
                if can_coexist_helper(p1 + 1, p2, p3, used):
                    return True
                used.remove(i)
        return False
        
    is_sub1, _ = is_subsequence(r1, universe)
    is_sub2, _ = is_subsequence(r2, universe)
    is_sub3, _ = is_subsequence(r3, universe)
    
    if not (is_sub1 and is_sub2 and is_sub3):
        return False
        
    return can_coexist_helper(0, 0, 0, set())

def solve(n, q, universe, queries):
    religions = ['', '', '']
    results = []
    
    for query in queries:
        if query[0] == '+':
            rel_idx = int(query[1]) - 1
            char = query[2]
            religions[rel_idx] += char
        else:
            rel_idx = int(query[1]) - 1
            religions[rel_idx] = religions[rel_idx][:-1]
            
        can_coexist = can_religions_coexist(universe, religions[0], religions[1], religions[2])
        results.append('YES' if can_coexist else 'NO')
        
    return results
```