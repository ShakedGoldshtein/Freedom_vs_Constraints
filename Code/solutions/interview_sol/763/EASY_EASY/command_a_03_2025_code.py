```python
def solve(T: int, test_cases: list[tuple[int, str, str]]) -> list[str]:
    """
    Determines if it is possible to convert string S into string P by performing swap operations.

    Args:
        T (int): Number of test cases.
        test_cases (list): List of tuples, each containing (N, S, P) where:
            N (int): Length of the binary strings S and P.
            S (str): The original binary string.
            P (str): The target binary string.

    Returns:
        list: A list of "Yes" or "No" strings indicating whether the conversion is possible for each test case.
    """
    results = []
    for case in test_cases:
        N, S, P = case
        ones_S = S.count("1")
        ones_P = P.count("1")

        # If the number of '1's in S and P are different, conversion is impossible
        if ones_S != ones_P:
            results.append("No")
            continue

        # Initialize pointers for S and P
        s_ptr = 0
        p_ptr = 0

        # Traverse both strings
        while s_ptr < N and p_ptr < N:
            # Move pointers in S and P until a '1' is found in P
            while s_ptr < N and S[s_ptr] == "0":
                s_ptr += 1
            while p_ptr < N and P[p_ptr] == "0":
                p_ptr += 1

            # If a '1' is found in P, check if there's a corresponding '1' in S
            if p_ptr < N:
                if s_ptr < N and S[s_ptr] == "1":
                    s_ptr += 1
                else:
                    # If no corresponding '1' is found in S, conversion is impossible
                    results.append("No")
                    break
                p_ptr += 1
        else:
            # If all '1's in P have corresponding '1's in S, conversion is possible
            results.append("Yes")

    return results


# Example usage:
# T = 3
# test_cases = [
#     (2, "00", "00"),
#     (3, "101", "010"),
#     (4, "0110", "0011")
# ]
# print(solve(T, test_cases))
```