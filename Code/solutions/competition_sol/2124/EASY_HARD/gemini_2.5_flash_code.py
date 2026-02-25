```python
import math

def solve(n_nodes, m_edges, x_bears, edges_input):
    
    # Dinic's Algorithm for Maximum Flow
    # Takes number of nodes, adjacency list representation of the graph, source, and sink.
    # Adjacency list: Each entry graph[u] is a list of [v, capacity, reverse_edge_index]
    def dinic(n, graph, source, sink):
        total_flow = 0
        
        # Pre-allocate arrays for performance
        levels = [-1] * n
        ptr = [0] * n # Pointer for DFS to avoid re-exploring saturated edges

        # BFS to build the level graph
        def bfs():
            for i in range(n):
                levels[i] = -1 # Reset levels for new phase
            q = [source]
            levels[source] = 0
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                for i in range(len(graph[u])):
                    v, capacity, _ = graph[u][i]
                    if capacity > 0 and levels[v] == -1:
                        levels[v] = levels[u] + 1
                        q.append(v)
            return levels[sink] != -1 # Return true if sink is reachable

        # DFS to find augmenting paths in the level graph
        def dfs(u, pushed):
            if pushed == 0:
                return 0
            if u == sink:
                return pushed
            
            # Iterate through edges from u starting from ptr[u]
            while ptr[u] < len(graph[u]):
                edge = graph[u][ptr[u]]
                v, capacity, rev = edge[0], edge[1], edge[2]

                # Only traverse to nodes in the next level with available capacity
                if levels[v] != levels[u] + 1 or capacity == 0:
                    ptr[u] += 1
                    continue
                
                tr = dfs(v, min(pushed, capacity))
                if tr == 0:
                    ptr[u] += 1
                    continue
                
                # Update capacities in both forward and backward (residual) edges
                edge[1] -= tr # Decrease forward edge capacity
                graph[v][rev][1] += tr # Increase backward (residual) edge capacity
                return tr
            return 0 # No augmenting path found from u

        # Main Dinic loop: Repeatedly find augmenting paths in level graphs
        while bfs():
            for i in range(n):
                ptr[i] = 0 # Reset pointers for DFS for each new level graph
            
            while True:
                pushed = dfs(source, float('inf')) # Try to push infinite amount of flow
                if pushed == 0:
                    break # No more augmenting paths in this level graph
                total_flow += pushed
                
        return total_flow

    # Adjust node indices to be 0-indexed (from 1 to n to 0 to n-1)
    original_edges_list = []
    for a, b, c in edges_input:
        original_edges_list.append((a - 1, b - 1, c))

    source_node = 0
    sink_node = n_nodes - 1

    # Predicate function for binary search:
    # Checks if it's possible for x_bears to each carry 'weight_per_bear'
    def check_feasible(weight_per_bear):
        # If weight_per_bear is very close to zero or negative, it's considered not feasible
        # for achieving a positive total weight delivery. This handles division by zero and
        # ensures we search for strictly positive per-bear weight.
        if weight_per_bear <= 1e-9: # A small epsilon to handle floating point comparisons
            return False

        graph_for_dinic = [[] for _ in range(n_nodes)]
        
        for u, v, capacity_c in original_edges_list:
            # Calculate effective capacity for bears: how many bears can use this edge
            # if each carries 'weight_per_bear'. Use floor division (int() truncates for positive numbers).
            effective_capacity = int(capacity_c / weight_per_bear)
            
            if effective_capacity > 0:
                # Add forward edge (u -> v) with calculated capacity
                graph_for_dinic[u].append([v, effective_capacity, len(graph_for_dinic[v])])
                # Add backward edge (v -> u) for residual graph, initial capacity 0
                graph_for_dinic[v].append([u, 0, len(graph_for_dinic[u]) - 1])
        
        # Calculate the maximum number of bears that can simultaneously carry 'weight_per_bear'
        max_bears_flow = dinic(n_nodes, graph_for_dinic, source_node, sink_node)
        
        # Return True if enough bears (x_bears or more) can be accommodated
        return max_bears_flow >= x_bears

    # Binary search for the maximum 'weight_per_bear'
    low = 0.0
    # The maximum possible individual edge capacity is 1,000,000. This is an upper bound
    # for the weight a single bear can carry.
    high = 1_000_000.0 

    # Perform a fixed number of iterations for floating point binary search.
    # 100 iterations are typically sufficient to achieve high precision (e.g., 10^-6)
    # over a large range (e.g., 10^6).
    for _ in range(100): 
        mid = (low + high) / 2.0
        if check_feasible(mid):
            low = mid # 'mid' is achievable, try for higher weight per bear
        else:
            high = mid # 'mid' is not achievable, reduce weight per bear

    # After binary search, 'low' will hold the maximum feasible weight_per_bear.
    # The total delivered weight is this maximum per-bear weight multiplied by the number of bears.
    max_w_per_bear = low
    
    return max_w_per_bear * x_bears
```