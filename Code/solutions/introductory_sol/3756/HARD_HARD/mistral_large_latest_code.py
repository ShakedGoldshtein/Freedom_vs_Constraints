```python
def goldbach_representations(n: int) -> list[str]:
    """
    Returns all unique Goldbach representations of an even number n as a list of strings in increasing order.
    Returns an empty list if n is odd or <= 2.

    Args:
        n: An integer where 2 < n < 32000.

    Returns:
        List of strings representing prime pairs that sum to n, or empty list if no representations exist.
    """
    if n <= 2 or n % 2 != 0:
        return []

    sieve = _sieve_of_eratosthenes(n)
    representations = []

    for p in range(2, n // 2 + 1):
        q = n - p
        if sieve[p] and sieve[q] and p <= q:
            representations.append(f"{p}+{q}")

    return representations

def _sieve_of_eratosthenes(limit: int) -> list[bool]:
    """
    Generates a sieve (boolean list) where sieve[i] is True if i is a prime number.

    Args:
        limit: Upper bound for the sieve (inclusive).

    Returns:
        Boolean list where index represents the number and value indicates primality.
    """
    if limit < 2:
        return [False] * (limit + 1)

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            sieve[num*num : limit+1 : num] = [False] * len(sieve[num*num : limit+1 : num])

    return sieve
```