```python
import math

MAX_N = 100000
_is_prime = [True] * (MAX_N + 1)

def _sieve_of_eratosthenes():
    _is_prime[0] = _is_prime[1] = False
    for p in range(2, int(math.sqrt(MAX_N)) + 1):
        if _is_prime[p]:
            for multiple in range(p * p, MAX_N + 1, p):
                _is_prime[multiple] = False

_sieve_of_eratosthenes()

def can_form_sum_of_k_primes(n: int, k: int) -> int:
    if n < 2 * k:
        return 0

    if k == 1:
        return 1 if _is_prime[n] else 0

    if k == 2:
        if n % 2 == 0:
            return 1
        else:
            return 1 if (n - 2 > 1 and _is_prime[n - 2]) else 0
    
    # For K >= 3
    if n % 2 == 0: # N is even
        # N = (K-2)*2 + p1 + p2.
        # Remaining sum needed: n_rem = N - 2 * (K - 2) = N - 2*K + 4.
        # Since N >= 2*K (from initial check), N - 2*K >= 0.
        # Thus, n_rem >= 4.
        # Any even number >= 4 can be expressed as the sum of two primes (Goldbach Conjecture).
        return 1
    else: # N is odd
        # N must be formed by an odd number of odd primes, or by 2 and an even number of odd primes.
        # This simplifies to: N must be formed by (K-3)*2 + p1+p2+p3 if K is odd,
        # or by 2 + (K-1 primes summing to N-2) if K is even.
        # In both scenarios, if N > 2*K, it implies there's enough "room" for the remaining primes
        # to form a sum that satisfies Goldbach's Weak Conjecture (sum of 3 primes for odd number >= 7).
        # Specifically:
        # If K is odd: N_rem = N - 2*(K-3) = N - 2K + 6. If N > 2K, then N >= 2K+1 (N is odd).
        #   N_rem >= (2K+1) - 2K + 6 = 7. So an odd N_rem >= 7 can be formed by 3 primes.
        # If K is even: We must use one '2'. Remaining problem is (N-2, K-1).
        #   N' = N-2 (odd), K' = K-1 (odd). Apply same logic: N' > 2*K' => (N-2) > 2*(K-1) => N-2 > 2K-2 => N > 2K.
        return 1 if n > 2 * k else 0

```