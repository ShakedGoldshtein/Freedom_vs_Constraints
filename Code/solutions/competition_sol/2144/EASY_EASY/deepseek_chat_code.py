```python
def solve(k, boxes):
    total_sum = 0
    box_sums = []
    all_nums = {}
    for i in range(k):
        s = sum(boxes[i])
        box_sums.append(s)
        total_sum += s
        for num in boxes[i]:
            all_nums[num] = i

    if total_sum % k != 0:
        return "No"
    target = total_sum // k

    diffs = [box_sums[i] - target for i in range(k)]

    graph = [{} for _ in range(k)]
    for i in range(k):
        for num in boxes[i]:
            need = diffs[i] + num
            if need in all_nums and all_nums[need] != i:
                j = all_nums[need]
                graph[i][num] = (need, j)

    masks = [0] * (1 << k)
    cycles = []
    for start in range(k):
        for num in boxes[start]:
            visited = set()
            current = start
            mask = 0
            path = []
            val = num
            found = True
            while True:
                if current in visited:
                    break
                visited.add(current)
                mask |= (1 << current)
                path.append((val, current))
                if val not in graph[current]:
                    found = False
                    break
                nxt_val, nxt_box = graph[current][val]
                if nxt_box == start and nxt_val == num:
                    break
                if nxt_box in visited and nxt_box != start:
                    found = False
                    break
                val = nxt_val
                current = nxt_box
            if found and current == start and graph[current].get(val, (None, None))[0] == num:
                if masks[mask] == 0:
                    masks[mask] = len(cycles)
                    cycles.append((mask, path))
            else:
                continue

    dp = [None] * (1 << k)
    dp[0] = []
    for mask in range(1 << k):
        if dp[mask] is None:
            continue
        for i in range(len(cycles)):
            cycle_mask, cycle = cycles[i]
            if (mask & cycle_mask) == 0:
                new_mask = mask | cycle_mask
                if dp[new_mask] is None:
                    dp[new_mask] = dp[mask] + [cycle]

    full_mask = (1 << k) - 1
    if dp[full_mask] is None:
        return "No"

    result_cycles = dp[full_mask]
    ans = [None] * k
    for cycle in result_cycles:
        for i in range(len(cycle)):
            val, box_from = cycle[i]
            _, box_to = cycle[(i - 1) % len(cycle)]
            ans[box_from] = (val, box_to + 1)

    output = ["Yes"]
    for i in range(k):
        output.append(f"{ans[i][0]} {ans[i][1]}")
    return "\n".join(output)
```