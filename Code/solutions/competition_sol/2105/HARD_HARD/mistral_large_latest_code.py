```python
def solve(n):
    if n == 0:
        return (0, [])

    max_price = n + 1
    min_prime = 2
    max_possible_prime = int((max_price) ** 0.5) + 2

    # Sieve of Eratosthenes to find primes up to max_price
    sieve = [True] * (max_price + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, max_possible_prime):
        if sieve[i]:
            sieve[i*i::i] = [False] * len(sieve[i*i::i])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # For each number, find its smallest prime factor (spf)
    spf = [0] * (max_price + 1)
    for p in primes:
        for multiple in range(p, max_price + 1, p):
            if spf[multiple] == 0:
                spf[multiple] = p

    # Assign colors based on the smallest prime factor
    color_map = {}
    colors = []
    current_color = 1

    for price in range(2, max_price + 1):
        if spf[price] == 0:  # price is 1 (unreachable here) or 0 (unreachable)
            continue
        if spf[price] not in color_map:
            color_map[spf[price]] = current_color
            current_color += 1
        colors.append(color_map[spf[price]])

    # Handle the case where all primes are the same (e.g., n=1)
    k = max(color_map.values()) if color_map else 0

    return (k, colors)
```