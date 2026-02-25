```python
def solve(n, operations):
    and_val = 1023
    or_val = 0
    xor_val = 0
    
    for op, x in operations:
        x = int(x)
        if op == '&':
            and_val &= x
            or_val &= x
            xor_val &= x
        elif op == '|':
            and_val |= x
            or_val |= x
            xor_val |= x
        elif op == '^':
            and_val ^= x
            or_val ^= x
            xor_val ^= x
    
    final_and = 1023
    final_or = 0
    final_xor = 0
    
    for bit in range(10):
        bit_mask = 1 << bit
        
        and_bit = and_val & bit_mask
        or_bit = or_val & bit_mask
        xor_bit = xor_val & bit_mask
        
        input_0 = 0
        input_1 = bit_mask
        
        for op, x in operations:
            x = int(x)
            if op == '&':
                input_0 &= x
                input_1 &= x
            elif op == '|':
                input_0 |= x
                input_1 |= x
            elif op == '^':
                input_0 ^= x
                input_1 ^= x
        
        output_0 = input_0 & bit_mask
        output_1 = input_1 & bit_mask
        
        if output_0 == 0 and output_1 == 0:
            final_and &= ~bit_mask
        elif output_0 == 0 and output_1 == bit_mask:
            pass
        elif output_0 == bit_mask and output_1 == 0:
            final_xor ^= bit_mask
        elif output_0 == bit_mask and output_1 == bit_mask:
            final_or |= bit_mask
    
    result_ops = []
    
    if final_and != 1023:
        result_ops.append(('&', final_and))
    if final_or != 0:
        result_ops.append(('|', final_or))
    if final_xor != 0:
        result_ops.append(('^', final_xor))
    
    return len(result_ops), result_ops
```