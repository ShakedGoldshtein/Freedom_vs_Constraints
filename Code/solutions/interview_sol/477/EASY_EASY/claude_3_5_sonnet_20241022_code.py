```python
def solve(n, k):
    def kthGrammar(i, k, l):
        if i == 1:
            return "0"
        
        prev_len = (1 << (i-1)) - 1
        if k <= prev_len:
            return kthGrammar(i-1, k, prev_len)
        elif k == prev_len + 1:
            return "1"
        else:
            k_mirror = 2 * (prev_len + 1) - k
            return "1" if kthGrammar(i-1, k_mirror, prev_len) == "0" else "0"
    
    return kthGrammar(n, k, (1 << n) - 1)
```