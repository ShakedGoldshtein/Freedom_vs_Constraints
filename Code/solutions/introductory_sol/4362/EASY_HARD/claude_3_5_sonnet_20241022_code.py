```python
def solve(text):
    # Split into sentences
    sentences = text.lower().split('.')
    sentences = [s.split('!') for s in sentences]
    sentences = [item for sublist in sentences for item in sublist]
    sentences = [s.split('?') for s in sentences]
    sentences = [item for sublist in sentences for item in sublist if item.strip()]
    
    result = []
    punctuation = "`,;()-"
    
    # Process each sentence
    for i, sentence in enumerate(sentences):
        # Get ending punctuation from original text
        if i < len(sentences)-1 or text[-1] not in '.!?':
            end = '.'
        else:
            end = text[-1]
            
        # Clean and reverse words
        words = sentence.translate(str.maketrans('', '', punctuation)).strip().split()
        words.reverse()
        
        result.append(' '.join(words) + end)
        
    return ' '.join(result)
```