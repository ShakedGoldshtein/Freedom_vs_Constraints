```python
import math
from collections import Counter

def compute_cost(wire_length, requirements):
    total_wires = 0
    for req in requirements:
        if req % wire_length != 0:
            return float('inf')
        total_wires += req // wire_length
    return total_wires

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[idx]); idx += 1
        A = list(map(int, input_data[idx:idx + n]))
        idx += n
        
        freq = Counter(A)
        unique_lengths = sorted(freq.keys())
        
        best_length = 1
        min_cost = compute_cost(1, A)
        
        for candidate in unique_lengths:
            cost = compute_cost(candidate, A)
            if cost < min_cost:
                min_cost = cost
                best_length = candidate
        
        results.append(f"{best_length} {min_cost}")
    
    print("\n".join(results))

if __name__ == "__main__":
    solve()
```