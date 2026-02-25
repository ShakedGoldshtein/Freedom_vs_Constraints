```python
def solve(x: str) -> str:
    words = x.split()
    transformed_words = []

    for word in words:
        if not word:
            transformed_words.append("")
            continue

        char_list = list(word)
        n = len(char_list)

        mid_idx = -1
        if n % 2 != 0:
            mid_idx = n // 2

        for i in range(0, n - 1, 2):
            # Check if either current index 'i' or the next index 'i + 1'
            # corresponds to the middle character of an odd-length word.
            # If so, skip the swap for this pair to leave the middle character in place.
            if i == mid_idx or (i + 1) == mid_idx:
                continue
            else:
                # Perform an in-place swap of characters
                char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
        
        transformed_words.append("".join(char_list))
    
    return " ".join(transformed_words)
```