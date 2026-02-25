```python
def solve(n):
    if n == 1:
        return [0]
    
    primes = []
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    questions = []
    for p in primes:
        power = p
        while power <= n:
            questions.append(power)
            power *= p
    
    return [len(questions)] + questions
```