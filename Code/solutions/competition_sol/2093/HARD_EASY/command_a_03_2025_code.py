```python
def find_increasing_sequences(n: int, arr: list[int]) -> list[list[int]]:
    """
    Finds representation of the given array with one or several increasing sequences.

    Args:
        n (int): The number of elements in the array.
        arr (list[int]): The array of distinct integers.

    Returns:
        list[list[int]]: A list of increasing sequences.
    """
    used = [False] * n  # Tracks whether an element has been used in a sequence
    sequences = []  # Stores the resulting sequences

    while any(not u for u in used):
        current_sequence = []
        last = -1  # Tracks the last element added to the current sequence
        for i in range(n):
            if not used[i] and (last == -1 or arr[i] > arr[last]):
                used[i] = True
                current_sequence.append(arr[i])
                last = i
        sequences.append(current_sequence)

    return sequences


def solve(n: int, arr: list[int]) -> list[str]:
    """
    Solves the problem by finding and formatting the increasing sequences.

    Args:
        n (int): The number of elements in the array.
        arr (list[int]): The array of distinct integers.

    Returns:
        list[str]: A list of strings, each representing an increasing sequence.
    """
    sequences = find_increasing_sequences(n, arr)
    return [" ".join(map(str, seq)) for seq in sequences]
```