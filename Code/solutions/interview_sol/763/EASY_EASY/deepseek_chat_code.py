```python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        S = data[idx]
        idx += 1
        P = data[idx]
        idx += 1
        
        if S == P:
            results.append("Yes")
            continue
            
        s_ones = S.count('1')
        p_ones = P.count('1')
        if s_ones != p_ones:
            results.append("No")
            continue
            
        possible = True
        s_count = 0
        p_count = 0
        for i in range(n):
            s_count += 1 if S[i] == '1' else 0
            p_count += 1 if P[i] == '1' else 0
            if s_count < p_count:
                possible = False
                break
                
        results.append("Yes" if possible else "No")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
```