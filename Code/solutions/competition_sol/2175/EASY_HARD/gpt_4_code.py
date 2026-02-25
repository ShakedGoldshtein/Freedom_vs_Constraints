```python
def solve(m, nums):
    from bisect import bisect_right
    b = []
    res = []
    p = [0] * 600
    for i in range(m):
        x = nums[i]
        f = [0] * 600
        f[599] = i
        for j in range(len(b) - 1, -1, -1):
            if (x >> b[j]) & 1:
                if not f[b[j]]:
                    break
                x ^= 1 << b[j]
                f ^= p[b[j]]
        else:
            if x > 0:
                b.insert(bisect_right(b, x.bit_length() - 1), x.bit_length() - 1)
                p[x.bit_length() - 1] = f
                res.append([0])
                continue
        res.append([bin(f).count('1')] + [item for item in range(599, -1, -1) if f[item]])
    return res
```