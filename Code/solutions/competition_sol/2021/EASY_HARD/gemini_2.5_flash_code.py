```python
import collections

def solve(n: int, m: int, edges: list[list[int]]):
    # Build adjacency list for the graph. Vertices are 1-indexed.
    # adj[0] is unused to maintain 1-indexing.
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # colors[i] stores the partition (0 for A, 1 for B) assigned to vertex i.
    # -1 means the vertex has not been colored yet.
    colors = [-1] * (n + 1)
    
    # Lists to store vertices belonging to each partition.
    partition_A = []
    partition_B = []

    # Iterate through all vertices to handle disconnected components.
    for i in range(1, n + 1):
        if colors[i] == -1:  # If vertex i is uncolored, it belongs to a new component.
            q = collections.deque()
            q.append(i)
            colors[i] = 0  # Assign vertex i to partition 0 (e.g., A)
            partition_A.append(i)

            while q:
                u = q.popleft()
                current_color = colors[u]

                for v in adj[u]:
                    if colors[v] == -1:  # If neighbor v is uncolored
                        colors[v] = 1 - current_color  # Assign the opposite color
                        if colors[v] == 0:
                            partition_A.append(v)
                        else:
                            partition_B.append(v)
                        q.append(v)
                    elif colors[v] == current_color:
                        # Conflict: neighbor v has the same color as u.
                        # This means an odd-length cycle exists, and the graph is not bipartite.
                        return -1 
        
    # If no conflicts were found after checking all components, the graph is bipartite.
    # The two partitions (partition_A and partition_B) form the required disjoint vertex covers.
    # Return the sorted lists of vertices for partitions A and B.
    # The caller is responsible for formatting the output as per the problem description.
    return (sorted(partition_A), sorted(partition_B))

```