```python
def press_button_times(n):
    result = []
    current_number = 2
    for level in range(1, n+1):
        next_number = (level + 1)**2
        plus_presses = (next_number - current_number) // level
        result.append(plus_presses)
        current_number = next_number
    return result

print(press_button_times(3))    # example usage
```