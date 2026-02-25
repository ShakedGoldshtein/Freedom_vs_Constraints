```python
def value_modulo(T, test_cases):
    out=[]
    for i in range(T):
        A, N, M = test_cases[i]
        len_A = len(str(A))
        multiply = pow(10, len_A * N, M)
        X = (multiply - 1) // (pow(10, len_A, M) - 1)
        out.append((A * X) % M)
    return out
```