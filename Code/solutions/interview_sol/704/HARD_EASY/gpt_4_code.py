Here is the production-grade Python solution for the provided problem:

```python
def find_modulo(T, test_cases):
    result_list = []
    for num in range(T):
        A, N, M = test_cases[num]
        str_num = str(A) * N
        int_num = int(str_num)
        result = int_num % M
        result_list.append(result)
    return result_list
```

You can call the function with example input like this:

```python
T = 2
test_cases = [(12, 2, 17), (523, 3, 11)]
print(find_modulo(T, test_cases))
```

This function `find_modulo` takes two arguments: the number of test cases `T` and a list of tuples as `test_cases` where each tuple contains three integers `A`, `N` and `M`. The function, for each test case, creates a big number by repetitively appending `N` instances of `A` as a string, Converts the resultant string to an integer, calculates its modulo `M` and appends the result to the `result_list`. Finally, returns the `result_list`.