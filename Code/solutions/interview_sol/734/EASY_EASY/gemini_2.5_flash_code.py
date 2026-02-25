```python
import collections

def solve(N, a):
    """
    Rearrange caps on markers such that no marker has the same color as its cap.

    Args:
        N (int): The number of markers.
        a (list[int]): A list of N integers, where a[i] is the color of the i-th marker.

    Returns:
        tuple: A tuple containing:
               - "No" if no such rearrangement is possible.
               - "Yes" and a list of N integers representing the colors of the caps
                 on markers 0 to N-1, if a rearrangement is possible.
    """
    
    # 1. Count frequencies of each color to determine the maximum frequency.
    freq_map = collections.Counter(a)

    # 2. Find the maximum frequency of any color.
    # If N is 0 (though constraints say N >= 1), max_freq would be 0.
    max_freq = 0
    if N > 0:
        max_freq = max(freq_map.values())

    # 3. Check for impossibility condition.
    # If the most frequent color appears more than N/2 times, it's impossible.
    # This is because 'max_freq' caps of this color must be placed on markers
    # that are NOT this color. There are N - max_freq such markers.
    # If max_freq > N - max_freq, then there aren't enough non-matching markers.
    # This inequality simplifies to 2 * max_freq > N.
    if max_freq * 2 > N:
        return ("No",)

    # 4. Prepare data for a constructive solution.
    # We need to sort the marker colors while preserving their original indices
    # to reconstruct the output in the correct order.
    indexed_a = []
    for i in range(N):
        indexed_a.append((a[i], i))
    
    # Sort the markers primarily by color, and secondarily by original index (stable sort is fine).
    indexed_a.sort()

    # Extract the sorted colors and their corresponding original indices.
    colors_sorted = [item[0] for item in indexed_a]
    original_indices = [item[1] for item in indexed_a]

    # 5. Generate cap colors using a cyclic shift on the sorted marker colors.
    # We shift the sorted colors by 'max_freq' positions.
    # This guarantees that colors_sorted[i] will not be equal to colors_sorted[(i + max_freq) % N].
    # If they were equal, it would imply a contiguous block of at least (max_freq + 1)
    # identical colors in the sorted array, contradicting 'max_freq' being the maximum frequency.
    shifted_caps = [0] * N
    for i in range(N):
        shifted_caps[i] = colors_sorted[(i + max_freq) % N]

    # 6. Map the generated cap colors back to their original marker positions.
    # The marker that was originally at `original_indices[i]` (and which had color `colors_sorted[i]`)
    # will receive the cap `shifted_caps[i]`.
    result_caps = [0] * N
    for i in range(N):
        result_caps[original_indices[i]] = shifted_caps[i]

    return ("Yes", result_caps)

```