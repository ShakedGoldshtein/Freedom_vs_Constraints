```python
MOD = 10**9 + 7


def solve(actions: list[tuple[str, int]]) -> int:
    """
    Solves the order book problem by restoring the directions of ADD actions.

    Args:
        actions (list of tuples): A list of actions where each action is a tuple of (action_type, price).
                                  action_type is either "ADD" or "ACCEPT".
                                  price is an integer representing the price of the order.

    Returns:
        int: The number of ways to restore directions of ADD actions modulo 10^9 + 7.
             Returns 0 if it's impossible to correctly restore directions.
    """
    buy: set[int] = set()  # Set to store BUY orders
    sell: set[int] = set()  # Set to store SELL orders
    ways: int = 1  # Number of ways to restore directions

    for action, price in actions:
        if action == "ADD":
            # If both buy and sell sets are empty, the new order can be either BUY or SELL
            if not buy and not sell:
                ways = (ways * 2) % MOD
                sell.add(price)  # Arbitrarily add to sell, but it could be either
            else:
                # Determine if the new order should be BUY or SELL based on existing orders
                if buy and price > min(sell):
                    return 0  # Invalid ADD action, cannot add BUY order with price > best SELL
                if sell and price < max(buy):
                    return 0  # Invalid ADD action, cannot add SELL order with price < best BUY
                if not buy or price < min(sell):
                    buy.add(price)  # Add as BUY order
                elif not sell or price > max(buy):
                    sell.add(price)  # Add as SELL order
                else:
                    return 0  # Invalid ADD action, cannot determine direction
        elif action == "ACCEPT":
            # Check if the accepted price exists in either buy or sell set
            if price in buy:
                buy.remove(price)
            elif price in sell:
                sell.remove(price)
            else:
                return 0  # Invalid ACCEPT action, price not found in either set

    return ways


# Example usage:
# actions = [("ADD", 1), ("ACCEPT", 1), ("ADD", 2), ("ACCEPT", 2), ("ADD", 3), ("ACCEPT", 3)]
# print(solve(actions))  # Output: 8
```