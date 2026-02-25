```python
def find_kth_bit(n: int, k: int) -> str:
    """
    Find the kth bit in the nth string Sn using the given rules for string construction.
    """
    def generate_length(n: int) -> int:
        """Calculate length of string Sn"""
        if n == 1:
            return 1
        return 2 * generate_length(n-1) + 1
    
    def find_bit(n: int, k: int) -> str:
        """Recursively find bit at position k in string Sn"""
        if n == 1:
            return "0"
            
        prev_len = generate_length(n-1)
        mid = prev_len + 1
        
        if k == mid:
            return "1"
        elif k < mid:
            return find_bit(n-1, k)
        else:
            # For positions after midpoint, use inverted and reversed version of first half
            k_mirror = 2*mid - k
            bit = find_bit(n-1, k_mirror)
            return "1" if bit == "0" else "0"
            
    return find_bit(n, k)
```