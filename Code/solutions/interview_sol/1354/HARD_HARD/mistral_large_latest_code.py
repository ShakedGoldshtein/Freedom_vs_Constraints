```python
MOD = 10**9 + 7

def solve_tree_coloring(test_cases):
    results = []
    for case in test_cases:
        n, k, edges = case
        if n == 0:
            results.append(0)
            continue

        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Precompute parent and children for each node (root at 1)
        parent = [0] * (n + 1)
        children = [[] for _ in range(n + 1)]
        stack = [(1, None, False)]
        while stack:
            node, par, visited = stack.pop()
            if not visited:
                parent[node] = par
                stack.append((node, par, True))
                for neighbor in adj[node]:
                    if neighbor != par:
                        stack.append((neighbor, node, False))
            else:
                for neighbor in adj[node]:
                    if neighbor != par:
                        children[node].append(neighbor)

        # DP[node][color]: number of ways to color subtree rooted at 'node' with 'node' having 'color'
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for color in range(1, k + 1):
            dp[1][color] = 1

        # Post-order traversal to fill DP
        stack = [(1, False)]
        while stack:
            node, processed = stack.pop()
            if not processed:
                stack.append((node, True))
                for child in reversed(children[node]):
                    stack.append((child, False))
            else:
                for color in range(1, k + 1):
                    if dp[node][color] == 0:
                        continue
                    current = dp[node][color]
                    for child in children[node]:
                        # Child must have the same color as parent
                        dp[child][color] = (dp[child][color] + current) % MOD

                # For leaf nodes, all colors are possible if not already set
                if not children[node]:
                    for color in range(1, k + 1):
                        if dp[node][color] == 0:
                            dp[node][color] = 1

        # Now, for non-leaf nodes, if a child can have a different color, it must be a new component
        # We need to recompute considering independent subtrees
        # Reset DP for a bottom-up approach with independent subtrees
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for node in range(1, n + 1):
            if not children[node]:
                for color in range(1, k + 1):
                    dp[node][color] = 1

        # Post-order traversal to compute DP with independent subtrees
        stack = [(1, False)]
        while stack:
            node, processed = stack.pop()
            if not processed:
                stack.append((node, True))
                for child in reversed(children[node]):
                    stack.append((child, False))
            else:
                # The node can be colored in any color, and each child's subtree can be colored independently
                # But if the node's color is c, all children must also be c (or their subtrees must be monochromatic with c)
                # So for each color c for the node, the number of ways is product of:
                # (number of ways child's subtree is monochromatic with c) for all children
                # Plus, if the node is a leaf, it's just 1 for each color
                total_ways = [0] * (k + 1)
                for color in range(1, k + 1):
                    ways = 1
                    for child in children[node]:
                        # The child's subtree must be monochromatic with 'color'
                        # So the child must be 'color', and all its descendants must be 'color'
                        # But since we're doing bottom-up, dp[child][color] already represents the number of ways
                        # the subtree rooted at child is monochromatic with color 'color'
                        ways = (ways * dp[child][color]) % MOD
                    total_ways[color] = ways

                # Now, the node can also be colored differently from its parent (if it's not the root)
                # But the condition requires that if two nodes have the same color, all nodes on the path between them must have the same color
                # This implies that