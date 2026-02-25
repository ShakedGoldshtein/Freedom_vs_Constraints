```python
def _prime_factorize(num):
    """
    Finds all distinct prime factors of a given number.

    Args:
        num (int): The number to factorize. Must be >= 2.

    Returns:
        set[int]: A set of distinct prime factors.
    """
    factors = set()
    d = 2
    temp = num
    while d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:  # If temp is still > 1, it is a prime factor itself
        factors.add(temp)
    return factors


def _count_coprime_in_range(N, prime_factors_P):
    """
    Counts the number of integers x such that 1 <= x <= N and GCD(x, P) = 1,
    where P is defined by its distinct prime factors.
    
    This function uses the Principle of Inclusion-Exclusion, also known as
    the Mobius inversion formula for counting numbers coprime to P up to N.

    Args:
        N (int): The upper limit of the range [1, N].
        prime_factors_P (set[int]): A set of distinct prime factors of P.

    Returns:
        int: The count of integers in [1, N] coprime to P.
    """
    # If P has no prime factors (i.e., P=1, which is not possible per constraints N,P >= 2),
    # all numbers from 1 to N would be coprime to P.
    if not prime_factors_P:
        return N

    # Convert set to sorted list for consistent indexing with bit manipulation
    primes = sorted(list(prime_factors_P))
    m = len(primes)  # Number of distinct prime factors

    total_coprime_count = 0

    # Iterate through all 2^m subsets of the prime factors.
    # Each 'i' from 0 to 2^m - 1 represents a unique subset.
    for i in range(1 << m):
        current_product = 1
        num_factors_in_subset = 0  # Used to determine the sign for inclusion-exclusion

        # Reconstruct the product 'd' for the current subset
        for j in range(m):
            if (i >> j) & 1:  # If the j-th prime is included in the current subset
                current_product *= primes[j]
                num_factors_in_subset += 1
        
        # The term to add or subtract is N // current_product.
        # If current_product > N, then N // current_product will be 0, which is correct.
        term = N // current_product
        
        # Apply Mobius function logic:
        # Add if the number of factors in the subset is even (including 0 for the empty set).
        # Subtract if the number of factors in the subset is odd.
        if num_factors_in_subset % 2 == 0:
            total_coprime_count += term
        else:
            total_coprime_count -= term
            
    return total_coprime_count


def solve(N, P):
    """
    Calculates the total number of "good pairs" (a, b) such that 1 <= a < b <= N
    and GCD(a*b, P) = 1.

    A pair (a, b) is defined as a "good pair" if 1 <= a < b <= N and GCD(a*b, P) = 1.
    The condition GCD(a*b, P) = 1 implies that 'a' and 'b' must both be coprime to P.
    That is, GCD(a, P) = 1 AND GCD(b, P) = 1.

    The solution proceeds in three steps:
    1. Identify all distinct prime factors of P.
    2. Count how many integers `x` in the range `[1, N]` satisfy `GCD(x, P) = 1`.
       Let this count be `K`.
    3. The number of good pairs (a, b) with `a < b` chosen from these `K` integers
       is given by the combination formula `K * (K - 1) / 2`.

    Time Complexity:
        O(sqrt(P)) for prime factorization.
        O(2^m * m) for counting coprime numbers, where `m` is the number of distinct
        prime factors of P. For P <= 10^5, `m` is at most 7 (2*3*5*7*11*13*17 > 10^5).
        Overall time complexity is dominated by O(sqrt(P) + 2^m * m), which is highly efficient.

    Space Complexity:
        O(m) for storing distinct prime factors.

    Args:
        N (int): The upper bound for 'a' and 'b' (constraint: 2 <= N <= 10^5).
        P (int): The integer for GCD calculation (constraint: 2 <= P <= 10^5).

    Returns:
        int: The total number of good pairs.
    """
    # Step 1: Find all distinct prime factors of P
    prime_factors_P = _prime_factorize(P)

    # Step 2: Count numbers 'x' in the range [1, N] that are coprime to P.
    # This count is 'K'.
    k_count = _count_coprime_in_range(N, prime_factors_P)

    # Step 3: Calculate the number of pairs (a, b) such that a < b
    # from the k_count numbers. This is a combination (K choose 2).
    if k_count < 2:
        return 0  # Not enough numbers to form a pair
    else:
        return k_count * (k_count - 1) // 2

```