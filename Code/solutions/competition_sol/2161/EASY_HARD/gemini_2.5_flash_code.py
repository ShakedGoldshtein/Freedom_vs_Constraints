```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            return True
        return False

def solve(n, m, w_max, weights, beauties, friends_pairs):
    dsu = DSU(n)

    for x, y in friends_pairs:
        # Input Hoses are 1-indexed, convert to 0-indexed
        dsu.union(x - 1, y - 1)

    # Group Hoses by their friendship groups
    # groups_members: dictionary where keys are root elements and values are lists of member indices
    groups_members = {}
    for i in range(n):
        root = dsu.find(i)
        if root not in groups_members:
            groups_members[root] = []
        groups_members[root].append(i)

    # dp[current_weight] = maximum beauty achievable with current_weight
    # Initialize with -1 to indicate unreachable states.
    # dp[0] = 0 as 0 weight can always be achieved with 0 beauty (by taking no Hoses).
    dp = [-1] * (w_max + 1)
    dp[0] = 0

    # Iterate through each friendship group
    for root_id in groups_members:
        current_group_indices = groups_members[root_id]
        
        # Calculate all valid (weight, beauty) options for the current group.
        # These options are mutually exclusive: either take all, or take one, or take none.
        options = [] 

        # Option 1: Take all Hoses in this group
        group_total_weight = 0
        group_total_beauty = 0
        for hos_idx in current_group_indices:
            group_total_weight += weights[hos_idx]
            group_total_beauty += beauties[hos_idx]
        
        if group_total_weight <= w_max:
            options.append((group_total_weight, group_total_beauty))

        # Option 2: Take exactly one Hos from this group
        for hos_idx in current_group_indices:
            hos_weight = weights[hos_idx]
            hos_beauty = beauties[hos_idx]
            # An individual Hos might be too heavy, so check its weight
            if hos_weight <= w_max:
                options.append((hos_weight, hos_beauty))

        # Create a temporary DP array to store results after considering the current group.
        # This prevents using newly calculated values from the same group's options within the same group iteration.
        # Initialize next_dp with current dp values (representing not taking anything from this group).
        next_dp = list(dp) 

        # Iterate through all possible previous weights (from 0 up to w_max).
        # We try to add each option from the current group to these previous states.
        for prev_w in range(w_max + 1):
            # If this previous weight was unreachable, we cannot extend it, so skip.
            if dp[prev_w] == -1:
                continue
            
            # For each mutually exclusive option from the current group:
            for item_w, item_b in options:
                # Check if adding this option keeps the total weight within limits.
                if prev_w + item_w <= w_max:
                    # Update next_dp[new_total_weight] if the new beauty is greater.
                    next_dp[prev_w + item_w] = max(next_dp[prev_w + item_w], dp[prev_w] + item_b)
        
        # After processing all options for the current group, update the main dp array.
        dp = next_dp

    # The maximum beauty is the largest valid value in the dp array.
    max_beauty = 0
    for val in dp:
        if val != -1: # Filter out unreachable states
            max_beauty = max(max_beauty, val)

    return max_beauty

```