```python
def solve(test_cases: list[tuple[int, list[list[int]]]]) -> list[int]:
    """
    Solves the coin game problem for multiple test cases.

    Args:
        test_cases (list): A list of tuples, where each tuple contains:
            - n (int): Number of rows of coins.
            - rows (list): A list of lists, where each inner list represents a row of coins.

    Returns:
        list: A list of integers representing the maximum amount of money Chef can earn for each test case.
    """
    results = []
    for case in test_cases:
        n, rows = case
        total = 0
        for row in rows:
            # Extract the number of coins and the coin values from the row
            c, *coins = row
            # Sort the coins in ascending order
            coins.sort()
            # Calculate the number of coins Chef can take from this row
            chef_coins = (c + 1) // 2
            # Add the sum of the first 'chef_coins' coins to the total
            total += sum(coins[:chef_coins])
        results.append(total)
    return results


def main() -> list[int]:
    """
    Reads input, processes each test case, and returns the results.

    Returns:
        list: A list of integers representing the maximum amount of money Chef can earn for each test case.
    """
    import json

    # Read input from stdin
    input_data = json.loads(input())
    test_cases = []
    for case in input_data:
        n = case[0]
        rows = [list(row) for row in case[1:]]
        test_cases.append((n, rows))
    return solve(test_cases)


# Example usage:
# input_data = [
#     [2, [4, 5, 2, 3, 4], [2, 1, 6]]
# ]
# print(solve(input_data))
```