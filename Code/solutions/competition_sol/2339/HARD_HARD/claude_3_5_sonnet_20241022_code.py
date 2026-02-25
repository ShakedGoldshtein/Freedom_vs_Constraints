```python
def solve_binary_strings(n: int, a: str, b: str) -> list[int]:
    """
    Transforms binary string a into b using prefix flip+reverse operations.
    Returns list where first element is number of operations k, followed by k prefix lengths.
    """
    if a == b:
        return [0]
    
    def flip_prefix(s: str, length: int) -> str:
        """Flips and reverses prefix of length k in string s"""
        if length == 0:
            return s
        prefix = ''.join('1' if c == '0' else '0' for c in s[:length][::-1])
        return prefix + s[length:]
        
    result = []
    current = list(a)
    target = list(b)
    n = len(current)
    
    # Process bit by bit from right to left
    for i in range(n-1, -1, -1):
        if current[i] != target[i]:
            if i == 0:
                # Just flip single bit
                result.append(1)
                current[0] = target[0]
            else:
                if current[0] == target[i]:
                    # Flip prefix up to position i
                    result.append(i+1)
                    current = list(flip_prefix(''.join(current), i+1))
                else:
                    # Flip first bit then prefix up to position i
                    result.append(1)
                    current = list(flip_prefix(''.join(current), 1))
                    result.append(i+1)
                    current = list(flip_prefix(''.join(current), i+1))
                    
    return [len(result)] + result

def solve_test_cases(t: int, cases: list[tuple[int, str, str]]) -> list[list[int]]:
    """
    Solves multiple test cases.
    Input: number of cases t and list of (n, a, b) tuples
    Returns: list of solutions for each case
    """
    results = []
    for n, a, b in cases:
        results.append(solve_binary_strings(n, a, b))
    return results
```