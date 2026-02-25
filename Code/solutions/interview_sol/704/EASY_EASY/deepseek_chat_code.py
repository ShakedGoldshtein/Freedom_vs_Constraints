```python
def mod_pow(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

def solve_test_case(A, N, M):
    if N == 0:
        return 0
    
    len_A = len(str(A))
    pow_10_len = mod_pow(10, len_A, M)
    
    numerator = (mod_pow(pow_10_len, N, M) - 1 + M) % M
    denominator = (pow_10_len - 1 + M) % M
    
    if denominator == 0:
        return (A % M * N) % M
    
    inv_denom = pow(denominator, M - 2, M)
    geometric_sum = (numerator * inv_denom) % M
    
    return (A % M * geometric_sum) % M

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        A = int(input_data[index])
        N = int(input_data[index+1])
        M = int(input_data[index+2])
        index += 3
        results.append(str(solve_test_case(A, N, M)))
    print("\n".join(results))

if __name__ == "__main__":
    main()
```