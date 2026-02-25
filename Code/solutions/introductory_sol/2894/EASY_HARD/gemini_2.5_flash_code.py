```python
def triple_trouble(one, two, three):
    """
    Combines three input strings by grouping their letters.
    Takes the first letter of all inputs, then the second, and so on.

    Args:
        one (str): The first input string.
        two (str): The second input string.
        three (str): The third input string.

    Returns:
        str: The combined string.

    Example:
        triple_trouble("aa", "bb", "cc") == "abcabc"
    """
    return "".join(c1 + c2 + c3 for c1, c2, c3 in zip(one, two, three))
```