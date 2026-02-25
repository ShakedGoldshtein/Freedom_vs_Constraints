```python
def solve(T, test_cases):
    results = []
    for _ in range(T):
        N = test_cases[_][0]
        S = test_cases[_][1]
        P = test_cases[_][2]
        
        # Count ones and zeroes in both strings
        ones_s = S.count('1')
        ones_p = P.count('1')
        
        # If number of 1s different, impossible
        if ones_s != ones_p:
            results.append("No")
            continue
            
        # Check if there are any inversions
        inversions = False
        for i in range(N):
            if S[i] != P[i]:
                inversions = True
                break
                
        # If no inversions needed
        if not inversions:
            results.append("Yes")
            continue
            
        # Get positions of 1s in S and P
        pos_s = [i for i in range(N) if S[i] == '1']
        pos_p = [i for i in range(N) if P[i] == '1']
        
        # Check if any 1 in S appears after its target position in P
        can_swap = False
        for i in range(len(pos_s)):
            if pos_s[i] > pos_p[i]:
                can_swap = True
                break
                
        results.append("Yes" if can_swap else "No")
            
    return results
```