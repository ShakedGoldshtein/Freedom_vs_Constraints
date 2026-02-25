```python
def solve(n, actions):
    MOD = 1000000007
    
    class OrderBook:
        def __init__(self):
            self.buy_offers = []  
            self.sell_offers = []
            self.price_to_direction = {}
            self.active_prices = set()

        def add_order(self, price, direction):
            if price in self.active_prices:
                return False
                
            if direction == 'BUY':
                if self.sell_offers and price >= self.sell_offers[0]:
                    return False
                self.buy_offers.append(price)
                self.buy_offers.sort(reverse=True)
            else:
                if self.buy_offers and price <= self.buy_offers[0]:
                    return False
                self.sell_offers.append(price)
                self.sell_offers.sort()
                
            self.active_prices.add(price)
            self.price_to_direction[price] = direction
            return True

        def accept_order(self, price):
            if price not in self.active_prices:
                return False
                
            direction = self.price_to_direction[price]
            if direction == 'BUY' and (not self.buy_offers or self.buy_offers[0] != price):
                return False
            if direction == 'SELL' and (not self.sell_offers or self.sell_offers[0] != price):
                return False
                
            self.active_prices.remove(price)
            if direction == 'BUY':
                self.buy_offers.remove(price)
            else:
                self.sell_offers.remove(price)
            return True

    def try_assignment(assignments):
        book = OrderBook()
        for action, price in actions:
            if action == 'ADD':
                direction = assignments.get(price)
                if not book.add_order(price, direction):
                    return False
            else:  # ACCEPT
                if not book.accept_order(price):
                    return False
        return True

    # Build graph of dependencies
    add_prices = []
    for action, price in actions:
        if action == 'ADD':
            add_prices.append(price)

    # Try each possible assignment of directions
    result = 0
    for mask in range(1 << len(add_prices)):
        assignments = {}
        for i, price in enumerate(add_prices):
            assignments[price] = 'BUY' if mask & (1 << i) else 'SELL'
        
        if try_assignment(assignments):
            result = (result + 1) % MOD
            
    return result

```