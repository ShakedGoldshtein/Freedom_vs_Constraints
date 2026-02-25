```python
import math

class FenwickTree:
    """
    A Fenwick Tree (Binary Indexed Tree) implementation for efficient
    prefix sum queries and single-point updates.
    It supports finding the k-th smallest element.
    Values are expected to be 1-indexed for the Fenwick tree operations
    (e.g., if array values are 1 to MAX_VAL).
    """
    def __init__(self, max_val_for_bit: int):
        """
        Initializes the Fenwick Tree.
        :param max_val_for_bit: The maximum possible value an element can have.
                                 The tree will support values from 1 to max_val_for_bit.
        """
        self.max_val_for_bit = max_val_for_bit
        self.tree = [0] * (max_val_for_bit + 1)

    def update(self, val: int, delta: int):
        """
        Adds `delta` to the count of `val`.
        :param val: The value (1-indexed) to update.
        :param delta: The amount to add (can be positive or negative).
        """
        idx = val
        while idx <= self.max_val_for_bit:
            self.tree[idx] += delta
            idx += idx & (-idx)

    def query(self, val: int) -> int:
        """
        Calculates the prefix sum up to `val` (inclusive).
        :param val: The value (1-indexed) up to which the sum is calculated.
        :return: The sum of counts for all values from 1 to `val`.
        """
        idx = val
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & (-idx)
        return s

    def find_kth(self, k: int) -> int:
        """
        Finds the smallest value `v` such that the sum of counts for all values <= `v` is >= `k`.
        This is essentially finding the k-th order statistic.
        Assumes `k` is 1-indexed (e.g., 1 for the first element, 2 for the second).
        :param k: The 1-indexed rank of the element to find.
        :return: The 1-indexed value of the k-th smallest element. Returns -1 if k is
                 non-positive (which should not happen given problem constraints K >= 1,
                 leading to effective_k_in_s >= 1).
        """
        if k <= 0:
            return -1 # k-th element must be positive for rank
        
        # Binary search for the k-th element.
        # Start from potential index 0 (representing values less than 1), and build up by powers of 2.
        idx = 0
        
        # Find the largest power of 2 that is less than or equal to max_val_for_bit.
        # This determines the highest bit to start searching from in the implicit binary search.
        pos_bit = 1
        while pos_bit * 2 <= self.max_val_for_bit:
            pos_bit *= 2
        
        # Traverse down through powers of 2.
        while pos_bit > 0:
            # Check if taking a jump of 'pos_bit' would keep us within bounds
            # and if the k-th element is beyond the sum contained in tree[idx + pos_bit].
            # `self.tree[idx + pos_bit]` represents the sum of frequencies
            # in a block (or range) ending at `idx + pos_bit`.
            if idx + pos_bit <= self.max_val_for_bit and k > self.tree[idx + pos_bit]:
                k -= self.tree[idx + pos_bit] # Reduce k by the count of elements in this block.
                idx += pos_bit               # Move `idx` to the end of this block.
            pos_bit //= 2
        
        # After the loop, `idx` is the largest index such that the prefix sum up to `idx` is < original k.
        # Therefore, `idx + 1` is the smallest value whose prefix sum is >= original k.
        return idx + 1


def solve(n: int, k: int, a: list[int]) -> int:
    """
    Calculates the number of beautiful subarrays for a given array A and integer K.

    A subarray S = [A_l, ..., A_r] is beautiful if the number of occurrences (F)
    of its K-th smallest element (X) in S, i.e., F, itself appears in S.

    Time Complexity: O(N^2 * log(MAX_A_VALUE))
    Space Complexity: O(MAX_A_VALUE)

    :param n: The length of the array A.
    :param k: The integer K used in the problem definition.
    :param a: The input array of N integers.
    :return: The total count of beautiful subarrays.
    """
    MAX_A_VALUE = 2000
    total_beautiful_subarrays = 0

    # Iterate over all possible starting positions l (0-indexed)
    for l in range(n):
        # Initialize Fenwick Tree and direct frequency count array for the current subarray A[l...r].
        # These structures will track frequencies for the subarray A[l...r] as r increases,
        # making updates and queries efficient.
        current_freq_counts = [0] * (MAX_A_VALUE + 1)
        fenwick_tree = FenwickTree(MAX_A_VALUE)

        # Iterate over all possible ending positions r (0-indexed) for the current l
        for r in range(l, n):
            current_element = a[r]

            # 1. Update frequency counts and Fenwick Tree for the current element A[r]
            # This incorporates A[r] into the subarray S = A[l...r].
            current_freq_counts[current_element] += 1
            fenwick_tree.update(current_element, 1)

            len_s = r - l + 1

            # 2. Calculate 'm', the number of times S is concatenated to form B.
            # 'm' is the smallest integer such that m * len_s >= K.
            # This is equivalent to ceil(K / len_s).
            m = (k + len_s - 1) // len_s

            # 3. Find 'X', the K-th smallest element of array B (S concatenated m times).
            # The frequencies of elements in B are m * freq_s[v].
            # To find the K-th element in B, we need to find the element v such that
            # m * (sum of freq_s[i] for i < v) < K <= m * (sum of freq_s[i] for i <= v).
            # This is equivalent to finding the (ceil(K/m))-th smallest element in S itself,
            # considering only the frequencies within S.
            effective_k_in_s = (k + m - 1) // m # This is ceil(K / m).

            # Find X using the Fenwick Tree, which operates on frequencies of S.
            # X will be a value from 1 to MAX_A_VALUE.
            X = fenwick_tree.find_kth(effective_k_in_s)
            
            # According to problem constraints (K >= 1, len_s >= 1), effective_k_in_s will always
            # be at least 1 and at most len_s (total elements in S). Thus, X will always be found.

            # 4. Calculate 'F', the number of occurrences of X in S.
            # Since X is an element present in S, F will always be >= 1.
            F = current_freq_counts[X]

            # 5. Check if S is beautiful.
            # S is beautiful if F occurs in S at least once.
            # This means the count of the numerical value F in S must be greater than 0.
            if current_freq_counts[F] > 0:
                total_beautiful_subarrays += 1

    return total_beautiful_subarrays

```