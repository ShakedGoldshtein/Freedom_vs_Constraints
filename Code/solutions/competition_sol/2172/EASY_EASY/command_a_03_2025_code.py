```python
import math


def sieve(n: int) -> list[int]:
    """Generate all prime numbers up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit for generating prime numbers.

    Returns:
        list[int]: A list of prime numbers up to n.
    """
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime numbers
    for current_prime in range(2, int(math.sqrt(n)) + 1):
        if sieve[current_prime]:
            for multiple in range(current_prime * current_prime, n + 1, current_prime):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b using the Euclidean algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a


def solve(n: int) -> str:
    """Calculate the sum of 1/(v(i)*u(i)) for i from 2 to n, where v(i) is the largest prime <= i and u(i) is the smallest prime > i.

    Args:
        n (int): The upper limit for the summation.

    Returns:
        str: The result as an irreducible fraction "p/q".
    """
    primes = sieve(n + 1)
    p_prev, p_cur = primes[0], primes[1]
    numerator, denominator = 0, 1

    i = 2
    while i <= n:
        # Find the range where v(i) and u(i) are constant
        low, high = i, n
        while high - low > 1:
            mid = (low + high) // 2
            if primes[-1] - primes[bisect_left(primes, mid)] < 2:
                low = mid
            else:
                high = mid
        # Update the numerator and denominator
        numerator += (low - i + 1) * p_prev
        denominator *= p_cur
        i = low + 1
        if i <= n:
            p_prev, p_cur = p_cur, primes[bisect_left(primes, i) + 1]

    # Simplify the fraction
    common_divisor = gcd(numerator, denominator)
    return f"{numerator // common_divisor}/{denominator // common_divisor}"


from bisect import bisect_left


def main() -> None:
    """Main function to handle multiple test cases."""
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))


if __name__ == "__main__":
    main()
```