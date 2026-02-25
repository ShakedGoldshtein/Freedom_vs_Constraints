```python
# Function to add two arguments
def add(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both a and b must be either int or float")
        return a + b
    except TypeError as e:
        print(str(e))
```
```python
# Function to concatenate two arguments
def concat(a, b):
    try:
        if not isinstance(a, str) or not isinstance(b, str):
            raise TypeError("Both a and b must be string")
        return a + b
    except TypeError as e:
        print(str(e))
```