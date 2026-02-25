```python
def solve(n, strings, m, operations):
    current_strings = strings.copy()
    result = []
    for a, b in operations:
        s_a = current_strings[a - 1]
        s_b = current_strings[b - 1]
        new_str = s_a + s_b
        current_strings.append(new_str)
        max_k = 0
        for k in range(1, len(new_str) + 1):
            all_substrings = set()
            for i in range(len(new_str) - k + 1):
                substring = new_str[i:i+k]
                all_substrings.add(substring)
            if len(all_substrings) == 2 ** k:
                max_k = k
            else:
                break
        result.append(max_k)
    return result
```