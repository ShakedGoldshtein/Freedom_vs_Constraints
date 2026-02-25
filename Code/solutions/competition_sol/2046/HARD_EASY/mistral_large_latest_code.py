```python
def solve_farmer_john_program(n, a_sequence):
    results = []
    for i in range(1, n):
        x, y = 1, 0
        sequence = [i] + a_sequence.copy()
        visited = set()
        steps = 0
        max_steps = 2 * len(sequence)  # Prevent infinite loops in practice

        while True:
            if x <= 0 or x > len(sequence):
                results.append(y)
                break
            if (x, y) in visited:
                results.append(-1)
                break
            if steps > max_steps:
                results.append(-1)
                break
            visited.add((x, y))
            steps += 1

            # Step 2: Increase both x and y by a_x
            x += sequence[x - 1]
            y += sequence[x - 1]

            if x <= 0 or x > len(sequence):
                results.append(y)
                break
            if (x, y) in visited:
                results.append(-1)
                break
            if steps > max_steps:
                results.append(-1)
                break
            visited.add((x, y))
            steps += 1

            # Step 3: Increase y by a_x, decrease x by a_x
            y += sequence[x - 1]
            x -= sequence[x - 1]

        # Early termination if already determined non-terminating
        if len(results) == i and results[-1] == -1:
            results.extend([-1] * (n - 1 - i))
            break

    return results
```