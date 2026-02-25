```python
import math

def _get_leaf_depth_multiplier(node_index: int) -> int:
    """
    Calculates the depth multiplier (depth + 1) for a given leaf node index
    in a 0-indexed complete binary tree.
    The root is at depth 0.
    
    Args:
        node_index: The 0-indexed array index of the leaf node.
    
    Returns:
        The depth of the node plus one.
    """
    # For a 0-indexed complete binary tree, the depth of node at index 'i' is floor(log2(i+1)).
    # Example:
    # Node 0 (root): log2(1)=0, depth 0
    # Nodes 1,2: log2(2)=1, log2(3) approx 1.58 -> floor(1.58)=1, depth 1
    # Nodes 3,4,5,6: log2(4)=2, ..., log2(7) approx 2.8 -> floor(2.8)=2, depth 2
    
    # If node_index is 0, log2(1) is 0. This works directly.
    # We add 1 to depth to get the multiplier as per problem definition.
    depth = math.floor(math.log2(node_index + 1))
    return depth + 1

def calculate_min_total_tree_change(n_total_nodes: int, leaf_values: list[int]) -> int:
    """
    Calculates the minimum change needed in the sum of all node values in a complete
    binary tree such that all leaf nodes have the same value.

    The tree adheres to the property: value(parent) = value(left_child) + value(right_child).
    This implies the value of any node is the sum of its descendant leaf values.
    The total sum of all nodes in such a tree is sum(leaf_value_i * (depth_i + 1)).

    Args:
        n_total_nodes: The total number of nodes in the complete binary tree (N in prompt).
        leaf_values: A list of integer values for the leaf nodes, ordered from
                     left-most to right-most. The number of values in this list
                     must be equal to ceil(n_total_nodes / 2) to maintain consistency
                     with a complete binary tree definition.

    Returns:
        The minimum non-negative integer change (difference) in the total sum of
        all nodes required to make all leaf node values equal.

    Raises:
        ValueError: If n_total_nodes is less than 1, or if the number of
                    provided leaf_values does not match the expected count
                    for a complete binary tree with n_total_nodes.
    """
    if n_total_nodes < 1:
        raise ValueError("Number of nodes must be at least 1.")

    # Calculate the expected number of leaf nodes for a complete binary tree with N_total_nodes.
    # In a complete binary tree with N nodes, the number of leaf nodes L is ceil(N/2).
    expected_leaf_count = math.ceil(n_total_nodes / 2)

    if len(leaf_values) != expected_leaf_count:
        # This check ensures consistency between n_total_nodes and the provided leaf_values list.
        # If the number of provided leaf values does not match the expected count for a complete
        # binary tree with n_total_nodes, the input is considered ill-formed for the problem's
        # geometric constraints.
        raise ValueError(
            f"Provided leaf_values count ({len(leaf_values)}) does not match "
            f"expected count ({expected_leaf_count}) for a complete binary tree with {n_total_nodes} nodes."
        )

    # In a 0-indexed array representation of a complete binary tree,
    # leaf nodes are located at indices from floor(N/2) to N-1.
    leaf_start_index = n_total_nodes // 2

    s_total_original = 0  # Sum of all node values in the original tree
    k_sum_of_multipliers = 0  # Sum of (depth + 1) for all leaves, which is the multiplier for target X

    # Iterate through the provided leaf values and their corresponding indices
    for i, current_leaf_value in enumerate(leaf_values):
        # Calculate the actual 0-indexed array position for the current leaf
        node_index = leaf_start_index + i
        
        # Determine how many times this leaf's value contributes to the total tree sum
        # (itself + its ancestors)
        depth_multiplier = _get_leaf_depth_multiplier(node_index)
        
        s_total_original += current_leaf_value * depth_multiplier
        k_sum_of_multipliers += depth_multiplier

    # If there are no leaves (should not happen for n_total_nodes >= 1), no change needed.
    if k_sum_of_multipliers == 0:
        return 0

    # To minimize the change |S_total_new - S_total_original|, the new total sum
    # S_total_new = X * k_sum_of_multipliers, where X is the target value for all leaves.
    # X should be chosen as an integer closest to S_total_original / k_sum_of_multipliers.
    
    target_x_float = s_total_original / k_sum_of_multipliers
    
    # Check the two integer values closest to target_x_float
    x1 = math.floor(target_x_float)
    x2 = math.ceil(target_x_float)

    # Calculate the total sum of the tree if all leaves were X1
    s_total_new1 = x1 * k_sum_of_multipliers
    # Calculate the total sum of the tree if all leaves were X2
    s_total_new2 = x2 * k_sum_of_multipliers

    # Calculate the absolute difference from the original total sum for both possibilities
    change1 = abs(s_total_new1 - s_total_original)
    change2 = abs(s_total_new2 - s_total_original)

    # The minimum change is the smaller of the two differences
    return min(change1, change2)
```