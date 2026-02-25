```python
def solve(T: int, test_cases: list[tuple[int, int, list[int], list[tuple[int, int]]]]) -> list[list[int]]:
    results = []
    for case in test_cases:
        N, Q, mountains, queries = case
        for query in queries:
            if query[0] == 0:
                A, B = query[1], query[2]
                mountains[A] = B
            else:
                A = query[1]
                current_height = mountains[A]
                found = False
                for i in range(A + 1, N):
                    if mountains[i] > current_height and mountains[i] not in mountains[:i]:
                        results.append(mountains[i])
                        found = True
                        break
                if not found:
                    results.append(-1)
    return results


# Example usage:
# T = 1
# test_cases = [
#     (10, 5, [1, 3, 5, 4, 5, 6, 7, 8, 4, 5], [
#         (1, 7), (1, 3), (1, 1), (0, 2, 7), (1, 3)
#     ])
# ]
# print(solve(T, test_cases))
```