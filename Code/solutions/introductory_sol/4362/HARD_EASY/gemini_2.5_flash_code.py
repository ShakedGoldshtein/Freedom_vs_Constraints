```python
import re

def _translate_single_sentence(sentence_text: str) -> str:
    """
    Translates a single frog speech sentence by reversing its words
    and handling specific punctuation rules.

    Args:
        sentence_text: The input sentence string, which may include a final
                       punctuation mark and internal punctuation to be removed.

    Returns:
        The translated sentence string.
    """
    if not sentence_text:
        return ""

    # 1. Identify and store the final punctuation (if any)
    # The problem specifies sentences end with one of '.', '!', or '?'.
    # We remove it for word processing and re-add it at the end.
    final_punctuation = ''
    if sentence_text and sentence_text[-1] in ".!?":
        final_punctuation = sentence_text[-1]
        sentence_text = sentence_text[:-1]

    # 2. Remove other specified punctuation: `, ; ( ) - `
    # Using str.maketrans and str.translate is efficient for multiple character deletion.
    punctuation_to_remove = ",;()-"
    translator = str.maketrans("", "", punctuation_to_remove)
    cleaned_text = sentence_text.translate(translator)

    # 3. Split into words.
    # str.split() without arguments handles arbitrary whitespace between words
    # and removes empty strings from the resulting list (e.g., "  a  b  ".split() -> ['a', 'b']).
    words = cleaned_text.split()

    # 4. Reverse the order of words
    words.reverse()

    # 5. Join the reversed words with a single space and re-add the final punctuation
    return " ".join(words) + final_punctuation


def translate_frog_speech(frog_speech: str) -> str:
    """
    Translates frog speech, which involves reversing words in each sentence
    and handling specific punctuation rules, across multiple sentences.

    Sentences are separated by arbitrary amounts of spaces. Each sentence
    ends with one of '.', '!', or '?'. Other punctuation (`, ; ( ) - `)
    is omitted. All input is assumed to be lowercase and apostrophes are forbidden.

    Args:
        frog_speech: A string containing one or more sentences in frog speech.

    Returns:
        A string with the translated sentences, joined by single spaces.
    """
    # Handle empty or all-whitespace input strings immediately
    if not frog_speech.strip():
        return ""

    # Use regex to split the input string by sentence-ending punctuation.
    # The pattern r'([.!?])' captures the punctuation, so it's included in the resulting list.
    # Example: "s1. s2?" -> ['s1', '.', ' s2', '?', '']
    parts = re.split(r'([.!?])', frog_speech)

    translated_sentences = []
    # Iterate through the parts, treating them as pairs of (sentence_content, punctuation).
    # The loop processes two elements at a time. The last element might be an empty string
    # if the input ends with punctuation, which is naturally handled by the range.
    for i in range(0, len(parts), 2):
        sentence_content = parts[i]
        # Get the corresponding final punctuation; if no punctuation follows (e.g., last segment), it's empty.
        final_punctuation = parts[i+1] if (i + 1) < len(parts) else ''

        # Strip leading/trailing whitespace from the content part. This is crucial
        # for handling arbitrary spaces *between* sentences (e.g., "good.   is not").
        processed_content = sentence_content.strip()

        # Only process if there's actual content or a final punctuation. This avoids
        # processing empty strings that result from `re.split` (e.g., from " . " or a trailing empty part).
        if processed_content or final_punctuation:
            full_sentence_for_translation = processed_content + final_punctuation
            translated_sentences.append(_translate_single_sentence(full_sentence_for_translation))

    # Join the translated sentences with a single space.
    # Example outputs imply a single space between translated sentences regardless
    # of the number of spaces in the original input.
    return " ".join(translated_sentences)
```