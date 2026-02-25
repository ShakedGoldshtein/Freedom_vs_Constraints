```python
def simplify(directions):
    if not directions:
        return ""

    visited = set()
    path = []
    current = (0, 0)
    visited.add(current)
    path.append(current)

    dir_map = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
    simplified = []

    for i, d in enumerate(directions):
        dx, dy = dir_map[d]
        new_pos = (current[0] + dx, current[1] + dy)

        if new_pos in visited:
            loop_start = path.index(new_pos)
            loop_length = len(path) - loop_start
            simplified = simplified[:loop_start]
            path = path[:loop_start + 1]
            current = new_pos
        else:
            simplified.append(d)
            path.append(new_pos)
            current = new_pos
            visited.add(current)

    return ''.join(simplified)
```