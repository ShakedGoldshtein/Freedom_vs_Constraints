```python
def divide_stones(n, stones):
    stones.sort(reverse=True)
    solo = []
    chewbacca = []
    total_value_solo, total_value_chewbacca = 0, 0
    for stone in stones:
        if total_value_solo <= total_value_chewbacca:
            solo.append(stone)
            total_value_solo += stone
        else:
            chewbacca.append(stone)
            total_value_chewbacca += stone
    return solo[::-1], chewbacca[::-1]

```
Please note that due to the constraints of the problem, the specific function has a time complexity of O(n log n) due to the sort operation and a space complexity of O(n) as we are storing the results in two separate lists. This is likely the most efficient solution given the requirements of the problem.