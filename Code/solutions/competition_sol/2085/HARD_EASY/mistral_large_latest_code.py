```python
def solve(n, initial_strings, m, operations):
    strings = initial_strings.copy()
    results = []

    for a, b in operations:
        a_idx, b_idx = a - 1, b - 1
        new_str = strings[a_idx] + strings[b_idx]
        strings.append(new_str)
        max_k = compute_max_k(new_str)
        results.append(max_k)

    return results

def compute_max_k(s):
    max_possible_k = 0
    n = len(s)
    if n == 0:
        return 0

    for k in range(1, n + 1):
        if all_binary_strings_present(s, k):
            max_possible_k = k
        else:
            break
    return max_possible_k

def all_binary_strings_present(s, k):
    required = 1 << k
    seen = set()

    for i in range(len(s) - k + 1):
        substring = s[i:i+k]
        if substring not in seen:
            seen.add(substring)
            if len(seen) == required:
                return True
    return len(seen) == required
```