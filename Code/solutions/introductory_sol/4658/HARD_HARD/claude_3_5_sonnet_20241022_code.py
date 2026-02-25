```python
def max_product(lst, k):
    """
    Returns the product of k maximal numbers in the list.
    
    Args:
        lst: List of integers (size >= 3)
        k: Number of elements to multiply (k <= len(lst))
    
    Returns:
        Product of k maximal numbers in lst
    """
    if not lst or k <= 0 or k > len(lst):
        return 0
        
    # Sort list in descending order
    sorted_lst = sorted(lst, reverse=True)
    
    # Calculate product of first k elements
    product = 1
    for i in range(k):
        product *= sorted_lst[i]
        
    return product
```