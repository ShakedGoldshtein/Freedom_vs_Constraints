```python
def max_product(lst: list[int], n_largest_elements: int) -> int:
    """
    Calculate the product of the k maximal numbers in a list.

    Args:
        lst (list): A list of integers.
        n_largest_elements (int): The number of largest elements to consider.

    Returns:
        int: The product of the k maximal numbers.
    """
    # Sort the list in descending order to easily access the largest elements
    sorted_lst = sorted(lst, reverse=True)
    
    # Select the k largest elements
    largest_elements = sorted_lst[:n_largest_elements]
    
    # Calculate the product of the selected elements
    product = 1
    for num in largest_elements:
        product *= num
    
    return product
```