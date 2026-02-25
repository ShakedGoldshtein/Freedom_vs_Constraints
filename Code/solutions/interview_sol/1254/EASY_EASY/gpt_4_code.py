```python
def is_contest_balanced(T, tests):
    results = []
    for t in range(T):
        N, P, problems = tests[t]
        cakewalk_count = len([p for p in problems if p >= P // 2])
        hard_count = len([p for p in problems if p <= P // 10])
        if cakewalk_count == 1 and hard_count == 2:
            results.append("yes")
        else:
            results.append("no")
    return results

tests = [
    (3, 100, [10, 1, 100]),
    (3, 100, [11, 1, 100]),
    (3, 100, [10, 1, 10]),
    (3, 100, [10, 1, 50]),
    (4, 100, [50, 50, 50, 50]),
    (4, 100, [1, 1, 1, 1])
] 

print(is_contest_balanced(6, tests))
```
This function is_contest_balanced checks if a contest is balanced by counting the number of cakewalk and hard problems. If there is exactly 1 cakewalk problem and exactly 2 hard problems, then it considers the contest as balanced and appends "yes" to the results list. Otherwise, it appends "no". It then returns the results list after looping through all the test cases.