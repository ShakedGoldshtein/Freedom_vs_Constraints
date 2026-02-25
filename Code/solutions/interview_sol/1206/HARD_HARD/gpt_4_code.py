```Python
from collections import Counter
from operator import itemgetter

def voter_list(n1, voters1, n2, voters2, n3, voters3):
    all_voters = voters1 + voters2 + voters3
    voter_count = Counter(all_voters)
    selected_voters = [k for k, v in voter_count.items() if v > 1]
    selected_voters.sort()
    return len(selected_voters), selected_voters

n1 = 5
voters1 = [23, 30, 42, 57, 90]
n2 = 6
voters2 = [21, 23, 35, 57, 90, 92]
n3 = 5
voters3 = [21, 23, 30, 57, 90]

final_count, final_list = voter_list(n1, voters1, n2, voters2, n3, voters3)
print(final_count)
print("\n".join(map(str, final_list)))
```

This Python script will parse the list of voters from the three lists and count the frequency of every voter appearing in the list. The final list would only include those voters appearing at least twice in the overall listing. The lists are already sorted in ascending order as per the prompt requirement and then converted to the desired output format. The code handles cases where the lists are not the same length, provided the lengths match the parameters n1, n2, and n3.