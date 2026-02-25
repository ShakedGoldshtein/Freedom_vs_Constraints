```python
def levenshtein_distance(str1: str, str2: str) -> int:
    """
    Calculate the Levenshtein distance between two strings.
    Args:
        str1: First string
        str2: Second string
    Returns:
        Minimum number of single character edits required to transform str1 into str2
    """
    # Handle empty string cases
    if not str1:
        return len(str2)
    if not str2:
        return len(str1)
        
    # Create matrix of dimensions len(str1)+1 x len(str2)+1
    rows = len(str1) + 1
    cols = len(str2) + 1
    distance_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Initialize first row and column
    for i in range(rows):
        distance_matrix[i][0] = i
    for j in range(cols):
        distance_matrix[0][j] = j
        
    # Fill in the rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if str1[i-1] == str2[j-1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
                
            distance_matrix[i][j] = min(
                distance_matrix[i-1][j] + 1,  # deletion
                distance_matrix[i][j-1] + 1,  # insertion
                distance_matrix[i-1][j-1] + substitution_cost  # substitution
            )
            
    return distance_matrix[rows-1][cols-1]
```