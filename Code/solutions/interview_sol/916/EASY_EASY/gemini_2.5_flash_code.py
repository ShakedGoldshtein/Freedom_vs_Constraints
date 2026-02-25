```python
def gcd(a, b):
    """
    Calculates the Greatest Common Divisor (GCD) of two non-negative integers
    using the Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return a

def solve(N, M):
    """
    Calculates the minimum amount to be spent by Chef and Chefu.
    Chef has coins of denomination N, and Chefu has coins of denomination M.
    They want to purchase cakes of equal minimum price, which means the price
    must be a multiple of N and M. This is equivalent to finding the
    Least Common Multiple (LCM) of N and M.

    The relationship between LCM and GCD is:
    LCM(N, M) = (N * M) / GCD(N, M)
    """
    
    # Calculate the Greatest Common Divisor (GCD) of N and M.
    common_divisor = gcd(N, M)
    
    # Calculate the Least Common Multiple (LCM).
    # We use (N // common_divisor) * M to avoid potential overflow if N*M
    # were extremely large, though Python integers handle arbitrary precision.
    # It's generally a safer approach.
    lcm_value = (N // common_divisor) * M
    
    return lcm_value
```