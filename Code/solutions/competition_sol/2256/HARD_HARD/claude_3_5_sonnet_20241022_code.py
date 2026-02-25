```python
def solve(n, m):
    # Return early for 1x1 grid
    if n == 1 and m == 1:
        return [(1,1)]
        
    def is_valid(x, y):
        return 1 <= x <= n and 1 <= y <= m
    
    def get_vector(p1, p2):
        return (p2[0] - p1[0], p2[1] - p1[1])
        
    def find_path(curr_pos, visited, used_vectors):
        # Found valid solution
        if len(visited) == n*m:
            return visited
            
        x, y = curr_pos
        
        # Try all possible next positions
        for next_x in range(1, n+1):
            for next_y in range(1, m+1):
                if (next_x,next_y) in visited:
                    continue
                    
                vector = get_vector((x,y), (next_x,next_y))
                if vector == (0,0) or vector in used_vectors:
                    continue
                
                # Try this move    
                visited.add((next_x,next_y))
                used_vectors.add(vector)
                
                result = find_path((next_x,next_y), visited, used_vectors)
                if result:
                    return result
                    
                visited.remove((next_x,next_y)) 
                used_vectors.remove(vector)
                
        return None

    # Start search from (1,1)
    visited = {(1,1)}
    used_vectors = set()
    
    path = find_path((1,1), visited, used_vectors)
    
    if path is None:
        return -1
    else:
        return list(path)

```