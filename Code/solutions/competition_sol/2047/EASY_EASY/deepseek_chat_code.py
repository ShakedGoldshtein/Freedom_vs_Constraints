```python
def solve(n, k, grid):
    moves = []
    parking_spots = {}
    car_positions = {}
    
    for r in [0, 3]:
        for c in range(n):
            if grid[r][c] != 0:
                parking_spots[grid[r][c]] = (r, c)
    
    for r in [1, 2]:
        for c in range(n):
            if grid[r][c] != 0:
                car_positions[grid[r][c]] = (r, c)
    
    def is_empty(pos):
        r, c = pos
        return grid[r][c] == 0
    
    def move_car(car, to_r, to_c):
        nonlocal moves
        from_r, from_c = car_positions[car]
        grid[from_r][from_c] = 0
        grid[to_r][to_c] = car
        car_positions[car] = (to_r, to_c)
        moves.append((car, to_r + 1, to_c + 1))
    
    def find_path(start, target, occupied):
        sr, sc = start
        tr, tc = target
        
        if sr == tr and sc == tc:
            return []
        
        visited = set()
        queue = [(sr, sc, [])]
        visited.add((sr, sc))
        
        while queue:
            r, c, path = queue.pop(0)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 4 and 0 <= nc < n:
                    if (nr, nc) == (tr, tc):
                        return path + [(nr, nc)]
                    if (nr, nc) not in visited and (nr, nc) not in occupied and is_empty((nr, nc)):
                        visited.add((nr, nc))
                        queue.append((nr, nc, path + [(nr, nc)]))
        return None
    
    def try_direct_park():
        for car in list(car_positions.keys()):
            pos = car_positions[car]
            spot = parking_spots[car]
            if pos[1] == spot[1]:
                if (pos[0] == 1 and spot[0] == 0) or (pos[0] == 2 and spot[0] == 3):
                    occupied = set(car_positions.values())
                    occupied.remove(pos)
                    path = find_path(pos, spot, occupied)
                    if path is not None:
                        for step in path:
                            move_car(car, step[0], step[1])
                        return True
        return False
    
    def try_move_to_temp():
        for car in list(car_positions.keys()):
            pos = car_positions[car]
            if pos[0] in [1, 2]:
                for dc in [-1, 1]:
                    nc = pos[1] + dc
                    if 0 <= nc < n:
                        temp_pos = (pos[0], nc)
                        if is_empty(temp_pos):
                            occupied = set(car_positions.values())
                            occupied.remove(pos)
                            path = find_path(pos, temp_pos, occupied)
                            if path is not None:
                                for step in path:
                                    move_car(car, step[0], step[1])
                                return True
        return False
    
    while car_positions:
        if try_direct_park():
            continue
        if try_move_to_temp():
            continue
        return -1
    
    if len(moves) > 20000:
        return -1
    
    result = [str(len(moves))]
    for move in moves:
        result.append(f"{move[0]} {move[1]} {move[2]}")
    return "\n".join(result)
```