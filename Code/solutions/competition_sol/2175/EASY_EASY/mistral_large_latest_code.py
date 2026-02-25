```python
def solve(m, numbers):
    basket = []
    result = []
    xor_map = {0: []}  # Maps XOR values to list of indices

    for idx, num_str in enumerate(numbers):
        num = int(num_str, 10)
        found = False
        current_xor = 0
        best_indices = []

        # Check all possible XOR combinations
        for mask in range(1, 1 << len(basket)):
            total = 0
            indices = []
            for bit in range(len(basket)):
                if mask & (1 << bit):
                    total ^= basket[bit]
                    indices.append(bit)
            if total == num:
                if not found or len(indices) < len(best_indices):
                    found = True
                    best_indices = indices.copy()
                    if len(best_indices) == 1:
                        break  # Can't get smaller than 1

        if found:
            result.append(f"{len(best_indices)} {' '.join(map(str, best_indices))}")
        else:
            result.append("0")

        basket.append(num)
        # Update XOR map (not used in this solution but could optimize further)
        new_xors = []
        for i in range(len(basket)):
            new_xor = basket[i] ^ (xor_map.get(0, [])[-1] if i == 0 else xor_map.get(basket[i-1], [])[-1])
            new_xors.append(new_xor)
        # This part is simplified; actual optimization would require more complex tracking

    return '\n'.join(result)
```