Here is the Python code to solve the problem:

```python
def is_contest_balanced(T, cases):
    results = []
    for i in range(T):
        N, P, problem_statistics = cases[i]
        cakewalks = hard = 0
        for statistic in problem_statistics:
            if statistic >= P//2:
                cakewalks += 1
            if statistic <= P//10:
                hard += 1
        if cakewalks == 1 and hard == 2:
            results.append('yes')
        else:
            results.append('no')
    return results


T = 6
cases = [
    (3, 100, [10, 1, 100]),
    (3, 100, [11, 1, 100]),
    (3, 100, [10, 1, 10]),
    (3, 100, [10, 1, 50]),
    (4, 100, [50, 50, 50, 50]),
    (4, 100, [1, 1, 1, 1])
]
print(is_contest_balanced(T, cases))
```

The function `is_contest_balanced` takes two parameters: the number of test cases and a list of cases. Each case consists of a tuple: the number of problems, the number of participants, and a list of problem-solving statistics. It returns the list of results for each case, whether the contest is balanced or not.