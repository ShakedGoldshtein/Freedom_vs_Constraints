```python
def solve(n, k, chains):
    chains.sort(key=lambda x: min(x))
    result = 0
    first_chain = chains[0]
    x = first_chain[0]
    for m in first_chain:
        if m == x:
            x += 1
        else:
            result += len(first_chain) - first_chain.index(m)
            break
    for chain in chains[1:]:
        result += len(chain)
    return result + (n - x) * 2
```