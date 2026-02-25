```python
def solve(s: str, t: str) -> str:
    """
    Determines the optimal company name based on the letters Oleg and Igor have.

    Args:
        s (str): A string representing the set of letters Oleg has.
        t (str): A string representing the set of letters Igor has.

    Returns:
        str: The optimal company name as a string of lowercase English letters.
    """
    n = len(s)
    # Convert strings to sorted lists for easier manipulation
    oleg_letters = sorted(s)
    igor_letters = sorted(t, reverse=True)

    # Initialize the result list with placeholders
    result = [""] * n
    # Initialize pointers for Oleg's and Igor's letters
    oleg_ptr = 0
    igor_ptr = 0
    # Initialize turn counter (0 for Oleg, 1 for Igor)
    turn = 0

    # Iterate over the positions in the result string
    for i in range(n):
        if turn == 0:
            # Oleg's turn: choose the smallest available letter
            result[i] = oleg_letters[oleg_ptr]
            oleg_ptr += 1
        else:
            # Igor's turn: choose the largest available letter
            result[i] = igor_letters[igor_ptr]
            igor_ptr += 1
        # Switch turns
        turn = 1 - turn

    return "".join(result)
```