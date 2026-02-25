```python
def triple_trouble(one: str, two: str, three: str) -> str:
    """
    Combines the letters of three input strings in groups, taking the first letter
    of each string, then the second, and so on, until all letters are grouped.

    Args:
        one (str): The first input string.
        two (str): The second input string.
        three (str): The third input string.

    Returns:
        str: A string with letters grouped from the three input strings.
    """
    result = []
    for i in range(len(one)):
        result.append(one[i])
        result.append(two[i])
        result.append(three[i])
    return ''.join(result)
```