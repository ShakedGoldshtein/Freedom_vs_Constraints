```python
def solve(test_cases):
    results = []
    for case in test_cases:
        N, rows = case
        dp = {}

        def dfs(state):
            if state in dp:
                return dp[state]
            total = 0
            max_chef = 0
            for i in range(N):
                left, right = state[i]
                if left <= right:
                    total += sum(rows[i][left:right+1])
            if total == 0:
                return 0
            max_chef = -float('inf')
            for i in range(N):
                left, right = state[i]
                if left <= right:
                    new_state = list(state)
                    new_state[i] = (left + 1, right)
                    new_state = tuple(new_state)
                    chef_take = rows[i][left] + (total - rows[i][left] - dfs(new_state))
                    if chef_take > max_chef:
                        max_chef = chef_take
                    new_state = list(state)
                    new_state[i] = (left, right - 1)
                    new_state = tuple(new_state)
                    ramsay_take = total - rows[i][right] - dfs(new_state)
                    if (total - ramsay_take) > max_chef:
                        max_chef = total - ramsay_take
            dp[state] = max_chef
            return max_chef

        initial_state = tuple((0, len(row)-1) for row in rows)
        results.append(dfs(initial_state))
    return results

def maximize_chef_money(test_cases_data):
    test_cases = []
    idx = 0
    T = test_cases_data[idx]
    idx += 1
    for _ in range(T):
        N = test_cases_data[idx]
        idx += 1
        rows = []
        for __ in range(N):
            parts = test_cases_data[idx]
            C_i = parts[0]
            coins = parts[1:]
            rows.append(coins)
            idx += 1
        test_cases.append((N, rows))
    return solve(test_cases)
```