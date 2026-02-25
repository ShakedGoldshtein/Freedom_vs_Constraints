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


def solve(T: int, test_cases: list[tuple[int, int]]) -> list[int]:
    """Determine if a number can be formed by the sum of K prime numbers.

    Args:
        T (int): The number of test cases.
        test_cases (list of tuples): Each tuple contains two integers (N, K).

    Returns:
        list of int: A list of 1s and 0s indicating whether each test case is possible.
    """
    results = []
    for N, K in test_cases:
        if K == 1:
            # If K is 1, N must be a prime number itself
            results.append(1 if is_prime(N) else 0)
        elif K == 2:
            # If K is 2, N must be either even or the sum of two primes
            # Since 2 is the only even prime, all even numbers >= 4 can be expressed as the sum of two primes
            # Odd numbers can be expressed as 2 + (N - 2), where (N - 2) must be prime
            if N % 2 == 0:
                results.append(1 if N >= 4 else 0)
            else:
                results.append(1 if is_prime(N - 2) else 0)
        else:
            # For K >= 3, any number >= 2K can be expressed as the sum of K primes
            # This is because we can use 2 (the smallest prime) multiple times
            results.append(1 if N >= 2 * K else 0)
    return results


# Example usage:
# T = 2
# test_cases = [(12, 2), (11, 2)]
# print(solve(T, test_cases))  # Output: [1, 0]
```