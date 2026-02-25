```python
def solve(T, cases):
    results = []
    
    for _ in range(T):
        N, Q = cases[_][0]
        queries = cases[_][1]
        
        # Create adjacency matrix with None for unfilled entries
        matrix = [[None]*N for _ in range(N)]
        for i, j, val in queries:
            matrix[i-1][j-1] = val
            matrix[j-1][i-1] = val # Mirror since absolute difference is symmetric
            
        # Check if possible to fill matrix
        result = check_possible(N, matrix)
        results.append("yes" if result else "no")
            
    return results

def check_possible(N, matrix):
    # For N=2 case
    if N == 2:
        if matrix[0][0] is not None and matrix[0][0] != 0:
            return False
        if matrix[1][1] is not None and matrix[1][1] != 0:
            return False
        if matrix[0][1] is not None and matrix[1][0] is not None and matrix[0][1] != matrix[1][0]:
            return False
        return True
        
    # Check diagonal elements
    for i in range(N):
        if matrix[i][i] is not None and matrix[i][i] != 0:
            return False
            
    # Check symmetry
    for i in range(N):
        for j in range(i+1,N):
            if matrix[i][j] is not None and matrix[j][i] is not None:
                if matrix[i][j] != matrix[j][i]:
                    return False
                    
    # Check triangle inequality
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if (matrix[i][j] is not None and 
                    matrix[j][k] is not None and 
                    matrix[i][k] is not None):
                    if matrix[i][j] + matrix[j][k] < matrix[i][k]:
                        return False
                        
    return True
```