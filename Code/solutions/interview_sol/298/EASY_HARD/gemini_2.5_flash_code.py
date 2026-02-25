```python
def multiply_strings(num1: str, num2: str) -> str:
    # Handle edge case: if either number is "0", the product is "0"
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    # The maximum length of the product can be m + n
    # Initialize a list of zeros for storing intermediate results
    result = [0] * (m + n)

    # Iterate from right to left for num1
    for i in range(m - 1, -1, -1):
        digit1 = int(num1[i])
        # Iterate from right to left for num2
        for j in range(n - 1, -1, -1):
            digit2 = int(num2[j])

            # Calculate the product of the two digits
            # Add to the current sum at the corresponding position
            # i + j + 1 is the current position for the units digit of this product
            # i + j is the position for the carry-over
            current_sum = digit1 * digit2 + result[i + j + 1]

            result[i + j + 1] = current_sum % 10  # Units digit
            result[i + j] += current_sum // 10    # Carry-over to the left position

    # Convert the result list to a string
    # Find the first non-zero digit to handle leading zeros
    # e.g., if result is [0, 0, 1, 2, 3], we want "123"
    first_digit_idx = 0
    while first_digit_idx < len(result) - 1 and result[first_digit_idx] == 0:
        first_digit_idx += 1

    # Join the digits from the first non-zero index to the end
    return "".join(map(str, result[first_digit_idx:]))

```