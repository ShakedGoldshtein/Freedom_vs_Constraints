```python
def solve(n, commands_data):
    """
    Determines if servers 'a' and 'b' are "alive" based on ping command results.

    A server is "alive" if at least half of the packets sent to it were successful.

    Args:
        n (int): The total number of ping commands performed.
                 (This parameter is included as per the problem's example signature,
                 though not strictly used in the calculation if commands_data is provided.)
        commands_data (list of lists): A list where each inner list represents
                                       a command with [t_i, x_i, y_i].
                                       t_i: 1 for server 'a', 2 for server 'b'.
                                       x_i: successful packets (out of 10).
                                       y_i: lost packets (out of 10).

    Returns:
        list of str: A list containing two strings:
                     - The state of server 'a' ("LIVE" or "DEAD").
                     - The state of server 'b' ("LIVE" or "DEAD").
    """
    successful_packets_a = 0
    total_packets_a = 0
    successful_packets_b = 0
    total_packets_b = 0

    for command in commands_data:
        server_type = command[0]
        successful_x = command[1]
        # y_i (lost packets) is command[2], but not needed as total packets per ping is always 10

        if server_type == 1:
            successful_packets_a += successful_x
            total_packets_a += 10  # Each ping sends 10 packets
        elif server_type == 2:
            successful_packets_b += successful_x
            total_packets_b += 10  # Each ping sends 10 packets

    # Determine the state for server 'a'
    # A server is "alive" if successful_packets * 2 >= total_packets
    state_a = "LIVE" if successful_packets_a * 2 >= total_packets_a else "DEAD"

    # Determine the state for server 'b'
    state_b = "LIVE" if successful_packets_b * 2 >= total_packets_b else "DEAD"

    return [state_a, state_b]
```