```python
def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"
        
    n1, n2 = len(num1), len(num2)
    result = [0] * (n1 + n2)
    
    for i in range(n1-1, -1, -1):
        for j in range(n2-1, -1, -1):
            digit1 = ord(num1[i]) - ord('0')
            digit2 = ord(num2[j]) - ord('0')
            product = digit1 * digit2
            
            p1, p2 = i + j, i + j + 1
            total = result[p2] + product
            
            result[p2] = total % 10
            result[p1] += total // 10
    
    result_str = ""
    start = 0
    while start < len(result) and result[start] == 0:
        start += 1
        
    if start == len(result):
        return "0"
        
    for i in range(start, len(result)):
        result_str += str(result[i])
        
    return result_str
```