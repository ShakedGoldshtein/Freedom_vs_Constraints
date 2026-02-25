```python
import math

def solve(n: int, _cache={}) -> str:
    """
    Calculates the sum sum_{i = 2}^{n} (1 / (v(i) * u(i))) as an irreducible fraction.

    v(n) is the largest prime number that does not exceed n.
    u(n) is the smallest prime number strictly greater than n.

    The sum can be simplified using a telescoping series:
    Let p_1, p_2, ..., p_k, p_{k+1}, ... be the sequence of prime numbers.
    For any i such that p_k <= i < p_{k+1}:
        v(i) = p_k
        u(i) = p_{k+1}
        The term is 1 / (p_k * p_{k+1}).
    There are (p_{k+1} - p_k) such values of i.

    So, sum_{i=p_k}^{p_{k+1}-1} (1 / (v(i) * u(i)))
    = (p_{k+1} - p_k) * (1 / (p_k * p_{k+1}))
    = (p_{k+1} - p_k) / (p_k * p_{k+1})
    = 1/p_k - 1/p_{k+1}.

    Let p_K be the largest prime number less than or equal to n.
    Let p_{K+1} be the smallest prime number strictly greater than n.

    The sum can be split into two parts:
    1. Complete intervals: sum_{j=1}^{K-1} sum_{i=p_j}^{p_{j+1}-1} (1 / (v(i) * u(i)))
       This is a telescoping sum: sum_{j=1}^{K-1} (1/p_j - 1/p_{j+1}) = 1/p_1 - 1/p_K.
       Since p_1 = 2, this part is 1/2 - 1/p_K.
    2. Partial interval: sum_{i=p_K}^{n} (1 / (v(i) * u(i)))
       For i in [p_K, n], v(i) = p_K and u(i) = p_{K+1}.
       There are (n - p_K + 1) terms.
       This part is (n - p_K + 1) / (p_K * p_{K+1}).

    Total sum = (1/2 - 1/p_K) + (n - p_K + 1) / (p_K * p_{K+1}).
    This is then converted to an irreducible fraction p/q.

    Args:
        n (int): The upper limit of the sum. (2 <= n <= 10^9)
        _cache (dict): A mutable dictionary used for memoization of precomputed primes.
                       This is a common idiom in competitive programming to avoid
                       recomputing expensive setup for multiple test cases
                       when the function signature doesn't allow explicit state passing.

    Returns:
        str: The sum as an irreducible fraction "p/q".
    """

    # Initialize cache on the first call to the function
    if "sieve" not in _cache:
        _MAX_N_VAL = 10**9
        # Max prime gap around 10^9 is about 1132 (for n up to 10^9).
        # We need a sieve up to sqrt(MAX_N) for efficient primality testing.
        # sqrt(10^9) is approx 31622.
        # A buffer is added to _SQRT_MAX_N to cover potential primes just above sqrt(N)
        # and to ensure the sieve can handle smaller numbers directly.
        _SQRT_MAX_N = int(_MAX_N_VAL**0.5) + 1500  # e.g., 31622 + 1500 = 33122
        
        # Sieve of Eratosthenes to precompute primes up to _SQRT_MAX_N
        _sieve = [True] * _SQRT_MAX_N
        _sieve[0] = _sieve[1] = False  # 0 and 1 are not prime
        for i in range(2, int(_SQRT_MAX_N**0.5) + 1):
            if _sieve[i]:
                for multiple in range(i*i, _SQRT_MAX_N, i):
                    _sieve[multiple] = False
        
        # Store the list of precomputed primes for trial division
        _precomputed_primes = [i for i, is_p in enumerate(_sieve) if is_p]
        
        # Store computed values in cache for subsequent calls
        _cache["sieve"] = _sieve
        _cache["precomputed_primes"] = _precomputed_primes
        _cache["SQRT_MAX_N"] = _SQRT_MAX_N

    # Retrieve precomputed values from cache
    _sieve = _cache["sieve"]
    _precomputed_primes = _cache["precomputed_primes"]
    _SQRT_MAX_N = _cache["SQRT_MAX_N"]

    def is_prime_test(num: int) -> bool:
        """
        Checks if a number is prime using a combination of sieve lookup
        and trial division with precomputed primes.
        """
        if num < _SQRT_MAX_N:
            return _sieve[num]
        # For larger numbers, perform trial division using precomputed primes
        for p in _precomputed_primes:
            if p * p > num: # Optimization: only check divisors up to sqrt(num)
                break
            if num % p == 0:
                return False
        return True # If no divisors found, it's prime

    def find_largest_prime_le_n(num_n: int) -> int:
        """
        Finds the largest prime number less than or equal to num_n.
        Iterates downwards from num_n. Guaranteed to find a prime for num_n >= 2.
        """
        for i in range(num_n, 1, -1): # Start from num_n, go down to 2
            if is_prime_test(i):
                return i
        # This part should not be reached for valid inputs (n >= 2)

    def find_smallest_prime_gt_n(num_n: int) -> int:
        """
        Finds the smallest prime number strictly greater than num_n.
        Iterates upwards from num_n + 1. Guaranteed to find a prime.
        """
        i = num_n + 1
        while True: # Keep incrementing until a prime is found
            if is_prime_test(i):
                return i
            i += 1

    # Find p_K (largest prime <= n) and p_K_plus_1 (smallest prime > n)
    p_K = find_largest_prime_le_n(n)
    p_K_plus_1 = find_smallest_prime_gt_n(n)

    # Calculate the numerator and denominator of the sum:
    # Sum = 1/2 - 1/p_K + (n - p_K + 1) / (p_K * p_K_plus_1)
    # Combine into a single fraction with common denominator: 2 * p_K * p_K_plus_1
    
    # Numerator calculation:
    # (p_K * p_K_plus_1)   [from 1/2]
    # - (2 * p_K_plus_1)   [from -1/p_K]
    # + (2 * (n - p_K + 1)) [from (n - p_K + 1) / (p_K * p_K_plus_1)]
    numerator = p_K * p_K_plus_1 - 2 * p_K_plus_1 + 2 * (n - p_K + 1)
    denominator = 2 * p_K * p_K_plus_1

    # Simplify the fraction by dividing both numerator and denominator by their GCD
    common_divisor = math.gcd(numerator, denominator)
    
    return f"{numerator // common_divisor}/{denominator // common_divisor}"

```