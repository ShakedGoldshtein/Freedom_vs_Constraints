```python
def solve(T, cases):
    results = []
    for case in cases:
        N, K, A = case
        count = 0
        for l in range(N):
            freq = [0] * 2001
            for r in range(l, N):
                length = r - l + 1
                m = (K + length - 1) // length
                total_len = m * length
                pos_in_sorted = K - 1
                block_pos = pos_in_sorted % length
                block_idx = pos_in_sorted // length
                
                freq[A[r]] += 1
                
                temp_freq = freq.copy()
                x = None
                cnt = 0
                for num in range(1, 2001):
                    if temp_freq[num] > 0:
                        if cnt + temp_freq[num] * m > pos_in_sorted:
                            x = num
                            break
                        cnt += temp_freq[num] * m
                
                if x is None:
                    continue
                
                f = freq[x]
                
                if any(freq[num] == f for num in range(1, 2001) if freq[num] > 0):
                    count += 1
        results.append(count)
    return results
```