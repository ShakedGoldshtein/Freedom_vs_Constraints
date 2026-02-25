```python
def solve(k, boxes):
    total_sum = 0
    box_sums = []
    all_nums = {}
    for i in range(k):
        nums = boxes[i]
        s = sum(nums)
        box_sums.append(s)
        total_sum += s
        for num in nums:
            all_nums[num] = i

    if total_sum % k != 0:
        return "No"
    target_sum = total_sum // k

    diffs = [box_sums[i] - target_sum for i in range(k)]

    graph = {}
    for i in range(k):
        nums = boxes[i]
        for num in nums:
            needed = diffs[i] + num
            if needed in all_nums and all_nums[needed] != i:
                graph[(i, num)] = (all_nums[needed], needed)

    cycles = []
    visited_global = set()

    def find_cycle(start_box, start_num):
        current_box = start_box
        current_num = start_num
        visited = set()
        path = []
        while True:
            if (current_box, current_num) in visited:
                idx = path.index((current_box, current_num))
                cycle = path[idx:]
                return cycle
            if (current_box, current_num) in visited_global:
                return None
            visited.add((current_box, current_num))
            path.append((current_box, current_num))
            if (current_box, current_num) not in graph:
                return None
            next_box, next_num = graph[(current_box, current_num)]
            current_box = next_box
            current_num = next_num

    for i in range(k):
        nums = boxes[i]
        for num in nums:
            if (i, num) in visited_global:
                continue
            cycle = find_cycle(i, num)
            if cycle is not None:
                boxes_in_cycle = set(box for box, num_val in cycle)
                if len(cycle) == len(boxes_in_cycle):
                    cycles.append(cycle)
                for node in cycle:
                    visited_global.add(node)

    n = k
    dp = [None] * (1 << n)
    dp[0] = []

    for cycle in cycles:
        mask = 0
        for box, num_val in cycle:
            mask |= (1 << box)
        if dp[mask] is None:
            dp[mask] = cycle

    for mask in range(1 << n):
        if dp[mask] is None:
            continue
        for cycle in cycles:
            new_mask = mask
            conflict = False
            for box, num_val in cycle:
                if mask & (1 << box):
                    conflict = True
                    break
                new_mask |= (1 << box)
            if not conflict and dp[new_mask] is None:
                dp[new_mask] = dp[mask] + cycle

    full_mask = (1 << n) - 1
    if dp[full_mask] is None:
        return "No"

    result_cycle = dp[full_mask]
    assignment = [None] * k
    for i in range(0, len(result_cycle), k):
        cycle_part = result_cycle[i:i+k]
        for box, num_val in cycle_part:
            next_box, next_num = graph[(box, num_val)]
            assignment[next_box] = (num_val, box + 1)

    output = ["Yes"]
    for i in range(k):
        output.append(f"{assignment[i][0]} {assignment[i][1]}")
    return "\n".join(output)
```