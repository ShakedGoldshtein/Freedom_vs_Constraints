```python
def max_number_with_segments(n: int) -> str:
    """
    Returns the greatest integer that can be displayed using no more than n segments.

    Args:
        n (int): The maximum number of segments that can be turned on.

    Returns:
        str: The greatest integer as a string, since it may not fit in standard integer types.
    """
    # Segment counts for digits 0-9: 6, 2, 5, 5, 4, 5, 6, 3, 7, 6
    # To maximize the number, prioritize digits with the least segments
    # Start with digit '1' (2 segments) and fill as many as possible
    # Then use digit '7' (3 segments) if remaining segments allow
    # Finally, use digit '4' (4 segments) if remaining segments allow

    result: list[str] = []
    while n >= 2:
        if n >= 7:
            # Use '1' (2 segments) as many times as possible
            count = n // 2
            result.extend(['1'] * count)
            n %= 2
        elif n >= 3:
            # Use '7' (3 segments)
            result.append('7')
            n -= 3
        else:
            # Use '4' (4 segments) if remaining segments allow
            if n >= 4:
                result.append('4')
                n -= 4
            else:
                # Use '1' (2 segments) if remaining segments allow
                result.append('1')
                n -= 2

    # Join the digits in reverse order to get the largest possible number
    return ''.join(reversed(result))


def solve(test_cases: list[int]) -> list[str]:
    """
    Solves the problem for multiple test cases.

    Args:
        test_cases (list[int]): A list of integers representing the maximum number of segments for each test case.

    Returns:
        list[str]: A list of strings, each representing the greatest integer for the corresponding test case.
    """
    results: list[str] = []
    for n in test_cases:
        results.append(max_number_with_segments(n))
    return results
```