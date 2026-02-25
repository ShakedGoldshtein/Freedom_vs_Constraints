```python
def translate(text):
    final_punctuations = {'.', '!', '?'}
    omitted_punctuations = {',', ';', '(', ')', '-'}

    result_sentences = []
    current_sentence_start = 0

    def extract_words(segment_text, omitted_punct_set):
        words = []
        current_word_chars = []
        for char in segment_text:
            if char.isspace():
                if current_word_chars:
                    words.append("".join(current_word_chars))
                    current_word_chars = []
            elif char not in omitted_punct_set:
                current_word_chars.append(char)
            # If char is in omitted_punct_set, it's skipped.
        if current_word_chars:
            words.append("".join(current_word_chars))
        return words

    for i, char in enumerate(text):
        if char in final_punctuations:
            # Extract the segment of text before the final punctuation, stripping surrounding spaces
            sentence_segment = text[current_sentence_start : i].strip()
            final_punct = char

            # Process this sentence segment
            cleaned_words = extract_words(sentence_segment, omitted_punctuations)
            
            reversed_words = cleaned_words[::-1]
            processed_sentence = " ".join(reversed_words) + final_punct
            result_sentences.append(processed_sentence)

            # Advance current_sentence_start to the character after the final punctuation,
            # skipping any intervening spaces.
            current_sentence_start = i + 1
            while current_sentence_start < len(text) and text[current_sentence_start].isspace():
                current_sentence_start += 1
    
    # Join all processed sentences with a single space as per example output
    return " ".join(result_sentences)
```