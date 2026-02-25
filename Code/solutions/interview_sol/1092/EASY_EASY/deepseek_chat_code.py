```python
def solve_test_case(N, K, E, M, others, sergey_first):
    total_others = []
    for scores in others:
        total = sum(scores[:E-1]) + scores[E-1]
        total_others.append(total)
    
    sergey_current = sum(sergey_first)
    total_others.sort(reverse=True)
    
    if K == N:
        required_total = 0
    else:
        required_total = total_others[K-1] + 1
    
    needed = required_total - sergey_current
    if needed > M:
        return "Impossible"
    if needed < 0:
        return 0
    return needed

def main():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        N = int(input_data[index]); index += 1
        K = int(input_data[index]); index += 1
        E = int(input_data[index]); index += 1
        M = int(input_data[index]); index += 1
        
        others = []
        for _ in range(N-1):
            scores = list(map(int, input_data[index:index+E]))
            index += E
            others.append(scores)
        
        sergey_first = list(map(int, input_data[index:index+E-1]))
        index += E-1
        
        result = solve_test_case(N, K, E, M, others, sergey_first)
        results.append(str(result))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
```