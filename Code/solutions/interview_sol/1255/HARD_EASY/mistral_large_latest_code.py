```python
def solve(test_cases):
    results = []
    for case in test_cases:
        s, k = case
        n = len(s)
        s_chars = set(s)
        available = [c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in s_chars]
        available.sort()

        if n == 26:
            results.append("NOPE")
            continue

        max_shared = min(k, n)
        min_shared = max(0, n - len(available))

        if max_shared < min_shared:
            results.append("NOPE")
            continue

        shared = min(max_shared, min_shared)
        needed = n - shared

        if needed > len(available):
            results.append("NOPE")
            continue

        t_chars = []
        s_sorted = sorted(s)
        available_ptr = 0

        for c in s_sorted:
            if shared > 0:
                t_chars.append(c)
                shared -= 1
            else:
                if available_ptr < len(available):
                    t_chars.append(available[available_ptr])
                    available_ptr += 1
                else:
                    break

        while len(t_chars) < n:
            if available_ptr < len(available):
                t_chars.append(available[available_ptr])
                available_ptr += 1
            else:
                break

        if len(t_chars) == n:
            candidate = ''.join(t_chars)
            actual_shared = len(set(candidate) & s_chars)
            if actual_shared <= k:
                results.append(candidate)
                continue

        shared = min(k, n)
        t_chars = []
        s_sorted = sorted(s)
        available_ptr = 0

        for i in range(n):
            if i < shared:
                t_chars.append(s_sorted[i])
            else:
                if available_ptr < len(available):
                    t_chars.append(available[available_ptr])
                    available_ptr += 1
                else:
                    break

        if len(t_chars) == n:
            candidate = ''.join(t_chars)
            actual_shared = len(set(candidate) & s_chars)
            if actual_shared <= k:
                results.append(candidate)
            else:
                results.append("NOPE")
        else:
            results.append("NOPE")

    return results

def process_input(input_data):
    T = input_data[0]
    test_cases = []
    for line in input_data[1:T+1]:
        parts = line.split()
        s = parts[0]
        k = int(parts[1])
        test_cases.append((s, k))
    return solve(test_cases)
```