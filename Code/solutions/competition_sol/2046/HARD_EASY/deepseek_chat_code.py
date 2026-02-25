```python
def solve(n, a_list):
    a = [0] * (n + 1)
    for i in range(2, n + 1):
        a[i] = a_list[i - 2]
    
    visited = [0] * (n + 1)
    dp = [0] * (n + 1)
    result = []
    
    for start in range(1, n):
        steps = []
        current = 1
        y = 0
        valid = True
        
        while True:
            if current <= 0 or current > n:
                break
                
            if current == 1:
                if start in steps:
                    result.append(-1)
                    valid = False
                    break
                steps.append(start)
                
            if visited[current] == start:
                result.append(-1)
                valid = False
                break
                
            if dp[current] != 0:
                y += dp[current]
                break
                
            visited[current] = start
            
            if current == 1:
                next_x = current + start
                if next_x <= 0 or next_x > n:
                    y += start
                    break
                y += start
                current = next_x
            else:
                y += a[current]
                next_x = current - a[current]
                if next_x <= 0 or next_x > n:
                    break
                current = next_x
                
        if valid:
            result.append(y)
            for node in steps:
                if node <= n:
                    dp[node] = y
                    
    return result

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a_list = list(map(int, data[1:1+n-1]))
    results = solve(n, a_list)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
```