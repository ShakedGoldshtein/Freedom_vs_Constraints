```python
def solve_xor_sum(m, numbers):
    basket = []
    result = []
    
    def find_xor_subset(target):
        n = len(basket)
        dp = {0: []}
        
        for i in range(n):
            curr = basket[i]
            new_dp = dp.copy()
            for xor_sum, indices in dp.items():
                new_xor = xor_sum ^ curr
                if new_xor not in new_dp:
                    new_dp[new_xor] = indices + [i]
            dp = new_dp
            
        if target in dp:
            return dp[target]
        return None
        
    def format_output(subset):
        if subset is None:
            return "0"
        return f"{len(subset)} {' '.join(map(str, subset))}"
    
    for num in numbers:
        subset = find_xor_subset(num)
        result.append(format_output(subset))
        basket.append(num)
        
    return result

```