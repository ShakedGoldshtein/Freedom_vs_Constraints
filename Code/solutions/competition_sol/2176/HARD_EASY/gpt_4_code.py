```python
from bisect import insort_left, bisect_left
from collections import deque
MOD = 10**9 + 7

def order_book(n, events):
    buy = []
    sell = deque()
    dp = [[0, 0] for _ in range(n)]
    dp[-1][0] = dp[-1][1] = 1
    for i in reversed(range(n)):
        op, price = events[i]
        if op == "ADD":
            buy_ins = bisect_left(buy, price)
            sell_ins = bisect_left(sell, price)
            if buy and price < buy[-1]:
                dp[i-1][0] = (dp[i][0] * (len(buy) - buy_ins)
                              + dp[i][1] * (len(buy) - buy_ins + 1)) % MOD
            else:
                dp[i-1][0] = dp[i][0] * (len(buy) - buy_ins) % MOD
            if sell and price > sell[0]:
                dp[i-1][1] = (dp[i][0] * (len(sell) - sell_ins)
                              + dp[i][1] * (len(sell) - sell_ins + 1)) % MOD
            else:
                dp[i-1][1] = dp[i][0] * (len(sell) - sell_ins) % MOD
            insort_left(buy, price)
        else:
            if sell and price > sell[0]:
                dp[i-1][0] = dp[i][0]
            else:
                dp[i-1][0] = 0
            if buy and price < buy[-1]:
                dp[i-1][1] = dp[i][1]
            else:
                dp[i-1][1] = 0
            if sell and sell[0] == price:
                sell.popleft()
            else:
                buy.pop()
    return dp[0][0]

n = int(input().strip())
events = []
for _ in range(n):
    op, price = input().strip().split()
    price = int(price)
    events.append((op, price))

print(order_book(n, events))
```
