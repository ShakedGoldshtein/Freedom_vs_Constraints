```python
def solve(n, strings, m, operations):
    # store all strings including ones created during operations
    all_strings = list(strings)
    result = []
    
    # helper function to check if all binary strings of length k exist in s
    def check_length(s, k):
        # generate all possible binary strings of length k
        from itertools import product
        bin_strings = [''.join(map(str, p)) for p in product([0,1], repeat=k)]
        
        # check if each binary string is a substring
        for b in bin_strings:
            if b not in s:
                return False
        return True
    
    # process each operation
    for a, b in operations:
        # concatenate strings indexed at a-1 and b-1
        new_string = all_strings[a-1] + all_strings[b-1]
        all_strings.append(new_string)
        
        # find max k by binary search
        left, right = 0, len(new_string)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if check_length(new_string, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        result.append(ans)
    
    return result
```