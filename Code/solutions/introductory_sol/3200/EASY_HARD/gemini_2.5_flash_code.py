```python
def thirt(n):
    REMAINDERS = [1, 10, 9, 12, 3, 4]
    
    current_num = n
    previous_num = -1  # Initialize with a value that won't match n initially to ensure loop runs at least once

    while current_num != previous_num:
        previous_num = current_num
        
        sum_of_products = 0
        num_str = str(current_num)
        
        # Iterate through the digits of the number from right to left
        for i in range(len(num_str)):
            # Get the digit from the rightmost position
            digit = int(num_str[len(num_str) - 1 - i])
            
            # Get the corresponding remainder from the repeating sequence
            remainder_val = REMAINDERS[i % len(REMAINDERS)]
            
            sum_of_products += digit * remainder_val
        
        current_num = sum_of_products
        
    return current_num

```