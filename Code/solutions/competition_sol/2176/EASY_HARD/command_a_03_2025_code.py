```python
MOD = 10**9 + 7


def solve(n: int, actions: list[tuple[str, int]]) -> int:
    """
    Solves the order book log restoration problem.

    Args:
        n (int): The number of actions in the log.
        actions (list of tuples): A list of actions where each action is a tuple of (action_type, price).
                                  action_type is either "ADD" or "ACCEPT", and price is an integer.

    Returns:
        int: The number of ways to restore directions of ADD actions modulo 10^9 + 7.
             Returns 0 if it's impossible to correctly restore directions.
    """
    # Initialize the order book with two heaps: buy (max-heap) and sell (min-heap)
    buy: list[int] = []  # Max-heap for buy orders
    sell: list[int] = []  # Min-heap for sell orders
    ways: int = 1  # Number of ways to restore directions

    for action, price in actions:
        if action == "ADD":
            # Determine if the new order can be added as a BUY or SELL
            can_buy: bool = not sell or price < sell[0]  # Can add as BUY if no sell or price < min sell
            can_sell: bool = not buy or price > buy[0]  # Can add as SELL if no buy or price > max buy

            if can_buy and can_sell:
                # If both options are valid, multiply the number of ways by 2
                ways = (ways * 2) % MOD
            elif can_buy:
                # If only BUY is valid, add to buy heap
                buy.append(price)
                buy.sort(reverse=True)  # Maintain max-heap property
            elif can_sell:
                # If only SELL is valid, add to sell heap
                sell.append(price)
                sell.sort()  # Maintain min-heap property
            else:
                # If neither option is valid, it's impossible to restore directions
                return 0
        else:  # ACCEPT
            if price in buy:
                # If the accepted price is in buy heap, remove it
                buy.remove(price)
                buy.sort(reverse=True)  # Maintain max-heap property
            elif price in sell:
                # If the accepted price is in sell heap, remove it
                sell.remove(price)
                sell.sort()  # Maintain min-heap property
            else:
                # If the price is not in either heap, it's impossible to restore directions
                return 0

    return ways
```