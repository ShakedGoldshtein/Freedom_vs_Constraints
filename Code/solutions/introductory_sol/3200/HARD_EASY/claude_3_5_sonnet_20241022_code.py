```python
def thirt(n):
    sequence = [1, 10, 9, 12, 3, 4]
    seq_len = len(sequence)
    
    def calc_remainder(num):
        digits = list(str(num))[::-1] # Reverse digits
        total = 0
        for i, d in enumerate(digits):
            seq_index = i % seq_len
            total += int(d) * sequence[seq_index]
        return total
        
    prev = n
    while True:
        curr = calc_remainder(prev)
        if curr == prev:
            return curr
        prev = curr
```