```python
class MountainTracker:
    def __init__(self, heights):
        self.n = len(heights)
        self.heights = heights.copy()
        self.next_higher = [-1] * self.n
        self.prev_occurrence = {}
        self.next_occurrence = {}
        self._build_data_structures()
    
    def _build_data_structures(self):
        stack = []
        for i in range(self.n):
            while stack and self.heights[i] > self.heights[stack[-1]]:
                idx = stack.pop()
                self.next_higher[idx] = i
            stack.append(i)
        
        self.prev_occurrence.clear()
        self.next_occurrence.clear()
        
        for i in range(self.n):
            height = self.heights[i]
            if height in self.prev_occurrence:
                self.next_occurrence[self.prev_occurrence[height]] = i
            self.prev_occurrence[height] = i
        
        for height in set(self.heights):
            if height in self.prev_occurrence:
                self.next_occurrence[self.prev_occurrence[height]] = -1
    
    def update(self, index, new_height):
        self.heights[index] = new_height
        self._rebuild_affected_region(max(0, index - 1), min(self.n - 1, index + 1))
    
    def _rebuild_affected_region(self, start, end):
        stack = []
        for i in range(max(0, start - 1), min(self.n, end + 2)):
            while stack and self.heights[i] > self.heights[stack[-1]]:
                idx = stack.pop()
                if start - 1 <= idx <= end + 1:
                    self.next_higher[idx] = i
            stack.append(i)
        
        while stack:
            idx = stack.pop()
            if start - 1 <= idx <= end + 1:
                self.next_higher[idx] = -1
        
        affected_indices = set()
        for i in range(max(0, start - 1), min(self.n, end + 2)):
            affected_indices.add(i)
            height = self.heights[i]
            if height in self.prev_occurrence:
                prev_idx = self.prev_occurrence[height]
                if prev_idx != i and prev_idx in affected_indices:
                    self.next_occurrence[prev_idx] = i
        
        for i in sorted(affected_indices):
            height = self.heights[i]
            self.prev_occurrence[height] = i
        
        for height in set(self.heights[i] for i in affected_indices):
            if height in self.prev_occurrence:
                last_idx = self.prev_occurrence[height]
                self.next_occurrence[last_idx] = -1
    
    def query(self, index):
        current_height = self.heights[index]
        next_idx = self.next_higher[index]
        
        while next_idx != -1:
            next_height = self.heights[next_idx]
            if self.next_occurrence.get(next_idx, -1) == -1:
                return next_height
            next_idx = self.next_higher[next_idx]
        
        return -1

def process_queries(T, test_cases):
    results = []
    
    for _ in range(T):
        n, q = test_cases[_]['nq']
        heights = test_cases[_]['heights']
        queries = test_cases[_]['queries']
        
        tracker = MountainTracker(heights)
        case_results = []
        
        for query in queries:
            if query[0] == 0:
                _, A, B = query
                tracker.update(A, B)
            else:
                _, A = query
                result = tracker.query(A)
                case_results.append(result)
        
        results.append(case_results)
    
    return results

def solve(T, nq_list, heights_list, queries_list):
    test_cases = []
    for i in range(T):
        test_cases.append({
            'nq': nq_list[i],
            'heights': heights_list[i],
            'queries': queries_list[i]
        })
    
    return process_queries(T, test_cases)
```