```python
def solve(n, commands):
    """
    Determines if servers a and b are 'alive' based on ping command results.
    
    Args:
        n: Number of ping commands
        commands: List of lists containing [t, x, y] for each command
                 where t=1 for server a, t=2 for server b
                 x is packets reached, y is packets lost
    
    Returns:
        List containing two strings - status of server a and b 
        Either "LIVE" or "DEAD" for each server
    """
    # Track total packets and successful packets for each server
    server_a_total = 0
    server_a_success = 0
    server_b_total = 0
    server_b_success = 0
    
    # Process each command
    for t, x, y in commands:
        if t == 1:  # Server a
            server_a_total += (x + y)
            server_a_success += x
        else:  # Server b
            server_b_total += (x + y) 
            server_b_success += x
            
    # Server is alive if at least half packets reached successfully
    result = []
    result.append("LIVE" if server_a_success * 2 >= server_a_total else "DEAD")
    result.append("LIVE" if server_b_success * 2 >= server_b_total else "DEAD")
    
    return result
```