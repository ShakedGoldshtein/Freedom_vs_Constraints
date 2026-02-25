```python
def remove(sentence: str) -> str:
    if not sentence:
        return sentence
    stripped = sentence.rstrip('!')
    return stripped + '!' * (len(sentence) - len(stripped))
```