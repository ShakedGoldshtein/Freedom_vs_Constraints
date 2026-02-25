```python
def find_kth_bit(n: int, k: int) -> str:
    def helper(n, k):
        if n == 1:
            return '0'
        length = 2 ** n - 1
        mid = (length + 1) // 2
        if k == mid:
            return '1'
        elif k < mid:
            return helper(n - 1, k)
        else:
            inverted = helper(n - 1, length - k + 1)
            return '1' if inverted == '0' else '0'
    return helper(n, k)
```