```python
import collections
import math

class DinicMaxFlow:
    """
    Implements Dinic's algorithm for finding maximum flow in a graph.
    Optimized for performance with level graph and blocking flow.
    """

    def __init__(self, n_nodes: int, source: int, sink: int):
        """
        Initializes the DinicMaxFlow solver.

        Args:
            n_nodes (int): The total number of nodes in the graph.
            source (int): The index of the source node.
            sink (int): The index of the sink node.
        """
        self.n = n_nodes
        self.source = source
        self.sink = sink
        self.adj = [[] for _ in range(n_nodes)]
        self.level = [-1] * n_nodes  # Stores levels of nodes in the level graph
        self.ptr = [0] * n_nodes    # Pointers for DFS to avoid re-exploring edges

    def add_edge(self, u: int, v: int, capacity: int):
        """
        Adds a directed edge from u to v with a given capacity.
        Also adds a reverse edge with 0 initial capacity for residual graph.

        Args:
            u (int): The starting node of the edge.
            v (int): The ending node of the edge.
            capacity (int): The capacity of the edge. Must be non-negative.
        """
        # An edge is represented as [to_node, current_capacity, index_of_reverse_edge_in_adj[v]]
        self.adj[u].append([v, capacity, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1]) # Reverse edge for residual graph

    def _bfs(self) -> bool:
        """
        Performs a Breadth-First Search to build the level graph.
        Returns True if the sink is reachable from the source, False otherwise.
        """
        self.level = [-1] * self.n
        q = collections.deque([self.source])
        self.level[self.source] = 0
        while q:
            u = q.popleft()
            for edge_idx in range(len(self.adj[u])):
                v, capacity, _ = self.adj[u][edge_idx]
                if capacity > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[self.sink] != -1

    def _dfs(self, u: int, pushed: int) -> int:
        """
        Performs a Depth-First Search to find an augmenting path and push flow.

        Args:
            u (int): The current node.
            pushed (int): The maximum flow that can be pushed through this path so far.

        Returns:
            int: The amount of flow pushed through the path found.
        """
        if pushed == 0:
            return 0
        if u == self.sink:
            return pushed

        # Iterate through edges starting from ptr[u] to optimize.
        # This pointer ensures that edges that are already saturated or don't
        # lead to an augmenting path in the current DFS phase are not re-explored.
        while self.ptr[u] < len(self.adj[u]):
            edge = self.adj[u][self.ptr[u]]
            v, capacity, rev_idx = edge[0], edge[1], edge[2]

            # Only consider edges that are part of the level graph and have capacity
            if self.level[v] != self.level[u] + 1 or capacity == 0:
                self.ptr[u] += 1
                continue

            tr = self._dfs(v, min(pushed, capacity))
            if tr == 0:
                self.ptr[u] += 1
                continue

            # Update capacities of forward and reverse edges
            self.adj[u][self.ptr[u]][1] -= tr
            self.adj[v][rev_idx][1] += tr
            return tr
        return 0

    def max_flow(self) -> int:
        """
        Calculates the maximum flow from the source to the sink using Dinic's algorithm.

        Returns:
            int: The total maximum flow.
        """
        total_flow = 0
        while self._bfs():
            # Reset ptrs for each BFS phase to allow DFS to explore all valid paths
            # from each node in the current level graph.
            self.ptr = [0] * self.n
            while True:
                pushed = self._dfs(self.source, float('inf')) # Push maximum possible flow
                if pushed == 0: # No more augmenting paths in the current level graph
                    break
                total_flow += pushed
        return total_flow


def solve(n: int, m: int, x: int, edges: list[tuple[int, int, int]]) -> float:
    """
    Calculates the maximum total weight Niwel can deliver using exactly x bears.

    The problem is transformed into finding the maximum weight 'W_per_bear'
    such that 'x' bears can travel from node 1 to node n, each carrying 'W_per_bear'.
    This is solved using binary search on 'W_per_bear', with a Dinic's max-flow
    algorithm in the check function to determine feasibility.

    Args:
        n (int): The number of nodes in the city graph (2 <= n <= 50).
        m (int): The number of directed edges (1 <= m <= 500).
        x (int): The number of bears (1 <= x <= 100 000).
        edges (list[tuple[int, int, int]]): A list of tuples, where each tuple
            (a_i, b_i, c_i) represents a directed edge from a_i to b_i
            with weight capacity c_i. Node indices are 1-based.

    Returns:
        float: The maximum total weight Niwel can deliver.
               The result is accurate to 10^-6 absolute or relative error.
    """

    # Node indices are 1-based in input, convert to 0-based for internal use.
    source_node = 0  # Represents original node 1
    sink_node = n - 1  # Represents original node n

    def check(W_per_bear_candidate: float) -> bool:
        """
        Checks if it's possible for 'x' bears to deliver goods, each carrying
        'W_per_bear_candidate' weight, from source to sink.

        This is done by constructing a flow network where edge capacities
        represent the number of bears that can use that edge.

        Args:
            W_per_bear_candidate (float): The candidate weight per bear.

        Returns:
            bool: True if 'x' or more bears can pass, False otherwise.
        """
        # If W_per_bear is extremely small (close to zero), any edge capacity
        # becomes effectively infinite for the number of bears it can carry.
        # Since a path from 1 to n is guaranteed, 'x' bears can always pass
        # if W_per_bear is negligible. This also prevents division by zero.
        if W_per_bear_candidate <= 1e-9: # Using a small epsilon
            return True

        flow_solver = DinicMaxFlow(n, source_node, sink_node)

        for u, v, capacity_c in edges:
            # Convert 1-based nodes to 0-based
            u_0based = u - 1
            v_0based = v - 1

            # Calculate the maximum number of bears that can use this edge
            # if each bear carries W_per_bear_candidate weight.
            # We use math.floor because the number of bears must be an integer.
            effective_capacity = math.floor(capacity_c / W_per_bear_candidate)

            if effective_capacity > 0:
                # Add edge to the flow network. The capacity for bears is capped
                # at 'x' because we only need to achieve 'x' total flow.
                # Any capacity beyond 'x' is redundant for this specific target.
                flow_solver.add_edge(u_0based, v_0based, min(effective_capacity, x))

        max_bears_flow = flow_solver.max_flow()
        return max_bears_flow >= x

    # Binary search for the maximum W_per_bear
    # Lower bound for W_per_bear (0.0 implies no weight or negligible weight)
    low = 0.0
    # Upper bound for W_per_bear: The maximum possible capacity of a single edge.
    # The problem guarantees m >= 1, so `edges` will not be empty.
    high = float(max(c for _, _, c in edges))

    # Initialize the result for the maximum weight per bear found so far.
    max_W_per_bear = 0.0

    # Perform binary search for a fixed number of iterations to achieve required precision.
    # 100 iterations are typically sufficient for `10^-6` error given an initial range of `10^6`.
    for _ in range(100):
        mid = (low + high) / 2.0
        if check(mid):
            max_W_per_bear = mid # 'mid' is achievable, try for higher
            low = mid
        else:
            high = mid # 'mid' is too high, reduce upper bound

    # The total maximum weight delivered is the number of bears multiplied by the
    # maximum achievable weight per bear.
    return x * max_W_per_bear
```