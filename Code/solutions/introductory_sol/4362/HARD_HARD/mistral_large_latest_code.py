```python
import re
from typing import List

def translate_frog_speech(text: str) -> str:
    """
    Translates a string from frog speech to normal English by reversing each sentence's words,
    preserving only the final punctuation (., !, ?) and removing other punctuation marks.

    Args:
        text: Input string in frog speech (lowercase, no apostrophes).

    Returns:
        Translated string with sentences reversed and punctuation normalized.
    """
    if not text.strip():
        return text

    sentences = _split_sentences(text)
    translated_sentences = [_translate_sentence(sentence) for sentence in sentences]
    return ' '.join(translated_sentences)

def _split_sentences(text: str) -> List[str]:
    """
    Splits the input text into sentences, preserving the sentence-ending punctuation.
    Sentences are split on one or more whitespace characters.
    """
    return re.split(r'\s+', text.strip())

def _translate_sentence(sentence: str) -> str:
    """
    Translates a single sentence by:
    1. Extracting and preserving the final punctuation (., !, ?)
    2. Removing all other punctuation marks
    3. Reversing the order of the remaining words
    4. Reattaching the preserved punctuation
    """
    if not sentence:
        return sentence

    punctuation = _extract_punctuation(sentence)
    words = _extract_and_clean_words(sentence, punctuation)

    if not words:
        return punctuation if punctuation else sentence

    reversed_words = ' '.join(reversed(words))
    return f"{reversed_words}{punctuation}" if punctuation else reversed_words

def _extract_punctuation(sentence: str) -> str:
    """
    Extracts the final punctuation mark (., !, ?) from a sentence if it exists.
    Returns an empty string if no valid punctuation is found.
    """
    last_char = sentence[-1]
    return last_char if last_char in {'.', '!', '?'} else ''

def _extract_and_clean_words(sentence: str, punctuation: str) -> List[str]:
    """
    Extracts words from a sentence, removing all punctuation marks except the preserved one.
    Returns a list of cleaned words (lowercase, no punctuation).
    """
    # Remove the preserved punctuation if it exists
    base_sentence = sentence[:-1] if punctuation else sentence

    # Remove all other punctuation marks and split into words
    words = re.findall(r"[^\s,;()\-]+", base_sentence)
    return [word for word in words if word]
```