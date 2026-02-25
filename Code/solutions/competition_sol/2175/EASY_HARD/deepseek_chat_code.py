```python
def solve(m, numbers):
    class LinearBasis:
        def __init__(self):
            self.basis = []
            self.indices = []
        
        def insert(self, x, idx):
            for i, (b, _) in enumerate(self.basis):
                if x ^ b < x:
                    x ^= b
            if x:
                for i, (b, _) in enumerate(self.basis):
                    if b ^ x < b:
                        self.basis[i] = (b ^ x, self.indices[i])
                self.basis.append((x, idx))
                self.indices.append(idx)
                return False
            return True
        
        def represent(self, x):
            if x == 0:
                return []
            temp = x
            used = []
            for i, (b, idx) in enumerate(self.basis):
                if temp ^ b < temp:
                    temp ^= b
                    used.append(idx)
            if temp == 0:
                return used
            return None
    
    basis = LinearBasis()
    result = []
    
    for i, num in enumerate(numbers):
        x = int(num)
        if basis.insert(x, i):
            rep = basis.represent(x)
            if rep is not None:
                rep.sort()
                result.append(f"{len(rep)} " + " ".join(map(str, rep)))
            else:
                result.append("0")
        else:
            result.append("0")
    
    return result
```