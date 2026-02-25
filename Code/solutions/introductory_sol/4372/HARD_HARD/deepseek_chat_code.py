```python
def calculate_lost_sheep(friday_sheep, saturday_sheep, total_sheep):
    """
    Calculate the number of sheep lost after final counting on Saturday.
    
    Args:
        friday_sheep: List of positive integers representing sheep groups returned on Friday
        saturday_sheep: List of positive integers representing sheep groups returned on Saturday  
        total_sheep: Total number of sheep that should be on the farm
    
    Returns:
        Number of sheep lost (positive integer)
    """
    if total_sheep <= 0:
        return total_sheep
    
    def sum_sheep_groups(groups):
        """Helper function to safely sum sheep groups."""
        return sum(groups) if groups else 0
    
    friday_total = sum_sheep_groups(friday_sheep)
    saturday_total = sum_sheep_groups(saturday_sheep)
    
    returned_total = friday_total + saturday_total
    
    if returned_total > total_sheep:
        return 0
    
    return total_sheep - returned_total
```