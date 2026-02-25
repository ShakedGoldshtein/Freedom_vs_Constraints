```python
def inside_out(x):
    words = x.split()
    result = []
    for word in words:
        n = len(word)
        if n <= 2:
            result.append(word)
        elif n % 2 == 0:
            mid = n // 2
            reversed_left = word[:mid][::-1]
            reversed_right = word[mid:][::-1]
            result.append(reversed_left + reversed_right)
        else:
            mid = n // 2
            reversed_left = word[:mid][::-1]
            reversed_right = word[mid+1:][::-1]
            result.append(reversed_left + word[mid] + reversed_right)
    return ' '.join(result)
```