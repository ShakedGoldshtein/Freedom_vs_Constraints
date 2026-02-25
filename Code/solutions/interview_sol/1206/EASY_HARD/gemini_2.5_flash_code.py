```python
def find_majority_voters(n1, n2, n3, list1, list2, list3):
    s1 = set(list1)
    s2 = set(list2)
    s3 = set(list3)

    # Find elements present in at least two lists using set operations:
    # (s1 & s2) finds elements common to list1 and list2
    # (s1 & s3) finds elements common to list1 and list3
    # (s2 & s3) finds elements common to list2 and list3
    # The union (|) of these three results gives all elements that appear in at least two lists.
    majority_set = (s1 & s2) | (s1 & s3) | (s2 & s3)

    # Convert the resulting set to a list and sort it in ascending order
    final_sorted_list = sorted(list(majority_set))

    return final_sorted_list
```