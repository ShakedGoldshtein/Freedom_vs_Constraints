```python
def construct_permutation(n, k):
    if k == 1:
        return list(range(1, n + 1))

    res = []
    left = 1
    right = n
    for i in range(k):
        if i % 2 == 0:
            res.append(left)
            left += 1
        else:
            res.append(right)
            right -= 1

    if k % 2 == 1:
        res.extend(range(left, right + 1))
    else:
        res.extend(range(right, left - 1, -1))

    return res
```