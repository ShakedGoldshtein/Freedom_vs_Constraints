```python
import collections

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by size: attach smaller tree under root of larger tree
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i # Swap to ensure root_i is larger or equal
            
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        return False

def solve(N, Q, queries):
    dsu = DSU(N)
    
    # Store unique constraints to handle B[i][j] vs B[j][i] and duplicate entries
    # Key: (min(u,v), max(u,v)), Value: val
    given_entries = {} 
    
    # Store (u,v) pairs where B[u][v] = 1, will process after all 0-constraints
    adj_ones_raw = []

    for u_orig, v_orig, val in queries:
        # Convert to 0-indexed
        u, v = u_orig - 1, v_orig - 1

        # Diagonal check: B[i][i] must be 0
        if u == v:
            if val != 0:
                return "no"
            continue # Diagonal entries only constrain to be 0, no further graph implications

        # Normalize (u,v) for consistent key in given_entries and to handle symmetry
        # B[i][j] must equal B[j][i]
        u_prime, v_prime = min(u, v), max(u, v)

        if (u_prime, v_prime) in given_entries:
            # Check for conflicting values for the same pair
            if given_entries[(u_prime, v_prime)] != val:
                return "no"
        else:
            given_entries[(u_prime, v_prime)] = val
            if val == 0:
                dsu.union(u, v)
            elif val == 1:
                adj_ones_raw.append((u, v))
    
    # After all 0-constraints processed, build the component graph for 1-constraints
    # Nodes in this graph are the roots of DSU components
    adj_comp = collections.defaultdict(set)
    
    for u, v in adj_ones_raw:
        root_u = dsu.find(u)
        root_v = dsu.find(v)

        # If u and v are forced to be in the same component (A[u]=A[v] implies B[u][v]=0)
        # AND B[u][v]=1 is given, it's a contradiction.
        if root_u == root_v:
            return "no"
        
        # Add an edge between the roots of the components
        # This implies |A[root_u] - A[root_v]| = 1
        adj_comp[root_u].add(root_v)
        adj_comp[root_v].add(root_u)

    # Perform 2-coloring (bipartite check) on the component graph
    # `colors` stores 0 or 1 for each root (component), -1 for uncolored (represented by not being in dict)
    colors = {} 

    # Iterate over all possible initial nodes (0 to N-1) to ensure all DSU components are processed.
    # `dsu.find(i)` will return the representative (root) of the component that `i` belongs to.
    for i in range(N):
        root = dsu.find(i) # Get the representative of the component containing i

        if root not in colors:
            # Start BFS from this uncolored root
            q = collections.deque([(root, 0)]) # (node, color)
            colors[root] = 0
            
            while q:
                curr_root, curr_color = q.popleft()
                
                # Check neighbors in the component graph
                for neighbor_root in adj_comp[curr_root]:
                    if neighbor_root not in colors:
                        # Assign opposite color to uncolored neighbor
                        colors[neighbor_root] = 1 - curr_color
                        q.append((neighbor_root, 1 - curr_color))
                    elif colors[neighbor_root] == curr_color:
                        # Conflict found: neighbor has same color, thus the graph is not bipartite.
                        # This means we cannot assign A values such that |A[u]-A[v]|=1 for all edges.
                        return "no"
    
    return "yes"

```