```python
def add_numbers(T, pairs):
    # Validate constraints
    if T < 1 or T > 1000:
        raise ValueError("T must be between 1 and 1000.")
    if not all(0 <= pair[0] <= 10000 and 0 <= pair[1] <= 10000 for pair in pairs):
        raise ValueError("A and B must be between 0 and 10000.")

    # Loop through pair list and do the sum
    return [sum(pair) for pair in pairs]
```