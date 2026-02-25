```python
MAX_N_VAL = 100000
_is_prime_sieve = [True] * (MAX_N_VAL + 1)

def _initialize_sieve():
    """
    Initializes the prime sieve up to MAX_N_VAL.
    This function should be called once to precompute primes.
    """
    # Check if sieve has already been initialized (e.g., if 0 and 1 are already False)
    if not _is_prime_sieve[0] and not _is_prime_sieve[1]:
        return

    _is_prime_sieve[0] = _is_prime_sieve[1] = False
    for p in range(2, int(MAX_N_VAL**0.5) + 1):
        if _is_prime_sieve[p]:
            for multiple in range(p*p, MAX_N_VAL + 1, p):
                _is_prime_sieve[multiple] = False

# Call the sieve initialization once at module load time
_initialize_sieve()

def solve(N: int, K: int) -> int:
    """
    Determines if N can be formed by the sum of exactly K prime numbers.

    Args:
        N: The target number.
        K: The number of prime numbers.

    Returns:
        1 if N can be formed, 0 otherwise.
    """
    # 1. Global Minimum Sum Check:
    # The smallest prime is 2. The sum of K primes must be at least 2*K.
    if N < 2 * K:
        return 0

    # 2. Case K = 1: N must be a prime number itself.
    if K == 1:
        # N >= 2 is guaranteed by the global minimum sum check (N < 2*1 is N < 2).
        # N is within [2, MAX_N_VAL], so _is_prime_sieve[N] is a valid access.
        return 1 if _is_prime_sieve[N] else 0

    # 3. Case K = 2: N must be the sum of two primes.
    if K == 2:
        # N >= 4 is guaranteed by the global minimum sum check (N < 2*2 is N < 4).
        if N % 2 == 0:
            # Goldbach's Conjecture states that every even integer greater than 2 is the sum of two primes.
            # This holds true for N <= 10^5. Since N >= 4 and N is even, it's always possible.
            return 1
        else: # N is odd
            # To get an odd sum from two primes, one prime must be 2, and the other must be N-2.
            # N-2 must be an odd prime.
            # N is odd and N >= 2K=4 implies N >= 5. So N-2 >= 3.
            return 1 if _is_prime_sieve[N - 2] else 0

    # 4. Case K >= 3:
    # We already know N >= 2*K from the initial check.
    if N % 2 == 0: # N is even
        # For N even and K >= 3 (and N >= 2K), it is always possible to form N as a sum of K primes.
        # This relies on generalizations of Goldbach's conjecture. For example, any even number
        # can be represented as sum of K primes (by repeatedly using 2s and reducing to a 2-prime sum).
        return 1
    else: # N is odd
        # For N odd and K >= 3, we need to form an odd sum using K primes.
        # If K is even: We must use exactly one '2' (since an even number of odd primes sums to an even number).
        #   So, N = 2 + (sum of K-1 primes). This means (N-2) must be formed by (K-1) primes.
        #   Here, N-2 is odd, and K-1 is odd. This reduces to the (odd N, odd K) subproblem.
        # If K is odd: We can use K odd primes, or an even number of '2's (0, 2, 4...) and an odd number of odd primes.
        #   The minimum sum achievable for an odd N using K primes (when K is odd or even but forcing one '2')
        #   is 2*(K-1) + 3 (using K-1 '2's and one '3'), which simplifies to 2K+1.
        # So, if N is odd (regardless of K's parity when K >= 3), the condition is N >= 2K + 1.
        if N >= 2 * K + 1:
            return 1
        else:
            return 0
```