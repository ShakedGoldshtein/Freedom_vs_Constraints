```python
def count_ways(V: int, W: int) -> int:
    """
    Calculate the number of ways to serve dishes A and B on V plates.

    Args:
        V (int): Number of plates (and servings of dish A).
        W (int): Number of servings of dish B.

    Returns:
        int: Number of valid ways to serve the dishes.
    """
    # If there are more servings of B than plates, limit W to V
    W = min(W, V)
    
    # Base cases
    if V == 1:
        return 2 if W >= 1 else 1
    if W == 0:
        return 1
    
    # Initialize DP table
    dp = [[0] * (W + 1) for _ in range(V + 1)]
    
    # Fill DP table
    for i in range(1, V + 1):
        for j in range(W + 1):
            if i == 1:
                dp[i][j] = 1 if j <= 1 else 2
            else:
                dp[i][j] = dp[i - 1][j] + (dp[i - 2][j - 1] if i >= 2 and j >= 1 else 0)
    
    return dp[V][W]


def solve(test_cases: list[tuple[int, int]]) -> list[int]:
    """
    Solve multiple test cases for the dinner party problem.

    Args:
        test_cases (list of tuples): Each tuple contains (V, W) for a test case.

    Returns:
        list of int: List of results for each test case.
    """
    results = []
    for V, W in test_cases:
        results.append(count_ways(V, W))
    return results
```