```python
def determine_server_status(n, commands):
    """
    Determines the status ("LIVE" or "DEAD") of servers a and b based on ping command results.

    Args:
        n: Number of ping commands (2 <= n <= 1000).
        commands: List of tuples, each containing (t, x, y) where:
            - t: 1 for server a, 2 for server b.
            - x: Packets received (0 <= x <= 10).
            - y: Packets lost (0 <= y <= 10, x + y = 10).

    Returns:
        A tuple of two strings: (server_a_status, server_b_status).
    """
    def calculate_status(total_packets, received_packets):
        return "LIVE" if received_packets >= total_packets / 2 else "DEAD"

    a_total = 0
    a_received = 0
    b_total = 0
    b_received = 0

    for t, x, y in commands:
        if t == 1:
            a_total += 10
            a_received += x
        else:
            b_total += 10
            b_received += x

    return (
        calculate_status(a_total, a_received),
        calculate_status(b_total, b_received)
    )
```