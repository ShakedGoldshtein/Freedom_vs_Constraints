```python
from typing import List, Tuple
from collections import defaultdict
import heapq

def solve(n: int, q: int, phones: List[Tuple[int, int]], queries: List[Tuple[int, List[int]]]) -> List[int]:
    brand_phones = defaultdict(list)

    for price, brand in phones:
        brand_phones[brand].append(price)

    for brand in brand_phones:
        brand_phones[brand].sort()
        while len(brand_phones[brand]) > n:
            brand_phones[brand].pop(0)

    answers = []

    for b, preference in queries:
        candidate_phones = []
        for brand in preference:
            for price in brand_phones[brand]:
                if len(candidate_phones) < b:
                    heapq.heappush(candidate_phones, price)
                else:
                    heapq.heappushpop(candidate_phones, price)
        if len(candidate_phones) < b:
            answers.append(-1)
        else:
            answers.append(candidate_phones[0])

    return answers
```