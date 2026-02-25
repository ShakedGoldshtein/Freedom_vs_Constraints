```python
import sys


def solve(n: int, adj_matrix: list[list[int]], deletions: list[int]) -> list[int]:
    """
    Solves the problem of calculating the sum of shortest paths between all pairs of remaining vertices
    after each deletion step in a weighted directed graph.

    Args:
        n (int): The number of vertices in the graph.
        adj_matrix (list of list of int): The adjacency matrix representing the graph.
        deletions (list of int): The list of vertices to be deleted in order.

    Returns:
        list of int: A list containing the sum of shortest paths between all pairs of remaining vertices
                     before each deletion step.
    """
    # Initialize the distance matrix with the adjacency matrix
    dist = [row[:] for row in adj_matrix]

    # Apply Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Initialize the result list
    result = []

    # Iterate over the deletions in reverse order
    for x in reversed(deletions):
        x -= 1  # Convert to 0-based index

        # Calculate the sum of shortest paths between all pairs of remaining vertices
        total = 0
        for i in range(n):
            for j in range(n):
                if i != j and i != x and j != x:
                    total += dist[i][j]

        # Append the result for the current step
        result.append(total)

        # Update the distance matrix by removing the vertex x
        for i in range(n):
            for j in range(n):
                if dist[i][x] + dist[x][j] == dist[i][j]:
                    # If x was on the shortest path from i to j, find a new shortest path
                    for k in range(n):
                        if k != x and dist[i][k] + dist[k][j] < dist[i][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]

    # Reverse the result to match the order of deletions
    return result[::-1]


# Read input
n = int(sys.stdin.readline())
adj_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
deletions = list(map(int, sys.stdin.readline().split()))

# Solve and print the result
result = solve(n, adj_matrix, deletions)
print(" ".join(map(str, result)))
```