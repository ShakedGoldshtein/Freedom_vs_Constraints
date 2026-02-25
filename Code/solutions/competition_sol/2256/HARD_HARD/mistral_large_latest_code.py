```python
def solve_hamiltonian_jump_path(n, m):
    if n == 1 and m == 1:
        return [(1, 1)]

    if n == 1:
        return _solve_single_row(m)
    if m == 1:
        return _solve_single_column(n)

    if n % 2 == 0 and m % 2 == 0:
        return _solve_even_even(n, m)
    elif n % 2 == 1 and m % 2 == 1:
        return _solve_odd_odd(n, m)
    else:
        return _solve_mixed_parity(n, m)

def _solve_single_row(m):
    path = [(1, y) for y in range(1, m + 1)]
    return path

def _solve_single_column(n):
    path = [(x, 1) for x in range(1, n + 1)]
    return path

def _solve_even_even(n, m):
    path = []
    for x in range(1, n + 1):
        if x % 2 == 1:
            for y in range(1, m + 1):
                path.append((x, y))
        else:
            for y in range(m, 0, -1):
                path.append((x, y))
    return path

def _solve_odd_odd(n, m):
    path = []
    for x in range(1, n + 1):
        if x % 2 == 1:
            for y in range(1, m + 1):
                path.append((x, y))
        else:
            for y in range(m, 0, -1):
                path.append((x, y))
    return path

def _solve_mixed_parity(n, m):
    if n % 2 == 1:
        return _solve_mixed_parity_odd_rows(n, m)
    else:
        return _solve_mixed_parity_even_rows(n, m)

def _solve_mixed_parity_odd_rows(n, m):
    path = []
    for x in range(1, n + 1):
        if x % 2 == 1:
            for y in range(1, m + 1):
                path.append((x, y))
        else:
            for y in range(m, 0, -1):
                path.append((x, y))
    return path

def _solve_mixed_parity_even_rows(n, m):
    path = []
    for x in range(1, n + 1):
        if x % 2 == 1:
            for y in range(1, m + 1):
                path.append((x, y))
        else:
            for y in range(m, 0, -1):
                path.append((x, y))
    return path

def hamiltonian_jump_path(n, m):
    path = solve_hamiltonian_jump_path(n, m)
    if path is None:
        return "-1"
    return path
```