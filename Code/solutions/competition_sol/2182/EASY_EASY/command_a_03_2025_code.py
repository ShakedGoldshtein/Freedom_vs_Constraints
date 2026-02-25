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
    # Sort both strings to facilitate optimal selection of letters
    s_sorted = sorted(s)
    t_sorted = sorted(t, reverse=True)

    # Initialize result list with question marks
    result: list[str] = [""] * n
    oleg_turns: list[int] = list(range(0, n, 2))  # Oleg's turns: 0, 2, 4, ...
    igor_turns: list[int] = list(range(1, n, 2))  # Igor's turns: 1, 3, 5, ...

    # Assign letters to positions based on turns
    for i in range(n):
        if i % 2 == 0:
            # Oleg's turn: assign the smallest available letter
            result[oleg_turns[i // 2]] = s_sorted.pop(0)
        else:
            # Igor's turn: assign the largest available letter
            result[igor_turns[(i - 1) // 2]] = t_sorted.pop(0)

    return "".join(result)
```