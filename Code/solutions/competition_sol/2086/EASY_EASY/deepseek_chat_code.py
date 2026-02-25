```python
def solve(n, q, arr, queries):
    max_val = max(arr)
    max_index = arr.index(max_val)
    operations = []
    dq = arr[:]
    for i in range(n):
        A = dq.pop(0)
        B = dq.pop(0)
        operations.append((A, B))
        if A > B:
            dq.insert(0, A)
            dq.append(B)
        else:
            dq.insert(0, B)
            dq.append(A)
        if A == max_val or B == max_val:
            break
    
    cycle = dq[:]
    results = []
    for m in queries:
        if m <= len(operations):
            A, B = operations[m-1]
            results.append((A, B))
        else:
            index = (m - len(operations) - 1) % (n - 1)
            A = max_val
            B = cycle[index + 1]
            results.append((A, B))
    
    return results
```