```python
def solve(n):
    if n == 0:
        return (0, [])

    max_num = n + 1
    spf = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        if spf[i] == 0:
            spf[i] = i
            for j in range(i * i, max_num + 1, i):
                if spf[j] == 0:
                    spf[j] = i
        else:
            if spf[i] == i:
                continue
            temp = i
            min_prime = spf[i]
            while temp % min_prime == 0:
                temp //= min_prime
            if temp > 1:
                spf[i] = spf[temp]

    color = [0] * (max_num + 1)
    current_color = 1
    for i in range(2, max_num + 1):
        if color[i] == 0:
            if spf[i] == i:
                color[i] = current_color
                current_color += 1
            else:
                color[i] = color[spf[i]]

    colors = [color[i] for i in range(2, max_num + 1)]
    k = max(colors) if colors else 0
    return (k, colors)
```