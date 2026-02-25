```python
def triple_trouble(first, second, third):
    """
    Combines three strings by grouping letters at each position together.
    All input strings have same length.
    Returns combined string.
    """
    result = []
    for i in range(len(first)):
        result.extend([first[i], second[i], third[i]])
    return ''.join(result)
```