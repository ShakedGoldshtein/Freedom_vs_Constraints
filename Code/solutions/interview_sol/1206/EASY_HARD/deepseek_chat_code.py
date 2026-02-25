```python
def solve(N1, N2, N3, list1, list2, list3):
    from collections import defaultdict
    
    count = defaultdict(int)
    
    for num in list1:
        count[num] += 1
    for num in list2:
        count[num] += 1
    for num in list3:
        count[num] += 1
    
    result = []
    for num in sorted(count.keys()):
        if count[num] >= 2:
            result.append(num)
    
    return [len(result)] + result
```