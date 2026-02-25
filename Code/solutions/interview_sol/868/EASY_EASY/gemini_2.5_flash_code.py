```python
import math

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1) # Fenwick tree is 1-indexed
        self.size = size

    def update(self, index, delta):
        """Adds delta to the element at `index`."""
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)

    def find_kth_element(self, k):
        """
        Finds the smallest index `idx` such that the cumulative sum from 1 to `idx` is >= k.
        This effectively finds the k-th smallest element (1-indexed k).
        Time complexity: O(log self.size) using binary lifting.
        """
        if k <= 0:
            # If k is non-positive, which should not happen based on constraints (K >= 1).
            # Return 1 as a safe default, as A_i values are >= 1.
            return 1 
        
        current_sum = 0
        pos = 0
        
        # Find the largest power of 2 less than or equal to self.size.
        # This determines the initial step size for binary lifting.
        pw = 1
        while pw <= self.size:
            pw *= 2
        pw //= 2 

        # Perform binary lifting
        while pw > 0:
            # Check if taking a step of size `pw` (to `pos + pw`)
            # is within the tree's bounds and if the sum up to `pos + pw`
            # would still be less than `k`.
            if pos + pw <= self.size and current_sum + self.tree[pos + pw] < k:
                current_sum += self.tree[pos + pw]
                pos += pw
            pw //= 2
        
        # After the loop, `pos` is the largest index such that the sum up to `pos` is < k.
        # Therefore, `pos + 1` is the smallest index such that the sum up to `pos + 1` is >= k.
        # This `pos + 1` corresponds to the value of the k-th smallest element.
        return pos + 1

MAX_A_VAL = 2000 # Maximum possible value for A_i

def solve(N, K, A):
    beautiful_subarrays_count = 0

    # Iterate through all possible starting positions (l) of a subarray
    for l in range(N):
        # `current_counts` stores the frequencies of elements in the current subarray S = A[l...r].
        # `A_i` values are 1-indexed (1 to MAX_A_VAL), so `current_counts` is sized accordingly.
        current_counts = [0] * (MAX_A_VAL + 1)
        
        # Fenwick tree to maintain cumulative counts for values 1 to MAX_A_VAL.
        # This allows efficient querying for the k-th smallest element.
        ft = FenwickTree(MAX_A_VAL)
        
        # Iterate through all possible ending positions (r) of a subarray, starting from l
        for r in range(l, N):
            val_ar = A[r] # The new element to be added to the subarray
            
            # Update frequencies and Fenwick tree for the current subarray A[l...r]
            current_counts[val_ar] += 1
            ft.update(val_ar, 1) # Add A[r] to the Fenwick tree
            
            L = r - l + 1 # Length of the current subarray S

            # Calculate `m`: smallest integer such that m * L >= K
            # Using integer division for ceiling: (numerator + denominator - 1) // denominator
            m = (K + L - 1) // L
            
            # `X` is the K-th smallest element in `B`, where `B` is `S` repeated `m` times.
            # This is equivalent to finding the `needed_cumulative_count`-th smallest element in `S`.
            # We need the smallest value `X` such that `m * (count of elements <= X in S) >= K`.
            # This simplifies to `(count of elements <= X in S) >= K / m`.
            # The smallest integer value for `(count of elements <= X in S)` is `ceil(K/m)`.
            needed_cumulative_count = (K + m - 1) // m
            
            # Find X using the Fenwick tree's `find_kth_element` method
            X = ft.find_kth_element(needed_cumulative_count)
            
            # `F` is the number of occurrences of `X` in `S`.
            F = current_counts[X]
            
            # Check if `S` is beautiful: "F occurs in S at least once."
            # This means the *value* `F` (the count) must be present in `S`.
            # `F` must be a valid index (1 to MAX_A_VAL) for `current_counts`.
            # `current_counts[F] >= 1` verifies that the value `F` is present in `S`.
            if 1 <= F <= MAX_A_VAL and current_counts[F] >= 1:
                beautiful_subarrays_count += 1
                
    return beautiful_subarrays_count

```