```python
def solve_game(n, m):
    """
    Determines the winner of the game for given board dimensions n x m.
    
    The game is solved using the Sprague-Grundy theorem and dynamic programming
    to compute Grundy numbers for positions. Since n and m can be up to 10^6,
    we find a pattern in the Grundy numbers to solve efficiently.
    
    Args:
        n: Number of rows (1-indexed, target is (n, m))
        m: Number of columns (1-indexed, target is (n, m))
    
    Returns:
        "Tuzik" if the first player wins, "Vanya" otherwise
    """
    # Adjust to 0-indexed for easier modulo operations
    # The game starts at (0,0) and ends at (n-1, m-1)
    r, c = n - 1, m - 1
    
    # Compute Grundy number for position (r, c)
    # Observation: Grundy(r, c) = (r % 3) ^ (c % 3) for most cases
    # But we need to handle the special case when both are multiples of 3
    grundy_r = r % 3
    grundy_c = c % 3
    
    # The losing positions are where Grundy number is 0
    # If Grundy(r, c) != 0, first player wins
    if grundy_r == 0 and grundy_c == 0:
        return "Vanya"
    else:
        return "Tuzik"

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    for i in range(t):
        n = int(input_data[2*i + 1])
        m = int(input_data[2*i + 2])
        results.append(solve_game(n, m))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
```