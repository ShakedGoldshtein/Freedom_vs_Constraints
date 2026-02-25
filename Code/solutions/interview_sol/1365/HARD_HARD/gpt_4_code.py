```python
def number_of_strings(s):
    if ('c' in s) or ('k' in s):
        return 0
    MOD = 10**9+7
    count_ff = s.count('ff')
    count_gg = s.count('gg')
    possibilities = pow(2, count_ff, MOD) * pow(2, count_gg, MOD)
    possibilities %= MOD
    return possibilities
```