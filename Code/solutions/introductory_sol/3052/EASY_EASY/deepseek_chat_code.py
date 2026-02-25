```python
def remove(s):
    count = 0
    for char in reversed(s):
        if char == '!':
            count += 1
        else:
            break
    return s.replace('!', '') + '!' * count
```