```python
from collections import defaultdict

def solve(k, box):
    total = sum(sum(box[i]) for i in range(k))
    if total % k != 0:
        return "No"
    average = total // k
    m = defaultdict(int)
    for i in range(k):
        for j in box[i]:
            m[j] = i
    visited = [0]*k
    result = [(0, 0)]*k
    for i in range(k):
        if not visited[i]:
            j = i
            path = []
            while visited[j] == 0:
                visited[j] = 1
                path.append(j)
                s = sum(box[j]) - result[j][0]
                if m[average - s] >= 0 and (average - s not in box[j] or box[j].count(average - s) == 1 and visited[m[average - s]] == 0):
                    j = m[average - s]
                    result[j] = (average - s, i+1)
                else:
                    for l in path:
                        visited[l] = 0
                        result[l] = (0, 0)
                    break
    if visited.count(0) == 0:
        return ["Yes"] + [f'{x[0]} {x[1]}' for x in result]
    else:
        return "No"

print(solve(4, [[1, 7, 4], [3, 2], [8, 5], [10]]))
print(solve(2, [[3, -2], [-1, 5]]))
print(solve(2, [[-10, 10], [0, -20]]))
```