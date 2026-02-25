```python
class DSU:
    """
    A Disjoint Set Union (DSU) data structure optimized for tracking parity
    differences between elements.
    Each element `i` in the DSU is assigned a `parity_diff[i]` value,
    representing `(A[i] - A[parent[i]]) % 2`.
    This allows determining the parity of `(A[i] - A[j]) % 2` for any `i` and `j`
    if they are in the same connected component.
    """

    def __init__(self, n: int):
        """
        Initializes the DSU with `n` elements.
        Each element is initially in its own set, with a parent pointing to itself
        and a parity difference of 0.

        Args:
            n: The number of elements in the DSU (0-indexed).
        """
        self.parent = list(range(n))
        self.parity_diff = [0] * n  # Stores (A[i] - A[parent[i]]) % 2

    def find(self, i: int) -> tuple[int, int]:
        """
        Finds the root of the set containing element `i` and computes the
        parity of `(A[i] - A[root]) % 2` using path compression.

        Args:
            i: The element to find the root for.

        Returns:
            A tuple containing:
            - The root of the set containing `i`.
            - The parity of `(A[i] - A[root]) % 2`.
        """
        if self.parent[i] == i:
            return i, 0  # `i` is its own root, so difference is 0
        
        # Recursively find the root and update parent for path compression
        root, diff_from_parent_to_root = self.find(self.parent[i])
        
        # A[i] - A[root] = (A[i] - A[parent[i]]) + (A[parent[i]] - A[root])
        # So, (A[i] - A[root]) % 2 = (current parity_diff[i] + diff_from_parent_to_root) % 2
        self.parity_diff[i] = (self.parity_diff[i] + diff_from_parent_to_root) % 2
        self.parent[i] = root
        
        return root, self.parity_diff[i]

    def union(self, i: int, j: int, required_val_parity: int) -> bool:
        """
        Unites the sets containing elements `i` and `j`, or checks for consistency
        if they are already in the same set.
        The `required_val_parity` specifies `(A[i] - A[j]) % 2`.

        Args:
            i: The first element (0-indexed).
            j: The second element (0-indexed).
            required_val_parity: The expected parity of `(A[i] - A[j]) % 2`.
                                 0 if `A[i]` and `A[j]` must have the same parity.
                                 1 if `A[i]` and `A[j]` must have different parities.

        Returns:
            True if the union operation is successful or consistent, False if an
            inconsistency is detected.
        """
        root_i, diff_i_to_root_parity = self.find(i)
        root_j, diff_j_to_root_parity = self.find(j)

        if root_i != root_j:
            # Union the two components. Make `root_i` the parent of `root_j`.
            self.parent[root_j] = root_i
            
            # We want (A[i] - A[j]) % 2 == required_val_parity
            # (A[root_i] + diff_i_to_root_parity) - (A[root_j] + diff_j_to_root_parity) % 2 == required_val_parity
            # Rearranging for (A[root_j] - A[root_i]) % 2, which will be stored in parity_diff[root_j]:
            # (A[root_j] - A[root_i]) % 2 == (diff_i_to_root_parity - diff_j_to_root_parity - required_val_parity) % 2
            # Adding 2 ensures the result before modulo is non-negative
            self.parity_diff[root_j] = (diff_i_to_root_parity - diff_j_to_root_parity - required_val_parity + 2) % 2
            return True
        else:
            # `i` and `j` are already in the same component.
            # Check if the existing parity relationship is consistent with `required_val_parity`.
            # The current parity difference (A[i] - A[j]) % 2 is:
            # ((A[root_i] + diff_i_to_root_parity) - (A[root_j] + diff_j_to_root_parity)) % 2
            # Since root_i == root_j, this simplifies to (diff_i_to_root_parity - diff_j_to_root_parity) % 2
            current_relative_parity = (diff_i_to_root_parity - diff_j_to_root_parity + 2) % 2
            return current_relative_parity == required_val_parity


def solve(n: int, q_queries: list[tuple[int, int, int]]) -> str:
    """
    Determines if a partially filled matrix B can be completed to be a "good" matrix.

    A matrix B (N x N) is good if there exists an array A (N elements) such that
    B[i][j] = |A[i] - A[j]| for all i, j.
    Given Q entries B[i][j] (0 or 1), this function checks if a consistent
    array A can be formed. It relies on the property that B[i][j] = 0 implies
    A[i] and A[j] have the same parity, and B[i][j] = 1 implies A[i] and A[j]
    have different parities.

    Args:
        n: The dimension of the N x N matrix B.
        q_queries: A list of tuples `(i, j, val)`, where `B[i][j]` is filled
                   with `val`. Indices `i` and `j` are 1-based.

    Returns:
        "yes" if it's possible to complete the matrix to be good, "no" otherwise.
    """
    dsu = DSU(n) # Initialize DSU for N elements (0-indexed: 0 to N-1)

    for r_idx, c_idx, val in q_queries:
        # Convert 1-based indices to 0-based
        i = r_idx - 1
        j = c_idx - 1

        # Constraint 1: B[k][k] must always be 0.
        # If B[i][i] is given as 1, it's an immediate contradiction.
        if i == j:
            if val == 1:
                return "no"
            # If val is 0 for B[i][i], it's always consistent (A[i]=A[i]), so no action needed.
            continue

        # Determine the required parity of (A[i] - A[j]) based on `val`.
        # If val = 0: |A[i] - A[j]| = 0 => A[i] = A[j] => (A[i] - A[j]) % 2 = 0
        # If val = 1: |A[i] - A[j]| = 1 => A[i] != A[j], and A[i], A[j] differ by 1.
        # This implies (A[i] - A[j]) % 2 = 1.
        required_val_parity = 0 if val == 0 else 1

        # Attempt to unite the components for i and j with the required parity relationship.
        # If an inconsistency is detected during union, it's impossible.
        if not dsu.union(i, j, required_val_parity):
            return "no"

    # If all queries are processed without detecting any inconsistency, it's possible.
    return "yes"

```