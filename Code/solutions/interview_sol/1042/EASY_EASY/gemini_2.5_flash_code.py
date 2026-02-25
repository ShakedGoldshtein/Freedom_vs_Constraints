```python
def solve(N, P):
    """
    Calculates the number of "good pairs" (a, b) such that 1 <= a < b <= N
    and GCD(a * b, P) = 1.

    A pair (a, b) is good if GCD(a * b, P) = 1. This implies that 'a' must be
    coprime to 'P' and 'b' must be coprime to 'P'.
    The problem reduces to finding the number of pairs (a, b) such that
    1 <= a < b <= N, GCD(a, P) = 1, and GCD(b, P) = 1.

    Steps:
    1. Find all distinct prime factors of P.
    2. Count how many numbers 'x' in the range [1, N] are coprime to P.
       Let this count be 'k'. This is done using the Principle of Inclusion-Exclusion.
       A number 'x' is coprime to 'P' if it is not divisible by any of P's prime factors.
       We calculate the count of numbers in [1, N] divisible by at least one prime factor of P,
       and subtract this from N to get 'k'.
    3. The total number of good pairs is the number of ways to choose 2 distinct
       numbers from these 'k' coprime numbers, which is k * (k - 1) // 2.
    """

    # Step 1: Find distinct prime factors of P
    prime_factors = []
    temp_P = P
    d = 2
    while d * d <= temp_P:
        if temp_P % d == 0:
            prime_factors.append(d)
            while temp_P % d == 0:
                temp_P //= d
        d += 1
    if temp_P > 1:  # If temp_P is still > 1, it's a prime factor itself
        prime_factors.append(temp_P)

    # Step 2: Calculate 'k', the count of numbers x in [1, N] such that GCD(x, P) = 1
    # This uses the Principle of Inclusion-Exclusion.
    # We count numbers divisible by at least one prime factor of P.
    
    m = len(prime_factors)
    count_divisible_by_any_factor = 0

    # Iterate through all non-empty subsets of prime_factors using bitmasks.
    # Each 'i' represents a subset: if the j-th bit of 'i' is set, the j-th prime factor is in the subset.
    for i in range(1, 1 << m):  # 'i' goes from 1 to (2^m - 1)
        current_product = 1
        num_factors_in_subset = 0
        
        # Calculate the product of prime factors in the current subset.
        # Optimize by breaking early if current_product exceeds N, as N // current_product would then be 0.
        for j in range(m):
            if (i >> j) & 1:  # If the j-th prime factor is in the current subset
                # Check if multiplying by prime_factors[j] would cause current_product to exceed N.
                # This prevents potential overflow and unnecessary calculations.
                if prime_factors[j] > N // current_product:
                    current_product = N + 1  # Mark as exceeding N
                    break 
                
                current_product *= prime_factors[j]
                num_factors_in_subset += 1
        
        # If the product of this subset's factors is greater than N,
        # there are no multiples of this product in the range [1, N].
        if current_product > N:
            continue

        term = N // current_product
        
        # Apply Inclusion-Exclusion:
        # Add terms for subsets with an odd number of factors.
        # Subtract terms for subsets with an even number of factors.
        if num_factors_in_subset % 2 == 1:
            count_divisible_by_any_factor += term
        else:
            count_divisible_by_any_factor -= term

    # The count of numbers x in [1, N] such that GCD(x, P) = 1 is:
    # Total numbers (N) - count of numbers divisible by at least one prime factor of P.
    k = N - count_divisible_by_any_factor

    # Step 3: Calculate the number of good pairs (combinations)
    # This is k C 2 (k choose 2) = k * (k - 1) / 2.
    # We need at least 2 numbers (k >= 2) to form a pair.
    if k < 2:
        return 0
    else:
        return k * (k - 1) // 2

```