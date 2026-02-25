```python
from collections import Counter
import sys
import math

def solve(T, data):
    results = []
    
    for _ in range(T):
        N = data[_][0]
        A = data[_][1]

        counter = Counter(A)

        possible_lengths = sorted(counter.keys())

        dp = [0]*(possible_lengths[-1]+1)
        dp_count = [0]*(possible_lengths[-1]+1)

        dp[possible_lengths[0]] = counter[possible_lengths[0]]*possible_lengths[0]
        dp_count[possible_lengths[0]] = counter[possible_lengths[0]]

        for i in range(1, len(possible_lengths)):
            dp[possible_lengths[i]] = dp[possible_lengths[i-1]]
            dp_count[possible_lengths[i]] = dp_count[possible_lengths[i-1]]

            if possible_lengths[i] != possible_lengths[i-1] + 1:
                dp[possible_lengths[i]] += possible_lengths[i] * counter[possible_lengths[i]]
                dp_count[possible_lengths[i]] += counter[possible_lengths[i]]
            else:
                if possible_lengths[i-1] - 1 >= 0:
                    dp[possible_lengths[i]] = max(
                            dp[possible_lengths[i]],
                            dp[possible_lengths[i-1] - 1] + possible_lengths[i] * counter[possible_lengths[i]]
                        )
                    dp_count[possible_lengths[i]] = max(
                            dp_count[possible_lengths[i]],
                            dp_count[possible_lengths[i-1]-1] + counter[possible_lengths[i]]
                        )

        min_cost = sys.maxsize
        min_len = -1

        for i in range(len(dp)):
            if dp[i] == dp[-1] and dp_count[i] < min_cost:
                min_cost = dp_count[i]
                min_len = i

        results.append((min_len, min_cost))

    return results
```