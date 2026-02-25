```python
def levenshtein_distance(s1, s2):
    """
    Calculate the Levenshtein distance between two strings.
    
    Args:
        s1 (str): First string
        s2 (str): Second string
    
    Returns:
        int: The minimum number of single-character edits (insertions, 
             deletions, substitutions) needed to transform s1 into s2
    """
    if s1 is None or s2 is None:
        raise ValueError("Input strings cannot be None")
    
    # Handle empty string cases efficiently
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    
    # Use the shorter string as the inner dimension to optimize space
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    
    # Initialize previous row (deletion costs)
    previous_row = list(range(len(s1) + 1))
    
    for i2, char2 in enumerate(s2):
        # Initialize current row with deletion cost for empty s1
        current_row = [i2 + 1]
        
        for i1, char1 in enumerate(s1):
            # Calculate costs for all operations
            insertion_cost = current_row[i1] + 1
            deletion_cost = previous_row[i1 + 1] + 1
            substitution_cost = previous_row[i1] + (0 if char1 == char2 else 1)
            
            # Take minimum cost
            current_row.append(min(insertion_cost, deletion_cost, substitution_cost))
        
        previous_row = current_row
    
    return previous_row[-1]
```