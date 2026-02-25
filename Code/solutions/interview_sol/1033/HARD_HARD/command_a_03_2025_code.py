```python
def solve(n: int, leaf_values: list[int]) -> int:
    """
    Calculate the minimum change required to make all leaf nodes of a complete binary tree have the same value.

    Args:
        n (int): Total number of nodes in the binary tree.
        leaf_values (list[int]): List of values at the leaf nodes.

    Returns:
        int: The minimum change required to make all leaf nodes have the same value.
    """
    if n == 1:
        return 0  # No change needed for a single node

    # Calculate the target value for all leaf nodes
    total_sum = sum(leaf_values)
    target = total_sum / len(leaf_values)

    # Calculate the total change required
    change = sum(abs(val - target) for val in leaf_values)

    # Since the sum of changes at leaf nodes must be balanced by changes at internal nodes,
    # the minimum change is half of the total change at leaf nodes.
    return change // 2
```