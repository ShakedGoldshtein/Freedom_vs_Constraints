```python
def minimal_total_sweets(n, m, b, g):
    """
    Computes the minimal total number of sweets boys could have presented to girls
    under the given constraints. Returns -1 if the situation is impossible.

    Args:
        n: Number of boys.
        m: Number of girls.
        b: List of n integers, where b[i] is the minimal sweets i-th boy gave to any girl.
        g: List of m integers, where g[j] is the maximal sweets j-th girl received from any boy.

    Returns:
        Minimal total sweets or -1 if impossible.
    """
    def is_possible(x):
        # Check if x is a feasible total sweets count
        # We need to assign a_{i,j} such that:
        # 1. min_j a_{i,j} = b_i for all i
        # 2. max_i a_{i,j} = g_j for all j
        # 3. sum_{i,j} a_{i,j} <= x

        # For each boy, the minimal a_{i,j} is b_i, so at least one a_{i,j} must be >= b_i
        # For each girl, the maximal a_{i,j} is g_j, so all a_{i,j} <= g_j for that j

        # First, check if b_i <= g_j for at least one j for each i (since min_j a_{i,j} = b_i)
        # And g_j >= max_i b_i for each j (since max_i a_{i,j} = g_j)
        max_b = max(b) if b else 0
        for gj in g:
            if gj < max_b:
                return False

        # Now, for each boy, at least one a_{i,j} must be >= b_i, and all a_{i,j} <= g_j
        # The minimal sum is sum_i (b_i) + sum_j (g_j) - max(sum(b), sum(g))
        # But we need to ensure that for each j, at least one a_{i,j} = g_j (since g_j is the max for that j)
        # So the minimal sum is sum_j g_j + sum_i (b_i - max_j a_{i,j})
        # But since max_j a_{i,j} >= b_i (because min_j a_{i,j} = b_i), the minimal sum is sum_j g_j + sum_i (b_i - g_j) if b_i <= g_j for all i,j
        # But this is not straightforward, so we proceed with binary search and feasibility check

        # The minimal possible sum is sum(b) + sum(g) - max(sum(b), sum(g))? Not sure.
        # Instead, we'll model this as a flow problem or use binary search with feasibility checks.

        # For the feasibility check, we can use the following approach:
        # For each boy i, the minimal a_{i,j} is b_i, and at least one a_{i,j} must be exactly b_i (since it's the min)
        # For each girl j, the maximal a_{i,j} is g_j, and at least one a_{i,j} must be exactly g_j (since it's the max)
        # So, for each boy i, we can assign b_i to one girl j where b_i <= g_j (since a_{i,j} <= g_j)
        # Then, for each girl j, the remaining a_{i,j} can be <= g_j, but at least one must be g_j
        # So, the minimal sum is sum(b) + sum(g) - sum(min(b_i, g_j) for some assignment)

        # But this is complex. Instead, we can use the following necessary and sufficient conditions:
        # 1. For each boy i, there exists at least one girl j such that b_i <= g_j
        # 2. For each girl j, there exists at least one boy i such that b_i <= g_j
        # 3. The sum of all b_i must be <= x, and the sum of all g_j must be <= x
        # But this is not sufficient. We need a better approach.

        # Alternative approach: The minimal sum is sum(b) + sum(g) - sum(min(b_i, g_j) for some optimal assignment)
        # But this is not straightforward to compute.

        # Instead, we can use the following:
        # The minimal sum is sum(b) + sum(g) - sum(min(b_i, g_j) for some assignment where each b_i is assigned to a g_j >= b_i)
