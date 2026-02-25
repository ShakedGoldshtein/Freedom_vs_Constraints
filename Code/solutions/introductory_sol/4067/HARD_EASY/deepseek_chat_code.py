```python
def iq_test(numbers):
    """
    Finds the position (1-based) of the number that differs in evenness from the others.
    
    Args:
        numbers: A string of space-separated integers
        
    Returns:
        int: The 1-based index of the number that differs in evenness
    """
    if not numbers or not numbers.strip():
        raise ValueError("Input cannot be empty")
    
    num_list = numbers.split()
    
    if len(num_list) < 3:
        raise ValueError("At least 3 numbers are required")
    
    try:
        nums = [int(num) for num in num_list]
    except ValueError as e:
        raise ValueError("All elements must be valid integers") from e
    
    even_count = 0
    odd_count = 0
    even_positions = []
    odd_positions = []
    
    for i, num in enumerate(nums):
        if num % 2 == 0:
            even_count += 1
            even_positions.append(i + 1)
        else:
            odd_count += 1
            odd_positions.append(i + 1)
    
    if even_count == 0 or odd_count == 0:
        raise ValueError("All numbers have the same evenness")
    
    if even_count == 1:
        return even_positions[0]
    elif odd_count == 1:
        return odd_positions[0]
    else:
        raise ValueError("No single number differs in evenness")