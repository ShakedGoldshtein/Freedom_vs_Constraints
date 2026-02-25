```python
def multiply_strings(num1: str, num2: str) -> str:
    """
    Multiplies two non-negative integers represented as strings and returns their product
    as a string.

    This function implements string multiplication similar to the long multiplication
    method taught in arithmetic, without using built-in BigInteger libraries or
    converting inputs to integers directly.

    Args:
        num1: The first non-negative integer as a string.
        num2: The second non-negative integer as a string.
              Both strings contain only digits '0'-'9', do not have leading zeros
              (except for the number "0" itself), and have a length less than 110.

    Returns:
        The product of num1 and num2 as a string.
    """
    # Handle the edge case where one or both numbers are "0".
    # The product will always be "0" in such scenarios.
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    # The maximum possible length of the product of two numbers with lengths m and n
    # is m + n. Initialize a list of zeros to store intermediate sums and carries.
    # result[k] will store the digit for the k-th place value (from right).
    # Specifically, result[i + j + 1] will store the units digit of (digit1 * digit2)
    # plus any carry from the right, and result[i + j] will store the carry to the left.
    result = [0] * (m + n)

    # Iterate through num1 from right to left (least significant digit first).
    for i in range(m - 1, -1, -1):
        digit1 = int(num1[i])

        # Iterate through num2 from right to left.
        for j in range(n - 1, -1, -1):
            digit2 = int(num2[j])

            # Calculate the product of the current digits (digit1 * digit2).
            # Add this product to the current value at result[i + j + 1],
            # which represents the current place value for their combined product.
            current_sum = (digit1 * digit2) + result[i + j + 1]

            # The units digit of `current_sum` goes into result[i + j + 1].
            result[i + j + 1] = current_sum % 10
            # The carry (tens digit of `current_sum`) is added to the next
            # higher place value, result[i + j].
            result[i + j] += current_sum // 10

    # Convert the list of integers representing digits into a single string.
    # Find the first non-zero digit to eliminate any leading zeros.
    first_digit_index = 0
    # Keep advancing `first_digit_index` as long as it points to a zero AND
    # it's not the very last digit (e.g., to handle "0" itself if it somehow
    # bypassed the initial check, although that won't happen here).
    while first_digit_index < len(result) - 1 and result[first_digit_index] == 0:
        first_digit_index += 1

    # Join the digits from the first non-zero digit onwards to form the final product string.
    return "".join(map(str, result[first_digit_index:]))
```