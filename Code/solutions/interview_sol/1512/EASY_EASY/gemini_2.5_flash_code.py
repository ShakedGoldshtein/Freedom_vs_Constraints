```python
def solve(N, M):
    dist_row = N - 1
    dist_col = M - 1

    grundy_row = dist_row % 4
    grundy_col = dist_col % 3

    overall_grundy = grundy_row ^ grundy_col

    if overall_grundy > 0:
        return "Tuzik"
    else:
        return "Vanya"

```