```python
import sys

def floyd_warshall(n: int, dist: list[list[int]]) -> None:
    """
    Applies the Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices.

    Args:
        n (int): Number of vertices in the graph.
        dist (list of list of int): Adjacency matrix representing the graph.

    Returns:
        None: The function modifies the dist matrix in place.
    """
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

def solve(n: int, adj_matrix: list[list[int]], removal_order: list[int]) -> list[int]:
    """
    Solves the problem by calculating the sum of shortest paths before each removal step.

    Args:
        n (int): Number of vertices in the graph.
        adj_matrix (list of list of int): Adjacency matrix representing the graph.
        removal_order (list of int): Order in which vertices are removed.

    Returns:
        list of int: List of sums of shortest paths before each removal step.
    """
    # Initialize distance matrix with the adjacency matrix
    dist = [row[:] for row in adj_matrix]
    
    # Apply Floyd-Warshall to find shortest paths
    floyd_warshall(n, dist)
    
    result = []
    remaining_vertices = set(range(n))
    
    # Iterate over the removal order in reverse
    for x in reversed(removal_order):
        # Calculate the sum of shortest paths for remaining vertices
        total = 0
        for i in remaining_vertices:
            for j in remaining_vertices:
                if i != j:
                    total += dist[i][j]
        
        result.append(total)
        
        # Remove the vertex and update the distance matrix
        remaining_vertices.remove(x - 1)
        for i in range(n):
            for j in range(n):
                if dist[i][j] == dist[i][x - 1] + dist[x - 1][j]:
                    # Find an alternative path that doesn't go through the removed vertex
                    alt_path = float('inf')
                    for k in remaining_vertices:
                        if dist[i][k] + dist[k][j] < alt_path:
                            alt_path = dist[i][k] + dist[k][j]
                    dist[i][j] = alt_path
    
    # Reverse the result to match the original removal order
    return result[::-1]

# Read input
n = int(sys.stdin.readline())
adj_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
removal_order = list(map(int, sys.stdin.readline().split()))

# Solve and print the result
result = solve(n, adj_matrix, removal_order)
print(' '.join(map(str, result)))
```