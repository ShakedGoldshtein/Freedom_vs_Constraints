```python
from math import comb

def solve(S: int, N: int, M: int, K: int) -> float:

  if M <= 1 or N > 1 and K == 0: return 1.0 
  if S == N: return 1.0
  if N > M or M-1 < K: return 0.0

  chance = 0
  for i in range(max(0, K-1), min(M-1, N-1) + 1):
    chance += comb(M-1, i) * comb(S-M, N-i-1)
  total_ways = comb(S-1, N-1)

  answer = chance / total_ways
  return round(answer, 6)
```