```python
def capitalize_name(full_name):
    return ' '.join(word.capitalize() for word in full_name.split())
```