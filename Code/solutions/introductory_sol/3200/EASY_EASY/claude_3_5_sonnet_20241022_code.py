```python
def thirt(n):
    sequence = [1, 10, 9, 12, 3, 4]
    seq_len = len(sequence)
    
    def calc_sum(num):
        digits = [int(d) for d in str(num)[::-1]]
        total = 0
        for i, d in enumerate(digits):
            total += d * sequence[i % seq_len]
        return total
        
    prev = n
    while True:
        curr = calc_sum(prev)
        if curr == prev:
            return curr
        prev = curr
```