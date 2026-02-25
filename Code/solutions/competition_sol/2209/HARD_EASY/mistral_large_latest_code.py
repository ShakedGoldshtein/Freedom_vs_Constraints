```python
import sys
from collections import deque

def solve(n, edges):
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    # Find all leaves
    leaves = []
    for i in range(1, n + 1):
        if len(adj[i]) == 1:
            leaves.append(i)

    # Function to compute min and max f
    def compute_f():
        # Case 1: All leaves have a common ancestor (star-like or path)
        # Min f is 1 (all edges same weight)
        # Max f is number of edges (all edges different weights)

        # Case 2: Leaves have multiple common ancestors (general tree)
        # Min f is number of leaves - 1 (using XOR properties)
        # Max f is number of edges (all edges different weights)

        # Compute the minimal f: number of leaves - 1
        min_f = len(leaves) - 1 if len(leaves) > 1 else 1

        # Compute the maximal f: number of edges
        max_f = n - 1

        # Special case: if tree is a path (all leaves are endpoints of a path)
        # Then min_f is 1 (all edges same weight)
        if is_path_tree(adj, n):
            min_f = 1

        return min_f, max_f

    def is_path_tree(adj, n):
        # Check if the tree is a path (all nodes have degree <= 2)
        degree_two_count = 0
        for i in range(1, n + 1):
            if len(adj[i]) > 2:
                return False
            if len(adj[i]) == 2:
                degree_two_count += 1
        return degree_two_count == n - 2

    return compute_f()

def solve_problem(n, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    leaves = []
    for i in range(1, n + 1):
        if len(adj[i]) == 1:
            leaves.append(i)

    # Compute minimal f
    if len(leaves) == 2:
        min_f = 1
    else:
        # Find the minimal number of distinct weights needed
        # This is equivalent to the number of edges in the minimal spanning tree of the leaves
        # Which is (number of leaves - 1)
        min_f = len(leaves) - 1

    # Compute maximal f
    max_f = n - 1

    # Special case: if the tree is a star, min_f is 1
    if is_star_tree(adj, n):
        min_f = 1

    # Another special case: if the tree is a path, min_f is 1
    if is_path_tree(adj, n):
        min_f = 1

    return min_f, max_f

def is_star_tree(adj, n):
    center = -1
    for i in range(1, n + 1):
        if len(adj[i]) == n - 1:
            center = i
            break
    if center == -1:
        return False
    for i in range(1, n + 1):
        if i != center and len(adj[i]) != 1:
            return False
    return True

def is_path_tree(adj, n):
    degree_two_count = 0
    for i in range(1, n + 1):
        if len(adj[i]) > 2:
            return False
        if len(adj[i]) == 2:
            degree_two_count += 1
    return degree_two_count == n - 2

def solve_final(n, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    leaves = []
    for i in range(1, n + 1):
        if len(adj[i]) == 1:
            leaves.append(i)

    # Minimal f is 1 if the tree is a star or a path, else number of leaves - 1
    if is_star_tree(adj, n) or is_path_tree(adj, n):
        min_f = 1
    else:
        min_f = len(leaves) - 1

    # Maximal f is always the number of