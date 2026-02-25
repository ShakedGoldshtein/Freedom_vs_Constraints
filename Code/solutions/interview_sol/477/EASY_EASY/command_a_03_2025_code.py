```python
def solve(n: int, k: int) -> str:
    def generate_s(n: int) -> str:
        if n == 1:
            return "0"
        prev = "0"
        for i in range(2, n + 1):
            inverted = ''.join('1' if bit == '0' else '0' for bit in prev)
            prev = prev + "1" + inverted[::-1]
        return prev

    s_n = generate_s(n)
    return s_n[k - 1]
```