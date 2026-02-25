```python
def disarium_number(number):
    str_num = str(number)
    sum_val = sum(int(str_num[i]) ** (i + 1) for i in range(len(str_num)))
    return "Disarium !!" if sum_val == number else "Not !!"
```