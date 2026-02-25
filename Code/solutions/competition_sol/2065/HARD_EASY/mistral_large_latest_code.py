```python
def min_time_to_assemble(n, k, chains):
    """
    Calculate the minimum time required to assemble all matryoshka dolls into a single chain (1 → 2 → ... → n).

    Args:
        n (int): Total number of matryoshka dolls.
        k (int): Number of initial chains.
        chains (list of list of int): Each sublist represents a chain, where the first element is the length,
                                      followed by the doll numbers in ascending order (innermost to outermost).

    Returns:
        int: Minimum time in seconds to assemble all dolls into a single chain.
    """
    # Parse the chains into a set of outermost dolls and a mapping of dolls to their immediate parent
    parent = {}
    outermost = set()
    for chain in chains:
        m = chain[0]
        dolls = chain[1:]
        for i in range(m - 1):
            inner = dolls[i]
            outer = dolls[i + 1]
            parent[inner] = outer
        outermost.add(dolls[-1])

    # The target chain is 1 → 2 → ... → n, so the parent of i should be i+1 (except for n)
    target_parent = {i: i + 1 for i in range(1, n)}

    # Calculate the cost to disassemble all current chains into individual dolls
    disassemble_cost = 0
    for chain in chains:
        m = chain[0]
        if m > 1:
            disassemble_cost += m - 1

    # Calculate the cost to assemble the target chain from individual dolls
    assemble_cost = 0
    # The target chain requires n-1 operations (each doll except the outermost needs to be nested)
    assemble_cost = n - 1

    # However, some dolls might already be in the correct relative order, reducing the cost
    # We need to find the longest increasing subsequence (LIS) in the current structure that matches the target
    # But since the problem is about minimal operations, we can think of it as:
    # The minimal cost is (n - 1) - (number of correct adjacent pairs in the current structure)
    # But this is not straightforward, so we need a better approach.

    # Alternative approach: The minimal time is the sum of:
    # 1. Time to disassemble all current chains into individual dolls (disassemble_cost)
    # 2. Time to assemble the target chain from individual dolls (assemble_cost)
    # But we can optimize by reusing some existing nested structures if they match the target.

    # To optimize, we can think of the problem as transforming the current forest of trees into a single path (1 → 2 → ... → n).
    # The minimal operations are:
    # 1. For each doll not in the correct position, we need to extract it (if nested) and then nest it correctly.
    # 2. The key observation is that the minimal time is (n - 1) - (number of correct adjacent pairs in the current structure)
    #    plus the time to break incorrect adjacent pairs.

    # However, a more precise way is to consider that:
    # - Each correct adjacent pair (i, i+1) in the current structure saves 1 operation (since it's already correctly nested).
    # - All other dolls need to be moved, which requires breaking their current nesting and then nesting them correctly.

    # So the minimal time is:
    # (total dolls - 1) - (number of correct adjacent pairs) + (number of incorrect adjacent pairs)

    # But this is not accurate. Let's think differently.

    # The minimal time is the sum of:
    # 1. The time to break all current nestings (each chain of length m contributes m-1 breaks)
    # 2. The time to build the target chain (n-1 nestings)
    # But we can save time if some current nestings are already part of the target chain.

    # So the correct formula is:
    # total_time = disassemble_cost + assemble_cost - 2 * (number of correct adjacent pairs in current structure)
    # Because each correct pair saves one break and one make operation.

    # Now, count the number of correct adjacent pairs in the current structure
    correct_pairs = 0
    for chain in chains:
        dolls = chain[1:]
        for i in range(len(dolls) - 1):
            inner = dolls[i]
            outer = dolls[i + 1]
            if outer == inner + 1:
                correct