```python
def optimize_calpas_program(n: int, commands: list[tuple[str, int]]) -> tuple[int, list[tuple[str, int]]]:
    """
    Optimizes a CALPAS program consisting of bitwise AND, OR, XOR operations.

    The optimized program will consist of at most 3 lines (one AND, one OR, one XOR)
    and will produce the same output as the original program for all arguments
    from 0 to 1023.

    The strategy is to determine the final state of the program for two "basis" inputs:
    0 (all bits are 0) and 1023 (all bits are 1 for 10 bits, 2^10 - 1).
    Let f(x) be the function performed by the program. We compute f(0) and f(1023).
    For each bit position i, let b0_i = (f(0) >> i) & 1 and b1_i = (f(1023) >> i) & 1.
    The optimized program uses a canonical form: ((x & A) | B) ^ C.
    The constants A, B, C are derived such that for each bit i, this form matches
    the behavior determined by (b0_i, b1_i).

    Args:
        n: The number of commands in the original program.
        commands: A list of tuples, where each tuple contains an operation character
                  ("&", "|", or "^") and an integer constant (0-1023).

    Returns:
        A tuple containing:
        - The integer k (0 <= k <= 3), the length of the optimized program.
        - A list of tuples, representing the optimized commands in the same format
          as the input.
    """
    # MAX_BIT_VAL represents 10 bits, all set to 1 (2^10 - 1)
    MAX_BIT_VAL = 1023

    # Track the outcome for an initial input of 0 and an initial input of MAX_BIT_VAL (all 1s)
    # val_if_input_0: what 0 becomes after all original operations
    # val_if_input_1023: what 1023 becomes after all original operations
    val_if_input_0 = 0
    val_if_input_1023 = MAX_BIT_VAL

    # Apply all original commands to both basis values
    for op_char, constant in commands:
        if op_char == '&':
            val_if_input_0 &= constant
            val_if_input_1023 &= constant
        elif op_char == '|':
            val_if_input_0 |= constant
            val_if_input_1023 |= constant
        elif op_char == '^':
            val_if_input_0 ^= constant
            val_if_input_1023 ^= constant
        # The problem constraints guarantee valid operators, so no 'else' branch is strictly needed.

    # Derive the constants for the optimized program of the form:
    # `((x & AND_CONST) | OR_CONST) ^ XOR_CONST`
    #
    # For each bit position 'i' (0 to 9):
    # Let b0_i be the i-th bit of val_if_input_0.
    # Let b1_i be the i-th bit of val_if_input_1023.
    #
    # The behavior for each bit x_i can be one of four types:
    # 1. (b0_i, b1_i) = (0,0): output for bit i is always 0.
    # 2. (b0_i, b1_i) = (0,1): output for bit i is x_i.
    # 3. (b0_i, b1_i) = (1,0): output for bit i is ~x_i (NOT x_i).
    # 4. (b0_i, b1_i) = (1,1): output for bit i is always 1.
    #
    # We construct A, B, C to achieve these specific bitwise behaviors:
    # A (AND_CONST): bit i is 0 only if (b0_i, b1_i) is (0,0). Otherwise, it's 1.
    #                This means A_i = 1 for cases 2, 3, 4, and A_i = 0 for case 1.
    # B (OR_CONST): bit i is 1 only if (b0_i, b1_i) is (1,1). Otherwise, it's 0.
    #                This means B_i = 1 for case 4, and B_i = 0 for cases 1, 2, 3.
    # C (XOR_CONST): bit i is 1 only if (b0_i, b1_i) is (1,0). Otherwise, it's 0.
    #                This means C_i = 1 for case 3, and C_i = 0 for cases 1, 2, 4.

    AND_CONST = 0  # Initialized to all zeros. Bits will be set to 1 if needed.
    OR_CONST = 0   # Initialized to all zeros. Bits will be set to 1 if needed.
    XOR_CONST = 0  # Initialized to all zeros. Bits will be set to 1 if needed.

    # Iterate through each of the 10 relevant bits (0 to 9)
    for i in range(10):
        # Extract the i-th bit of the final values for input 0 and 1023
        b0_i = (val_if_input_0 >> i) & 1
        b1_i = (val_if_input_1023 >> i) & 1

        # Determine the i-th bit of AND_CONST (A)
        # If (b0_i, b1_i) is (0,0), then A_i should be 0. Otherwise A_i should be 1.
        if not (b0_i == 0 and b1_i == 0):
            AND_CONST |= (1 << i)  # Set i-th bit of AND_CONST to 1

        # Determine the i-th bit of OR_CONST (B)
        # If (b0_i, b1_i) is (1,1), then B_i should be 1. Otherwise B_i should be 0.
        if b0_i == 1 and b1_i == 1:
            OR_CONST |= (1 << i)  # Set i-th bit of OR_CONST to 1

        # Determine the i-th bit of XOR_CONST (C)
        # If (b0_i, b1_i) is (1,0), then C_i should be 1. Otherwise C_i should be 0.
        if b0_i == 1 and b1_i == 0:
            XOR_CONST |= (1 << i)  # Set i-th bit of XOR_CONST to 1

    # Construct the list of optimized commands
    optimized_commands = []

    # Only add an operation if its constant is not the identity for that operation type
    # (i.e., not a no-op).
    if AND_CONST != MAX_BIT_VAL:  # Identity for AND is 1023 (all 1s)
        optimized_commands.append(("&", AND_CONST))
    if OR_CONST != 0:  # Identity for OR is 0 (all 0s)
        optimized_commands.append(("|", OR_CONST))
    if XOR_CONST != 0:  # Identity for XOR is 0 (all 0s)
        optimized_commands.append(("^", XOR_CONST))

    return len(optimized_commands), optimized_commands
```