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
        if p * p <= n:
            questions.append(p * p)
        questions.append(p)
    questions = sorted(list(set(questions)))
    k = len(questions)
    return (k, questions)
```