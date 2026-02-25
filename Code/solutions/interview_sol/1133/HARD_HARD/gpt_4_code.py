```python
from collections import Counter
from math import gcd
from functools import reduce

def solve(T, sequences):
    result = []
    for i in range(T):
        N, A = sequences[i]
        factors = Counter()
        for j in A:
            divisor = 2
            while divisor * divisor <= j:
                while (j % divisor) == 0:
                    factors[divisor] += 1
                    j //= divisor 
                divisor += 1
            if j > 1:
               factors[j] += 1
        res_gcd = reduce(gcd, factors.values())
        wire_length = max(factors.keys())
        total_wires = sum(v // res_gcd for v in factors.values())
        result.append((wire_length, total_wires))
    return result

# Test the function
print(solve(1, [ (3, [2,4,8]) ]))

```