```python
MOD = 10**9 + 7

def solve(n, actions):
    from bisect import bisect_left, bisect_right
    
    orders = []
    accepted = set()
    add_actions = []
    accept_actions = []
    
    for i, (action_type, price) in enumerate(actions):
        if action_type == "ADD":
            add_actions.append((price, i))
        else:
            accept_actions.append((price, i))
    
    add_actions.sort()
    accept_actions.sort()
    
    add_indices = {price: idx for idx, (price, _) in enumerate(add_actions)}
    
    events = []
    for price, idx in add_actions:
        events.append((idx, 'add', price))
    for price, idx in accept_actions:
        events.append((idx, 'accept', price))
    
    events.sort(key=lambda x: x[0])
    
    buy_orders = []
    sell_orders = []
    
    for _, event_type, price in events:
        if event_type == 'add':
            if not sell_orders or price < sell_orders[0]:
                buy_orders.append(price)
            elif not buy_orders or price > buy_orders[-1]:
                sell_orders.append(price)
            else:
                return 0
            buy_orders.sort()
            sell_orders.sort()
        else:
            if buy_orders and buy_orders[-1] == price:
                buy_orders.pop()
            elif sell_orders and sell_orders[0] == price:
                sell_orders.pop(0)
            else:
                return 0
    
    all_prices = [price for price, _ in add_actions]
    all_prices.sort()
    
    buy_candidates = []
    sell_candidates = []
    ambiguous = []
    
    for price, idx in add_actions:
        if price in accepted:
            continue
        
        pos = bisect_left(all_prices, price)
        left_ok = pos == 0 or all_prices[pos - 1] not in accepted
        right_ok = pos == len(all_prices) - 1 or all_prices[pos + 1] not in accepted
        
        if left_ok and right_ok:
            ambiguous.append(price)
        elif left_ok:
            buy_candidates.append(price)
        elif right_ok:
            sell_candidates.append(price)
        else:
            return 0
    
    result = 1
    count_ambiguous = len(ambiguous)
    
    for _ in range(count_ambiguous + 1):
        result = (result * 2) % MOD
    
    return result
```