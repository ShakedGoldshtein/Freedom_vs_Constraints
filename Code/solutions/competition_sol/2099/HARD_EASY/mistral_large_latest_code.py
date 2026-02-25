```python
def construct_permutation(n: int, k: int) -> list[int]:
    """
    Constructs a permutation of length n where the absolute differences between consecutive
    elements contain exactly k distinct values.

    Args:
        n: Length of the permutation (1 <= n <= 10^5).
        k: Number of distinct absolute differences required (1 <= k < n).

    Returns:
        A valid permutation as a list of integers, or raises ValueError if no solution exists.
    """
    if not (1 <= k < n <= 10**5):
        raise ValueError("Constraints violated: 1 ≤ k < n ≤ 10^5")

    if k == 1:
        return list(range(1, n + 1))

    permutation = []
    remaining = set(range(1, n + 1))
    current = 1
    permutation.append(current)
    remaining.remove(current)

    # Generate k-1 distinct differences by alternating between high and low values
    for diff in range(2, k + 1):
        next_val = current + diff
        if next_val <= n and next_val in remaining:
            permutation.append(next_val)
            remaining.remove(next_val)
            current = next_val
        else:
            next_val = current - diff
            if next_val >= 1 and next_val in remaining:
                permutation.append(next_val)
                remaining.remove(next_val)
                current = next_val
            else:
                # Fallback: adjust strategy if direct approach fails
                break

    # Fill remaining values in sorted order to avoid introducing new differences
    remaining_sorted = sorted(remaining)
    if remaining_sorted:
        if permutation[-1] < remaining_sorted[0]:
            permutation.extend(remaining_sorted)
        else:
            permutation.extend(reversed(remaining_sorted))

    # Verify the solution meets the k distinct differences requirement
    differences = set()
    for i in range(1, n):
        diff = abs(permutation[i] - permutation[i - 1])
        differences.add(diff)
        if len(differences) > k:
            # Reconstruct with a different approach if initial attempt fails
            return _alternative_construction(n, k)

    return permutation

def _alternative_construction(n: int, k: int) -> list[int]:
    """
    Alternative construction method when the primary approach fails to meet the k distinct differences.
    Uses a pattern of alternating between two segments to control the number of distinct differences.
    """
    if k == n - 1:
        return [i for i in range(1, n + 1) if i % 2 == 1] + [i for i in range(1, n + 1) if i % 2 == 0]

    # Split into two segments: first k+1 elements form a "wave" with k distinct differences,
    # and the rest are filled in order to avoid new differences.
    wave = []
    current = 1
    direction = 1  # 1 for increasing, -1 for decreasing
    step = 1
    used = set()
    used.add(current)
    wave.append(current)

    for _ in range(k):
        next_val = current + direction * step
        if 1 <= next_val <= n and next_val not in used:
            wave.append(next_val)
            used.add(next_val)
            current = next_val
            direction *= -1
            step += 1
        else:
            # Adjust step if next_val is invalid
            next_val = current - direction * step
            if 1 <= next_val <= n and next_val not in used:
                wave.append(next_val)
                used.add(next_val)
                current = next_val
                direction *= -1
                step += 1
            else:
                break

    remaining = sorted(set(range(1, n + 1)) - used)
    if remaining:
        if wave[-1] < remaining[0]:
            wave.extend(remaining)
        else:
            wave.extend(reversed(remaining))

    return wave
```