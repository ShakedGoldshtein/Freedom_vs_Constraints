```python
def solve(test_cases: list[tuple[int, list[list[int]]]]) -> list[int]:
    """
    Solves the coin game problem for multiple test cases.

    Args:
        test_cases (list of tuples): Each tuple contains:
            - n (int): Number of rows of coins.
            - rows (list of lists): Each inner list represents a row of coins.

    Returns:
        list of int: The maximum amount of money Chef can earn for each test case.
    """
    results = []
    for case in test_cases:
        n, rows = case
        total = 0
        for row in rows:
            c, coins = row[0], row[1:]
            # Chef takes the first (leftmost) coins, and Ramsay takes the last (rightmost) coins.
            # The number of coins Chef can take is ceil(c / 2).
            chef_coins = coins[: (c + 1) // 2]
            total += sum(chef_coins)
        results.append(total)
    return results


def main() -> None:
    """
    Reads input, processes each test case, and prints the results.
    """
    import sys

    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])  # Number of test cases
    idx += 1
    test_cases = []
    for _ in range(T):
        N = int(data[idx])  # Number of rows in the current test case
        idx += 1
        rows = []
        for _ in range(N):
            C_i = int(data[idx])  # Number of coins in the current row
            idx += 1
            A_i = list(map(int, data[idx : idx + C_i]))  # Coin values in the current row
            idx += C_i
            rows.append([C_i] + A_i)
        test_cases.append((N, rows))
    results = solve(test_cases)
    for res in results:
        print(res)


if __name__ == "__main__":
    main()
```