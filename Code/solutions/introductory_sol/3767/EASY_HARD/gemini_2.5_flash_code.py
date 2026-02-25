```python
DIGIT_MAP = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGIT_VALUES = {char: i for i, char in enumerate(DIGIT_MAP)}

# Pre-calculate factorials up to a sufficient limit for conversion.
# The maximum possible string length for a base-36 digit system in factorial
# representation would mean the highest coefficient corresponds to 35!.
# So we precompute up to 35!.
MAX_FACTORIAL_IDX = len(DIGIT_MAP) # 36, means 0! to 35!
PRECOMPUTED_FACTORIALS = [1] # 0!
for i in range(1, MAX_FACTORIAL_IDX):
    PRECOMPUTED_FACTORIALS.append(PRECOMPUTED_FACTORIALS[-1] * i)


def dec_to_fact_string(decimal_num: int) -> str:
    """
    Converts a decimal number to its factorial representation string.
    
    Args:
        decimal_num: A positive integer (decimal number).
                     Handles 0 by returning "0".

    Returns:
        A string representing the factorial number.
    """
    if decimal_num == 0:
        return "0"

    # Determine the largest factorial needed.
    # We find 'k' such that k! <= decimal_num < (k+1)!.
    # Then we will generate coefficients for k!, (k-1)!, ..., 0!.
    
    # facts will store [0!, 1!, ..., k!] where k! is the largest factorial <= decimal_num
    # and (k+1)! > decimal_num.
    facts = [1] # 0!
    i = 1
    while True:
        # Calculate next factorial (i!)
        # Use try-except for OverflowError if Python had fixed-size ints
        # Python handles large integers automatically, so overflow is less of a concern
        # unless number exceeds available memory.
        next_fact_val = facts[-1] * i
        if next_fact_val > decimal_num:
            # We found the first factorial (i!) that is greater than decimal_num.
            # So, the largest factorial we can use for division is (i-1)!.
            # The `facts` list already contains factorials up to (i-1)!.
            break
        facts.append(next_fact_val)
        i += 1
    
    result = []
    remainder = decimal_num
    
    # Iterate from the highest relevant factorial down to 0!.
    # The `facts` list has elements from 0! to (i-1)!.
    # So we loop from `len(facts) - 1` down to `0`.
    for fact_idx in range(len(facts) - 1, -1, -1):
        current_fact = facts[fact_idx]
        coefficient = remainder // current_fact
        result.append(DIGIT_MAP[coefficient])
        remainder %= current_fact
        
    return "".join(result)


def fact_string_to_dec(fact_string: str) -> int:
    """
    Converts a factorial representation string to a decimal number.

    Args:
        fact_string: A string representing the factorial number.
                     Digits '0'-'9' and 'A'-'Z' are supported.

    Returns:
        The decimal representation as an integer.
    """
    decimal_num = 0
    L = len(fact_string)

    # The factorial string "c_n c_{n-1} ... c_1 c_0" has length L.
    # The digit at index j (0-indexed from left) corresponds to the (L - 1 - j)! position.
    for j in range(L):
        char = fact_string[j]
        coefficient = DIGIT_VALUES[char]
        
        # The factorial power for the current digit.
        fact_power = L - 1 - j
        
        # Multiply the coefficient by the corresponding factorial value
        # and add to the total decimal number.
        # PRECOMPUTED_FACTORIALS[fact_power] gives (fact_power)!.
        decimal_num += coefficient * PRECOMPUTED_FACTORIALS[fact_power]
            
    return decimal_num

```