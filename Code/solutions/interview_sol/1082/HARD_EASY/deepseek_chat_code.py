```python
from collections import defaultdict, deque

class MagicalTree:
    def __init__(self, n, sweetness):
        self.n = n
        self.sweetness = [0] + sweetness
        self.graph = defaultdict(list)
        self.parent = [0] * (n + 1)
        self.depth = [0] * (n + 1)
        self.subtree_sum = [0] * (n + 1)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def build_tree(self):
        stack = [(1, 0)]
        visited = [False] * (self.n + 1)
        visited[1] = True
        
        while stack:
            node, par = stack.pop()
            self.parent[node] = par
            for neighbor in self.graph[node]:
                if neighbor != par:
                    self.depth[neighbor] = self.depth[node] + 1
                    visited[neighbor] = True
                    stack.append((neighbor, node))
    
    def precompute_subtree_sums(self):
        order = []
        stack = [(1, 0, False)]
        
        while stack:
            node, par, visited = stack.pop()
            if visited:
                self.subtree_sum[node] = self.sweetness[node]
                for child in self.graph[node]:
                    if child != par:
                        self.subtree_sum[node] += self.subtree_sum[child]
            else:
                stack.append((node, par, True))
                for child in self.graph[node]:
                    if child != par:
                        stack.append((child, node, False))
    
    def update_sweetness(self, node, new_sweetness):
        diff = new_sweetness - self.sweetness[node]
        self.sweetness[node] = new_sweetness
        
        current = node
        while current != 0:
            self.subtree_sum[current] += diff
            current = self.parent[current]
    
    def get_total_sweetness(self, node):
        return self.subtree_sum[node]

def solve(n, sweetness_list, edges, queries):
    tree = MagicalTree(n, sweetness_list)
    
    for u, v in edges:
        tree.add_edge(u, v)
    
    tree.build_tree()
    tree.precompute_subtree_sums()
    
    results = []
    for query in queries:
        if query[0] == 1:
            node = query[1]
            results.append(tree.get_total_sweetness(node))
        else:
            node, new_sweetness = query[1], query[2]
            tree.update_sweetness(node, new_sweetness)
    
    return results
```