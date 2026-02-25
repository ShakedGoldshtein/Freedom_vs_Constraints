```python
def solve(m, numbers):
    rows, res, pos, ind = [], [], {}, 0
    
    for x in numbers:
        temp, idxs = x, []
        
        for i in range(ind-1, -1, -1):
            if temp & (1 << rows[i]):
                temp ^= (1 << rows[i])
                idxs.extend(res[i])
                
        if temp > 0:
            cur_ind = temp.bit_length() - 1
            rows = [cur_ind] + rows
            res = [idxs + [ind]] + res
            pos[cur_ind] = len(res) - 1
            yield '0'
        else:
            i = pos[idxs[0]]
            rows = rows[i+1:] + [rows[i]]
            res = res[i+1:] + [res[i]]
            for i in range(len(rows)):
                pos[rows[i]] = i
            yield str(len(idxs)) + ' ' + ' '.join(map(str, idxs[::-1]))
        
        ind += 1
            
numbers = [7,6,5,4,3,2,1]
gen = solve(7, numbers)
for _ in range(7):
    print(next(gen))
```