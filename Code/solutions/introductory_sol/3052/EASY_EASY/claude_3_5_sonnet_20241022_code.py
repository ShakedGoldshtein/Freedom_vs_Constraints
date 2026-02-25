```python
def remove(s):
    end = ""
    while s and s[-1] == "!":
        end = "!" + end
        s = s[:-1]
    return s.replace("!", "") + end
```