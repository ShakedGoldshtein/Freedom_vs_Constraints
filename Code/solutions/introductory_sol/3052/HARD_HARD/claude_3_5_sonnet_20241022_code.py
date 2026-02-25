```python
def remove(s: str) -> str:
    if not s:
        return s
        
    # Count trailing exclamation marks
    end_marks = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != '!':
            break
        end_marks += 1
            
    # Remove all ! except trailing ones
    result = s[:-end_marks] if end_marks > 0 else s
    result = result.replace('!', '')
    
    # Add back trailing exclamation marks
    return result + '!' * end_marks
```