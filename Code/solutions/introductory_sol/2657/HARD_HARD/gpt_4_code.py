```python
def acronym_generator(input_string):
    try:
        if not isinstance(input_string, str):
            raise ValueError("Please provide a valid string")
        words = input_string.split()
        acronym = ''.join(word[0] for word in words if word)
        return acronym
    except Exception as error:
        return str(error)
```