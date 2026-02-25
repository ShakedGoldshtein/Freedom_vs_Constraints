```python
def solve(N, pairs):
    if N == 1:
        return 0

    all_nums = []
    for x, y in pairs:
        all_nums.append(x)
        all_nums.append(y)
    
    all_nums.sort()
    total_len = len(all_nums)
    
    candidate1 = (all_nums[N-1] - all_nums[0]) * (all_nums[total_len-1] - all_nums[N])
    
    min_r = float('inf')
    max_r = 0
    min_b = float('inf')
    max_b = 0
    
    sorted_pairs = []
    for x, y in pairs:
        sorted_pairs.append((min(x, y), max(x, y)))
    
    sorted_pairs.sort(key=lambda p: p[0])
    
    min_b = float('inf')
    max_b = 0
    for i in range(N-1, -1, -1):
        min_b = min(min_b, sorted_pairs[i][1])
        max_b = max(max_b, sorted_pairs[i][1])
    
    candidate2 = (sorted_pairs[N-1][0] - sorted_pairs[0][0]) * (max_b - min_b)
    
    heap = []
    import heapq
    for i in range(N):
        heapq.heappush(heap, sorted_pairs[i][1])
    
    min_diff = float('inf')
    max_val = max(heap)
    for i in range(N):
        min_val = heap[0]
        min_diff = min(min_diff, max_val - min_val)
        if sorted_pairs[i][1] == heap[0]:
            heapq.heappop(heap)
            while heap and heap[0] <= sorted_pairs[i][0]:
                heapq.heappop(heap)
        if not heap:
            break
        heapq.heappush(heap, sorted_pairs[i][0])
        max_val = max(max_val, sorted_pairs[i][0])
    
    candidate3 = (all_nums[total_len-1] - all_nums[0]) * min_diff
    
    return min(candidate1, candidate2, candidate3)
```