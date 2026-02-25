```python
def solve(t, test_cases):
    results = []
    
    for _ in range(t):
        n, q = test_cases[_][0]
        filled = test_cases[_][1]
        
        # Create adjacency matrix with None for unfilled values
        matrix = [[None]*n for _ in range(n)]
        for i,j,val in filled:
            matrix[i-1][j-1] = val
            matrix[j-1][i-1] = val # Matrix must be symmetric
            
        # Check if diagonal is all 0s (required for absolute differences)
        for i in range(n):
            if matrix[i][i] is not None and matrix[i][i] != 0:
                results.append("no")
                break
        else:
            # Try to find valid arrangement of values
            # If any 1s exist, vertices must be in different sets
            # If any 0s exist between vertices, they must be in same set
            colors = [None]*n # Used to track bipartite coloring
            valid = True
            
            # Do bipartite coloring
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] is not None:
                        if matrix[i][j] == 1:
                            # Must be different colors
                            if colors[i] is None and colors[j] is None:
                                colors[i] = 0
                                colors[j] = 1
                            elif colors[i] is None:
                                colors[i] = 1 - colors[j]
                            elif colors[j] is None:
                                colors[j] = 1 - colors[i]
                            elif colors[i] == colors[j]:
                                valid = False
                                break
                        else: # matrix[i][j] == 0
                            # Must be same color
                            if colors[i] is None and colors[j] is None:
                                colors[i] = colors[j] = 0
                            elif colors[i] is None:
                                colors[i] = colors[j]
                            elif colors[j] is None:
                                colors[j] = colors[i]
                            elif colors[i] != colors[j]:
                                valid = False
                                break
                if not valid:
                    break
            
            results.append("yes" if valid else "no")
            
    return results
```