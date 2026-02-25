```python
def solve(n, k, chains):
    chains.sort(key=lambda c: -c[-1])

    largest_stamp = 0
    for chain in chains:
        for i in range(len(chain)):
            if chain[i] == i + 1:
                largest_stamp = i + 1
            else:
                break

    disassemble_time = sum([len(chain) for chain in chains]) - largest_stamp
    assemble_time = n - 1
    return disassemble_time + assemble_time
```