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
        mask = 1 << bit
        init_0 = 0
        init_1 = mask
        
        for op, x in operations:
            x_val = int(x)
            if op == '&':
                init_0 &= x_val
                init_1 &= x_val
            elif op == '|':
                init_0 |= x_val
                init_1 |= x_val
            elif op == '^':
                init_0 ^= x_val
                init_1 ^= x_val
        
        if (init_0 & mask) == 0 and (init_1 & mask) == 0:
            final_and &= ~mask
        elif (init_0 & mask) == 0 and (init_1 & mask) == mask:
            pass
        elif (init_0 & mask) == mask and (init_1 & mask) == 0:
            final_xor |= mask
        elif (init_0 & mask) == mask and (init_1 & mask) == mask:
            final_or |= mask
    
    result = []
    if final_and != 1023:
        result.append(('&', final_and))
    if final_or != 0:
        result.append(('|', final_or))
    if final_xor != 0:
        result.append(('^', final_xor))
    
    return len(result), result
```