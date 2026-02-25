```python
def findKthBit(n, k):
    if n == 1:
        return "0"
    
    length = (1 << n) - 1
    mid = length // 2 + 1
    
    if k == mid:
        return "1"
    elif k < mid:
        return findKthBit(n - 1, k)
    else:
        prev = findKthBit(n - 1, length - k + 1)
        return "1" if prev == "0" else "0"
```