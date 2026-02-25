```python
def triple_trouble(one: str, two: str, three: str) -> str:
    """
    Combines three input strings by grouping their characters sequentially.

    Takes the first character of each string, then the second character of each,
    and so on, until all characters are processed.
    All input strings are expected to be of the same length.

    Args:
        one: The first input string.
        two: The second input string.
        three: The third input string.

    Returns:
        A new string combining the characters from the three input strings
        in groups.

    Examples:
        triple_trouble("aa", "bb", "cc") == "abcabc"
        triple_trouble("a", "b", "c") == "abc"
        triple_trouble("", "", "") == ""
    """
    
    # Since all input strings are guaranteed to be of the same length,
    # we can use the length of any one of them for iteration.
    num_chars = len(one)
    
    # Use a list to collect characters, as appending to a list and then
    # joining is generally more efficient for building strings in Python
    # than repeated string concatenation with the '+' operator.
    result_chars = []
    
    # Iterate through the characters by index
    for i in range(num_chars):
        # Append the character from each string at the current index
        result_chars.append(one[i])
        result_chars.append(two[i])
        result_chars.append(three[i])
        
    # Join all collected characters to form the final combined string.
    return "".join(result_chars)
```