```python
def lost_sheep(friday: list[int], saturday: list[int], total: int) -> int:
    """
    Calculate number of lost sheep given Friday returns, Saturday returns and total sheep.
    
    Args:
        friday: List of sheep groups that returned on Friday
        saturday: List of sheep groups that returned on Saturday  
        total: Total number of sheep that should return
        
    Returns:
        Number of sheep lost (not returned)
    """
    friday_sum = sum(friday)
    saturday_sum = sum(saturday)
    return total - (friday_sum + saturday_sum)
```