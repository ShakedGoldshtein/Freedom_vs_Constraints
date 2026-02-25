```python
def solve(t: int, test_cases: list[int]) -> list[str]:
    """
    Solves the problem of finding the greatest integer that can be displayed on a screen
    with a limited number of segments that can be turned on.

    Args:
        t (int): The number of test cases.
        test_cases (list[int]): A list of integers representing the maximum number of segments
                                that can be turned on for each test case.

    Returns:
        list[str]: A list of strings, where each string is the greatest integer that can be
                   displayed for the corresponding test case.
    """
    # Precompute the number of segments required for each digit
    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    result = []
    for n in test_cases:
        # Initialize the result as an empty string
        num = ""
        remaining_segments = n
        # Start with the most significant digit
        while remaining_segments > 0:
            # Find the largest digit that can be displayed with the remaining segments
            for digit in range(9, -1, -1):
                if segments[digit] <= remaining_segments:
                    # Append the digit to the result and subtract the segments used
                    num += str(digit)
                    remaining_segments -= segments[digit]
                    break
        # If no digits can be displayed, append a '0' (though this should not happen given the constraints)
        if not num:
            num = "0"
        result.append(num)
    return result


def main() -> None:
    """
    Main function to handle input and output for the problem.
    Reads input from standard input, processes each test case, and prints the results.
    """
    import sys

    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    test_cases = list(map(int, data[1 : t + 1]))
    results = solve(t, test_cases)
    for res in results:
        print(res)


if __name__ == "__main__":
    main()
```