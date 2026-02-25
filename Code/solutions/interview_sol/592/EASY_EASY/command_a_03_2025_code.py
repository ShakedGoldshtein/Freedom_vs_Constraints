```python
def solve(T: int, test_cases: list[tuple[str, int, list[str]]]) -> list[str]:
    """
    Determines the winner of the game for each test case.

    Args:
        T (int): The number of test cases.
        test_cases (list): A list of tuples, where each tuple contains:
            - S (str): The string Tracy writes on the whiteboard.
            - N (int): The number of words in the dictionary.
            - words (list): A list of strings representing the dictionary words.

    Returns:
        list: A list of strings, where each string is the name of the winner for each test case.
    """
    results = []
    for case in test_cases:
        S, N, words = case
        # Create a set of words for efficient lookup
        word_set = set(words)
        # Initialize a DP table where dp[i] represents whether the first player can win
        # with the substring S[i:]
        dp = [False] * (len(S) + 1)
        dp[-1] = True  # Base case: empty string is a losing position for the current player

        # Fill the DP table from the end of the string to the beginning
        for i in range(len(S) - 1, -1, -1):
            for j in range(i + 1, len(S) + 1):
                if S[i:j] in word_set and dp[j]:
                    dp[i] = True
                    break

        # If dp[0] is True, Teddy (first player) can force a win
        if dp[0]:
            results.append("Teddy")
        else:
            results.append("Tracy")
    return results


# Example usage:
# test_cases = [
#     ("codechef", 2, ["code", "chef"]),
#     ("foo", 1, ["bar"]),
#     ("mississippi", 4, ["ssissi", "mippi", "mi", "ppi"])
# ]
# print(solve(3, test_cases))
```