```python
from collections import defaultdict, deque


def solve(test_cases: list[tuple[int, int, list[tuple[int, int, int]]]]) -> list[str]:
    """
    Solves the problem of determining if a partially filled matrix B can be completed to be 'good'.

    Args:
        test_cases (list): A list of tuples, where each tuple contains:
            - N (int): The dimension of the matrix.
            - Q (int): The number of filled entries in the matrix.
            - entries (list): A list of tuples, where each tuple contains (i, j, val) representing a filled entry.

    Returns:
        list: A list of strings, where each string is either "yes" or "no" indicating whether the corresponding test case can be solved.
    """
    results = []
    for case in test_cases:
        N, Q, entries = case
        # Initialize the graph and distance dictionary
        graph = defaultdict(list)
        distance = defaultdict(int)

        # Build the graph and distance dictionary from the entries
        for i, j, val in entries:
            graph[i].append(j)
            graph[j].append(i)
            distance[(i, j)] = val
            distance[(j, i)] = val

        # Initialize the result for this test case
        result = "yes"

        # Perform BFS to check for inconsistencies
        for i in range(1, N + 1):
            if i not in graph:
                continue
            queue = deque()
            queue.append((i, float("inf")))
            visited = set()
            visited.add(i)
            while queue:
                node, w = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        if distance[(node, neighbor)] == 1:
                            queue.append((neighbor, min(w, 1)))
                        else:
                            queue.append((neighbor, min(w, 0)))
                    else:
                        if (
                            distance[(node, neighbor)] == 1
                            and w == 0
                            or distance[(node, neighbor)] == 0
                            and w == 1
                        ):
                            result = "no"
                            break
                if result == "no":
                    break
            if result == "no":
                break
        results.append(result)
    return results


def main() -> None:
    """
    Reads input, processes each test case, and prints the results.
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
        Q = int(data[idx + 1])
        idx += 2
        entries = []
        for _ in range(Q):
            i = int(data[idx])
            j = int(data[idx + 1])
            val = int(data[idx + 2])
            entries.append((i, j, val))
            idx += 3
        test_cases.append((N, Q, entries))
    results = solve(test_cases)
    for res in results:
        print(res)


if __name__ == "__main__":
    main()
```