```python
def solve(m, numbers):
    basket = []
    result = []
    xor_map = {0: []}  # Maps XOR sums to list of index sets (as tuples)

    for idx, num_str in enumerate(numbers):
        num = int(num_str, 10) if num_str else 0
        found = False
        solution = None

        # Check all possible XOR sums in the map
        for xor_sum in xor_map:
            target = xor_sum ^ num
            if target in xor_map:
                # Find the smallest set of indices
                for indices in xor_map[target]:
                    if not any(i == idx for i in indices):  # Ensure current num isn't used
                        solution = indices
                        found = True
                        break
                if found:
                    break

        if found:
            result.append(f"{len(solution)} {' '.join(map(str, solution))}")
        else:
            result.append("0")

        # Update the XOR map with new possible sums
        new_xor_map = {}
        for xor_sum in xor_map:
            new_xor = xor_sum ^ num
            for indices in xor_map[xor_sum]:
                new_indices = tuple(sorted(indices + (idx,)))
                if new_xor in new_xor_map:
                    new_xor_map[new_xor].append(new_indices)
                else:
                    new_xor_map[new_xor] = [new_indices]

        # Merge new sums into the existing map
        for xor_sum in new_xor_map:
            if xor_sum in xor_map:
                xor_map[xor_sum].extend(new_xor_map[xor_sum])
            else:
                xor_map[xor_sum] = new_xor_map[xor_sum]

        # Add the current number itself
        if num in xor_map:
            xor_map[num].append((idx,))
        else:
            xor_map[num] = [(idx,)]

        basket.append(num)

    return '\n'.join(result)
```