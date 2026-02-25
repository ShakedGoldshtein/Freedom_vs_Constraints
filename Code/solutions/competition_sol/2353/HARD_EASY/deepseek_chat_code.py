```python
def solve(n, a):
    def next_permutation(arr):
        i = len(arr) - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i < 0:
            return False
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1:] = reversed(arr[i + 1:])
        return True

    def compute_subset_sums(arr):
        total = sum(arr)
        possible = [False] * (total + 1)
        possible[0] = True
        for num in arr:
            for s in range(total, num - 1, -1):
                if possible[s - num]:
                    possible[s] = True
        return possible

    def is_valid_permutation(a, b):
        sum_a = compute_subset_sums(a)
        sum_b = compute_subset_sums(b)
        for s in range(1, len(sum_a)):
            if sum_a[s] and sum_b[s]:
                return False
        return True

    a_sorted = sorted(a)
    b = a_sorted[:]
    
    if n == 1:
        return [-1]
    
    found = False
    while True:
        if not is_valid_permutation(a_sorted, b):
            found = True
            break
        if not next_permutation(b):
            break
    
    if found:
        return b
    else:
        return [-1]
```