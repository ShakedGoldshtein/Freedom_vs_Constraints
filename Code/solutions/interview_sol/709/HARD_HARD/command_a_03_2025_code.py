```python
import math


def max_gcd(arr: list[int]) -> int:
    """
    Calculate the maximum possible GCD after performing allowed operations.

    Args:
        arr (list[int]): The input array of integers.

    Returns:
        int: The maximum possible GCD after performing the operations.
    """
    n = len(arr)
    if n == 1:
        return arr[0]

    # Calculate the GCD of the entire array
    full_gcd = arr[0]
    for num in arr[1:]:
        full_gcd = math.gcd(full_gcd, num)

    # Calculate the GCD of the array after reversing
    reversed_gcd = arr[-1]
    for num in arr[-2::-1]:
        reversed_gcd = math.gcd(reversed_gcd, num)

    # Calculate the maximum GCD after removing any subarray
    max_subarray_gcd = 0
    for i in range(n):
        current_gcd = arr[i]
        for j in range(i + 1, n):
            current_gcd = math.gcd(current_gcd, arr[j])
            if current_gcd > max_subarray_gcd:
                max_subarray_gcd = current_gcd

    # Return the maximum of the three possible GCDs
    return max(full_gcd, reversed_gcd, max_subarray_gcd)


def solve(test_cases: list[tuple[int, list[int]]]) -> list[int]:
    """
    Solve the problem for multiple test cases.

    Args:
        test_cases (list[tuple[int, list[int]]]): A list of tuples, where each tuple contains:
            - n (int): The length of the array.
            - arr (list[int]): The array of integers.

    Returns:
        list[int]: A list of integers representing the maximum possible GCD for each test case.
    """
    results = []
    for case in test_cases:
        n, arr = case
        if n == 0:
            results.append(0)
            continue
        results.append(max_gcd(arr))
    return results


def main() -> list[int]:
    """
    Main function to read input, process test cases, and return results.

    Returns:
        list[int]: A list of integers representing the maximum possible GCD for each test case.
    """
    import sys

    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    test_cases = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx : idx + N]))
        idx += N
        test_cases.append((N, arr))
    return solve(test_cases)


# Example usage:
# test_cases = [(1, [2]), (2, [2, 4])]
# print(solve(test_cases))
```