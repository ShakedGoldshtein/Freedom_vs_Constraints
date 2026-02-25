```python
def multiply(num1: str, num2: str) -> str:
    """
    Multiplies two non-negative integers represented as strings and returns the result as a string.
    Implements the standard multiplication algorithm with O(n*m) time complexity and O(n+m) space.
    """
    if num1 == "0" or num2 == "0":
        return "0"

    # Reverse both numbers for easier digit-wise processing
    rev_num1 = num1[::-1]
    rev_num2 = num2[::-1]

    # Initialize result array with zeros (max possible length is len(num1) + len(num2))
    result = [0] * (len(num1) + len(num2))

    # Multiply each digit of num1 with each digit of num2
    for i in range(len(rev_num1)):
        for j in range(len(rev_num2)):
            digit1 = ord(rev_num1[i]) - ord('0')
            digit2 = ord(rev_num2[j]) - ord('0')
            product = digit1 * digit2

            # Add to the current position and handle carry-over
            total = product + result[i + j]
            result[i + j] = total % 10
            result[i + j + 1] += total // 10

    # Convert result array to string, skipping leading zeros
    # The result is in reverse order, so reverse it back
    result_str = []
    leading_zero = True
    for digit in reversed(result):
        if leading_zero and digit == 0:
            continue
        leading_zero = False
        result_str.append(str(digit))

    return ''.join(result_str) if result_str else "0"
```