```python
def max_column_sums(n, w, arrays):
    column_max_sums = [0] * w

    for arr in arrays:
        l, elements = arr[0], arr[1:]
        if l == 0:
            continue
        max_prefix = [0] * (w + 1)
        max_suffix = [0] * (w + 1)

        for i in range(1, w + 1):
            max_prefix[i] = max_prefix[i - 1] + (elements[i - 1] if i <= l else 0)

        for i in range(w, 0, -1):
            max_suffix[i] = max_suffix[i + 1] + (elements[w - i] if (w - i + 1) <= l else 0)

        current_max = max_prefix[min(l, w)]
        for i in range(1, w + 1):
            left = max(0, i - l)
            right = min(w, i + l - 1)
            window_sum = max_prefix[right] - max_prefix[left]
            current_max = max(current_max, window_sum)

        for i in range(1, w + 1):
            left = max(0, i - l)
            right = min(w, i + l - 1)
            window_sum = max_prefix[right] - max_prefix[left]
            if window_sum > column_max_sums[i - 1]:
                column_max_sums[i - 1] = window_sum

    return column_max_sums
```