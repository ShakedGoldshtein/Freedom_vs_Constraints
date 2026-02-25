```python
def solve(n, k, chains):
    def count_operations(chain):
        ops = 0
        for i in range(len(chain)-1):
            ops += 1  # Operation to remove each doll except last
        return ops
            
    # Count operations needed to disassemble all chains
    total_ops = 0
    for chain in chains:
        total_ops += count_operations(chain)
        
    # Count operations needed to build final chain
    for i in range(1, n):
        total_ops += 1  # Operation to nest each doll
        
    return total_ops

def test():
    # Test case 1
    n1, k1 = 3, 2
    chains1 = [[1,2], [3]]
    assert solve(n1, k1, chains1) == 1
    
    # Test case 2
    n2, k2 = 7, 3  
    chains2 = [[1,3,7], [2,5], [4,6]]
    assert solve(n2, k2, chains2) == 10
```