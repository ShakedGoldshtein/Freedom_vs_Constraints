```python
def iq_test(numbers_str):
    numbers = list(map(int, numbers_str.split()))
    even_count = 0
    odd_count = 0
    last_even_pos = -1
    last_odd_pos = -1

    for i, num in enumerate(numbers, start=1):
        if num % 2 == 0:
            even_count += 1
            last_even_pos = i
        else:
            odd_count += 1
            last_odd_pos = i

    if even_count == 1:
        return last_even_pos
    elif odd_count == 1:
        return last_odd_pos
    else:
        raise ValueError("No unique evenness found in the input sequence")
```