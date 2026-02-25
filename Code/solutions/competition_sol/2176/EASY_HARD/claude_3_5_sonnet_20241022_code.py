```python
def solve(n, actions):
    MOD = 1000000007
    
    # Track currently active orders and their prices
    active_orders = set()
    # Track whether an order MUST be buy or sell based on constraints
    must_be_buy = set()  
    must_be_sell = set()
    
    for i, (action, price) in enumerate(actions):
        if action == "ADD":
            active_orders.add(price)
            
            # Check if this order must be BUY or SELL based on prices
            for p in active_orders:
                if p != price:
                    if p < price and p not in must_be_sell:
                        must_be_buy.add(p)
                    if p > price and p not in must_be_buy:  
                        must_be_sell.add(p)
                        
        else: # ACCEPT
            # Can only accept best BUY or best SELL
            best_buy = -1
            best_sell = float('inf')
            
            for p in active_orders:
                if p in must_be_buy:
                    best_buy = max(best_buy, p)
                elif p in must_be_sell:
                    best_sell = min(best_sell, p)
                else:
                    if p < price:
                        must_be_buy.add(p)
                        best_buy = max(best_buy, p)
                    elif p > price:
                        must_be_sell.add(p)
                        best_sell = min(best_sell, p)
            
            # Price must match either best buy or best sell
            if price != best_buy and price != best_sell:
                return 0
                
            active_orders.remove(price)
            if price in must_be_buy:
                must_be_buy.remove(price)
            if price in must_be_sell:
                must_be_sell.remove(price)
    
    # Count orders that could be either BUY or SELL
    undecided = len(active_orders) - len(must_be_buy) - len(must_be_sell)
    
    # Each undecided order doubles number of possibilities
    return pow(2, undecided, MOD)
```