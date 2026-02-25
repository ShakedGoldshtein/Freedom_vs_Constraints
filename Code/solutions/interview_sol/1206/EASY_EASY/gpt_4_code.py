```python
from collections import Counter

def get_final_voters_list(n1, n2, n3, list1, list2, list3):
    counter = Counter(list1+list2+list3)
    final_list = [id for id in counter if counter[id]>1]
    return len(final_list), sorted(final_list)
```
