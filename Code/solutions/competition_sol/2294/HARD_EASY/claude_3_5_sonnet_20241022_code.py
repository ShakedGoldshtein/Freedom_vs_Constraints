```python
def solve(n, pairs):
    """
    Find minimum possible value of (Rmax - Rmin) * (Bmax - Bmin)
    where R and B are sets of red and blue painted numbers
    
    Args:
        n: Number of bags/pairs
        pairs: List of (x,y) tuples representing numbers in each bag
    
    Returns:
        Minimum possible value of the product
    """
    all_nums = []
    for x, y in pairs:
        all_nums.extend([x, y])
    all_nums.sort()
    
    result = float('inf')
    
    # Try all possible divisions of numbers into red and blue groups
    for i in range(1 << (2*n)):
        if bin(i).count('1') != n:  # Must use exactly n numbers for each color
            continue
            
        red = []
        blue = []
        for j in range(2*n):
            # Check if jth bit is set
            if i & (1 << j):
                # Cannot use both numbers from same bag
                bag_idx = j//2
                other_idx = (bag_idx * 2) + (1 if j % 2 == 0 else 0)
                if i & (1 << other_idx):
                    break
                red.append(all_nums[j])
            else:
                blue.append(all_nums[j])
        
        if len(red) != n or len(blue) != n:
            continue
            
        r_diff = max(red) - min(red)
        b_diff = max(blue) - min(blue)
        result = min(result, r_diff * b_diff)
        
    return result

```