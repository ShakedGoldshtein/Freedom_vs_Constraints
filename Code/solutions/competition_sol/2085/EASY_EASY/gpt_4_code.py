```python
def solve(n, strings, m, operations):
    all_bin = ['0', '1']
    k = 1
    out = []
    curr_strs = strings[:]
    for  op in operations:
        str_len = len(curr_strs[op[0] - 1]) + len(curr_strs[op[1] - 1])
        curr_strs.append(curr_strs[op[0] - 1] + curr_strs[op[1] - 1])
        while len(all_bin[-1]) < str_len and '0'*(k + 1) not in curr_strs[-1] and '1'*(k + 1) not in curr_strs[-1]:
            all_bin.append(all_bin[-1] + '0')
            all_bin.append(all_bin[-2] + '1')
            k += 1
        k_copy = k
        while any(bin_str not in curr_strs[-1] for bin_str in all_bin) and k_copy > 0:
            k_copy -= 1
            all_bin = all_bin[:2**k_copy]
        out.append(k_copy)
    return out
```