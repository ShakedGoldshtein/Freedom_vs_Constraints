```python
def solve_caps_rearrangement(test_cases):
    results = []
    for case in test_cases:
        N, a = case
        freq = {}
        for color in a:
            freq[color] = freq.get(color, 0) + 1

        possible = True
        for color, count in freq.items():
            if count > (N + 1) // 2:
                possible = False
                break

        if not possible:
            results.append("No")
            continue

        from collections import defaultdict
        color_indices = defaultdict(list)
        for idx, color in enumerate(a):
            color_indices[color].append(idx)

        rearrangement = [0] * N
        for color in color_indices:
            indices = color_indices[color]
            other_colors = [c for c in freq if c != color]
            if not other_colors:
                possible = False
                break
            for i in range(len(indices)):
                if i < len(other_colors):
                    chosen_color = other_colors[i % len(other_colors)]
                    rearrangement[indices[i]] = chosen_color
                else:
                    chosen_color = other_colors[i % len(other_colors)]
                    rearrangement[indices[i]] = chosen_color

        if not possible:
            results.append("No")
        else:
            for i in range(N):
                if rearrangement[i] == a[i]:
                    for c in freq:
                        if c != a[i]:
                            rearrangement[i] = c
                            break
            results.append(("Yes", rearrangement))

    output = []
    for res in results:
        if res == "No":
            output.append("No")
        else:
            yes, arr = res
            output.append("Yes")
            output.append(' '.join(map(str, arr)))
    return '\n'.join(output)

def solve(T, cases):
    test_cases = []
    for case in cases:
        N, a = case
        test_cases.append((N, a))
    return solve_caps_rearrangement(test_cases)
```