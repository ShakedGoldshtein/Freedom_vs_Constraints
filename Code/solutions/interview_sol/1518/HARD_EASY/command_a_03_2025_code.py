```python
def is_prime(n: int) -> bool:
    """Check if a number is prime.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes_up_to(n: int) -> int:
    """Count the number of primes up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit to count primes up to.

    Returns:
        int: The count of prime numbers up to n.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sum(sieve)


def can_form_sum(n: int, k: int) -> int:
    """Determine if n can be formed by the sum of k prime numbers.

    Args:
        n (int): The target number to form.
        k (int): The number of prime numbers to sum.

    Returns:
        int: 1 if n can be formed by the sum of k primes, 0 otherwise.
    """
    if k == 1:
        return 1 if is_prime(n) else 0
    if k == 2:
        if n < 2:
            return 0
        if n % 2 == 0:
            return 1
        return 1 if is_prime(n - 2) else 0
    if k >= 3:
        if n < 3 * k:
            return 0
        if n % 2 == 0:
            return 1
        if n % 2 != 0 and k >= 2:
            return 1
    return 0


def solve(test_cases: list[tuple[int, int]]) -> list[int]:
    """Solve the problem for multiple test cases.

    Args:
        test_cases (list of tuples): Each tuple contains (N, K) for a test case.

    Returns:
        list of int: A list of results (1 or 0) for each test case.
    """
    results = []
    for n, k in test_cases:
        results.append(can_form_sum(n, k))
    return results


# Example usage:
# test_cases = [(12, 2), (11, 2)]
# print(solve(test_cases))
```