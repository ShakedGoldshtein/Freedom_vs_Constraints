```python
def solve(test_cases):
    results = []
    for case in test_cases:
        s, k = case
        n = len(s)
        s_set = set(s)
        available = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in s_set]
        required_diff = n - k
        if required_diff <= 0:
            if k >= n:
                results.append("NOPE")
            else:
                results.append("NOPE")
            continue
        if len(available) < required_diff:
            results.append("NOPE")
            continue
        t_list = []
        available_sorted = sorted(available)
        diff_chars = available_sorted[:required_diff]
        remaining_needed = n - required_diff
        common_chars = []
        s_sorted = sorted(s)
        for c in s_sorted:
            if c in available:
                continue
            if remaining_needed > 0:
                common_chars.append(c)
                remaining_needed -= 1
        t_list = diff_chars + common_chars
        t_list_sorted = sorted(t_list)
        t = ''.join(t_list_sorted)
        if F(s, t) > k:
            results.append("NOPE")
        else:
            results.append(t)
    return results

def F(s, t):
    s_set = set(s)
    t_set = set(t)
    return len(s_set & t_set)

def solve_test_cases(T, cases):
    test_cases = []
    for case in cases:
        parts = case.split()
        s = parts[0]
        k = int(parts[1])
        test_cases.append((s, k))
    return solve(test_cases)
```