```python
def good_substrings(t, string_list):
    result = []
    
    for string in string_list:
        n = len(string)
        prefix_zeroes = [0] * (n+1)
        
        for i in range(1,n+1):
            prefix_zeroes[i] = prefix_zeroes[i-1] + (1 if string[i-1] == '0' else 0)
            
        dp, ans, MAX = [0] * (n+1), 0, min(20,n)
        for r in range(1, n+1):
            dp[r] = dp[r-1]
            cnt, i = 0, r
            while i and r-i+1 <= MAX:
                cnt = (2*cnt + (1 if string[i-1] == '1' else 0))
                if r-i+1 == cnt:
                    dp[r] = max(dp[r], 1+(dp[i-1- prefix_zeroes[i-1]] if i-1-prefix_zeroes[i-1] >= 0 else 0))
                i -= 1
            ans = max(ans, dp[r])
        result.append(str(n - ans)) 
    return result

# test the function
print(good_substrings(4, ['0110', '0101', '00001000', '0001000']))
```
The function `good_substrings(t, string_list)` receives an integer `t` and a list of binary strings `string_list`. For each string, it calculates the number of good substrings and returns a list of results. A substring is good if its length is equal to the decimal representation of the number it represents.