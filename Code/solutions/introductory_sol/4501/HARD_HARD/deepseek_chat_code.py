```python
def inside_out(words):
    """
    Process a string of words by turning each word 'inside out'.
    
    For each word:
    - Even length: reverse both halves
    - Odd length: reverse both halves, keeping middle character in place
    
    Args:
        words: String containing space-separated words
        
    Returns:
        String with each word processed according to inside-out rules
    """
    if not words:
        return ""
    
    def process_word(word):
        if not word:
            return ""
        
        n = len(word)
        mid = n // 2
        
        if n % 2 == 0:
            # Even length: reverse first half and second half
            return word[:mid][::-1] + word[mid:][::-1]
        else:
            # Odd length: reverse first half, keep middle, reverse second half
            return word[:mid][::-1] + word[mid] + word[mid+1:][::-1]
    
    word_list = words.split(' ')
    processed_words = [process_word(word) for word in word_list]
    
    return ' '.join(processed_words)
```