```python
def solve(text):
    if not text:
        return ""
        
    words = text.split()
    result = ""
    
    for word in words:
        if word:
            result += word[0]
            
    return result
```