```python
def solve(n, q_count, word_of_universe, evolutions):
    """
    Determines if three religion descriptions can form disjoint subsequences of the Word of Universe
    after a series of evolutions.

    Args:
        n (int): The length of the Word of Universe.
        q_count (int): The number of religion evolutions.
        word_of_universe (str): The Word of Universe string.
        evolutions (list): A list of evolution operations. Each operation is a string
                           like "+ 1 a" or "- 2".

    Returns:
        list: A list of strings, either "YES" or "NO", for each evolution.
    """

    # Constants
    MAX_RELIGION_LEN = 250
    ALPHABET_SIZE = 26
    
    # Precompute next_char_table[i][char_code]
    # Stores the smallest index k >= i such that word_of_universe[k] == char_code.
    # If not found, it stores n (which acts as an "infinity" value for indices 0 to n-1).
    # The table size is (n + 1) to handle lookups for starting index up to n.
    # next_char_table[n] will contain all n's, correctly indicating no char found from index n onwards.
    next_char_table = [[n] * ALPHABET_SIZE for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for char_code in range(ALPHABET_SIZE):
            next_char_table[i][char_code] = next_char_table[i + 1][char_code]
        char_idx = ord(word_of_universe[i]) - ord('a')
        next_char_table[i][char_idx] = i

    # dp[l1][l2][l3] stores the minimum ending index in word_of_universe
    # after successfully matching religion 0 up to l1 characters,
    # religion 1 up to l2 characters, and religion 2 up to l3 characters,
    # all as disjoint subsequences.
    # A value of n signifies that it's impossible to form these subsequences.
    # Base case: dp[0][0][0] = -1 (no characters used, so the previous ending index is -1).
    # This allows next_char_table[0] to be correctly accessed for the first character.
    dp = [[[n for _ in range(MAX_RELIGION_LEN + 1)] 
            for _ in range(MAX_RELIGION_LEN + 1)] 
           for _ in range(MAX_RELIGION_LEN + 1)]
    dp[0][0][0] = -1

    religions = ["", "", ""] # Store religion descriptions as strings
    lengths = [0, 0, 0]      # Current lengths of religion descriptions

    results = []

    for evolution in evolutions:
        parts = evolution.split()
        op_type = parts[0]
        religion_idx = int(parts[1]) - 1 # Convert to 0-indexed religion (0, 1, or 2)

        if op_type == '+':
            char_to_add = parts[2]
            religions[religion_idx] += char_to_add
            lengths[religion_idx] += 1
            
            # Get current lengths for DP table dimensions
            L1, L2, L3 = lengths[0], lengths[1], lengths[2]

            # The calculation of dp[x][y][z] depends on:
            # dp[x-1][y][z] (extending religion 0)
            # dp[x][y-1][z] (extending religion 1)
            # dp[x][y][z-1] (extending religion 2)
            # We iterate over the relevant slice of the DP table that is affected by the change.
            # The order of loops for inner dimensions ensures dependencies are met within the current slice.

            if religion_idx == 0: # Religion 1 (s1) grew to length L1
                s1_char_code = ord(char_to_add) - ord('a')
                for j in range(L2 + 1):
                    for k in range(L3 + 1):
                        current_min_end_idx = n # Initialize with impossible value
                        
                        # Option 1: Extend s1 (the religion that just grew)
                        # The previous state is dp[L1-1][j][k]
                        if dp[L1 - 1][j][k] < n: 
                            prev_end_idx = dp[L1 - 1][j][k]
                            # Find next occurrence of s1_char_code after prev_end_idx
                            next_occ = next_char_table[prev_end_idx + 1][s1_char_code]
                            current_min_end_idx = min(current_min_end_idx, next_occ)
                        
                        # Option 2: Extend s2 (religion 2)
                        # The previous state is dp[L1][j-1][k]
                        if j > 0 and dp[L1][j - 1][k] < n:
                            prev_end_idx = dp[L1][j - 1][k]
                            s2_char_code = ord(religions[1][j - 1]) - ord('a') # Last char of s2
                            next_occ = next_char_table[prev_end_idx + 1][s2_char_code]
                            current_min_end_idx = min(current_min_end_idx, next_occ)

                        # Option 3: Extend s3 (religion 3)
                        # The previous state is dp[L1][j][k-1]
                        if k > 0 and dp[L1][j][k - 1] < n:
                            prev_end_idx = dp[L1][j][k - 1]
                            s3_char_code = ord(religions[2][k - 1]) - ord('a') # Last char of s3
                            next_occ = next_char_table[prev_end_idx + 1][s3_char_code]
                            current_min_end_idx = min(current_min_end_idx, next_occ)
                        
                        dp[L1][j][k] = current_min_end_idx

            elif religion_idx == 1: # Religion 2 (s2) grew to length L2
                s2_char_code = ord(char_to_add) - ord('a')
                for i in range(L1 + 1):
                    for k in range(L3 + 1):
                        current_min_end_idx = n
                        
                        # Option 1: Extend s1 (religion 1)
                        # The previous state is dp[i-1][L2][k]
                        if i > 0 and dp[i - 1][L2][k] < n:
                            prev_end_idx = dp[i - 1][L2][k]
                            s1_char_code = ord(religions[0][i - 1]) - ord('a') # Last char of s1
                            next_occ = next_char_table[prev_end_idx + 1][s1_char_code]
                            current_min_end_idx = min(current_min_end_idx, next_occ)
                        
                        # Option 2: Extend s2 (the religion that just grew)
                        # The previous state is dp[i][L2-1][k]
                        if dp[i][L2 - 1][k] < n:
                            prev_end_idx = dp[i][L2 - 1][k]
                            next_occ = next_char_table[prev_end_idx + 1][s2_char_code]
                            current_min_end_idx = min(current_min_end_idx, next_occ)

                        # Option 3: Extend s3 (religion 3)
                        # The previous state is dp[i][L2][k-1]
                        if k > 0 and dp[i][L2][k - 1] < n:
                            prev_end_idx = dp[i][L2][k - 1]
                            s3_char_code = ord(religions[2][k - 1]) - ord('a') # Last char of s3
                            next_occ = next_char_table[prev_end_idx + 1][s3_char_code]
                            current_min_end_idx = min(current_min_end_idx, next_occ)
                        
                        dp[i][L2][k] = current_min_end_idx
            
            else: # religion_idx == 2 (s3) grew to length L3
                s3_char_code = ord(char_to_add) - ord('a')
                for i in range(L1 + 1):
                    for j in range(L2 + 1):
                        current_min_end_idx = n
                        
                        # Option 1: Extend s1 (religion 1)
                        # The previous state is dp[i-1][j][L3]
                        if i > 0 and dp[i - 1][j][L3] < n:
                            prev_end_idx = dp[i - 1][j][L3]
                            s1_char_code = ord(religions[0][i - 1]) - ord('a') # Last char of s1
                            next_occ = next_char_table[prev_end_idx + 1][s1_char_code]
                            current_min_end_idx = min(current_min_end_idx, next_occ)
                        
                        # Option 2: Extend s2 (religion 2)
                        # The previous state is dp[i][j-1][L3]
                        if j > 0 and dp[i][j - 1][L3] < n:
                            prev_end_idx = dp[i][j - 1][L3]
                            s2_char_code = ord(religions[1][j - 1]) - ord('a') # Last char of s2
                            next_occ = next_char_table[prev_end_idx + 1][s2_char_code]
                            current_min_end_idx = min(current_min_end_idx, next_occ)
                        
                        # Option 3: Extend s3 (the religion that just grew)
                        # The previous state is dp[i][j][L3-1]
                        if dp[i][j][L3 - 1] < n:
                            prev_end_idx = dp[i][j][L3 - 1]
                            next_occ = next_char_table[prev_end_idx + 1][s3_char_code]
                            current_min_end_idx = min(current_min_end_idx, next_occ)
                        
                        dp[i][j][L3] = current_min_end_idx

        else: # op_type == '-' (remove last character)
            religions[religion_idx] = religions[religion_idx][:-1]
            lengths[religion_idx] -= 1
            # For removal, the DP table values for the new (shorter) lengths
            # are already computed correctly from previous states.
            # No need to explicitly revert or recompute the DP table.

        # After each evolution, check if co-existence is possible based on current lengths
        if dp[lengths[0]][lengths[1]][lengths[2]] < n: # If the final state is reachable
            results.append("YES")
        else:
            results.append("NO")
            
    return results
```