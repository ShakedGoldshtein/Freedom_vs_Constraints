```python
def solve(n, k, chains):
    def disassemble_chain(chain):
        moves = len(chain) - 1
        dolls = chain[::-1]  # reverse to get nested dolls from innermost out
        return moves, dolls
    
    def assemble_linear_chain(dolls):
        # To assemble dolls in order 1->2->3->...->n
        moves = len(dolls) - 1
        return moves
    
    # First disassemble all chains
    total_moves = 0
    all_dolls = []
    
    # Process each chain
    for chain in chains:
        moves, dolls = disassemble_chain(chain)
        total_moves += moves
        all_dolls.extend(dolls)
        
    # Sort dolls to get final ordering 1->2->...->n
    all_dolls.sort()
    
    # Add moves needed to assemble final chain
    total_moves += assemble_linear_chain(all_dolls)
    
    return total_moves
```