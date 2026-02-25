```python
from collections import deque

def solve(n, q, elements, queries):
    results = []
    for m in queries:
        dq = deque(elements)
        a, b = None, None
        for _ in range(m):
            if len(dq) < 2:
                break
            a, b = dq.popleft(), dq.popleft()
            if a > b:
                dq.appendleft(a)
                dq.append(b)
            else:
                dq.appendleft(b)
                dq.append(a)
        results.append((a, b) if a is not None and b is not None else (None, None))
    return results

def solve_large(n, q, elements, queries):
    if n == 0 or q == 0:
        return []

    # Preprocess the cycle detection
    visited = {}
    cycle_start = {}
    cycle_length = {}
    parent = {}
    order = []

    dq = deque(elements)
    step = 0
    current_state = tuple(dq)

    while current_state not in visited:
        visited[current_state] = step
        order.append(current_state)
        if len(dq) < 2:
            break
        a, b = dq.popleft(), dq.popleft()
        if a > b:
            dq.appendleft(a)
            dq.append(b)
        else:
            dq.appendleft(b)
            dq.append(a)
        step += 1
        new_state = tuple(dq)
        parent[new_state] = current_state
        current_state = new_state

    if current_state in visited:
        cycle_start_idx = visited[current_state]
        cycle_start_state = order[cycle_start_idx]
        cycle_length_val = step - cycle_start_idx
        cycle_start[cycle_start_state] = cycle_start_idx
        cycle_length[cycle_start_state] = cycle_length_val

    results = []
    for m in queries:
        if m >= step:
            if not cycle_start:
                results.append((None, None))
                continue
            cycle_state = order[cycle_start_idx]
            pos_in_cycle = (m - cycle_start_idx) % cycle_length_val
            target_state = None
            for state in order[cycle_start_idx:]:
                if visited[state] - cycle_start_idx == pos_in_cycle:
                    target_state = state
                    break
            if not target_state:
                results.append((None, None))
                continue
            dq = deque(target_state)
            a, b = dq.popleft(), dq.popleft()
            results.append((a, b))
        else:
            dq = deque(elements)
            for _ in range(m):
                a, b = dq.popleft(), dq.popleft()
                if a > b:
                    dq.appendleft(a)
                    dq.append(b)
                else:
                    dq.appendleft(b)
                    dq.append(a)
            results.append((a, b))
    return results

def solve_optimized(n, q, elements, queries):
    if n < 2:
        return [(None, None)] * q

    # Detect cycle and preprocess
    visited = {}
    state_sequence = []
    dq = deque(elements)
    step = 0
    current_state = tuple(dq)

    while current_state not in visited and len(dq) >= 2:
        visited[current_state] = step
        state_sequence.append(current_state)
        a, b = dq.popleft(), dq.popleft()
        if a > b:
            dq.appendleft(a)
            dq.append(b)
        else:
            dq.appendleft(b)
            dq.append(a)
        step += 1
        current_state = tuple(dq)

    if current_state in visited:
        cycle_start_step = visited[current_state]
        cycle_length = step - cycle_start_step
    else:
        cycle_start_step = step
        cycle_length = 0

    results = []
    for m in queries:
        if m >= step:
            if cycle_length == 0:
                results.append((None, None))
                continue
            pos_in_cycle = (m - cycle_start_step) % cycle_length
            target_step = cycle_start_step + pos_in_cycle
            target_state = state_sequence[target_step]
            dq = deque(target_state)
            a, b = dq.popleft(), dq.popleft()
            results.append((a, b))
        else:
            dq = deque(elements)
            for _ in range(m):
                a, b = dq.popleft(), dq.popleft()
                if a > b:
                   