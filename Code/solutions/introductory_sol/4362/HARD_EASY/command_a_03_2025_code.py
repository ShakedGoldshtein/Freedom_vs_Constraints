```python
import re

def translate_frog_speech(text: str) -> str:
    """
    Translates frog speech into proper English.

    Args:
        text (str): The input text in frog speech.

    Returns:
        str: The translated text in proper English.
    """
    # Define punctuation to keep at the end of sentences
    end_punctuation = {'.', '!', '?'}
    
    # Split text into sentences based on multiple spaces and end punctuation
    sentences = re.split(r'(?:\s+(?=[.!?]))', text)
    
    translated_sentences = []
    sentence_buffer = []
    
    for part in sentences:
        if part.strip() == '':
            continue
        if part[-1] in end_punctuation:
            # Add the last word to the buffer and translate the sentence
            sentence_buffer.append(part.rstrip(end_punctuation))
            translated = ' '.join(reversed(sentence_buffer)) + part[-1]
            translated_sentences.append(translated)
            sentence_buffer = []
        else:
            # Remove punctuation and add words to the buffer
            cleaned_part = re.sub(r'[,;()-]', '', part)
            sentence_buffer.extend(cleaned_part.split())
    
    return ' '.join(translated_sentences)
```