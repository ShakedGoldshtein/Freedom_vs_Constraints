```python
import collections

def solve(N: int, A: list[int]) -> tuple[str, list[int]] | tuple[str]:
    """
    Determines if caps can be rearranged such that no marker has a cap of the same color,
    and if so, provides one such rearrangement.

    Args:
        N: The number of markers.
        A: A list of N integers, where A[i] is the color of the i-th marker.

    Returns:
        A tuple:
        - If rearrangement is not possible: ("No",)
        - If rearrangement is possible: ("Yes", list_of_cap_colors)
          where list_of_cap_colors[i] is the color of the cap on the i-th marker.
    """
    # Count frequencies of each color to determine the maximum frequency.
    # This is used to check the impossibility condition.
    counts = collections.Counter(A)
    max_freq = 0
    # N is guaranteed to be >= 1 by constraints, so counts will not be empty.
    max_freq = max(counts.values())

    # If the most frequent color appears more than N/2 times, it's impossible.
    # Proof: Suppose color X appears K times, and K > N/2.
    # This means there are K markers of color X.
    # There are N-K caps of colors other than X.
    # Each of the K markers of color X must receive a cap that is *not* color X.
    # Since K > N/2 implies K > N - K, the number of markers of color X (K)
    # is strictly greater than the number of available non-X caps (N-K).
    # Therefore, at least K - (N-K) = 2K - N markers of color X must receive a cap of color X,
    # which violates the condition.
    if max_freq * 2 > N:
        return "No",

    # If rearrangement is possible (i.e., max_freq * 2 <= N), construct one such solution.
    # The strategy is to sort the markers by color (preserving original indices)
    # and then cyclically shift the cap assignments by N // 2 positions.

    # 1. Create a list of tuples (color, original_index) to keep track of
    #    each marker's original position after sorting.
    indexed_markers = []
    for i in range(N):
        indexed_markers.append((A[i], i))

    # 2. Sort this list based on marker color.
    #    If colors are the same, the original index breaks ties (standard tuple sort is lexicographical).
    sorted_markers = sorted(indexed_markers)

    # 3. Initialize the result array for cap colors. This array will store
    #    the cap color for each marker at its original index.
    result_caps = [0] * N

    # 4. Apply a cyclic shift of N // 2 to assign cap colors.
    #    For each marker in the sorted list (at index `i`), its cap will be the color
    #    of the marker that is `N // 2` positions ahead in the sorted list (cyclically).
    #    This shift guarantees that the cap color will not be the same as the marker's color
    #    due to the `max_freq * 2 <= N` condition. If there were a conflict, it would mean
    #    a color appears `N // 2 + 1` times, contradicting `max_freq * 2 <= N`.
    shift_amount = N // 2
    for i in range(N):
        # Get the original index of the i-th marker in the *sorted* list.
        marker_original_idx = sorted_markers[i][1]
        
        # Get the color of the cap, which comes from the marker at the shifted position.
        cap_color = sorted_markers[(i + shift_amount) % N][0]
        
        # Assign this cap color to the marker at its original position.
        result_caps[marker_original_idx] = cap_color

    # 5. Return "Yes" and the constructed list of cap colors.
    return "Yes", result_caps
```