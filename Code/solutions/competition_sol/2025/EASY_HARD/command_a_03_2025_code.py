```python
def solve(n: int) -> list[int]:
    """
    Returns the minimum number of questions Petya should ask to guarantee guessing Vasya's number,
    along with the sequence of questions (divisors) to ask.

    Args:
        n (int): The upper limit of the range of numbers Vasya could have thought of (1 ≤ n ≤ 10^3).

    Returns:
        list[int]: A list where the first element is the number of questions (k), followed by k divisors (y_i).
    """
    # Initialize the list of prime numbers up to n
    primes: list[int] = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    # The minimum number of questions is the number of primes less than or equal to n
    k: int = len(primes)

    # The questions are the prime numbers themselves
    return [k] + primes
```