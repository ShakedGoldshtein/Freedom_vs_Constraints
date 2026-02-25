```python
def count_good_substrings(queries):
    """
    Counts the number of good substrings for each binary string query.
    A substring is good if its length equals its decimal value when interpreted as binary.

    Args:
        queries: List of binary strings to process.

    Returns:
        List of integers representing the count of good substrings for each query.
    """
    def process_single_query(s):
        n = len(s)
        count = 0
        for i in range(n):
            current_value = 0
            for j in range(i, n):
                current_value = (current_value << 1) | (1 if s[j] == '1' else 0)
                length = j - i + 1
                if current_value == length:
                    count += 1
        return count

    return [process_single_query(s) for s in queries]
```