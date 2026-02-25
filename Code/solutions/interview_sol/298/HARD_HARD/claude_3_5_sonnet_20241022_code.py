```python
def multiply(num1: str, num2: str) -> str:
    """Multiply two numbers represented as strings without converting to integers directly"""
    
    # Handle edge cases
    if not num1 or not num2:
        return "0"
    if num1 == "0" or num2 == "0":
        return "0"
        
    # Create result array with max possible length
    n1, n2 = len(num1), len(num2)
    result = [0] * (n1 + n2)
    
    # Multiply each digit pair and add to result array
    for i in range(n1-1, -1, -1):
        for j in range(n2-1, -1, -1):
            digit1 = ord(num1[i]) - ord('0')
            digit2 = ord(num2[j]) - ord('0')
            product = digit1 * digit2
            
            # Add product to positions in result
            pos1 = i + j
            pos2 = i + j + 1
            product += result[pos2]
            
            result[pos2] = product % 10
            result[pos1] += product // 10
            
    # Convert result to string, removing leading zeros
    output = []
    start = 0
    while start < len(result) and result[start] == 0:
        start += 1
        
    # Handle case of all zeros
    if start == len(result):
        return "0"
        
    # Build final string
    for i in range(start, len(result)):
        output.append(str(result[i]))
        
    return "".join(output)
```