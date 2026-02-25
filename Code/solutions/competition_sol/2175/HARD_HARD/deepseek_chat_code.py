```python
class BinaryBasis:
    def __init__(self, max_bits):
        self.max_bits = max_bits
        self.basis = [None] * max_bits
        self.index_map = [None] * max_bits
    
    def add(self, num, idx):
        original_num = num
        used_indices = []
        
        for bit in range(self.max_bits - 1, -1, -1):
            if not (num >> bit) & 1:
                continue
                
            if self.basis[bit] is None:
                self.basis[bit] = num
                self.index_map[bit] = (original_num, idx, used_indices[:])
                return None
            else:
                num ^= self.basis[bit]
                used_indices.extend(self.index_map[bit][2])
                used_indices.append(self.index_map[bit][1])
        
        return sorted(set(used_indices))

def solve(m, numbers):
    max_bits = 600
    basis = BinaryBasis(max_bits)
    results = []
    
    for idx, num_str in enumerate(numbers):
        num = int(num_str)
        indices = basis.add(num, idx)
        
        if indices is None:
            results.append("0")
        else:
            result_str = f"{len(indices)}"
            for i in indices:
                result_str += f" {i}"
            results.append(result_str)
    
    return results
```