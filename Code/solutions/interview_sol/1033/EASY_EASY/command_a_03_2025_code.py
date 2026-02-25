```python
def solve(n: int, leaf_values: list[int]) -> int:
    """
    Calculate the minimum change required to make all leaf nodes of a complete binary tree have the same value.

    Args:
        n (int): Total number of nodes in the binary tree.
        leaf_values (list[int]): List of values at the leaf nodes of the tree.

    Returns:
        int: The minimum change required to make all leaf nodes have the same value.
    """
    if n == 1:
        return 0

    # Calculate the target value for all leaf nodes
    # The target value is the average of all leaf node values, rounded to the nearest integer
    target = round(sum(leaf_values) / len(leaf_values))

    # Calculate the total change required
    # The change is the sum of absolute differences between each leaf node value and the target
    total_change = sum(abs(val - target) for val in leaf_values)

    # Since the tree is complete and the sum of children equals the parent,
    # the total change is halved because each change propagates up the tree
    return total_change // 2
```