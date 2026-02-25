```python
class MountainSolver:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr.copy()
        self.next_higher = [-1] * n
        self.prev_occurrence = {}
        self.compute_next_higher()
    
    def compute_next_higher(self):
        stack = []
        for i in range(self.n):
            while stack and self.arr[stack[-1]] < self.arr[i]:
                idx = stack.pop()
                self.next_higher[idx] = i
            stack.append(i)
        
        self.prev_occurrence = {}
        for i in range(self.n):
            self.prev_occurrence[self.arr[i]] = i
    
    def update(self, idx, val):
        self.arr[idx] = val
        self.compute_next_higher()
    
    def query(self, idx):
        current_height = self.arr[idx]
        next_idx = self.next_higher[idx]
        
        if next_idx == -1:
            return -1
        
        candidate_height = self.arr[next_idx]
        prev_occurrence = self.prev_occurrence.get(candidate_height, -1)
        
        if prev_occurrence < idx or prev_occurrence == next_idx:
            return candidate_height
        
        while next_idx != -1:
            candidate_height = self.arr[next_idx]
            prev_occurrence = self.prev_occurrence.get(candidate_height, -1)
            if prev_occurrence < idx or prev_occurrence == next_idx:
                return candidate_height
            next_idx = self.next_higher[next_idx]
        
        return -1

def solve(T, cases):
    results = []
    for case in cases:
        n, q = case['nq']
        arr = case['arr']
        queries = case['queries']
        
        solver = MountainSolver(n, arr)
        case_results = []
        
        for query in queries:
            if query[0] == 0:
                solver.update(query[1], query[2])
            else:
                result = solver.query(query[1])
                case_results.append(result)
        
        results.append(case_results)
    
    return results
```