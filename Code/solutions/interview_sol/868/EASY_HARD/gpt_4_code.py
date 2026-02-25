```python
def num_of_beautiful_subarrays(T, test_cases):
    result = []
    
    for t in range(T):
        N, K, A = test_cases[t]
        total = 0
        
        for i in range(N):
            counter = [0]*2001
            max_counter = [0]*2001
            
            for j in range(i, N):
                counter[A[j]] += 1
                max_counter[counter[A[j]]] += 1
                
                if K % counter[A[j]] == 0:
                    m = K // counter[A[j]]
                else:
                    m = K // counter[A[j]] + 1
                
                if m <= max_counter[counter[A[j]]]:
                    total += 1
                    
        result.append(total)
        
    return result
```