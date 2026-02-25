```python
MOD = 10**9 + 7

def solve(n, actions):
    orders = []
    for i in range(n):
        op, p = actions[i]
        orders.append((op, p, i))
    
    events = []
    for op, p, idx in orders:
        if op == 'ADD':
            events.append(('ADD', p, idx))
        else:
            events.append(('ACCEPT', p, idx))
    
    buy_orders = []
    sell_orders = []
    accepted = set()
    
    for event in events:
        if event[0] == 'ADD':
            continue
        else:
            accepted.add(event[1])
    
    add_events = []
    for event in events:
        if event[0] == 'ADD':
            add_events.append(event)
        else:
            add_events.append(event)
    
    sorted_prices = sorted([p for op, p, idx in events])
    price_to_idx = {p: i for i, p in enumerate(sorted_prices)}
    
    seg_size = 1
    while seg_size < len(sorted_prices):
        seg_size <<= 1
    seg = [0] * (2 * seg_size)
    
    def update(pos, val):
        idx = pos + seg_size
        seg[idx] = val
        idx //= 2
        while idx:
            seg[idx] = seg[2*idx] + seg[2*idx+1]
            idx //= 2
    
    def query(l, r):
        res = 0
        l += seg_size
        r += seg_size
        while l < r:
            if l & 1:
                res += seg[l]
                l += 1
            if r & 1:
                r -= 1
                res += seg[r]
            l //= 2
            r //= 2
        return res
    
    for op, p, idx in events:
        if op == 'ADD':
            pos = price_to_idx[p]
            update(pos, 1)
        else:
            pos = price_to_idx[p]
            update(pos, 0)
    
    buy_min = None
    sell_max = None
    res = 1
    active_buys = []
    active_sells = []
    
    for op, p, idx in events:
        if op == 'ADD':
            if buy_min is None and sell_max is None:
                res = (res * 2) % MOD
                active_buys.append(p)
                active_sells.append(p)
                continue
            
            possible = 0
            if buy_min is not None and p < buy_min:
                possible += 1
            if sell_max is not None and p > sell_max:
                possible += 1
            
            if possible == 0:
                return 0
            res = (res * possible) % MOD
            
            if buy_min is not None and p < buy_min:
                active_buys.append(p)
                active_buys.sort(reverse=True)
            elif sell_max is not None and p > sell_max:
                active_sells.append(p)
                active_sells.sort()
            else:
                if p < buy_min:
                    active_buys.append(p)
                    active_buys.sort(reverse=True)
                else:
                    active_sells.append(p)
                    active_sells.sort()
        else:
            pos = price_to_idx[p]
            if p in active_buys:
                active_buys.remove(p)
                if active_buys:
                    buy_min = active_buys[0]
                else:
                    buy_min = None
            elif p in active_sells:
                active_sells.remove(p)
                if active_sells:
                    sell_max = active_sells[0]
                else:
                    sell_max = None
            else:
                return 0
    
    return res

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().split('\n')
    n = int(input_data[0])
    actions = []
    for i in range(1, n + 1):
        parts = input_data[i].split()
        actions.append((parts[0], int(parts[1])))
    print(solve(n, actions))
```