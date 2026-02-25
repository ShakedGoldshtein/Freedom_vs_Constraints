```python
def solve(N1, N2, N3, list1, list2, list3):
    """
    Produces the final voter list containing only IDs that appear in at least 2 out of 3 lists.
    
    Args:
        N1: Number of voters in first list
        N2: Number of voters in second list  
        N3: Number of voters in third list
        list1: First list of voter IDs in ascending order
        list2: Second list of voter IDs in ascending order
        list3: Third list of voter IDs in ascending order
    
    Returns:
        Tuple of (M, final_list) where:
        - M: Number of voters in final list
        - final_list: List of voter IDs in ascending order
    """
    def merge_lists():
        """Merge all three lists while tracking which list each element came from."""
        merged = []
        i = j = k = 0
        
        while i < N1 or j < N2 or k < N3:
            min_val = float('inf')
            if i < N1:
                min_val = min(min_val, list1[i])
            if j < N2:
                min_val = min(min_val, list2[j])
            if k < N3:
                min_val = min(min_val, list3[k])
            
            count = 0
            if i < N1 and list1[i] == min_val:
                count += 1
                i += 1
            if j < N2 and list2[j] == min_val:
                count += 1
                j += 1
            if k < N3 and list3[k] == min_val:
                count += 1
                k += 1
            
            merged.append((min_val, count))
        
        return merged
    
    def filter_majority(merged):
        """Filter elements that appear in at least 2 lists."""
        result = []
        for value, count in merged:
            if count >= 2:
                result.append(value)
        return result
    
    merged = merge_lists()
    final_list = filter_majority(merged)
    return len(final_list), final_list
```