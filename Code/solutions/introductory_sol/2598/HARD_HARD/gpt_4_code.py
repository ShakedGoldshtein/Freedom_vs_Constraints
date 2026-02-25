```python
def is_superset(setA, otherSets):
    try:
        for otherSet in otherSets:
            if not (setA > set(otherSet)):
                return False
        return True

    except Exception as error:
        print(f"An error occurred: {str(error)}")
        return False
```