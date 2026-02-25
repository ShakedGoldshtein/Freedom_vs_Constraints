```python
def find_kth_bit(n, k):
    length = (1 << n) - 1
    return _find_kth_bit_recursive(k, length)

def _find_kth_bit_recursive(k, length):
    if length == 1:
        return "0"
    
    mid = (length + 1) // 2
    
    if k == mid:
        return "1"
    elif k < mid:
        return _find_kth_bit_recursive(k, mid - 1)
    else:
        inverted_bit = _find_kth_bit_recursive(length - k + 1, mid - 1)
        return "1" if inverted_bit == "0" else "0"

def solve(n, k):
    if n < 1 or k < 1 or k > (1 << n) - 1:
        raise ValueError("Invalid input: n must be >= 1 and k must be between 1 and 2^n - 1")
    
    return find_kth_bit(n, k)
```