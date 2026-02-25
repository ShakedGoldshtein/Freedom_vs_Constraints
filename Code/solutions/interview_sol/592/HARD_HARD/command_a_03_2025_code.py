```python
def solve(T: int, test_cases: list[tuple[str, int, list[str]]]) -> list[str]:
    """
    Determine the winner of the game for each test case.

    Args:
        T (int): Number of test cases.
        test_cases (list): List of tuples, each containing:
            - S (str): The string Tracy writes on the whiteboard.
            - N (int): Number of words in the dictionary.
            - words (list): List of words in the dictionary.

    Returns:
        list: List of winners for each test case.
    """
    results = []
    for case in test_cases:
        S, N, words = case
        # Create a memoization dictionary to store results of subproblems
        memo = {}

        def dp(s: str) -> bool:
            """
            Recursive function to determine if the current player can win.

            Args:
                s (str): The current substring being considered.

            Returns:
                bool: True if the current player can win, False otherwise.
            """
            if s in memo:
                return memo[s]
            # Check all possible contiguous substrings that match dictionary words
            for word in words:
                if word in s:
                    # Find all occurrences of the word in the string
                    index = s.find(word)
                    while index != -1:
                        # Create the new string after removing the word
                        new_s = s[:index] + s[index + len(word) :]
                        # If the opponent cannot win from this state, current player wins
                        if not dp(new_s):
                            memo[s] = True
                            return True
                        index = s.find(word, index + 1)
            # If no winning move is found, current player loses
            memo[s] = False
            return False

        # Determine the winner based on the result of the dp function
        if dp(S):
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