```python
def translate_frog_speak(text):
    # Strip punctuation except .!?
    exclude = '`,;()-'
    text = ''.join(c for c in text.lower() if c not in exclude)
    
    # Split into sentences based on .!?
    sentences = []
    current = []
    i = 0
    while i < len(text):
        if text[i] in '.!?':
            current.append(text[i])
            sentences.append(''.join(current).strip())
            current = []
        else:
            current.append(text[i])
        i += 1
    if current:
        sentences.append(''.join(current).strip())
    
    # Process each sentence
    result = []
    for sentence in sentences:
        # Extract ending punctuation if present
        ending = ''
        if sentence and sentence[-1] in '.!?':
            ending = sentence[-1]
            sentence = sentence[:-1]
            
        # Split into words and reverse
        words = [w for w in sentence.split() if w]
        words.reverse()
        
        # Join with spaces and add ending
        if words:
            result.append(' '.join(words) + ending)
    
    # Join sentences with spaces
    return ' '.join(result)
```