```python
def solve(n: int, commands: list[tuple[int, int, int]]) -> tuple[str, str]:
    """
    Determines if servers 'a' and 'b' are "alive" based on the results of ping commands.

    Args:
        n (int): The number of commands executed.
        commands (list of tuples): Each tuple contains (t_i, x_i, y_i), where:
            - t_i (int): 1 for "ping a", 2 for "ping b".
            - x_i (int): Number of packets successfully reached the server.
            - y_i (int): Number of packets lost.

    Returns:
        tuple: A tuple containing two strings, "LIVE" or "DEAD" for servers 'a' and 'b' respectively.
    """
    # Initialize counters for total packets sent and successfully received for each server
    total_a, success_a = 0, 0
    total_b, success_b = 0, 0

    # Iterate over each command to accumulate totals
    for t, x, y in commands:
        if t == 1:  # Command is "ping a"
            total_a += 10
            success_a += x
        else:  # Command is "ping b"
            total_b += 10
            success_b += x

    # Determine if each server is "alive" based on the condition that at least half of the packets reached successfully
    status_a = "LIVE" if success_a * 2 >= total_a else "DEAD"
    status_b = "LIVE" if success_b * 2 >= total_b else "DEAD"

    return status_a, status_b
```