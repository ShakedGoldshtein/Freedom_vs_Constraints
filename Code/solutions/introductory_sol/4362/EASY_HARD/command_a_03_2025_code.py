```python
import re


def solve(text: str) -> str:
    """
    Translates the given text from the frog's language to standard English.

    Args:
        text (str): The input text in the frog's language.

    Returns:
        str: The translated text in standard English.
    """
    # Split the text into sentences based on punctuation marks
    sentences = re.split(r"(?<=[.!?])\s*", text)

    # Process each sentence
    translated_sentences = []
    for sentence in sentences:
        if sentence:  # Skip empty strings
            # Remove punctuation marks except the last one
            clean_sentence = re.sub(r"[^\w\s.!?]", "", sentence)
            # Split into words, reverse the order, and join back into a sentence
            words = clean_sentence.split()
            reversed_sentence = " ".join(reversed(words))
            # Ensure the last punctuation mark is preserved
            last_punctuation = clean_sentence[-1] if clean_sentence else ""
            translated_sentences.append(reversed_sentence.rstrip() + last_punctuation)

    # Join the translated sentences back into a single string
    return " ".join(translated_sentences)
```