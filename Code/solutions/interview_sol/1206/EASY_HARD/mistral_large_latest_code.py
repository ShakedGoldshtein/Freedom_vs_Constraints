```python
def solve(list1, list2, list3):
    from collections import defaultdict

    count = defaultdict(int)
    pointers = [0, 0, 0]
    lists = [list1, list2, list3]
    current = [None, None, None]

    def update_current():
        for i in range(3):
            if pointers[i] < len(lists[i]):
                current[i] = lists[i][pointers[i]]
            else:
                current[i] = None

    update_current()
    result = []

    while any(current):
        min_val = float('inf')
        for i in range(3):
            if current[i] is not None and current[i] < min_val:
                min_val = current[i]

        if min_val == float('inf'):
            break

        total = 0
        for i in range(3):
            if current[i] == min_val:
                total += 1
                pointers[i] += 1
                update_current()

        if total >= 2:
            result.append(min_val)

    return result
```