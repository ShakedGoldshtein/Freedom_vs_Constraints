```python
def solve(n: int, k: int, chains: list[list[int]]) -> int:
    """
    Calculate the minimum time to assemble one large chain of matryoshka dolls.

    Args:
        n (int): Total number of matryoshka dolls.
        k (int): Number of initial chains.
        chains (list of list of int): List of chains, where each chain is a list of matryoshka doll numbers.

    Returns:
        int: Minimum time in seconds to assemble one large chain.
    """
    # Initialize the total time to 0
    total_time = 0

    # Iterate over each chain
    for chain in chains:
        # The number of operations to disassemble a chain is (length of chain - 1)
        # Since each nesting requires one operation to remove
        total_time += len(chain) - 1

    # After disassembling all chains, we need to assemble them into one big chain
    # The number of operations to assemble the big chain is (n - 1)
    # Since each nesting requires one operation to insert
    total_time += n - 1

    return total_time
```