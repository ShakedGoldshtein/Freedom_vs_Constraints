```python
def solve(n, strings, m, operations):
    # Store all strings including those created by operations
    all_strings = strings.copy()
    result = []
    
    def find_max_k(s):
        # Check if string contains both 0 and 1, if not max k is 0
        if '0' not in s or '1' not in s:
            return 0
            
        # Try increasing k until we find one that doesn't work
        k = 1
        while True:
            # Generate all possible binary strings of length k
            need = set()
            for i in range(1 << k):
                binary = bin(i)[2:].zfill(k)
                need.add(binary)
            
            # Check if all binary strings of length k are substrings
            found_all = True
            for binary in need:
                if binary not in s:
                    found_all = False
                    break
                    
            if not found_all:
                return k - 1
                
            # Check if we can go any further based on string length
            if k + 1 > len(s):
                return k
                
            k += 1
    
    # Process each operation
    for i in range(m):
        a, b = operations[i]
        # Create new string by concatenating specified strings
        new_string = all_strings[a-1] + all_strings[b-1]
        all_strings.append(new_string)
        
        # Find max k for new string
        max_k = find_max_k(new_string)
        result.append(max_k)
        
    return result

# Example usage:
#n = 5
#strings = ['01', '10', '101', '11111', '0'] 
#m = 3
#operations = [[1,2], [6,5], [4,4]]
#print(solve(n, strings, m, operations))
```