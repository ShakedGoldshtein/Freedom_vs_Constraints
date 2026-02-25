```python
def count_substrings(t, array_s):
    res = []
    for idx in range(t):
        s = array_s[idx]
        c = [0]*(len(s) + 2)
        p = c[:]
        for i in range(len(s) - 1, -1, -1):
            c[i] = c[i+1]
            p[i] = p[i+1]
            if s[i] == '0':
                c[i] += 1
            else:
                p[i] += 1
        _sum = 0
        for i in range(len(s)):
            b = 0
            for l in range(i, min(len(s), i+20)):
                b = (b << 1) | (s[l] == '1')
                if b > l - i + 1:
                    break
                if b <= c[i] + p[l + 1]:
                    _sum += 1
        res.append(_sum)
    return res
```