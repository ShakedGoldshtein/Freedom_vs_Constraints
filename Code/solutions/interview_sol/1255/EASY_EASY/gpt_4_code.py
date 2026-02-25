```python
def solve(teaching_cases):
    result = []
    for tc in teaching_cases:
        s, k,= tc
        s = sorted(s)
        t = ['a'] * len(s)
        j = 0
        for i, c in enumerate('abcdefghijklmnopqrstuvwxyz'):
            if j == len(s):
                break
            elif c not in s or s[j] != c:
                t[j] = c
                j += 1
            elif s[j] == c and k > 0:
                t[j] = c
                j += 1
                k -= 1
        if j < len(s) or k > 0:
            result.append("NOPE")
        else:
            result.append("".join(t))

    return result
```