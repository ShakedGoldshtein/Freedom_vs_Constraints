```python
from typing import List, Tuple
from collections import deque
from heapq import heappush, heappop

def max_sum(n: int, w: int, arrs: List[Tuple[int, List[int]]]) -> List[int]:
    """
    Solve the problem
    """
    # Initialize Variables 
    prefix = [0] * (w + 2)
    minimums = []
    zeros = deque()
    res = [0] * (w + 1)

    for l, arr in arrs:
        arr = [0] + arr + [0] * (w - l)
        for r in reversed(arr):
            prefix.append(prefix[-1] + r)
        right_min = prefix[-1]
        for i in range(w + 1, 0, -1):
            right_min = min(right_min, prefix[i-1])
            minimums.append((right_min, len(prefix) - i))

    for j in range(1, w + 1):
        while zeros and zeros[0] 
heapq.heapify(minimums)

    for i in range(1, w + 1):
        res[i] = max(zeros[0][0] if zeros else float('-inf'), minimums[0][0] if minimums else float('-inf'))
        if zeros and zeros[0][1] == i:
            heappop(zeros)
        if minimums and minimums[0][1] == i:
            heappop(minimums)
    return res[1:]

def from_input_string(input_string: str) -> Tuple[int, int, List[Tuple[int, List[int]]]]:
    """
    Parse input string
    """
    lines = input_string.strip().split("\n")
    n, w = map(int, lines[0].strip().split())
    arrs = []
    for line in lines[1:]:
        data = list(map(int, line.strip().split()))
        l, arr = data[0], data[1:]
        arrs.append((l, arr))
    return n, w, arrs

def from_output_string(output_string: str) -> List[int]:
    """
    Parse output string
    """
    return list(map(int, output_string.strip().split()))

def to_input_string(inputs: Tuple[int, int, List[Tuple[int, List[int]]]]) -> str:
    """
    Convert inputs tuple to string representation
    """
    n, w, arrs = inputs
    res = []
    res.append(f"{n} {w}")
    for l, arr in arrs:
        res.append(f"{l} {' '.join(map(str, arr))}")
    return "\n".join(res)

def to_output_string(output: List[int]) -> str:
    """
    Convert output list to string representation
    """
    return " ".join(map(str, output))
```