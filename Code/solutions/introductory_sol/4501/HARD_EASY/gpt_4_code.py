Here is the Python code for the problem:

```python
def inside_out_word(word):
    length = len(word)
    mid = length // 2
    if length % 2 == 0:
        first_half = ''.join(sorted(word[:mid], reverse=True))
        second_half = ''.join(sorted(word[mid:]))
        new_word = first_half + second_half
    else:
        first_half = ''.join(sorted(word[:mid], reverse=True))
        second_half = ''.join(sorted(word[mid+1:]))
        new_word = first_half + word[mid] + second_half
    return new_word


def inside_out_words_in_string(s):
    words_list = s.split(' ')
    transformed_words = [inside_out_word(word) for word in words_list]
    result_string = ' '.join(transformed_words)
    return result_string
```
The function `inside_out_words_in_string(s)` accepts a string as input and returns a string after transforming all the words in it as per the mentioned conditions. The function `inside_out_word(word)` is a helper function which takes a word as input and returns the transformed word as per the 'inside_out' rule.