```python
def get_first_letters(s: str) -> str:
    return ''.join(word[0] for word in s.split() if word)
```