```python
def solve(m, numbers):
    # A number less than 10^600 (i.e., up to 10^600 - 1)
    # has a maximum bit length of ceil(log2(10^600)) = 1994.
    # So, bit positions range from 0 to 1993.
    MAX_BITS = 1994 
    
    # basis_values[k] stores the canonical basis element whose Most Significant Bit (MSB) is at position k.
    # If basis_values[k] is 0, no basis element has its MSB at position k.
    basis_values = [0] * MAX_BITS
    
    # basis_indices[k] stores a set of original basket indices that XORed together to form basis_values[k].
    basis_indices = [set() for _ in range(MAX_BITS)]
    
    results = []
    
    # Process each number Misha's robot picks up
    for original_basket_index, x in enumerate(numbers):
        temp_x = x
        temp_indices_for_x = set() # This set tracks the original basket indices that XOR up to the current temp_x
        
        # Attempt to represent x (or its reduced form temp_x) using existing basis elements.
        # Iterate from the highest possible bit position down to 0.
        for k in range(MAX_BITS - 1, -1, -1):
            if (temp_x >> k) & 1:  # If the k-th bit of temp_x is set
                if basis_values[k] != 0:  # If there's an existing basis element for this bit position
                    temp_x ^= basis_values[k]  # Reduce temp_x using the basis element
                    temp_indices_for_x ^= basis_indices[k] # Update the set of contributing indices
                # If basis_values[k] is 0, temp_x cannot be reduced at this bit position by an existing basis element.
                # It will either become 0 (fully dependent) or form a new basis element for position k (if it's its MSB).
        
        if temp_x == 0:
            # If temp_x becomes 0, it means the original 'x' can be represented as an XOR sum
            # of numbers at indices stored in temp_indices_for_x.
            sorted_indices = sorted(list(temp_indices_for_x))
            results.append(f"{len(sorted_indices)} {' '.join(map(str, sorted_indices))}")
        else:
            # If temp_x is not 0, it means 'x' is linearly independent of the current basis.
            # Thus, it cannot be represented as an XOR sum of numbers currently in the basket.
            # It now forms a new basis element.
            
            # Find the Most Significant Bit position of the reduced temp_x
            msb_pos = temp_x.bit_length() - 1
            
            # `temp_x` is the new basis element value.
            # `temp_indices_for_x` contains the indices of existing basket numbers
            # that XORed with `x` (implicitly, if `temp_x` was `x` initially) to produce `temp_x`.
            # Now, `x` itself (at `original_basket_index`) is put into the basket,
            # so it contributes to this new basis element.
            new_basis_element_indices = temp_indices_for_x.union({original_basket_index})

            # To maintain the basis in a "reduced row echelon form" (or Gaussian basis),
            # we use this new basis element (`temp_x`) to eliminate the `msb_pos` bit
            # from any other existing basis elements.
            for k in range(MAX_BITS):
                if k != msb_pos and (basis_values[k] >> msb_pos) & 1:
                    basis_values[k] ^= temp_x
                    basis_indices[k] ^= new_basis_element_indices
            
            # Finally, insert the new basis element itself.
            basis_values[msb_pos] = temp_x
            basis_indices[msb_pos] = new_basis_element_indices
            
            results.append("0")
            
    return results
```