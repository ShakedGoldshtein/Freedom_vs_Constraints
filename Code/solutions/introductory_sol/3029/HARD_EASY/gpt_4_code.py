Here's your requested Python code:

```python
def levenshtein_distance(string1, string2):
    # Initialize a matrix filled with zeros.
    matrix = [[0 for x in range(len(string2) + 1)] for x in range(len(string1) + 1)]

    # Initialize the first row and column with incremental values.
    for i in range(len(string1) + 1):
        matrix[i][0] = i
    for i in range(len(string2) + 1):
        matrix[0][i] = i

    # Fill the rest of the matrix, column by column.
    for col in range(1, len(string2) + 1):
        for row in range(1, len(string1) + 1):
            if string1[row - 1] == string2[col - 1]:
                # The characters match, so there's no cost to add.
                cost = 0
            else:
                # The characters differ, so there's a cost to add.
                cost = 1
            matrix[row][col] = min(matrix[row - 1][col] + 1, matrix[row][col - 1] + 1, matrix[row - 1][col - 1] + cost)

    # The final cell in the matrix will contain the Levenshtein distance.
    return matrix[len(string1)][len(string2)]
```

This function calculates the Levenshtein distance between two strings, taking into account character insertions, deletions, and substitutions.
