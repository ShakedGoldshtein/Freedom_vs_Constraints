```python
def determine_server_status(n, commands):
    a_total = 0
    a_success = 0
    b_total = 0
    b_success = 0

    for t, x, y in commands:
        if t == 1:
            a_total += 10
            a_success += x
        else:
            b_total += 10
            b_success += x

    a_status = "LIVE" if a_success * 2 >= a_total else "DEAD"
    b_status = "LIVE" if b_success * 2 >= b_total else "DEAD"

    return (a_status, b_status)
```