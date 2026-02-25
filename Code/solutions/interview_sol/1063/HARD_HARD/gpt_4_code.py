```python
def find_remainder(T, testcases):
    if not 1 <= T <= 1000:
        raise ValueError("T must be between 1 and 1000.")
    output = []
    for testcase in testcases:
        A, B = testcase
        if not (1 <= A <= 10000 and 1 <= B <= 10000):
            raise ValueError("A and B must be between 1 and 10000.")
        output.append(A % B)
    return output
```