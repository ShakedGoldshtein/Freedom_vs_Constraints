```python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx]); idx += 1
        rows = []
        for _ in range(N):
            C_i = int(data[idx]); idx += 1
            row = list(map(int, data[idx:idx+C_i]))
            idx += C_i
            rows.append(row)
        
        total_chef = 0
        moves = []
        
        for row in rows:
            length = len(row)
            if length % 2 == 0:
                left_sum = sum(row[:length//2])
                right_sum = sum(row[length//2:])
                moves.append((left_sum, right_sum, row))
            else:
                mid = length // 2
                left_sum = sum(row[:mid])
                right_sum = sum(row[mid+1:])
                mid_val = row[mid]
                moves.append((left_sum, right_sum, mid_val, row))
        
        chef_turn = True
        left_moves = []
        right_moves = []
        mid_vals = []
        
        for move in moves:
            if len(move) == 3:
                left_sum, right_sum, row = move
                left_moves.append((left_sum, row))
                right_moves.append((right_sum, row))
            else:
                left_sum, right_sum, mid_val, row = move
                left_moves.append((left_sum, row))
                right_moves.append((right_sum, row))
                mid_vals.append((mid_val, left_sum, right_sum, row))
        
        left_moves.sort(key=lambda x: x[0], reverse=True)
        right_moves.sort(key=lambda x: x[0], reverse=True)
        mid_vals.sort(key=lambda x: x[0], reverse=True)
        
        li = ri = mi = 0
        used = set()
        
        while li < len(left_moves) or ri < len(right_moves) or mi < len(mid_vals):
            if chef_turn:
                best_val = -1
                best_type = None
                best_index = -1
                
                if li < len(left_moves) and left_moves[li][0] > best_val and id(left_moves[li][1]) not in used:
                    best_val = left_moves[li][0]
                    best_type = 'left'
                    best_index = li
                
                if ri < len(right_moves) and right_moves[ri][0] > best_val and id(right_moves[ri][1]) not in used:
                    best_val = right_moves[ri][0]
                    best_type = 'right'
                    best_index = ri
                
                if mi < len(mid_vals) and mid_vals[mi][0] > best_val and id(mid_vals[mi][3]) not in used:
                    best_val = mid_vals[mi][0]
                    best_type = 'mid'
                    best_index = mi
                
                if best_type == 'left':
                    total_chef += best_val
                    used.add(id(left_moves[best_index][1]))
                    li += 1
                elif best_type == 'right':
                    total_chef += best_val
                    used.add(id(right_moves[best_index][1]))
                    ri += 1
                elif best_type == 'mid':
                    total_chef += best_val
                    used.add(id(mid_vals[best_index][3]))
                    mi += 1
                else:
                    break
            else:
                best_val = -1
                best_type = None
                best_index = -1
                
                if li < len(left_moves) and left_moves[li][0] > best_val and id(left_moves[li][1]) not in used:
                    best_val = left_moves[li][0]
                    best_type = 'left'
                    best_index = li
                
                if ri < len(right_moves) and right_moves[ri][0] > best_val and id(right_moves[ri][1]) not in used:
                    best_val = right_moves[ri][0]
                    best_type = 'right'
                    best_index = ri
                
                if mi < len(mid_vals) and mid_vals[mi][0] > best_val and id(mid_vals[mi][3]) not in used:
                    best_val = mid_vals[mi][0]
                    best_type = 'mid'
                    best_index = mi
                
