```python
def translate_frog_speech(text):
    import re

    # Split into sentences while preserving the sentence-ending punctuation
    sentences = re.split(r'(\s+)', text)
    processed = []
    current_words = []

    for part in sentences:
        if not part.strip():
            if current_words:
                processed.append(' '.join(reversed(current_words)))
                current_words = []
            processed.append(part)
            continue

        # Check if the part ends with a sentence-ending punctuation
        match = re.fullmatch(r'(.+)([.!?])', part)
        if match:
            words = match.group(1).split()
            punctuation = match.group(2)
            reversed_part = ' '.join(reversed(words)) + punctuation
            if current_words:
                processed.append(' '.join(reversed(current_words)))
                current_words = []
            processed.append(reversed_part)
        else:
            current_words.extend(part.split())

    if current_words:
        processed.append(' '.join(reversed(current_words)))

    return ''.join(processed)
```