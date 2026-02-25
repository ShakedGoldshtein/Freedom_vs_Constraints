```python
def hamming_distance(a, b):
    """
    Compute Hamming distance between two binary strings
    """
    try:
        if len(a) != len(b):
            raise ValueError("The lengths of both strings should be equal")
        return sum(el1 != el2 for el1, el2 in zip(a, b))
    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return None
```