```python
import sys
from math import gcd
from functools import lru_cache

def solve():
    def compute_max_cost(arr):
        n = len(arr)
        if n == 1:
            return arr[0] % (10**9 + 7)  # edge case, though constraints say N >= 2

        arr_sorted = sorted(arr)
        max_cost = 0

        # Precompute prefix mod products for all possible starting elements
        # The key observation is that the optimal ordering will have the largest elements
        # towards the end to minimize the mod operations' reduction effect

        # We'll try all possible last elements (since the last mod is critical)
        # and for each, try to arrange the remaining elements optimally

        # To optimize, we can use memoization or dynamic programming, but for N <= 5e5,
        # we need a smarter approach. The optimal ordering is likely to have the largest
        # elements at the end, but not necessarily in sorted order.

        # The maximum possible cost is the maximum element itself (when it's last)
        # or some combination where earlier mods don't reduce it too much.

        # So we can try all possible last elements, and for each, arrange the rest
        # in a way that maximizes the intermediate mods.

        # But for large N, this is O(N^2), which is not feasible for N=5e5.
        # So we need a better approach.

        # Key insight: The maximum cost is likely achieved when the largest element is last,
        # and the second largest is second last, etc., but not always.
        # However, for N=2, it's max(a, b) % min(a, b) if a != b, but the sample shows
        # that the order matters differently.

        # Alternative approach: The maximum cost is the maximum element in the array,
        # because you can arrange the array so that the largest element is last, and
        # the previous elements are such that their mods don't reduce the value below the max.
        # For example, if the max is M, and you have elements a1, a2, ..., a_{k} < M,
        # then you can arrange them in any order before M, and the result will be
        # (((a1 mod a2) mod a3) ... mod M). But since a_i < M, the final mod M could be up to M-1.
        # But the maximum possible is M-1, but the sample shows that sometimes the max is M itself
        # (when M is first, but then the next mod would reduce it).

        # Wait, in the sample, the max is 12, but the answer is 7, which is less than 12.
        # So the maximum cost is not necessarily the maximum element.

        # Another observation: the cost is always less than the largest element in the array,
        # because the last mod is by the largest element in the current ordering.

        # So the maximum possible cost is the second largest element in the array,
        # because if you arrange the array in descending order, the cost would be
        # (((a1 mod a2) mod a3) ... mod aN), where a1 > a2 > ... > aN.
        # The first mod is a1 % a2 = a1 - k*a2, which is < a2.
        # Then the next mod is (result) % a3, which is < a3, and so on.
        # So the final result is less than aN (the smallest element in the descending order).
        # But this contradicts the sample, where the answer is 7, which is the smaller of the two elements.

        # Wait, in the sample, the array is [7, 12]. If we arrange it in descending order [12, 7],
        # the cost is 12 % 7 = 5. If we arrange it as [7, 12], the cost is 7 % 12 = 7.
        # So the maximum cost is 7, which is the smaller element.

        # Hmm, so the maximum cost is not necessarily related to the largest element.
        # Maybe the maximum cost is the second largest element in the array.

        # Let's think differently: the cost is a series of mods. The maximum possible value
        # of the cost is limited by the smallest element in the array, because the last mod
        # is by some element, and the result must be less than that element.

        # But in the sample, the smallest element is 7, and the answer is 7, which is