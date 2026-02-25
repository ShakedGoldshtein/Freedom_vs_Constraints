```python
def solve_marker_caps(test_cases):
    results = []
    for case in test_cases:
        N, a = case
        freq = {}
        for color in a:
            freq[color] = freq.get(color, 0) + 1

        max_freq = max(freq.values()) if freq else 0
        if max_freq > (N + 1) // 2:
            results.append("No")
            continue

        color_to_indices = {}
        for idx, color in enumerate(a):
            color_to_indices.setdefault(color, []).append(idx)

        cap_assignment = [0] * N
        used = [False] * N

        for color in color_to_indices:
            indices = color_to_indices[color]
            for i in indices:
                found = False
                for j in range(N):
                    if not used[j] and a[j] != a[i]:
                        cap_assignment[i] = a[j]
                        used[j] = True
                        found = True
                        break
                if not found:
                    break
            if not found:
                break

        if all(cap_assignment[i] != a[i] for i in range(N)):
            results.append(("Yes", cap_assignment))
        else:
            results.append("No")

    return results

def process_input(test_cases_data):
    test_cases = []
    idx = 0
    T = test_cases_data[idx]
    idx += 1
    for _ in range(T):
        N = test_cases_data[idx]
        idx += 1
        a = test_cases_data[idx]
        idx += 1
        test_cases.append((N, a))
    return test_cases

def format_output(results):
    output = []
    for result in results:
        if result == "No":
            output.append("No")
        else:
            yes, assignment = result
            output.append("Yes")
            output.append(' '.join(map(str, assignment)))
    return output

def solve(T, test_cases_data):
    test_cases = process_input(test_cases_data)
    results = solve_marker_caps(test_cases)
    return format_output(results)
```