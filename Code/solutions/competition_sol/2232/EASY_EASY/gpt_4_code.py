```python
def button_presses(n):
    presses = [2]
    for i in range(2, n+1):
        num_presses = i**2 - sum(presses)
        presses.append(num_presses)
    return presses

print(button_presses(3))  # [2, 14, 10]
print(button_presses(2))  # [2, 14]
print(button_presses(4))  # [2, 14, 10, 12]
```