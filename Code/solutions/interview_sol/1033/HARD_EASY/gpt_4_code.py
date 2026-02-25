```python
def find_min_change(num_nodes, node_values):
    leaf_nodes = num_nodes // 2 + num_nodes % 2
    leaf_values = node_values[-leaf_nodes:]
    total = sum(leaf_values)
    target = total // leaf_nodes
    remainder = total % leaf_nodes

    changes = sorted([abs(value - target - (1 if i < remainder else 0)) for i, value in enumerate(leaf_values)])

    return sum(changes[i] for i in range(leaf_nodes - 1, -1, -2))

```