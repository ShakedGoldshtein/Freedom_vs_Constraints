```python
def min_sweets(n, m, boys, girls):
    boys.sort()
    girls.sort()
    if boys[-1] > girls[0]:
        return -1
    elif boys[-1] == girls[0]:
        return sum(girls) + boys[-2]*(m-1) + sum(boys[:-2])*m
    else:
        return sum(girls) + boys[-1]*(m-1) + sum(boys[:-1])*m
```