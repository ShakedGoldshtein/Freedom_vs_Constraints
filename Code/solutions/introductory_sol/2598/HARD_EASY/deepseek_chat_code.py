```python
def is_strict_superset(main_set_elements, other_sets_elements):
    """
    Check if the main set is a strict superset of all other sets.
    
    Args:
        main_set_elements: List of elements for the main set
        other_sets_elements: List of lists, where each inner list represents elements of another set
    
    Returns:
        bool: True if main set is strict superset of all other sets, False otherwise
    """
    main_set = set(main_set_elements)
    
    for other_set_elements in other_sets_elements:
        other_set = set(other_set_elements)
        
        # Check if main_set is superset (contains all elements of other_set)
        # and is strict (has at least one element not in other_set)
        if not (other_set.issubset(main_set) and len(main_set) > len(other_set)):
            return False
    
    return True


def solve(main_set_elements, n, other_sets_elements_list):
    """
    Determine if set A is a strict superset of each of the n other sets.
    
    Args:
        main_set_elements: Space separated elements of set A as a list
        n: Number of other sets
        other_sets_elements_list: List of n lists, each containing space separated elements of other sets
    
    Returns:
        bool: True if A is strict superset of all other sets, False otherwise
    """
    # Validate constraints
    if len(main_set_elements) == 0 or len(main_set_elements) >= 501:
        return False
    
    if n <= 0 or n >= 21:
        return False
    
    for other_set in other_sets_elements_list:
        if len(other_set) == 0 or len(other_set) >= 101:
            return False
    
    return is_strict_superset(main_set_elements, other_sets_elements_list)
```