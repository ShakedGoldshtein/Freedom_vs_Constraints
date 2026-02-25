```python
def is_balanced(N, P, participants):
    cakewalk_threshold = P // 2
    hard_threshold = P // 10
    
    cakewalk_count = 0
    hard_count = 0
    
    for participants_solved in participants:
        if participants_solved >= cakewalk_threshold:
            cakewalk_count += 1
        elif participants_solved <= hard_threshold:
            hard_count += 1
    
    return cakewalk_count == 1 and hard_count == 2

def main():
    T = int(input().strip())
    results = []
    
    for _ in range(T):
        N, P = map(int, input().split())
        participants = list(map(int, input().split()))
        results.append("yes" if is_balanced(N, P, participants) else "no")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
```