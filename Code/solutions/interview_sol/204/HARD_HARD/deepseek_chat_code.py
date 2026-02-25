```python
def search(nums, target):
    """
    Search for a target value in a rotated sorted array without duplicates.
    
    Args:
        nums: List of integers, rotated sorted array without duplicates
        target: Integer value to search for
    
    Returns:
        Integer index of target if found, -1 otherwise
    """
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            # Target is in the sorted left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            # Target is in the sorted right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1
```