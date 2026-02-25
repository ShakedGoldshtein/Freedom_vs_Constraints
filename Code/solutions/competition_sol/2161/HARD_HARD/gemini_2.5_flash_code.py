```python
import collections

class DSU:
    """
    Disjoint Set Union (DSU) data structure to manage friendship groups.
    Each set (group) stores its total weight, total beauty, and
    a list of individual (weight, beauty) pairs for Hoses within the group.
    """
    def __init__(self, n: int, weights: list[int], beauties: list[int]):
        """
        Initializes the DSU with n Hoses.
        Each Hos starts as its own group.

        Args:
            n: The number of Hoses (0-indexed).
            weights: List of weights for each Hos.
            beauties: List of beauties for each Hos.
        """
        self.parent = list(range(n))
        # Each group_info[i] stores data for the group whose root is i:
        # 'total_w': sum of weights of all Hoses in the group
        # 'total_b': sum of beauties of all Hoses in the group
        # 'individuals': list of (weight, beauty) for each Hos in the group
        self.group_info = [
            {
                'total_w': weights[i],
                'total_b': beauties[i],
                'individuals': [(weights[i], beauties[i])]
            } for i in range(n)
        ]

    def find(self, i: int) -> int:
        """
        Finds the representative (root) of the set containing element i
        with path compression.

        Args:
            i: The 0-indexed Hos ID.

        Returns:
            The 0-indexed representative of the set.
        """
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        """
        Unites the sets containing elements i and j.
        Merges group information from root_j into root_i.

        Args:
            i: The 0-indexed Hos ID.
            j: The 0-indexed Hos ID.

        Returns:
            True if a union occurred, False otherwise (i and j were already in the same set).
        """
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Merge root_j's group into root_i's group
            self.parent[root_j] = root_i
            self.group_info[root_i]['total_w'] += self.group_info[root_j]['total_w']
            self.group_info[root_i]['total_b'] += self.group_info[root_j]['total_b']
            self.group_info[root_i]['individuals'].extend(self.group_info[root_j]['individuals'])
            # Note: For efficiency, group_info[root_j] is not explicitly cleared.
            # We will only iterate over actual roots (parent[k] == k) later to get valid groups.
            return True
        return False


def solve_mehrdad_hoses(
    n: int,
    m: int,
    max_weight_capacity: int,
    weights: list[int],
    beauties: list[int],
    friendship_pairs: list[tuple[int, int]]
) -> int:
    """
    Calculates the maximum possible total beauty of Hoses Mehrdad can invite,
    adhering to friendship group rules and a maximum total weight capacity.

    The rules are: from each friendship group, Mehrdad can either invite all Hoses,
    or no more than one.

    Args:
        n: The total number of Hoses (1-indexed for input, converted to 0-indexed internally).
        m: The number of friendship pairs.
        max_weight_capacity: The maximum total weight the amphitheater can hold.
        weights: A list of n integers, where weights[i] is the weight of Hos i+1.
        beauties: A list of n integers, where beauties[i] is the beauty of Hos i+1.
        friendship_pairs: A list of m tuples (u, v), meaning Hos u and Hos v are friends.
                          Hoses are 1-indexed in this list.

    Returns:
        The maximum possible total beauty achievable.
    """
    # Input parameter validation (for robustness, not strictly required by prompt for competitive programming)
    if not (1 <= n <= 1000 and 0 <= m <= min(n * (n - 1) // 2, 10**5) and 1 <= max_weight_capacity <= 1000):
        # In a production system, this would likely raise an error or log a warning.
        # For competitive programming, inputs usually adhere to constraints.
        pass
    if not (len(weights) == n and len(beauties) == n):
        # Handle inconsistent input sizes if necessary.
        pass

    # Step 1: Identify friendship groups using DSU
    dsu = DSU(n, weights, beauties)

    for u, v in friendship_pairs:
        # Convert 1-indexed Hoses from input to 0-indexed for DSU
        dsu.union(u - 1, v - 1)

    # Collect all unique friendship groups (those whose index is still their own parent).
    # Each group in 'friendship_groups' contains:
    #   'total_w': weight if all Hoses in the group are invited
    #   'total_b': beauty if all Hoses in the group are invited
    #   'individuals': list of (w_i, b_i) for each Hos in the group
    friendship_groups = []
    for i in range(n):
        if dsu.parent[i] == i:  # If i is a root, it represents a unique friendship group
            friendship_groups.append(dsu.group_info[i])

    # Step 2: Solve using Dynamic Programming (0/1 Knapsack variant for groups)
    # dp[j] stores the maximum beauty achievable with a total weight of exactly j.
    # Initialize dp table with 0s, meaning 0 beauty for any weight if no Hoses are invited.
    dp = [0] * (max_weight_capacity + 1)

    for group in friendship_groups:
        # For each group, we have several mutually exclusive options:
        # A) Invite all Hoses in the group.
        # B) Invite exactly one specific Hos from the group.
        # C) Invite no Hoses from the group (implicitly handled by dp[j] not changing).

        # Compile all (weight, beauty) pairs for options A and B for the current group.
        group_options = []

        # Option A: Add the (total weight, total beauty) of inviting all Hoses in this group.
        # Only consider if the total weight is within the maximum allowed capacity.
        if group['total_w'] <= max_weight_capacity:
            group_options.append((group['total_w'], group['total_b']))
        
        # Option B: Add (weight, beauty) for each individual Hos in this group.
        # Only consider if the individual Hos's weight is within the maximum allowed capacity.
        for w_h, b_h in group['individuals']:
            if w_h <= max_weight_capacity:
                group_options.append((w_h, b_h))

        # Update the DP table using the collected group_options.
        # Iterate 'j' (current total weight) downwards. This is crucial for a 0/1 knapsack
        # type update, ensuring that when we calculate dp[j], dp[j - w_opt] refers
        # to a state obtained *before* considering the current group.
        for j in range(max_weight_capacity, -1, -1):
            for w_opt, b_opt in group_options:
                if j >= w_opt:
                    # Update dp[j] by comparing its current value (representing not taking
                    # any option from the current group, or a previously better option
                    # from the current group) with the value obtained by taking
                    # the current option (w_opt, b_opt) from this group.
                    dp[j] = max(dp[j], dp[j - w_opt] + b_opt)
    
    # The maximum beauty achievable is the largest value in the dp table,
    # as dp[j] represents the maximum beauty for weight j.
    return max(dp)

```