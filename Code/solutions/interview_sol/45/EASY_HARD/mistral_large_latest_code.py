```python
def solve(x):
    max_n = int((2 * x) ** 0.5) + 2
    nice = []
    for n in range(1, max_n + 1):
        total = n * (n + 1) // 2
        if total > x:
            continue
        k = 1
        while k * k <= n:
            if n % k == 0:
                d = n // k
                if (k + d) % 2 == 1:
                    m = (k + d) // 2
                    if m * m <= n:
                        nice.append(n)
                        break
            k += 1
    nice_sorted = sorted(nice)
    res = 0
    current_sum = 0
    for num in nice_sorted:
        if current_sum + num * (num + 1) // 2 <= x:
            current_sum += num * (num + 1) // 2
            res += 1
    return res

def solve_all(test_cases):
    return [solve(x) for x in test_cases]
```