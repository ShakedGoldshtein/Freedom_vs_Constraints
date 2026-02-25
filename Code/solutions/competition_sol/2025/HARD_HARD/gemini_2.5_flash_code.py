```python
import math

def _sieve_primes(limit: int) -> list[bool]:
    """
    Computes a boolean list indicating primality for numbers up to 'limit'
    using the Sieve of Eratosthenes.

    Args:
        limit: The upper bound for numbers to check for primality (inclusive).

    Returns:
        A list of booleans where is_prime[i] is True if i is prime, False otherwise.
        is_prime[0] and is_prime[1] are always False.
    """
    if limit < 2:
        return [False] * (limit + 1)

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    # Iterate up to sqrt(limit).
    # Any composite number n has at least one prime factor less than or equal to sqrt(n).
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            # Mark multiples of p as not prime.
            # Start from p*p because smaller multiples (p*2, p*3, ...)
            # would have already been marked by smaller primes.
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return is_prime

def find_optimal_questions(n: int) -> tuple[int, list[int]]:
    """
    Finds the minimum number of questions Petya should ask to guarantee
    guessing Vasya's number (1 to n), and the questions themselves.

    The questions are of the form "Is the unknown number divisible by y?".
    To uniquely identify any number x in the range [1, n], Petya needs to
    be able to determine its unique prime factorization. This is achieved
    by asking about all prime powers p^k such that p^k <= n. Each such
    question helps to ascertain the exponent of a prime factor in x's
    prime factorization.

    Args:
        n: The upper bound for Vasya's secret number (1 <= n <= 1000).

    Returns:
        A tuple where the first element is the count of questions (k),
        and the second element is a list of integers (y_i) representing
        the numbers Petya should ask about.
        If n=1, k will be 0 and the list of questions will be empty,
        as Petya already knows the number is 1.

    Raises:
        ValueError: If n is less than 1, violating the problem constraints.
    """
    if n < 1:
        raise ValueError("Input 'n' must be at least 1 according to problem constraints.")
    
    # If n is 1, the only possible number is 1. Petya knows it without asking any questions.
    if n == 1:
        return (0, [])

    # Step 1: Generate primality information up to n using a sieve.
    is_prime_sieve = _sieve_primes(n)
    
    questions = []

    # Step 2: Iterate through numbers from 2 to n. If a number 'p' is prime,
    # add 'p' and all its powers (p^2, p^3, ...) that are less than or equal to n
    # to the list of questions.
    for p in range(2, n + 1):
        if is_prime_sieve[p]:
            current_power = p
            while current_power <= n:
                questions.append(current_power)
                # Check if multiplying by 'p' again would exceed 'n'.
                # This prevents `current_power` from growing unnecessarily large
                # if the next power would already be greater than n.
                if current_power > n / p: # equivalent to current_power * p > n
                    break 
                current_power *= p

    return (len(questions), questions)
```