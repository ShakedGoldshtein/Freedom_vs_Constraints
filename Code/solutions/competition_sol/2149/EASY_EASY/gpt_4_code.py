```python
from collections import deque

def connected_components(n, m, lst):

    # Initialize flag and components matrix
    flag = [False] * (1 << n)
    components = [False] * (1 << n)

    # Add each integer to the flag list
    for i in lst:
        flag[i] = True

    # Perform BFS on all unvisited nodes
    ans = 0
    for integer in range(1 << n):
        if not flag[integer] or components[integer]:
            continue
            
        ans += 1
        queue = deque([integer])
        
        while queue:
            node = queue.popleft()
            
            if components[node]: continue
            components[node] = True
            
            # add all nodes reachable from here to the queue
            if flag[node]:
                for i in range(n):
                    queue.append(node ^ (1 << i))

    return ans

```