```python
def min_time_to_assemble(n, k, chains):
    # Parse the chains into a list of lists
    parsed_chains = []
    for chain in chains:
        m = chain[0]
        dolls = chain[1:]
        parsed_chains.append(dolls)

    # The target is always 1, 2, ..., n
    target = list(range(1, n + 1))

    # The cost is (total_dolls - k) * 2, because:
    # 1. Disassemble all chains into single dolls: (total_dolls - k) operations
    # 2. Assemble into one chain: (n - 1) operations
    # But since the target is 1..n, we can optimize by reusing some structure
    # However, the minimal time is always (n - k) * 2, because:
    # - To disassemble all chains into single dolls: (n - k) operations
    # - To assemble into one chain: (n - 1) operations
    # But the minimal is actually (n - k) + (n - 1) - overlaps, but the worst case is (n - k) + (n - 1)
    # But the problem's note suggests that the minimal is (n - k) + (n - 1) - (k - 1) = 2n - 2k
    # But the first sample gives 1, which is (3 - 2) + (3 - 1) - (2 - 1) = 1 + 2 - 1 = 2? No, sample output is 1.
    # So the initial approach is incorrect. Need to think differently.

    # Alternative approach: The minimal time is the sum of:
    # 1. The time to disassemble all chains into single dolls: sum over all chains (length - 1)
    # 2. The time to assemble the target chain: (n - 1)
    # But we can save time by reusing some structure. For example, if a chain is already a subsequence of the target, we can move it as a whole.
    # So the minimal time is (n - k) + (n - 1) - (number of chains that are already in the correct order and can be moved as a whole)
    # But this is complex. Maybe the minimal time is (n - k) + (n - 1) - (k - 1) = 2n - 2k, but sample 1 gives 2*3 - 2*2 = 2, but output is 1.
    # So this is not correct.

    # Correct approach: The minimal time is the sum of:
    # 1. The time to disassemble all chains into single dolls: sum over all chains (length - 1)
    # 2. The time to assemble the target chain: (n - 1)
    # But we can optimize by not disassembling chains that are already in the correct order and can be nested directly.
    # For example, in sample 1, chain [1,2] can be nested directly into 3, so only 1 operation is needed.

    # So the minimal time is (sum of (length - 1) for all chains) + (n - 1) - (number of chains that can be nested directly)
    # But how to compute the number of chains that can be nested directly? It's the number of chains that are contiguous in the target sequence.

    # So the algorithm is:
    # 1. Compute the total disassembly time: sum of (length - 1) for all chains.
    # 2. Compute the total assembly time: (n - 1).
    # 3. For each chain, check if it is a contiguous subsequence in the target (1..n). If yes, we can save (length - 1) operations (since we don't need to disassemble it, just nest it as a whole).
    # But we can only save for one such chain, because the target is a single chain. So the maximum savings is (max_length - 1) where max_length is the length of the longest chain that is contiguous in the target.

    # So the minimal time is (sum of (length - 1) for all chains) + (n - 1) - (max_length - 1) if there exists a chain that is contiguous in the target.

    # Compute the sum of (length - 1) for all chains
    disassembly_time = 0
    for chain in parsed_chains:
       