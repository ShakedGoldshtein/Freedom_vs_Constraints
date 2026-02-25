```python
import math

def _count_digits(n: int) -> int:
    """
    Counts the number of digits in a non-negative integer.
    Special case: 0 has 1 digit.

    Parameters:
        n (int): The non-negative integer.

    Returns:
        int: The number of digits in n.
    """
    if n == 0:
        return 1
    # For n > 0, the number of digits is floor(log10(n)) + 1.
    return int(math.log10(n)) + 1

def _sum_geometric_series_mod(P_val: int, N_val: int, M_val: int) -> int:
    """
    Calculates the sum of a geometric series (P_val^0 + P_val^1 + ... + P_val^(N_val-1)) % M_val.
    This function uses a modular exponentiation-like approach (binary exponentiation)
    for summing a geometric series efficiently.

    Parameters:
        P_val (int): The base of the geometric series. It should already be
                     taken modulo M_val (e.g., (10^D) % M).
        N_val (int): The number of terms in the series (corresponds to N).
        M_val (int): The modulus.

    Returns:
        int: The sum of the geometric series modulo M_val.
    """
    if N_val == 0:
        return 0
    if N_val == 1:
        return 1 % M_val  # P_val^0 = 1

    # Special case: If P_val % M_val evaluates to 1, then P_val^i % M_val is 1 for all i >= 0.
    # In this scenario, the sum becomes (1 + 1 + ... + 1) N_val times, which is N_val.
    if P_val == 1:
        return N_val % M_val

    # Recursive step based on binary exponentiation for sum
    if N_val % 2 == 0:  # If N_val is even, N_val = 2k
        k = N_val // 2
        sum_k_mod = _sum_geometric_series_mod(P_val, k, M_val)
        P_k_mod = pow(P_val, k, M_val)  # Calculate P_val^k % M_val
        # The sum S(P, 2k) = S(P, k) * (1 + P^k)
        return (sum_k_mod * (1 + P_k_mod)) % M_val
    else:  # If N_val is odd, N_val = 2k + 1
        k = N_val // 2
        sum_k_mod = _sum_geometric_series_mod(P_val, k, M_val)
        P_k_mod = pow(P_val, k, M_val)
        # The sum S(P, 2k+1) = S(P, 2k) + P^(2k)
        # S(P, 2k) = S(P, k) * (1 + P^k)
        sum_2k_mod = (sum_k_mod * (1 + P_k_mod)) % M_val
        P_2k_mod = pow(P_k_mod, 2, M_val)  # Calculate P_val^(2k) = (P_val^k)^2 % M_val
        return (sum_2k_mod + P_2k_mod) % M_val

def solve_homework_problem(A: int, N: int, M: int) -> int:
    """
    Calculates the value of X modulo M, where X is formed by concatenating
    the number A to itself N times.

    For example, if A = 120, N = 3, then X will be 120120120.
    The problem asks to find X modulo M.

    This solution uses optimal time and space complexity by leveraging
    modular arithmetic and efficient algorithms for geometric series summation.

    Parameters:
        A (int): The integer to be concatenated. Constraints: 0 <= A <= 10^9.
        N (int): The number of times A is appended. Constraints: 1 <= N <= 10^12.
        M (int): The modulus. Constraints: 2 <= M <= 10^9.

    Returns:
        int: The value of X modulo M.

    Time Complexity: O(log N) due to the binary exponentiation-like approach for
                     summing the geometric series. Calculating the number of digits
                     and initial modular exponentiation operations are negligible
                     in comparison.
    Space Complexity: O(log N) due to the recursion stack for the geometric series sum.
                      For N=10^12, the stack depth is approximately 40, which is minimal.
    """
    # Handle the base case where A is 0.
    # If A is 0, then the concatenated number X will be 0 (e.g., 00...0).
    # Therefore, X % M will always be 0.
    if A == 0:
        return 0

    # Determine the number of digits in A.
    # This value (D) determines the power of 10 by which subsequent A's are multiplied
    # when forming the large number X.
    num_digits_A = _count_digits(A)

    # Calculate P = 10^(num_digits_A) modulo M.
    # This P represents the modular multiplier for each block of A when shifted
    # left by D digits in the concatenated number X.
    P_mod_M = pow(10, num_digits_A, M)

    # Calculate the sum of the geometric series (P^0 + P^1 + ... + P^(N-1)) modulo M.
    # This sum (let's call it S_mod) is a key component in the formula for X.
    # Mathematically, S = (P^N - 1) / (P - 1). The `_sum_geometric_series_mod`
    # function computes this sum efficiently and correctly handles cases where
    # (P - 1) might not have a modular multiplicative inverse (e.g., when P % M = 1).
    S_mod = _sum_geometric_series_mod(P_mod_M, N, M)

    # The final result is derived from the formula X % M = (A % M * S_mod) % M.
    # We take A % M to keep intermediate calculations within modular bounds.
    return (A % M * S_mod) % M
```