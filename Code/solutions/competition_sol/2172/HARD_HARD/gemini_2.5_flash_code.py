```python
import math
from math import gcd

# --- Global Precomputation for Prime-related functions ---
# _SMALL_PRIMES will store a list of prime numbers up to a certain limit.
# This limit is chosen to be slightly larger than sqrt(MAX_N) for efficient
# trial division of numbers up to MAX_N (10^9).
_SMALL_PRIMES = []
_MAX_SIEVE_LIMIT_FOR_TRIAL_DIVISION = int(math.sqrt(10**9)) + 100

def _sieve_of_eratosthenes(limit: int) -> list[int]:
    """
    Generates a list of prime numbers up to 'limit' using the Sieve of Eratosthenes algorithm.
    
    Args:
        limit: The upper bound (inclusive) for prime number generation.
    
    Returns:
        A list of prime numbers up to 'limit'.
    """
    if limit < 2:
        return []
    is_prime_flags = [True] * (limit + 1)
    is_prime_flags[0] = is_prime_flags[1] = False
    
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime_flags[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime_flags[multiple] = False
                
    primes = [p for p, status in enumerate(is_prime_flags) if status]
    return primes

# Initialize the global small primes list once when the module is loaded.
# This ensures efficient prime checking across multiple test cases without recomputing.
_SMALL_PRIMES = _sieve_of_eratosthenes(_MAX_SIEVE_LIMIT_FOR_TRIAL_DIVISION)

def _is_prime_check(num: int) -> bool:
    """
    Checks if 'num' is a prime number.
    It uses trial division with the globally precomputed list of small primes.
    This function is efficient for numbers up to 10^9 because it only checks divisibility
    by primes up to sqrt(num), which are covered by _SMALL_PRIMES.

    Args:
        num: The integer to check for primality.

    Returns:
        True if 'num' is prime, False otherwise.
    """
    if num < 2:
        return False
    
    for p in _SMALL_PRIMES:
        if p * p > num:
            break  # Optimization: only check divisors up to sqrt(num)
        if num % p == 0:
            return False
            
    # If num is greater than the largest prime in _SMALL_PRIMES and it wasn't
    # divided by any of them, it must be prime.
    # This also covers the case where num is itself in _SMALL_PRIMES.
    return True

def _find_largest_prime_le(n: int) -> int:
    """
    Finds the largest prime number less than or equal to n.

    Args:
        n: The upper limit for the prime search.

    Returns:
        The largest prime number p such that p <= n.
        Raises ValueError if no such prime exists (i.e., n < 2).
    """
    if n < 2:
        raise ValueError("No prime number is less than or equal to n when n < 2.")
    
    # Iterate downwards from n to find the first prime.
    # The maximum prime gap is small enough for this to be efficient.
    for k in range(n, 1, -1):
        if _is_prime_check(k):
            return k
    # This part should ideally not be reached for n >= 2, as 2 is prime.
    raise RuntimeError("Should not happen: A prime was not found for n >= 2.")

def _find_smallest_prime_gt(n: int) -> int:
    """
    Finds the smallest prime number strictly greater than n.

    Args:
        n: The lower limit for the prime search (exclusive).

    Returns:
        The smallest prime number p such that p > n.
    """
    k = n + 1
    # Primes are infinite, so this loop will always find one.
    # The maximum prime gap is small enough for this to be efficient.
    while True:
        if _is_prime_check(k):
            return k
        k += 1

# --- Fraction Class for Arithmetic ---
class _Fraction:
    """
    Represents an irreducible fraction p/q with a positive denominator.
    Handles basic arithmetic operations (addition, subtraction, multiplication).
    """
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        # Simplify the fraction by dividing by the greatest common divisor
        common_divisor = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor
        
        # Ensure the denominator is positive
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __add__(self, other: '_Fraction') -> '_Fraction':
        """Adds two fractions."""
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return _Fraction(new_numerator, new_denominator)

    def __sub__(self, other: '_Fraction') -> '_Fraction':
        """Subtracts one fraction from another."""
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return _Fraction(new_numerator, new_denominator)

    def __mul__(self, other: '_Fraction' | int) -> '_Fraction':
        """
        Multiplies a fraction by another fraction or an integer.
        Args:
            other: Another _Fraction object or an integer.
        Returns:
            A new _Fraction object representing the product.
        """
        if isinstance(other, int):
            return _Fraction(self.numerator * other, self.denominator)
        return _Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __rmul__(self, other: int) -> '_Fraction':
        """
        Handles reverse multiplication (e.g., int * Fraction).
        Args:
            other: An integer.
        Returns:
            A new _Fraction object representing the product.
        """
        return self.__mul__(other)

    def __str__(self) -> str:
        """Returns the string representation of the fraction in "p/q" format."""
        return f"{self.numerator}/{self.denominator}"

# --- Main Solution Function ---
def solve(n: int) -> str:
    """
    Calculates the sum sum_{i = 2}^{n} 1 / (v(i) u(i)) as an irreducible fraction.
    v(i) is the largest prime number that does not exceed i.
    u(i) is the smallest prime number strictly greater than i.

    The sum is calculated using the derived formula:
    (1/2 - 1/P_j) + (n - P_j + 1) / (P_j * P_{j+1})
    where P_j is the largest prime number less than or equal to n,
    and P_{j+1} is the smallest prime number strictly greater than P_j.

    Args:
        n: The upper limit for the summation (2 <= n <= 10^9).

    Returns:
        The sum as an irreducible fraction string in "p/q" format.
    
    Raises:
        ValueError: If n is less than 2, as the problem specifies n >= 2.
    """
    if n < 2:
        raise ValueError("Input 'n' must be an integer >= 2.")

    # P_j: Largest prime number less than or equal to n.
    p_j = _find_largest_prime_le(n)

    # P_j_plus_1: Smallest prime number strictly greater than P_j.
    # This prime is used for u(i) for all i in the interval [P_j, n].
    p_j_plus_1 = _find_smallest_prime_gt(p_j)

    # Calculate the sum using the optimized formula:
    # Sum = (1/2 - 1/P_j) + (n - P_j + 1) / (P_j * P_{j+1})
    
    # Term 1: (1/2 - 1/P_j)
    term1 = _Fraction(1, 2) - _Fraction(1, p_j)
    
    # Term 2: (n - P_j + 1) / (P_j * P_{j+1})
    term2_numerator = n - p_j + 1
    term2_denominator = p_j * p_j_plus_1
    term2 = _Fraction(term2_numerator, term2_denominator)
    
    # Total sum
    total_sum = term1 + term2
    
    return str(total_sum)
```