```python
def translate_frog_speech(text):
    """
    Translates the frog's speech by reversing sentences while preserving final punctuation.
    
    Args:
        text (str): Input text containing one or more sentences
        
    Returns:
        str: Translated text with reversed sentences and preserved final punctuation
    """
    if not text:
        return ""
    
    # Define punctuation to remove (excluding sentence terminators)
    PUNCTUATION_TO_REMOVE = {',', ';', '(', ')', '-'}
    SENTENCE_TERMINATORS = {'.', '!', '?'}
    
    sentences = []
    current_sentence = []
    current_chars = []
    
    i = 0
    n = len(text)
    
    while i < n:
        char = text[i]
        
        if char in SENTENCE_TERMINATORS:
            # Found sentence terminator
            if current_chars:
                current_sentence.append(''.join(current_chars))
                current_chars = []
            
            if current_sentence:
                # Reverse the words and add the terminator
                reversed_sentence = ' '.join(reversed(current_sentence))
                sentences.append(reversed_sentence + char)
                current_sentence = []
            i += 1
            
        elif char.isspace():
            # Handle spaces - if we have accumulated characters, add as word
            if current_chars:
                current_sentence.append(''.join(current_chars))
                current_chars = []
            i += 1
            
        elif char in PUNCTUATION_TO_REMOVE:
            # Skip punctuation marks to remove
            i += 1
            
        else:
            # Regular character, add to current word
            current_chars.append(char)
            i += 1
    
    # Handle any remaining text without sentence terminator
    if current_chars:
        current_sentence.append(''.join(current_chars))
    
    if current_sentence:
        sentences.append(' '.join(reversed(current_sentence)))
    
    return ' '.join(sentences)
```