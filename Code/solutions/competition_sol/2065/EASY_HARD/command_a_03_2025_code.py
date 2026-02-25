```python
def solve(n: int, k: int, chains: list[list[int]]) -> int:
    """
    Calculate the minimum time required to assemble one large chain of matryoshka dolls.

    Args:
        n (int): The total number of matryoshka dolls.
        k (int): The number of initial chains of matryoshka dolls.
        chains (list of list of int): A list where each sublist represents a chain of matryoshka dolls.
                                      Each sublist starts with the number of dolls in the chain, followed by the doll numbers.

    Returns:
        int: The minimum number of seconds needed to assemble one large chain.
    """
    # Initialize the total time required
    total_time = 0

    # Iterate over each chain
    for chain in chains:
        # The first element is the number of dolls in the chain, so we skip it
        m = chain[0]
        # The time required to disassemble this chain is (m - 1) seconds
        total_time += m - 1

    # The time required to assemble the final chain is (n - 1) seconds
    # However, we need to subtract the time already spent disassembling the chains
    # because some of the disassembly steps are already part of the final assembly
    # The correct formula is: total_time = (n - 1) + (sum of (m_i - 1) for all chains) - (k - 1)
    # But since we already summed (m_i - 1) for all chains, we just need to add (n - 1) and subtract (k - 1)
    total_time += n - 1 - (k - 1)

    return total_time
```