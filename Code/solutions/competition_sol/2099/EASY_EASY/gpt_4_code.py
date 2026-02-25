Here is the Python code based on the given requirements:

```python
def solve(n, k):
    permutation = [i+1 for i in range(k+1)]
    permutation[1::2] = permutation[1::2][::-1]
    permutation.extend(list(range(k+2, n+1)))
    return permutation
```
This function calculates the permutation that meets the given requirements. It initially generates the permutation by first creating a list of integers from 1 to k+1. It then reverses the order of every second element. After that, it appends the remaining elements from k+2 to n to the permutation. The function finally returns the generated permutation.
