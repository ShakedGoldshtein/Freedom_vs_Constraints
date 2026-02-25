```python
def triple_trouble(str1, str2, str3):
    try:
        return ''.join(a + b + c for a, b, c in zip(str1, str2, str3))
    except TypeError:
        return "TypeError: All input parameters should be of string type."
    except Exception as e:
        return str(e)
```