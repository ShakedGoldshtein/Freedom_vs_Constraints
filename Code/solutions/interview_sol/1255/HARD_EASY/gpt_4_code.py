```python
def solve(T, tests):

    def test_case(s, k):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        chars = list(s)
        chars.sort()
        result = []
        for i, char in enumerate(alphabet):
            result.append(char)
            if chars and chars[0] == char:
                k -= 1
                chars.pop(0)

            if len(result) == len(s):
                break 

        return "".join(result) if k >= 0 else "NOPE"

    return [test_case(s, k) for s, k in tests]


print(solve(4, [('helowrd', 0), ('background', 0), ('abcdefghijklmnopqrstuvwxyz', 0), ('b', 1)]))
```