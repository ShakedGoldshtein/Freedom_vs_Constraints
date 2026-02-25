```python
from collections import defaultdict

def count_beautiful_subarrays(A, K):
    n = len(A)
    count = 0
    
    for l in range(n):
        freq = defaultdict(int)
        for r in range(l, n):
            freq[A[r]] += 1
            
            length = r - l + 1
            m = (K + length - 1) // length
            total_length = m * length
            
            pos_in_cycle = (K - 1) % length
            cycle_index = l + pos_in_cycle
            
            if cycle_index < n:
                X = A[cycle_index]
            else:
                full_cycles = K // length
                remaining = K % length
                if remaining == 0:
                    X = A[r]
                else:
                    X = A[l + remaining - 1]
            
            F = freq[X]
            
            if freq.get(F, 0) > 0:
                count += 1
                
    return count

def main():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        N = int(input_data[idx]); idx += 1
        K = int(input_data[idx]); idx += 1
        A = list(map(int, input_data[idx:idx+N]))
        idx += N
        results.append(count_beautiful_subarrays(A, K))
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```