```python
def solve(x: int) -> int:
    count = 0
    k = 1
    
    while True:
        val_2k = 1 << k
        val_2k_minus_1 = 1 << (k - 1)
        
        num_stairs_n = val_2k - 1
        
        current_staircase_cost = num_stairs_n * val_2k_minus_1
        
        if current_staircase_cost > x:
            break
            
        x -= current_staircase_cost
        count += 1
        
        k += 1
        
    return count

```