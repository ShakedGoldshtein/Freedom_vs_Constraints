```python
def thirt(n):
    pattern = [1, 10, 9, 12, 3, 4]
    
    def process_number(num):
        digits = [int(d) for d in str(num)][::-1]
        total = 0
        for i, digit in enumerate(digits):
            pattern_index = i % len(pattern)
            total += digit * pattern[pattern_index]
        return total
    
    current = n
    previous = None
    
    while current != previous:
        previous = current
        current = process_number(current)
    
    return current
```