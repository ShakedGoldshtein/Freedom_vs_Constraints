```python
def inside_out(x):
    result = []
    for word in x.split():
        mid = len(word) // 2
        if len(word) % 2 == 0:
            result.append(word[mid-1::-1] + word[:mid-1:-1])
        else:
            result.append(word[mid-1::-1] + word[mid] + word[:mid:-1])
    return ' '.join(result)
```