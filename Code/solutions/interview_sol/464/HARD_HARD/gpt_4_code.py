Here is a Python solution that meets all aforementioned requirements:

```python
def min_operations(n):
    """
    Calculate the minimum number of operations needed to make all elements of 
    array arr equal where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).
    In one operation, you can select two indices x and y (0 <= x, y < n) and subtract 1 from arr[x] 
    and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1).
    """
    mid_value = n // 2
    return mid_value * (mid_value + n % 2)
```
This code works by calculating the desired value that all elements in the array should be, which is the middle value of the array. The number of operations needed to make all elements equal to this value is the square of the middle index in case of even length array, or the product of middle index and next integer in case of an odd length array. 

This is because for each element, the number of add/subtract operations to reach the middle value equals to the absolute difference between their indices and the middle index. So the total number of operations is the sum of all differences, which forms an arithmetic series that can be calculated in constant time. 

Overall, this code has O(1) time complexity and O(1) space complexity since no array is actually created in the memory and the calculation is based on simple arithmetic operations. It handles all possible values in the input domain [1, 10^4] as defined in the constraints, which covers all the edge cases.