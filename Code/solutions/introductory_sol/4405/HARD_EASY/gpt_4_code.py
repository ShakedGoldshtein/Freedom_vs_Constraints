```python
def is_palindrome(input_str):
    """
    Function to make sure if the given input is a palindrome or not
    """
    # check if the input is not of type str, convert it
    if not isinstance(input_str, str):
        input_str = str(input_str)
    # Comparison of original string with the reverse of it.
    return input_str == input_str[::-1]

```