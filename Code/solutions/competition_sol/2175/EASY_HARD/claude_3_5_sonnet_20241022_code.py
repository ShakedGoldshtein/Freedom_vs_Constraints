```python
def solve(m, numbers):
    result = []
    basket = []
    
    def find_xor_sum(target, nums, curr_idx, curr_sum, used_indices):
        if curr_sum == target:
            return used_indices
        if curr_idx >= len(nums):
            return None
            
        # Try using current number
        next_sum = curr_sum ^ nums[curr_idx]
        used = find_xor_sum(target, nums, curr_idx + 1, next_sum, used_indices + [curr_idx])
        if used:
            return used
            
        # Try skipping current number    
        return find_xor_sum(target, nums, curr_idx + 1, curr_sum, used_indices)

    for i in range(m):
        curr_num = int(numbers[i])
        
        # First number always goes directly to basket
        if i == 0:
            result.append("0")
            basket.append(curr_num)
            continue
            
        # For each new number, check if it can be created from XOR of basket numbers
        indices = find_xor_sum(curr_num, basket, 0, 0, [])
        
        if indices:
            # If XOR representation found, output count and indices
            result.append(str(len(indices)) + " " + " ".join(map(str, indices)))
        else:
            # No XOR representation found
            result.append("0")
            
        basket.append(curr_num)
        
    return result
```