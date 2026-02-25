```python
def translate(text):
    sentences = []
    current = []
    word = []
    for char in text:
        if char.isalpha():
            word.append(char)
        elif char in '.!?':
            if word:
                current.append(''.join(word))
                word = []
            if current:
                current.reverse()
                sentences.append(''.join(current) + char)
                current = []
        else:
            if word:
                current.append(''.join(word))
                word = []
            if char == ' ' and current:
                current.append(' ')
    
    if word:
        current.append(''.join(word))
    if current:
        current.reverse()
        sentences.append(''.join(current))
    
    return ' '.join(sentences)
```