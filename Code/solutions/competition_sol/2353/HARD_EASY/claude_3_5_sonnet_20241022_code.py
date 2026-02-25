```python
def solve(n, arr):
    """
    Solves the permutation problem with non-equal subset sums.
    Returns -1 if no solution exists, otherwise returns valid permutation.
    Time complexity: O(n!)
    Space complexity: O(n)
    """
    def get_subset_sums(arr):
        # Get all subset sums except empty and full set
        sums = set()
        n = len(arr)
        for mask in range(1, (1 << n) - 1):
            subset_sum = 0
            for i in range(n):
                if mask & (1 << i):
                    subset_sum += arr[i]
            sums.add(subset_sum)
        return sums
    
    def check_valid(perm):
        # Check if permutation has different subset sums from original
        perm_sums = get_subset_sums(perm)
        orig_sums = get_subset_sums(arr)
        return len(perm_sums.intersection(orig_sums)) == 0
    
    def permutations(arr):
        # Generate all permutations
        if len(arr) <= 1:
            yield arr
        else:
            for i in range(len(arr)):
                arr[0], arr[i] = arr[i], arr[0]
                for perm in permutations(arr[1:]):
                    yield [arr[0]] + perm
                arr[0], arr[i] = arr[i], arr[0]
                
    # Special case for n=1
    if n == 1:
        return arr
    
    # Try all permutations
    arr_copy = arr.copy()
    for perm in permutations(arr_copy):
        if check_valid(perm):
            return perm
            
    return [-1]
```