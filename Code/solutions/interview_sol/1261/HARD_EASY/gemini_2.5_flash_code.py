```python
def build_network(n: int, m: int) -> list[tuple[int, int]] | tuple[int, int]:
    """
    Builds a computer network with N computers and M connections satisfying
    three mandatory conditions, or states impossibility.

    Conditions:
    1. The network is connected.
    2. The network remains connected even if any single computer is removed
       (i.e., the graph is 2-vertex-connected). This means any subset of N-1
       computers can still communicate with each other.
    3. There are no irrelevant connections. A connection is irrelevant if its
       removal still satisfies conditions 1 and 2. This implies the graph
       must be minimally 2-vertex-connected.

    A graph is minimally 2-vertex-connected if it is 2-vertex-connected, and
    the removal of any edge makes it no longer 2-vertex-connected.
    For N >= 3, minimally 2-vertex-connected graphs are precisely simple cycles,
    which have exactly N edges.
    For N = 2, a single edge is a minimally 2-vertex-connected graph.
    For N = 1, 0 edges are required, but M >= 1 constraint makes this case impossible.

    Args:
        n: The number of computers (1-indexed, 1 <= n <= 100).
        m: The number of connections (1 <= m <= n * (n - 1) / 2).

    Returns:
        A list of tuples, where each tuple (u, v) denotes a connection
        between computer u and computer v (1-indexed).
        Returns (-1, -1) if it's impossible to construct such a network.
    """

    # Case 1: N = 1 computer.
    # The maximum possible connections for N=1 is 1 * (1-1) / 2 = 0.
    # However, the problem constraint states 1 <= M.
    # This creates a contradiction, so it's impossible to build a network for N=1.
    if n == 1:
        return (-1, -1)

    # Case 2: N = 2 computers.
    # The maximum possible connections for N=2 is 2 * (2-1) / 2 = 1.
    # Therefore, M must be exactly 1.
    # A single connection (1, 2) forms a 2-vertex-connected graph for N=2.
    # Removing this connection disconnects the graph, so it's not irrelevant.
    if n == 2:
        if m == 1:
            return [(1, 2)]
        else:
            # Any M value other than 1 is impossible for N=2 within constraints.
            return (-1, -1)

    # Case 3: N >= 3 computers.
    # For a graph with N >= 3 vertices to satisfy all three requirements,
    # it must be a minimally 2-vertex-connected graph.
    # A known graph theory result states that a graph with N >= 3 vertices
    # is minimally 2-vertex-connected if and only if it is a simple cycle
    # of length N. A simple cycle on N vertices has exactly N edges.

    if m == n:
        connections = []
        # Create a cycle: 1-2, 2-3, ..., (N-1)-N, N-1
        for i in range(1, n):
            connections.append((i, i + 1))
        # Complete the cycle by connecting the last computer to the first
        connections.append((n, 1))
        return connections
    else:
        # If M < N: The graph cannot be 2-vertex-connected. A 2-vertex-connected
        # graph on N vertices (N >= 3) requires at least N edges.
        # If M > N: The graph cannot be minimally 2-vertex-connected.
        # Any 2-vertex-connected graph with M > N edges must contain at least
        # one 'irrelevant' connection whose removal leaves a 2-vertex-connected
        # graph, thus violating the third requirement.
        return (-1, -1)
```