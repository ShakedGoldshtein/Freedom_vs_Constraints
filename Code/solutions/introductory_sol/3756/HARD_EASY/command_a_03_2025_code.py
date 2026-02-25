```python
def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solve(n: int) -> list[str]:
    """Return a list of unique representations of n as the sum of two primes.

    Args:
        n (int): The even integer to represent as the sum of two primes.

    Returns:
        list[str]: A list of strings representing n as the sum of two primes,
                   or an empty list if n is odd.
    """
    if n % 2 != 0 or n < 4:
        return []

    result = []
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            result.append(f"{i}+{n - i}")
    return result
```