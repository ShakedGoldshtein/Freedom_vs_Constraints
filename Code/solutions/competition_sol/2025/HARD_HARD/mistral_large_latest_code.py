```python
def solve(n):
    if n == 1:
        return (0, [])

    primes = []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    questions = []
    for p in primes:
        if p <= n:
            questions.append(p)

    max_power = 1
    while max_power * 2 <= n:
        max_power *= 2
    if max_power > 1:
        questions.append(max_power)

    questions = sorted(questions)
    questions = list(dict.fromkeys(questions))

    return (len(questions), questions)
```