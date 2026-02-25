```python
def solve(n, q, word, evolutions):
    religions = [[], [], []]
    result = []

    for op in evolutions:
        if op[0] == '+':
            i, c = int(op[1]) - 1, op[2]
            religions[i].append(c)
        else:
            i = int(op[1]) - 1
            religions[i].pop()

        # Check if the current religions can be disjoint subsequences
        ptrs = [0, 0, 0]
        possible = True
        for char in word:
            found = False
            for i in range(3):
                if ptrs[i] < len(religions[i]) and religions[i][ptrs[i]] == char:
                    ptrs[i] += 1
                    found = True
                    break
            if found:
                continue
            # Check if any religion needs this character
            needed = False
            for i in range(3):
                if ptrs[i] < len(religions[i]):
                    needed = True
                    break
            if needed:
                possible = False
                break
        result.append("YES" if possible else "NO")

    return result
```